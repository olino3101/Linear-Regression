import sys
import os

# Add the src/ directory to the import path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from getTheta import GetTheta
from arrayInit import Load_xy
from calculs import LinearModel, StandardizeArr
# loss function is used to calculate how far the some of each point is from the predicted
def LossFunction(xArr, yArr, theta0, theta1):
    wrongness = 0
    for x, y in zip(xArr, yArr):
        predicted_value = LinearModel(theta0, theta1, x)
        error = (predicted_value - y) ** 2
        wrongness += error
    wrongness /= 2 * xArr.size
    return wrongness

def main():
    xArr, yArr = Load_xy()
    xArr = StandardizeArr(xArr)
    theta0, theta1 = GetTheta()
    meanSquaredError = int(LossFunction(xArr, yArr, theta0, theta1))
    print(f"Mean Squared Error (MSE) Is {meanSquaredError}")

if __name__ == "__main__":
    main()