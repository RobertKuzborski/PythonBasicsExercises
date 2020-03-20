from pathlib import Path

#Absolute path
# c:\Program Files\..
# /usr/local/bin

#Relative path

# directory check if exists, create, remove

path = Path("ecommerce")
path.mkdir()
print(path.exists())
path.rmdir()
print(path.exists())

# search files and directories
path1 = Path()

for file in path1.glob("*"): # *.* for files only, * for files and dir,
    print(file)
