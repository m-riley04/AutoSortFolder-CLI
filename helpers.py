'''This file is for storing and calling classes/functions that are for general use case that can be used in a variety of projects.'''
import os, shutil

def check_for_directory(path:str) -> bool:
    '''Checks for a directory and, in the event it is not found, creates it. Returns True if it exists and False if it had to create it.'''
    if not os.path.exists(path=path):
        os.mkdir(path=path)
        return False
    return True

def check_for_repeats(folder_path:str, file_name:str):
    '''Checks a directory for a repeat name/extension. If there is, it returns True, and False otherwise.'''
    _fileName, _fileExt = os.path.splitext(file_name)
    for file in os.listdir(folder_path):
        if file == _fileName and file.endswith(_fileExt):
            return True
    return False

def move_file(file_path:str, destination_folder_path:str):
    '''Takes a file path and a folder path and moves the file into the destination. Checks for repeats and makes sure not to overwrite.'''
    _filePath           = os.path.normpath(file_path)
    _filePathParts      = _filePath.split(os.sep)
    _file               = _filePathParts[len(_filePathParts)-1]
    _fileName, _fileExt = os.path.splitext(_file)

    repeats = 0
    while check_for_repeats(destination_folder_path, _file):
        repeats += 1

        # Remove repeat tag
        #if "(" in _fileName[0:-3] and ")" in _fileName[0:-3]:
        if repeats > 1:
            _fileName = _fileName[0:len(_fileName)-len(str(repeats))]
            
        # Add to end
        _fileName += f"{repeats}"
            
    shutil.move(file_path, f"{destination_folder_path}/{_fileName + _fileExt}")