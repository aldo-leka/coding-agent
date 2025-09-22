import os
import subprocess
from functions.config import EXECUTE_TIMEOUT
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs given '.py' file with a execution timeout of 30 seconds.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="The array of optional arguments to pass to the execution call.",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    try:
        joined_path = os.path.join(working_directory, file_path)
        abs_target = os.path.abspath(joined_path)
        abs_working = os.path.abspath(working_directory)

        if not (abs_target.startswith(abs_working + os.sep) or abs_target == abs_working):
            raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        
        if not os.path.isfile(abs_target):
            raise Exception(f'Error: File "{file_path}" not found.')
        
        if not abs_target.endswith(".py"):
            raise Exception(f'Error: "{file_path}" is not a Python file.')
        
        cmd = ["python", abs_target, *args]
        cp = subprocess.run(cmd, timeout=EXECUTE_TIMEOUT, capture_output=True, text=True)
        result = f"STDOUT: {cp.stdout}\nSTDERR: {cp.stderr}\n"
        if cp.returncode != 0:
            result += f"Process exited with code {cp.returncode}\n"
        
        if (cp.stdout.strip() == "" and cp.stderr.strip() == ""):
            result += "No output produced."

        print(result)
        return result
        

    except Exception as e:
        print(f"{str(e)}")
        return f"Error: executing Python file: {e}"
    
