# import pathlib
# file_path=pathlib.Path("nam.txt")
# print("file exists")

import os
if os.path.exists("rea.txt"):
    print("Exists")
else:
    print("Not exists")