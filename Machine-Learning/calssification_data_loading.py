import numpy as np
import os
import random
import cv2
from tqdm import tqdm
import pickle

# path of the Images can be downloaded from https://www.microsoft.com/en-us/download/confirmation.aspx?id=54765
DATADIR = "X:/Datasets/PetImages"

CATEGORIES = ["Dog", "Cat"]
training_data = []
IMG_SIZE = 50
# Reading the data and make an array of images that is reshaped


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in tqdm(os.listdir(path)):
            try:
                img_array = cv2.imread(os.path.join(
                    path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass


create_training_data()
random.shuffle(training_data)

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)
X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# Saving the data
pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()
