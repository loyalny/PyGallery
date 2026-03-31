import os

def trim_file_name(file_name, x=10):
    name, ext = os.path.splitext(file_name)

    if len(name) <= x:
        return file_name

    return f"{name[:x]}...{ext}"