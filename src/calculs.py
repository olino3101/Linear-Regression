import numpy as np
from typing import Optional, Tuple

def LinearModel(theta0, theta1, mileage):
    price_estimate = theta0 + (theta1 * mileage)
    return price_estimate

def StandardizeArr(xArr):
    xArr = (xArr - np.mean(xArr)) / np.std(xArr)
    return xArr

def Standardize(mileage, xArr):
    new_mileage = (mileage - np.mean(xArr)) / np.std(xArr)
    return new_mileage

def CalcTheta(learning_rate, xArr, yArr, theta0, theta1) -> Optional[Tuple[float, float]]:
    m = xArr.size
    gradient_theta0 = 0
    gradient_theta1 = 0
    for x, y in zip(xArr, yArr):
        predicted_value = LinearModel(theta0, theta1, x)
        error = predicted_value - y
        gradient_theta0 += error
        gradient_theta1 += error * x
    theta0 = theta0 - learning_rate * (1/m) * gradient_theta0
    theta1 = theta1 - learning_rate * (1/m) * gradient_theta1
    return theta0, theta1