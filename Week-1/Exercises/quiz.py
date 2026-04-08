import io, csv, os, ast, builtins, sys, readline
from contextlib import redirect_stdout

# Change working directory to script's folder
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

instructions = """
---
INSTRUCTIONS
For single-line answers, write your answer and press ENTER. 
Then press ENTER a second time on the empty line.

For multiline answers, enter each line one by one, then finish by pressing 
ENTER on an empty line. If you think the code would raise an error, type in 
'error' (without the quotation marks).

If there is no output, simply press ENTER. If the output is None, write 'None'
(without the quotation marks).
---
"""
prompt = "\nYour answer:"
error_answers = ["Error", "error", "ERROR"]

def _normalize(text, case_sensitive=True):
    """Normalize user and reference answers for robust comparison."""
    if text is None:
        return ""

    # Normalize text: tabs, newlines, whitespace, double quotes, etc.
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\\n", "\n").replace("\\t", "\t")
    text = text.replace('"', "'")
    text = text.strip()

    # remove trailing spaces on each line
    lines = [ln.rstrip() for ln in text.split("\n")]
    text = "\n".join(lines)

    return text if case_sensitive else text.lower()

def _try_parse_collection(text):
    """
    Try to parse user/reference text as a Python literal and return the object
    if it's a list or dict; otherwise return None.
    """
    try:
        obj = ast.literal_eval(text)
    except Exception:
        return None
    return obj if isinstance(obj, (list, dict)) else None

def _run_and_capture_stdout(code_snippet):
    """Run the snippet and capture printed stdout, or return last expression if no prints."""
    buf = io.StringIO()
    original_input = builtins.input
    try:
        builtins.input = lambda *args, **kwargs: ""  # avoid blocking if snippet calls input()
        ns = {}
        with redirect_stdout(buf):
            try:
                # If there's no 'print' in the code, evaluate last expression explicitly
                if "print(" not in code_snippet:
                    # Split lines, exec all but last, eval last
                    lines = code_snippet.strip().splitlines()
                    if len(lines) == 1:
                        # Single line, try eval
                        try:
                            result = eval(lines[0], ns, ns)
                            return str(result)
                        except Exception as e:
                            # Fall back to exec if eval fails
                            exec(code_snippet, ns, ns)
                            return buf.getvalue()
                    else:
                        # More than one line
                        body, last = "\n".join(lines[:-1]), lines[-1]
                        exec(body, ns, ns)
                        try:
                            result = eval(last, ns, ns)
                            return str(result)
                        except Exception:
                            exec(last, ns, ns)
                            return buf.getvalue()
                else:
                    # Has print → capture stdout
                    exec(code_snippet, ns, ns)
            except Exception as e:
                return f"Error::{type(e).__name__}"
    finally:
        builtins.input = original_input

    return buf.getvalue().rstrip("\n")

def _check_enter():
    print("Press ENTER to continue.")
    for _ in iter(input, ""):
        pass

def _read_multiline_answer():
    """
    Read multiline user input until Enter is pressed on a blank line.
    """

    lines = []
    while True:
        line = input()
        # Stop on blank line (user pressed Enter on empty line)
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def quiz_user(code_snippet, *, case_sensitive=True):
    """
    Display code, ask question, and check the user's answer by running the code.
    """
    print("\n--- Code snippet ---\n")
    print(code_snippet)

    error_type = None
    result = _run_and_capture_stdout(code_snippet)
    
    if result.startswith("Error::"):
        error_type = result.split("::", 1)[1]
        correct_answers = error_answers
    else:
        correct_answers = [result]

    all_answers = list(correct_answers)

    normalized_refs = [_normalize(ans, case_sensitive=case_sensitive) for ans in correct_answers]

    print(prompt)
    user_raw = _read_multiline_answer()
    user_norm = _normalize(user_raw, case_sensitive=case_sensitive)

    # Expand acceptable answers if any correct answer looks like <class 'typename'>
    extra_answers = []
    for ans in correct_answers:
        if ans.startswith("<class '") and ans.endswith("'>"):
            typename = ans[len("<class '"):-len("'>")]
            extra_answers.append(typename)
    normalized_refs.extend([_normalize(ans, case_sensitive=case_sensitive) for ans in extra_answers])
    all_answers.extend(extra_answers)

    # Structural comparison for list/dict answers (whitespace-insensitive for those)
    matched = False
    user_coll = _try_parse_collection(user_norm)
    if user_coll is not None:
        for ans in all_answers:
            ref_coll = _try_parse_collection(ans)
            if ref_coll is not None and user_coll == ref_coll:
                matched = True
                break

    # Fallback to normalized string comparison if not matched structurally
    if not matched and user_norm in normalized_refs:
        matched = True

    if matched:
        if correct_answers == error_answers:
            article = "an" if error_type and error_type[0].lower() in "aeiou" else "a"
            print(f"✅ Correct! (It would raise {article} {error_type})\n")
        else:
            print("✅ Correct!\n")
        return True, user_raw
    else:
        print("❌ Incorrect.")

        return False, user_raw

