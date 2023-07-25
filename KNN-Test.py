"""
A short program exploring KNearestNeighbors using simple data. 
If you want to know about the KNearestNeighbors algorithm, here is an article, https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
The plot here has no relation to the algorithm and was made for learning purposes. 
The masking system also has little relation to the algorithm and is also just for the plot. 
Definitions(in this specific project):
Plot: A graph made with matplotlib.
KNC: KNeighborsClassifier, or KNearestNeighbors.
X = the data for the heights.
y = part of the training data, it shows which heights are 5th grade and 6th grade. 
About KNearestNeighbors: 
KNearestNeighbors is an algorithm that classifies  numbers into categories based on data you've already given it. 
The way this works is by searching for the closest NEIGHBOR to the 
number inputted by the user. Using the data you have given it, it will classify what it is given. 
About the Plot: 
This plot is a simple line plot with two lines, one representing fifth grade and one representing 6th grade. 
The markers and colors have little meaning here, other than differentiation. The masking system here was used simply to separate the two grades and not have to do it 
manually, although one could argue that it could've been done in a more efficient manner. 
Step-by-Step: 
Step 1: Making the data
- This step is just making the heights and using y to classify them. 
Step 2: Creating the algorithm
- This is just one line of code where we create the algorithm(or KNC)
Step 3: Learning/Training
- This is where we fit X to y, and the algorithm makes the connections that they line up. For example, 
this stage is where the algorithm makes the connection that the 4.8 kid is a 5th grader. 
Step 4: Prediction/Testing
This is where the program uses what it knows to determine the nearest neighbor in the data to classify the kid. 
Step 5: Plotting
This is just a standard plot showcasing the data. 
"""
#adding the imports
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
newy = y[ymask]
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
#Floats are used in place of integers in order to make more precise heights. 
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
