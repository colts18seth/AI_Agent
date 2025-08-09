import os

def get_files_info(working_directory, directory="."):
    absJoinedPath = os.path.abspath(os.path.join(working_directory, directory))
    absWD = os.path.abspath(working_directory)

    if not absJoinedPath.startswith(absWD):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(absJoinedPath):
        return f'Error: "{directory}" is not a directory'
    
    try:
        filesList = os.listdir(absJoinedPath)
        filesList.sort()
        stringList = []
        for file in filesList:
            stringList.append(f' - {file}: file_size={os.path.getsize(os.path.join(absJoinedPath, file))} bytes, is_dir={os.path.isdir(os.path.join(absJoinedPath, file))}')
    except Exception as e:
        return f'Error: {e}'

    return f'\n'.join(stringList)