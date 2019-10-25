import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from constants import *


# Read out our data from CSV_PATH
# Filtering the tags by percentage
# Ordering the tags from the CSV file in descending order
data_frame = pd.read_csv(CSV_PATH, error_bad_lines=False)
data_frame = data_frame[data_frame["Percent"] > PERCENTAGE_LIMIT].sort_values(by=["Percent"],
                                                      ascending=False)

 # Plot our data
data_frame.plot(kind='line',x='Tag',y='Percent',color='blue')
plt.show()
