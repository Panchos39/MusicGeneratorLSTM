import io
import os
import base64
from IPython.display import HTML
import cv2
import numpy as np

def display_runs(path='./gym-results/'):
    '''
        displays all runs stored in the path provided
    '''
    videos = filter(lambda x: x.endswith(".mp4"), os.listdir(path))
    html = []
    for video_path in videos:
        video = io.open(os.path.join(path,video_path), 'r+b').read()
        encoded = base64.b64encode(video)
        html.append(html(data='''
            <center><video width="720" height="auto" alt="test"
                         controls><source src="data:video/mp4;base64,{0}"
                         type="video/mp4" /></video></center>'''
             .format(encoded.decode('ascii'))))

    if len(html) == 1:
        return html[0]
    
    else:
        return html

def preprocess(observation):
    observation = cv2.resize(observation, (84, 110),interpolation = cv2.INTER_NEAREST)
    observation = cv2.cvtColor(observation, cv2.COLOR_BGR2GRAY)
    observation = observation[26:103,:]
    #ret, observation = cv2.threshold(observation,1,255,cv2.THRESH_BINARY)
    return observation


def rolling_average(serie, T):
    rolling_average = []
    for _ in range(T,len(serie)):
        rolling_average.append(np.mean(serie[_-T:_])) 
    
    return rolling_average




