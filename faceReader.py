import pandas as pd

def import_data():
    #index = pd.read_csv("D:/PROJECTS/Distracted Driving/faceData/002/2-1.csv", header = None)
    path = input("Enter the video path: \n")
    index = pd.read_csv(path, header = None)
    index = index.iloc[9:]
    index.columns = ['Video Time', 'Neutral', 'Happy', 'Sad', 'Angry', 
                     'Surprised', 'Scared', 'Disgusted', 'Valence', 'Arousal', 
                     'Gender', 'Age', 'Beard', 'Moustache', 'Glasses', 'Ethnicity',
                     'Y - Head Orientation', 'X - Head Orientation', 'Z - Head Orientation',
                     'Landmarks', 'Quality', 'Mouth', 'Left Eye', 'Right Eye',
                     'Left Eyebrow', 'Right Eyebrow', 'Gaze Direction', 'Identity']
    #print(index.head(5))
    #print(index.columns)
    select_var = ['Video Time', 'Neutral', 'Happy', 'Sad', 'Angry', 
                  'Surprised', 'Scared', 'Disgusted', 'Arousal', 'Mouth',
                  'Left Eye', 'Right Eye', 'Gaze Direction']
    index = index[select_var]
    #print(index.head(5))
    #print(index.columns)
    return index

def in_cell (i, j):
    value = index.iloc[i][str(j)]
    return value
    
def noise_handle ():
    count = 0
    for i in range(len(index)):
        if in_cell(i, 'Neutral') == 'FIND_FAILED' or in_cell(i, 'Neutral') == 'FIT_FAILED':
            count += 1
#    print(count)
    if count > len(index)/3:
        print ("\n\nThis video is very noisy!\n\n")
#        exit()
    else:
        print ("\n\nThis video has a good quality!\n\n")
    length = len(index) / 24
    print ("The video duration is %.2f seconds in total\n\n" % (length))

def phone_talk ():
    for label in ['Happy', 'Angry', 'Sad']:
        for noise in ['FIND_FAILED', 'FIT_FAILED']:
            index[str(label)] = index[str(label)].replace(str(noise), int(0))
        index[str(label)] = index[str(label)].astype(float)    
        mean = index[str(label)].mean()
        index[str(label)] = index[str(label)].replace(int(0), mean)
        index[str(label)] = index[str(label)].astype(float)
           

    happy_std = index['Happy'].std()
    happy_2sigma = happy_std * 2
    happy_mean = index['Happy'].mean()
    happy_law = happy_mean + happy_2sigma
    
    angry_std = index['Angry'].std()
    angry_2sigma = angry_std * 2
    angry_mean = index['Angry'].mean()
    angry_law = angry_mean + angry_2sigma
    
    sad_std = index['Sad'].std()
    sad_1sigma = sad_std
    sad_mean = index['Sad'].mean()
    sad_law = sad_mean + sad_1sigma
    
    count = 0
    for i in range(len(index)):
        if (((in_cell(i, 'Mouth') == 'Open') and 
            ((in_cell(i, "Happy") > happy_law) or 
            (in_cell(i, "Angry") > angry_law))) or
            ((in_cell(i, 'Sad') > sad_law) and 
             (in_cell(i, 'Left Eye') == 'Closed') and 
             (in_cell(i, 'Right Eye') == 'Closed'))): 
            count += 1
    talk_time = count / 24
    print("The time that the driver used the cellphone is about %.4f second(s)\n\n" % (talk_time))
  
   
    
restart = 1
while restart != "x":  
    index = import_data()
    noise_handle()
    phone_talk()
    restart = input("press any key to start again, or 'x' to exit: \n")
           
        
            
    
