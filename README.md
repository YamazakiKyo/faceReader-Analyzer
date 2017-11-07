# .py-to-.exe
use 'cx_Freeze' to convert the python script to the executable program 

1. Download and install "cx_Freeze" directly issue the commend:
    python -m pip install cx_Freeze --upgrade
   or download from PyPI "https://pypi.python.org/pypi?:action=display&name=cx_Freeze&version=5.0.2", choose the appropriable version
   
2. Put the python script that you want to convert ("faceReader.py") with the file "setup.py" in one directory.

3. SHIFT + RIGHT CLICK to open the PowerShell in the directory. 

4. In the PowerShell, issue the commend:
    python setup.py build
   Then a new folder "build" will be created in the same directory, including all the packaged (compiled to .pkc already) that connected      to the console/kernel.  

5. Open the file "faceReader.exe", and here we done!
