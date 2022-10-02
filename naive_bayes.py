#-------------------------------------------------------------------------
# AUTHOR: Grecia Alvarado
# FILENAME: naive_bayes.py
# SPECIFICATION: Output classification for each test instance if confidence is >= 0.75
# FOR: CS 4210- Assignment #2
# TIME SPENT: 40 minutes
#-----------------------------------------------------------*/
#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH 
#AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays
#importing some Python libraries
import csv
from sklearn.naive_bayes import GaussianNB
#reading the training data in a csv file
db = []
X = []
Y = []
#reading the data in a csv file
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0:
         db.append (row)
#transform the original training features to numbers and add them to the 4D array
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 
#2], ...]]
tracker = {}
num = 1
for i in db:
  row = []
  for j in range(1, len(i)-1):
    if i[j] in tracker:
      row.append(tracker.get(i[j]))
      i[j] = tracker.get(i[j])
    else:
      tracker[i[j]] = num
      row.append(num)
      i[j] = num
      num += 1
  X.append(row)


#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
tracker2 = {}
num2 = 1
for j in db:
  for i in range(len(j)-1, len(j)):
    if j[i] in tracker2:
      Y.append(tracker2.get(j[i]))
    else:
      tracker2[j[i]] = num2
      Y.append(num2)
      num2 += 1

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
original = []
test = []
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, line in enumerate(reader):
      original.append(line)
      if i > 0:
         data = []
         for j, case in enumerate(line):
             if j < len(line)-1 and j>0:
                 data.append(tracker.get(line[j]))
         test.append(data)

#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + 
"Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + 
"Confidence".ljust(15))
#use your test samples to make probabilistic predictions. For instance: 
for count, set in enumerate(test):
    confidence = clf.predict_proba([set])[0]
    if confidence [0]>= 0.75 or confidence[1] >= 0.75:
        result = ""
        c = 0.0
        if confidence[0] > confidence[1]:
            result = "No"
            c = confidence[0]
        else:
            result = "Yes"
            c = confidence[1]
        print (original[count][0].ljust(15) + original[count][1].ljust(15) + original[count][2].ljust(15) + 
        original[count][3].ljust(15) + original[count][4].ljust(15) + result.ljust(15) + 
        str(c).ljust(15))