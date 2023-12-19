import os
import sys
import shutil
import AddVault
import RemoveVault
import MoveVault
import RenameVault
import RenameVault
import AddFile
import RemoveFile
import MoveFile
import RenameFile

if os.path.exists("Variables.txt"):
    with open("Variables.txt", "a") as f:
        f.write("")
else:
    with open("Variables.txt", "w") as f:
        f.write("")


if os.path.exists("Vaults.txt"):
    with open("Vaults.txt", "a") as f:
        f.write("")
else:
    with open("Vaults.txt", "w") as f:
        f.write("")
