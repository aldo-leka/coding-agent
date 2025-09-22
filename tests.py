from functions.run_python_file import run_python_file

run_python_file("calculator", "main.py") # (should print the calculator's usage instructions)
run_python_file("calculator", "main.py", ["3 + 5"]) # (should run the calculator... which gives a kinda nasty rendered result)
run_python_file("calculator", "tests.py")
run_python_file("calculator", "../main.py") # (this should return an error)
run_python_file("calculator", "nonexistent.py") # (this should return an error)
