# .py-to-.exe
Serve as a part of highway safety project, "Investigation Problem of Distracted Drivers on Louisiana Roadways":
(The faceReader.py is a python script, which works as an analyzer for the exported data from faceReader (the bio-information collector, http://www.noldus.com/facereader/facereader-online).)

How is works:
-- Collect the normal-distributed emotional data from drivers' face (e.g. happy, sad, angry, surprised, etc.)
-- Collect the gaze and other facial movement (left/right eye closed or not)
-- Use the double-permutation to do the handle noise data:
        1. substitute the noise data ("FIND_FAILED" or "FIT_FAILED") with "0"
        2. calculate the mean value for each column
        3. substitute the "0"s in step #1 with the mean value calculated in step #2 
-- Report if the analyzed video is too noisy: more than 1/3 of the data is noise data
-- Calculate the mean and standard deviation for column "Happy", "Angry", and "Sad"
-- Define the criteria for two distracted driving behaviors: 
        1. cell phone manipulation: "sad > sad.mean + n * sad.std" and "left_eye == closed" and "right_eye == closed"
        2. cell phone talking: if ("mouth == open"):{if ("happy > happy.mean + n * happy.std" and "angry > angry.mean + n * angry.std"): {talk_count += high_emotion_weight}; else: {talk_count += low_emotion_weight}; }
-- Calibrate the parameters by experiment, including:
        1. n sigma for "sad", "happy", and "angry"
        2. high emotion and low emotion weight for the different talking scenarios                         
        3. manipulation adjustment parameter                                
-- Report the distracted driving time by "manipulating the cell phone" and "talking through the cell phone" by divided the video processing cutting time (e.g. 24 pieces of pictures per second)                               
        
use 'cx_Freeze' to convert the python script to the executable program: 
-- Download and install "cx_Freeze" directly issue the commend: "python -m pip install cx_Freeze --upgrade", or download from PyPI "https://pypi.python.org/pypi?:action=display&name=cx_Freeze&version=5.0.2", choose the appropriable version
-- Put the python script that you want to convert ("faceReader.py") with the file "setup.py" in one directory
-- SHIFT + RIGHT CLICK to open the PowerShell in the directory
-- In the PowerShell, issue the commend: "python setup.py build"
-- A new folder "build" will be created in the same directory, including all the packaged (compiled to .pkc already) that connected to the console/kernel.  
