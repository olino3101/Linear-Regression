# Linear Regression – Car Price Estimator

This project implements a simple linear regression model to estimate car prices based on mileage. The code is written in Python with minimal dependencies.

---

## Project Structure

/
├── Acurracy.py # Calculates model precision (MSE)
├── EstimatePrice.py # Predicts car price from mileage
├── TrainModel.py # Trains the linear regression model
├── data/
│ ├── data.csv # Dataset with mileage and prices
│ └── theta.txt # Saved model parameters
├── src/
│ ├── [helper modules] # Supporting functions
└── README.md


---

## Program Descriptions

**TrainModel.py**  
Reads the dataset and performs gradient descent to find parameters θ₀ and θ₁ for the model:

estimatePrice(mileage) = θ₀ + (θ₁ × mileage)


Updates θ₀ and θ₁ using:

tmpθ₀ = learningRate * (1/m) * Σ(estimatePrice[i] - price[i])
tmpθ₁ = learningRate * (1/m) * Σ(estimatePrice[i] - price[i]) * mileage[i]


Saves parameters to `data/theta.txt`.

**EstimatePrice.py**  
Prompts for mileage input, loads trained parameters, predicts and displays estimated price. Warns if mileage is outside training range.

**Acurracy.py**  
Calculates and displays Mean Squared Error (MSE) between predicted and actual prices using the dataset and saved parameters.

---

## Usage

```bash
python3 TrainModel.py       # Train the model
python3 EstimatePrice.py    # Predict price for given mileage
python3 Acurracy.py         # Calculate model accuracy (MSE)

Data Format

data/data.csv should have two columns:

mileage,price
12000,24000
35000,17000
...

Requirements

Install NumPy:

pip install numpy

(Optional) For plotting, install Matplotlib:

pip install matplotlib

Author

BOSS


Let me know if you want it even more concise or with a different style!