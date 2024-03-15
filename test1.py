"""
Iterate through an Array and find the sum of any two elements which is numerically equal to 
the target value. If no array exits in the list then return 0 and exit!
"""
import time
import os
import threading
def mainFunc(targetValue, x):
    os.system('clear')
    values = []
    null = True
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            print(x)
            print(targetValue)
            print(values)
            print(x[i], ":", x[j])
            time.sleep(1)
            os.system('clear')
            if x[i] + x[j] == targetValue:
                values.append(x[i])
                values.append(x[j])
                print(values)
                null = False
        values=[]
    if null:
        return 0
x=[]
n = int(input("for n "))
for i in range(0, n+1):
    x.append(i)
print(x)
targetValue = int(input(" Enter the targetValue "))
def threadFunc():
    mainFunc(targetValue, x)
t = threading.Thread(target=threadFunc)
t.start()
