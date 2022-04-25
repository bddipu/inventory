import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="RigInv",
    version="1.1",
    description="Inventory Management",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, shortcutName = 'RigInv', icon = 'icon.ico')],
)
