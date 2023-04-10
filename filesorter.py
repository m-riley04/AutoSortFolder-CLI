from sortingmethod import SortingMethod
import os

OFF_LIMITS = ["autosortfolder.py", "filesorter.py", "main.py", "sortingmethod.py", "trayicon.py", "repeatedtimer.py", "autosortfolder-icon.ico", "extension", "alphabetic", "custom", ".git", "__pycache__", ".vscode", "helpers.py"]

#-- Class
class FileSorter:
    def __init__(self, root:str, method:SortingMethod=None):
        self._root      = root
        self.method     = method
    
    def sort_file(self, file_path:str):
        '''Sorts a file based on the FileSorter's sorting method'''
        if self.method == None:
            raise RuntimeError("Sorting method not specified.")

        _filePath           = os.path.normpath(file_path)
        _filePathParts      = _filePath.split(os.sep)
        _fileName           = _filePathParts[len(_filePathParts)-1]

        if _fileName not in OFF_LIMITS:
            return self.method.sort(file_path)
        
        return False