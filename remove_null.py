

import os
import pandas as pd
import time
start_time=time.time() 

def remove_null_columns(file_path,count):
    
    null_value_thresh = 0.5
    df = pd.read_csv(file_path, dtype=str, low_memory=False)
    print(f"{count}: Original number of columns: {len(df.columns)}")
    threshold = null_value_thresh * len(df.columns)
    null_counts = df.isnull().sum()
    columns_to_drop = null_counts[null_counts > threshold].index

    if len(columns_to_drop) > 0:
        df.drop(columns_to_drop, axis=1, inplace=True)
        print(f"{count}: Dropped {len(columns_to_drop)} columns with more than {threshold:.0f} null values.")
    else:
        print(f"{count}: No columns dropped as none exceeded the null value threshold.")
    
    # Save the modified DataFrame back to the same file
    df.to_csv(file_path, index=False)
    return df
    
# Directory containing the CSV files
directory = "C:\\Users\\91950\\Desktop\\Semester-4\\MLPR\\Project\\home-credit-credit-risk-model-stability\\csv_files\\train_demo"

# Iterate over files in the directory
count=0
for filename in os.listdir(directory):
    
    if filename.endswith(".csv"):  # Process only CSV files
        count+=1
        file_path = os.path.join(directory, filename)
        remove_null_columns(file_path,count)


end_time=time.time()
print(end_time-start_time)


