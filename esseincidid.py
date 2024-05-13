import pandas as pd

def create_dataframe():
    # Create a DataFrame
    df = pd.DataFrame({
        'Name': ['John', 'Mary', 'Peter'],
        'Age': [20, 25, 30]
    })
    return df

# Call the function and print the result
df = create_dataframe()
print(df)
