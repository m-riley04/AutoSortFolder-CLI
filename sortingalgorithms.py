from sortingmethod import SortingMethod
from helpers import check_for_directory, move_file, split_path, file_info, byte_size_conversion

#-- Constants
ICON_DATA = b"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"
ALPHABET = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

TEXT_EXTENSIONS = ['.txt', '.doc', '.docx', '.rtf', '.tex', '.wpd', '.wp5']
DOCUMENT_EXTENSIONS = ['.pdf', '.key', '.odp', '.pps', '.ppt', '.pptx', '.potx', '.potm', '.pot', '.ppam', '.ppsm', '.ppsx', ]
AUDIO_EXTENSIONS = ['.aif', '.aifc', '.aiff', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.wpl', '.aac', '.adt', '.adts']
COMPRESSED_EXTENSIONS = ['.7z', '.arg', '.deb', '.pkg', '.rar', '.rpm', '.gz', '.z', '.zip']
DISC_EXTENSIONS = ['.bin', '.dmg', '.iso', '.toast', '.vcd']
DATA_EXTENSIONS = ['.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml', '.ab', '.accdb', '.accde', '.accdr', '.accdt']
EMAIL_EXTENSIONS = ['.email', '.eml', '.emlx', '.msg', '.oft', '.ost', '.pst', '.vcf']
EXECUTABLE_EXTENSIONS = ['.apk', '.bat', '.bin', '.com', '.exe', '.gadget', '.jar', '.msi', '.wsf']
FONT_EXTENSIONS = ['.fnt', '.fon', '.otf', '.ttf', ".vlw", ".DFONT"]
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.JPG', '.JPEG', '.gif', '.bmp', '.ico', '.png', '.ps', '.svg', '.tif', '.tiff']
INTERNET_EXTENSIONS = ['.asp', '.aspx', '.cer', '.cfm', '.css', '.htm', '.html', '.js', '.jsp', '.part', '.rss', '.xhtml']
PROGRAMMING_EXTENSIONS = ['.c', '.cgi', '.pl', '.class', '.cpp', '.cs', '.h', '.java', '.php', '.py', '.sh', '.swift', '.vb']
SPREADSHEET_EXTENSIONS = ['.ods', '.xls', '.xlsm', '.xlt', '.xltm', '.xlsx']
SYSTEM_EXTENSIONS = ['.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns', '.ini', '.lnk', '.sys', '.tmp']
VIDEO_EXTENSIONS = ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv']
ADOBE_EXTENSIONS = ['.ai', '.psd', '.indd', '.prproj', '.aep']
EXTENSIONS = {
    "Text Extensions"       : TEXT_EXTENSIONS,
    "Document Extensions"   : DOCUMENT_EXTENSIONS,
    "Audio Extensions"      : AUDIO_EXTENSIONS,
    "Compressed Extensions" : COMPRESSED_EXTENSIONS,
    "Disc Extensions"       : DISC_EXTENSIONS,
    "Data Extensions"       : DATA_EXTENSIONS,
    "Email Extensions"      : EMAIL_EXTENSIONS,
    "Executable Extensions" : EXECUTABLE_EXTENSIONS,
    "Font Extensions"       : FONT_EXTENSIONS,
    "Image Extensions"      : IMAGE_EXTENSIONS,
    "Internet Extensions"   : INTERNET_EXTENSIONS,
    "Programming Extensions": PROGRAMMING_EXTENSIONS,
    "Spreadsheet Extensions": SPREADSHEET_EXTENSIONS,
    "System Extensions"     : SYSTEM_EXTENSIONS,
    "Video Extensions"      : VIDEO_EXTENSIONS,
    "Adobe Extensions"      : ADOBE_EXTENSIONS
}

#-- Sorting Methods
def sort_alphabetical(root, file_path):
    '''
        Sorting algorithm based on first character. 
        Takes a file and moves it to the characterized folder.
        If a folder is found for the character, return True. Otherwise, return False.
    '''
    _fileName, _fileExtension, _filePath = split_path(file_path)

    for character in ALPHABET:
        if character == _fileName[0]:
            # Check folder creation
            check_for_directory(f"{root}/alphabetical/{character}")

            # Add it to the folder
            move_file(file_path, f"{root}/alphabetical/{character}")

            # Return
            return True
        
    # Misc Folder
    check_for_directory(f"{root}/extension/Misc Characters")
    # Add to the misc folder
    move_file(file_path, f"{root}/extension/Misc Characters")

    return False

def sort_extension(root, file_path):
    '''
        Sorting algorithm based on extension. 
        Takes a file and moves it to assigned extension folder. 
        Folders go to their own directory, and everything else to a miscelaneous directory.
        If a folder is found for the extension, return True. Otherwise, return False.
    '''
    _fileName, _fileExtension, _filePath = split_path(file_path)

    for title, extensions in EXTENSIONS.items():
        if _fileExtension in extensions:
            # Check folder creation
            check_for_directory(f"{root}/extension/{title}")

            # Add it to the folder
            move_file(file_path, f"{root}/extension/{title}")

            # Return
            return True
        
        if _fileExtension == None:
            # Folder folder
            check_for_directory(f"{root}/extension/Folders")
            # Add to the folder folder
            move_file(file_path, f"{root}/extension/Folders")

            return True
    
    # Misc Folder
    check_for_directory(f"{root}/extension/Misc")
    # Add to the misc folder
    move_file(file_path, f"{root}/extension/Misc")

    return False

def sort_custom(root, file_path):
    '''Sorting algorithm based on custom parameters. Takes a file and moves it to assigned folder.'''

def sort_date_created(root, file_path):
    pass

def sort_date_modified(root, file_path):
    pass

def sort_date_accessed(root, file_path):
    pass

def sort_size(root, file_path):
    ''''''
    _fileInfo = file_info(file_path)
    _fileSize = _fileInfo["size"]

    if byte_size_conversion(_fileSize, 4) >= 1: # Bigger than a petabyte
        # Check folder creation
        check_for_directory(f"{root}/size/Petabyte+")

        # Add it to the folder
        move_file(file_path, f"{root}/size/Petabyte+")

        # Return
        return True
    if byte_size_conversion(_fileSize, 3) >= 1: # Bigger than a gigabyte
        # Check folder creation
        check_for_directory(f"{root}/size/Gigabyte+")

        # Add it to the folder
        move_file(file_path, f"{root}/size/Gigabyte+")

        # Return
        return True
    if byte_size_conversion(_fileSize, 2) >= 1: # Bigger than a gigabyte
        # Check folder creation
        check_for_directory(f"{root}/size/Megabyte+")

        # Add it to the folder
        move_file(file_path, f"{root}/size/Megabyte+")

        # Return
        return True
    if byte_size_conversion(_fileSize, 1) >= 1: # Bigger than a gigabyte
        # Check folder creation
        check_for_directory(f"{root}/size/Kilobyte+")

        # Add it to the folder
        move_file(file_path, f"{root}/size/Kilobyte+")

        # Return
        return True
    if byte_size_conversion(_fileSize, 1) < 1: # Byte sized
        # Check folder creation
        check_for_directory(f"{root}/size/Bytes")

        # Add it to the folder
        move_file(file_path, f"{root}/size/Bytes")

        # Return
        return True

    # Misc Folder
    check_for_directory(f"{root}/size/Misc")
    # Add to the misc folder
    move_file(file_path, f"{root}/size/Misc")

    return False

#-- Initialize Sorting Objects
SORTING_METHODS = [
    SortingMethod(name="Alphabetical", method=sort_alphabetical), 
    SortingMethod(name="Extension", method=sort_extension), 
    SortingMethod(name="Size", method=sort_size), 
    SortingMethod(name="Date Created", method=sort_date_created),
    SortingMethod(name="Date Modified", method=sort_date_modified),
    SortingMethod(name="Date Accessed", method=sort_date_accessed),
    SortingMethod(name="Custom", method=sort_custom)
    ]