import os
from functions.config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content in the specified file path truncated to 10000 characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to retrieve content from, relative to the working directory.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    try:
        joined_path = os.path.join(working_directory, file_path)
        abs_target = os.path.abspath(joined_path)
        abs_working = os.path.abspath(working_directory)

        if not (abs_target.startswith(abs_working + os.sep) or abs_target == abs_working):
            raise Exception(f'Cannot read "{file_path}" as it is outside the permitted working directory')
        
        if not os.path.isfile(abs_target):
            raise Exception(f'File not found or is not a regular file: "{file_path}"')
        
        with open(abs_target, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            result = f"{file_content_string}"
            if len(file_content_string) >= MAX_CHARS:
                result += f'...File "{file_path}" truncated at {MAX_CHARS} characters]'
            print(result)
            return result

    except Exception as e:
        err = f"Error: {str(e)}"
        print(err)
        return err