# import dependencies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
%matplotlib inline

# using pandas to read the database stored in the same folder
data = pd.read_csv(r"C:/Users/prane/Downloads/digit-recognizer/test.csv")  
