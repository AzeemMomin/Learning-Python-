# Program: Recursive Folder Scanner
# Real use case: Many operating system & tools scan folders recursively
# This program lists all files in nested folders

print("===== RECURSIVE FOLDER SCANNER =====")

def scan_folder (folder, level = 0):
    for name, content in folder.items():
        print("  " * level + "-" + name)

        # If valu is a dictionary -> scan again recursively
        if isinstance(content, dict):
            scan_folder(content, level + 1)

# Mock folder structure(dictionary)
filesystem = {
    "Documents": {
        "Resume.pdf": None,
        "project": {
            "Report.docx":None,
            "Data.xlsx":None
        }
    },
    "Pictures":{
        "Vacation": {
            "img1.jpg": None,
            "img2.jpg": None
        },
        "Profile.png": None
    }
}

scan_folder(filesystem)

