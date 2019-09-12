#!/usr/bin/env python
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "idna"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
executables = [Executable("Program.py", base=base)]
setup(  name = "pixieLogger",
        version = "0.1",
        description = "Super Amazing",
        options = {"build_exe": build_exe_options},
        executables = executables
        )
