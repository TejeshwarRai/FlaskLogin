import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "adult.csv"
df = pd.read_csv(url)

col_names = df.columns
for c in col_names:
    df[c] = df[c].replace("?", np.NaN)

df = df.apply(lambda x:x.fillna(x.value_counts().index[0]))
def cirr():
    
