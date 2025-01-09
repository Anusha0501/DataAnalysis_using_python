# -*- coding: utf-8 -*-
"""understanding data

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xRFDitxt7IyxWUbM9d0Nq_YKGUZFHG-Z
"""

import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/100 days of ML by campusX/train.csv')

df.shape # How big is the data?

df.sample(5) # How does the data look like?

df.info() # What is the data type of cols?

df.isnull().sum() # Are there any missing values?

df.describe() # How does the data look mathematically?

df.duplicated().sum() # Are there duplicate values?

df.corr()['Survived'] # How is the correlation between cols?

numeric_df = df.select_dtypes(include=['number'])
correlations = numeric_df.corr()
print(correlations['Survived'])