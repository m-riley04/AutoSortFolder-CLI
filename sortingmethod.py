class SortingMethod:
    def __init__(self, name, method, whitelist:list=[], blacklist:list=[]):
        self.name       = name
        self.method     = method
        self.whitelist  = whitelist
        self.blacklist  = blacklist
    
    def sort(self, file_path):
        '''Sorts the file using the SortingMethod's method of sorting. Returns True if the file was sorted, False otherwise.'''
        if self.whitelist != []:
            pass
        elif self.blacklist != []:
            pass
        else:
            self.method(file_path)
            return True
        
        return False
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self) -> str:
        return f"SortingMethod({self.name}, {self.method.__name__}, {self.whitelist}, {self.blacklist})"