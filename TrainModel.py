import sys
import os

# Add the src/ directory to the import path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from showGraph import ShowGraph
import numpy as np
from arrayInit import Load_xy
from calculs import CalcTheta, StandardizeArr

def WriteThetaIntoFile(theta0, theta1):
    file_name = 'data/theta.txt'
    try:
        with open(file_name, 'w') as file:
            file.write(f"theta0: {theta0}\n")
            file.write(f"theta1: {theta1}")
    except:
        print("File dont have the permission or does not exist")
    

def TrainData(xArr, yArr):
    xArr_standardize = StandardizeArr(xArr)
    theta0 = 0
    theta1 = 0
    learning_rate = 0.01

    # wrongness when its at theta0 = 0, theta1 = 0

    # loop (until you find the perfect) every time change the line
    for i in range(1000):
        theta0, theta1 = CalcTheta(learning_rate, xArr_standardize, yArr, theta0, theta1)

    #wrongness at the end if less then works
    # wrongness = LossFunction(xArr_standardize, yArr, theta0, theta1)
    
    WriteThetaIntoFile(theta0, theta1)
    ShowGraph(xArr_standardize, yArr, theta0, theta1, xArr)


def main():
    # get x and y. x = mileage, y = price
    x, y = Load_xy() or (None, None)
    if x is None or y is None:
        print("X or Y is None")
        exit(1)
    TrainData(x, y)

if __name__ == "__main__":
    main()
