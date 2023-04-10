from sortingmethod import SortingMethod
from helpers import split_path

OFF_LIMIT_FOLDERS = ["extension", "alphabetical", "size", "custom", ".git", "__pycache__", ".vscode"]
OFF_LIMIT_FILES = ["autosortfolder.py", "filesorter.py", "main.py", "sortingmethod.py", "trayicon.py", "repeatedtimer.py", "helpers.py", "autosortfolder-icon.ico", "README.md", "sortingalgorithms.py"]

#-- Class
class FileSorter:
    def __init__(self, root:str, method:SortingMethod=None):
        self._root      = root
        self.method     = method
    
    def sort_file(self, root, file_path:str):
        '''Sorts a file based on the FileSorter's sorting method'''
        if self.method == None:
            raise RuntimeError("Sorting method not specified.")

        _fileName, _fileExtension, _filePath = split_path(file_path)

        if (_fileName + _fileExtension) not in OFF_LIMIT_FILES and (_fileName + _fileExtension) not in OFF_LIMIT_FOLDERS:
            return self.method.sort(root, file_path)
        
        return False