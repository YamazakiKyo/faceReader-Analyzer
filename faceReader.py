# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:17:37 2017

@author: Yi

Université des Acadiens
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

''' Change to '8' from paticipant No.27 !'''
time_sec = 24

''' Parameters you can change and play with:'''
n_happy_sigma = 0.5  # How many S.D. we will add to the mean, used as the upperbond for "happy" emotion.
n_angry_sigma = 0.5  # How many S.D. we will add to the mean, used as the upperbond for "angry" emotion.
n_sad_sigma = 2  # How many S.D. we will add to the mean, used as the upperbond for "sad" emotion.
high_emotion_weight = 0.5
low_emotion_weight = 1.5
manipulating_adjustment = 2  # According to the observation, cell phone manipulating behavior includs looking up and down.

''' You have to change the data path in the below line'''
path = r"D:/PROJECTS/Distracted Driving/faceData/009/9-1.csv"


def import_data():
    ''' You have to change the data path in the below line'''
    index = pd.read_csv(str(path), header=None)
    index = index.iloc[9:]
    index.columns = ['Video Time', 'Neutral', 'Happy', 'Sad', 'Angry',
                     'Surprised', 'Scared', 'Disgusted', 'Valence', 'Arousal',
                     'Gender', 'Age', 'Beard', 'Moustache', 'Glasses', 'Ethnicity',
                     'Y - Head Orientation', 'X - Head Orientation', 'Z - Head Orientation',
                     'Landmarks', 'Quality', 'Mouth', 'Left Eye', 'Right Eye',
                     'Left Eyebrow', 'Right Eyebrow', 'Gaze Direction', 'Identity']
    select_var = ['Video Time', 'Neutral', 'Happy', 'Sad', 'Angry',
                  'Surprised', 'Scared', 'Disgusted', 'Arousal', 'Mouth',
                  'Left Eye', 'Right Eye', 'Gaze Direction']
    index = index[select_var]
    ''' Double-permution noise handling'''
    for label in ['Happy', 'Angry', 'Sad']:
        for noise in ['FIND_FAILED', 'FIT_FAILED']:
            index[str(label)] = index[str(label)].replace(str(noise), int(0))
        index[str(label)] = index[str(label)].astype(float)
        mean = index[str(label)].mean()
        index[str(label)] = index[str(label)].replace(int(0), mean)
        index[str(label)] = index[str(label)].astype(float)
    happy_std = index['Happy'].std()
    happy_Nsigma = happy_std * n_happy_sigma
    happy_mean = index['Happy'].mean()
    happy_law = happy_mean + happy_Nsigma
    #    print("happy mean: %.2f, happy std: %.2f, happy law: %.2f" % (happy_mean, happy_std, happy_law))
    angry_std = index['Angry'].std()
    angry_Nsigma = angry_std * n_angry_sigma
    angry_mean = index['Angry'].mean()
    angry_law = angry_mean + angry_Nsigma
    #    print("angry mean: %.2f, angry std: %.2f, angry law: %.2f\n\n" % (angry_mean, angry_std, angry_law))
    sad_std = index['Sad'].std()
    sad_Nsigma = sad_std * n_sad_sigma
    sad_mean = index['Sad'].mean()
    sad_law = sad_mean + sad_Nsigma
    return index, happy_law, angry_law, sad_law


def in_cell(i, j):
    content = index.iloc[i][str(j)]
    return content


def happy(i):
    if in_cell(i, "Happy") > happy_law:
        return True
    else:
        return False


def angry(i):
    if in_cell(i, "Angry") > angry_law:
        return True
    else:
        return False


def sad(i):
    if in_cell(i, "Sad") > sad_law:
        return True
    else:
        return False


def openMonth(i):
    if in_cell(i, 'Mouth') == 'Open':
        return True
    else:
        return False


def closeEyes(i):
    if (in_cell(i, 'Left Eye') == 'Closed') and (in_cell(i, 'Right Eye') == 'Closed'):
        return True
    else:
        return False


def noisy_report():
    count = 0
    for i in range(len(index)):
        if in_cell(i, 'Neutral') == 'FIND_FAILED' or in_cell(i, 'Neutral') == 'FIT_FAILED':
            count += 1
    if count > len(index) / 3:
        print("\n\nThis video is very noisy!\n\n")
    else:
        print("\n\nThis video has a good quality!\n\n")
    length = len(index) / time_sec
    print("The video duration is %.2f seconds in total\n\n" % (length))


def phone_distract(index):
    talk_count = 0
    use_count = 0
    for i in range(len(index)):
        if (sad(i)) and (closeEyes(i)):
            use_count += 1
        if openMonth(i):
            if (happy(i)) and (angry(i)):
                talk_count += high_emotion_weight
            else:
                talk_count += low_emotion_weight
    talk_time = talk_count / time_sec
    if talk_time < 10:
        talk_time = 0  # Try to handle the elasticity problem
    use_time = (use_count / time_sec) * manipulating_adjustment  # Because of the cell phone manipulating behavior
    total_time = talk_time + use_time
    print("The time that the driver talked on the cellphone is about %.2f second(s)\n\n" % (talk_time))
    print("The time that the driver manipulated the cellphone is about %.2f second(s)\n\n" % (use_time))
    print("The total time that the driver used the cellphone is about %.2f second(s)\n\n" % (total_time))


index, happy_law, angry_law, sad_law = import_data()
noisy_report()
phone_distract(index)
'''Let's plot the happy, angry, sad emotions, and their upperbound'''
ax = index.plot()
ax.axhline(y=happy_law, label='Happy_Law', linestyle='--', color='salmon', lw=2)
ax.axhline(y=angry_law, label='Angry_Law', linestyle='--', color='violet', lw=2)
ax.axhline(y=sad_law, label='Sad_Law', linestyle='--', color='steelblue', lw=2)

# restart = 1
# while restart != "x":
#    index = import_data()
#    noise_handle()
#    phone_distract()
#    restart = input("press any key to start again, or 'x' to exit: \n")



