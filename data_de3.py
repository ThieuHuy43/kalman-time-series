# De so 3
print("De so:", 2251262610 % 7 + 1)

import pandas as pd
df = pd.read_csv(r"C:\Users\PC\OneDrive\Dokumen\python_programming\kalman_filltering\data\podcast_dataset.csv")

# take "Wednesday" only
df_wednesday = df[df['Publication_Day'] == 'Wednesday']

# save
output_path = r"C:\Users\PC\OneDrive\Dokumen\python_programming\kalman_filltering\data\podcast_wednesday.csv"
df_wednesday.to_csv(output_path, index=False)

