import numpy as np
import pandas as pd
from scipy import stats

msg = "awesome"
one = 1
two = 2
print("Python is " + msg + " " + str(one+two))

arr = np.array([1, 2, 3, 4, 5, 54, 34, 56])
print(arr)

#mean median mode
print("Median: " + str(np.median(arr)))
print("Mean: " + str(np.mean(arr)))
print("Mode: " + str(stats.mode(arr).mode))

#standard deviation
print("Standard Deviation: " + str(np.std(arr)))