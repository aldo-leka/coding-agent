import os

def get_files_info(working_directory, directory="."):
    try:
        joined_path = os.path.join(working_directory, directory)
        abs_target = os.path.abspath(joined_path)
        abs_working = os.path.abspath(working_directory)
        
        if abs_target == abs_working:
            print("Result for current directory:")
        else:
            print(f"Result for '{directory}' directory:")

        if not (abs_target.startswith(abs_working + os.sep) or abs_target == abs_working):
            raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        if not os.path.isdir(abs_target):
            raise Exception(f'Error: "{directory}" is not a directory')
        
        contents = os.listdir(abs_target)
        contents_strs = []
        for content in contents:
            content_abs = os.path.join(abs_target, content)
            content = f"- {content}: file_size={os.path.getsize(content_abs)} bytes, is_dir={not os.path.isfile(content_abs)}"
            print(content)
            contents_strs.append(content)
        
        contents_str = "\n".join(contents_strs)
        return contents_str
    except Exception as e:
        print(e)
        return str(e)