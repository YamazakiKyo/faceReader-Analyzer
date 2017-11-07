from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Yi\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Yi\\Anaconda3\\tcl\\tk8.6"

build_exe_options = {"packages": ["os","numpy"], "includes": ["numpy", "pandas"]}
base = None
    
setup(name = "faceReader",
      version = "1.0",
      description = "Read from faceReader export file",
      executables = [Executable("faceReader.py")],
      options = {"build_exe": build_exe_options})
