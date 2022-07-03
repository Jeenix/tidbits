"""Script to print a list of files in the folder"""

import glob
import os

def main():
    LOCAL = os.path.dirname(os.path.realpath(__file__))
    file = glob.glob(pathname="*", root_dir=LOCAL, recursive=False) # can search for specific file types eg pathname="*.ipt"
    print("\n".join(file))
    f = open(LOCAL + "/files_summary.txt", "w")
    for lines in file:   
        f.write(str(lines)+"\n")
    f.close()

if __name__ == "__main__":
    main()