from typing import Optional, Tuple

file_path = 'data/theta.txt'

def GetTheta() -> Optional[Tuple[float, float]]:
    try:
        with open(file_path, 'r') as file:
            theta0_raw = file.readline()
            theta1_raw = file.readline()
            if not theta0_raw or not theta1_raw:
                raise ValueError("Make sure to have the two theta")
            theta0_text = theta0_raw.removeprefix("theta0: ").strip()
            theta1_text = theta1_raw.removeprefix("theta1: ").strip()

            theta0 = float(theta0_text)
            theta1 = float(theta1_text)
    
            return theta0, theta1
        
    except FileNotFoundError:
        print("The file does not exist, default value for both theta is 0")
    except ValueError as e:
        print(f"Data error: {e}, both theta will be 0")
    return 0, 0