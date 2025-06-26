import sys
import os

# Add the src/ directory to the import path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from getTheta import GetTheta
from calculs import LinearModel, Standardize
import numpy as np
from arrayInit import Load_xy

def main():
    #retrieve theta 0 and 1
    theta0, theta1 = GetTheta()

    #input mileage
    try:
        #get the mileage input
        mileage = float(input("How Many Mileage? "))
        # standardize
        mileage_data = Load_xy()
        mileage_standardize = Standardize(mileage, mileage_data)
        if mileage < np.min(mileage_data) or mileage > np.max(mileage_data):
            raise ValueError("Input km is out of training range")
        # calcul linear regression
        estimate_price = LinearModel(theta0, theta1, mileage_standardize)
        print(f"The estimate price for {mileage} km is {int(estimate_price)}$")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()