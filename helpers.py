'''This file is for storing and calling classes/functions that are for general use case that can be used in a variety of projects.'''
import os, shutil

def check_for_directory(path:str) -> bool:
    '''
    Checks for a directory and, in the event it is not found, creates it. 
    Returns True if it exists and False if it had to create it.
    '''
    if not os.path.exists(path=path):
        os.mkdir(path=path)
        return False
    return True

def check_for_repeats(folder_path:str, file_name:str):
    '''
    Checks a directory for a repeat name/extension. 
    If there is, it returns True, and False otherwise.
    '''
    _fileName, _fileExt = os.path.splitext(file_name)
    for file in os.listdir(folder_path):
        if file == _fileName and file.endswith(_fileExt):
            return True
    return False

def move_file(file_path:str, destination_folder_path:str):
    '''
    Takes a file path and a folder path and moves the file into the destination. 
    Checks for repeats and makes sure not to overwrite.
    '''
    _filePath           = os.path.normpath(file_path)
    _filePathParts      = _filePath.split(os.sep)
    _file               = _filePathParts[len(_filePathParts)-1]
    _fileName, _fileExt = os.path.splitext(_file)

    repeats = 0
    while check_for_repeats(destination_folder_path, _file):
        repeats += 1

        # Remove repeat tag
        if repeats > 1:
            _fileName = _fileName[0:len(_fileName)-len(str(repeats))]
            
        # Add to end
        _fileName += f"{repeats}"
            
    shutil.move(file_path, f"{destination_folder_path}/{_fileName + _fileExt}")

def split_path(path):
    '''Breaks down a path into parts and returns the name, extension, and path as a tuple.'''
    _path              	= os.path.normpath(path)
    _pathParts          = _path.split(os.sep)
    _name, _extension   = os.path.splitext(_pathParts[len(_pathParts)-1])
    return (_name, _extension, _path)

def file_info(path):
    '''
    Returns the needed information from a file in a dictionary that can be easily loaded into variables.
        - name
        - extension
        - path
        - creation date
        - modification date
        - access date
        - size
        - isFile
        - isDir
    
    '''
    _path                   = os.path.normpath(path)
    _pathParts              = _path.split(os.sep)
    _name, _extension       = os.path.splitext(_pathParts[len(_pathParts)-1])

    _stats = os.stat(path)
    _creationDate       = _stats.st_ctime
    _modificationDate   = _stats.st_mtime
    _accessDate         = _stats.st_atime
    _size               = _stats.st_size

    _isFile = os.path.isfile(path)
    _isDir = os.path.isdir(path)

    return {"name" : _name, "extension" : _extension, "path" : _path, "creation date" : _creationDate, "modification date" : _modificationDate, "access date" : _accessDate, "size" : _size, "isFile" : _isFile, "isDir" : _isDir}

def byte_size_conversion(bytes, convertSize:int=2):
    '''
    Converts an integer of bytes into a given output label:
        1 - kb
        2 - mb
        3 - gb
        4 - tb
        5 - pb
    '''
    match (convertSize):
        # Kilobytes
        case 1:
            return bytes * 0.001
        # Megabytes
        case 2:
            return bytes * 0.000001
        # Gigabytes
        case 3:
            return bytes * 0.000000001
        # Terabytes
        case 4:
            return bytes * 0.000000000001
        # Petabytes
        case 5:
            return bytes * 0.000000000000001