import numpy as np

# Dummy sales data
days = np.array([1, 2, 3, 4, 5])
sales = np.array([10, 15, 20, 25, 30])

# Simple regression
coeff = np.polyfit(days, sales, 1)

print("Model coefficients:", coeff)
