import os
from AddVault import *
from RemoveVault import *
from MoveVault import *
from RenameVault import *
from ChooseVault import *
from ChooseFile import *
from AddFile import *
from RemoveFile import *
from MoveFile import *
from RenameFile import *

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
