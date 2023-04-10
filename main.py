from autosortfolder import AutoSortFolder
from os import getcwd

def main():
    exec = AutoSortFolder(root=getcwd())
    exec.run()

if __name__ == "__main__":
    main()