def run_quiz_from_csv(filename, section = "Warm-up", start_row = 0):
    """
    Run a quiz by reading code snippets and questions from a CSV file.
    For each snippet, ask the user up to 3 times.
    If the user fails after 3 attempts, show the correct answer.
    """

    if section == "Warm-up":
        exercise_number = 1
    elif section == "Simple operations":
        exercise_number = 2
    elif section == "Conditionals":
        exercise_number = 3
    elif section == "Lists":
        exercise_number = 4
    elif section == "Dictionaries":
        exercise_number = 5

    welcome = f"\n---\nWELCOME TO EXERCISE 1.{exercise_number}: {section.upper()}!\nFor each of the following code snippets, predict the output.\n---\n"
    
    print(welcome)
    _check_enter()
    
    if exercise_number < 3:
        print(instructions)
        _check_enter()

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        total = len(rows)

        if section:
            rows = [row for row in rows if row.get('section', '').strip() == section]
            total = len(rows)

        results_file = f"Exercise-1.{exercise_number}-Answers.csv"

        # If a results file already exists, resume from the last attempted question
        resume_start_row = start_row
        append_mode = False
        if os.path.exists(results_file):
            try:
                with open(results_file, newline='', encoding='utf-8') as rf:
                    existing = list(csv.DictReader(rf))
                
                # Find last index where any answer was attempted
                last_attempted_idx = -1
                for i, r in enumerate(existing):
                    if any((r.get('answer1','') or '').strip() or (r.get('answer2','') or '').strip() or (r.get('answer3','') or '').strip()):
                        last_attempted_idx = i
                if last_attempted_idx >= 0:
                    resume_start_row = max(resume_start_row, last_attempted_idx + 1)
                append_mode = True
            
            except Exception:
                append_mode = False
                resume_start_row = start_row

        # Open results file (append if resuming, else create new with header)
        results_fields = ['section','code','answer1','answer2','answer3','correct']
        if append_mode:
            results_fp = open(results_file, 'a', newline='', encoding='utf-8')
            results_writer = csv.DictWriter(results_fp, fieldnames=results_fields)
        else:
            results_fp = open(results_file, 'w', newline='', encoding='utf-8')
            results_writer = csv.DictWriter(results_fp, fieldnames=results_fields)
            results_writer.writeheader()

        # Override start_row with resume position if any
        start_row = resume_start_row

        for idx, row in enumerate(rows):
            if idx < start_row:
                continue

            code = row.get('code', '').strip()
            if not code:
                continue

            print("-----------")
            print(f"QUESTION {idx + 1} out of {total}")

            section_name = row.get('section', '').strip()
            ans1 = ans2 = ans3 = ""
            got_it = 0
            
            # Run up to 3 attempts
            for attempt in range(3):
                correct, user_raw = quiz_user(code)
                if attempt == 0:
                    ans1 = user_raw
                elif attempt == 1:
                    ans2 = user_raw
                else:
                    ans3 = user_raw

                if correct:
                    got_it = 1
                    break
                else:
                    if attempt < 2:
                        print("\nPlease try again.")
            else:
                # After 3 failed attempts, show the correct answer
                result = _run_and_capture_stdout(code)
                if result.startswith("Error::"):
                    error_type = result.split("::", 1)[1]
                    correct_answers = error_answers
                else:
                    correct_answers = [result]

                print("\nThe correct answer was:\n---")
                if correct_answers == error_answers:
                    print(f"Error ({error_type})")
                else:
                    for ans in correct_answers:
                        print(ans)
                print("---\n")

            results_writer.writerow({
                'section': section_name,
                'code': code,
                'answer1': ans1,
                'answer2': ans2,
                'answer3': ans3,
                'correct': got_it,
            })
            

            if idx != (total - 1):
                _check_enter()
            else:
                pass

        # Ensure all writes are flushed to disk before reading back
        results_fp.close()

        # Read the full results file and count correct answers
        with open(results_file, newline='', encoding='utf-8') as rf:
            existing = list(csv.DictReader(rf))
            
        correct_count = sum(1 for r in existing if str(r.get('correct', '')).strip() == '1')
        print(f"You answered {correct_count} out of {total} questions correctly.")

if __name__ == "__main__":
    run_quiz_from_csv("snippets.csv")