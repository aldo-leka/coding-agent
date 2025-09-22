import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overrides the content of a file. If the file doesn't exist, it creates it.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write content to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write.",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    try:
        joined_path = os.path.join(working_directory, file_path)
        abs_target = os.path.abspath(joined_path)
        abs_working = os.path.abspath(working_directory)

        if not (abs_target.startswith(abs_working + os.sep) or abs_target == abs_working):
            raise Exception(f'Cannot write to "{file_path}" as it is outside the permitted working directory')
        
        with open(abs_target, "w" if os.path.exists(abs_target) else "x") as f:
            f.write(content)

        msg = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        print(msg)
        return msg

    except Exception as e:
        err = f"Error: {str(e)}"
        print(err)
        return err