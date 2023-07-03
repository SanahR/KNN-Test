import numpy as np
from sklearn.neighbors import KNeighborsClassifier as KNC
import matplotlib.pyplot as plt
#import random is not really needed
import random

# Step 1: Making the Data
X = np.array([[4.8],[4.9],[5.1],[5.4],[5.3]])
y = np.array([5,5,6,6,6])

#Separating the different grades for the plot
#Making 5th Grade
ymask = y==5
#Applying the masks
#newy is not really needed
newy = y[ymask
newx= X[ymask]

#Making 6th Grade
ymask2 = y==6
#Applying the masks
#Ultray is not really needed
ultray = y[ymask2]
ultrax = X[ymask2]
# Step 2: Creating the Algorithm
algo = KNC(n_neighbors = 1)


# Step 3: Learning/Training
algo.fit(X,y)


# Step 4: Prediction/Testing
#Adds an interactive element
ask = float(input("What is the student's height? ")) 
print(algo.predict([[ask]]))
#Two brackets needed in order to pass as 2D

#Making the Plot
#6th Grade Heights
plt.plot(ultrax, color = "MediumOrchid", label = "Sixth Grade",marker = "P",ms = 10)
#5th Grade Heights
plt.plot(newx, color = "Coral", label = "Fifth Grade",marker = "<",ms = 10)
#Making a legend/key
plt.legend()
#Making the labels make sense
plt.xticks([0,1,2],labels = [" "," "," "])
