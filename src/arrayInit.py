import numpy as np
import pandas as pd
from typing import Optional, Tuple

file_path = 'data/data.csv'
# x is mileage
# y is price
def Load_xy() -> Optional[Tuple[np.ndarray, np.ndarray]]:
    try:
        data = pd.read_csv(file_path)
        x = data.iloc[:, 0].to_numpy()
        y = data.iloc[:, 1].to_numpy()
        if x.size != y.size:
            raise ValueError()
        return x, y
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except ValueError:
        print("Problem with data, make sur its only number")
    exit(1)