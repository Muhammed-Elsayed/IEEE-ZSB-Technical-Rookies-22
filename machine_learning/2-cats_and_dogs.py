import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
print('mo')
DATADIR = "D:\machine learning"
CATEGORIES = ["DOG", "Cat"]


IMGSIZE = 110
new_array = cv2.resize(img_array, (IMGSIZE , IMGSIZE))


training_data = []
def creating_training_data():
    for category in CATEGORIES:
       path = os.path.join(DATADIR, category)
       class_num = CATEGORIES.index(category)
       for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE )
                new_array = cv2.resize(img_array, (IMGSIZE , IMGSIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass
            
creating_training_data()

import random
random.shuffle(training_data)
import pickle
pickle_out = open("X.pickle","wb")
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()
