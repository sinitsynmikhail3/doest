# Python code to get the first row of the DataFrame by using the iloc[] function
import pandas as pd

# Create a sample DataFrame
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

# Get the first row
first_row = df.iloc[0]
print(first_row)
