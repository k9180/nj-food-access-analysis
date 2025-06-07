import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV data
df = pd.read_csv('Food Access Research Atlas.csv', encoding='latin1')

# Step 2: Filter for New Jersey only
df_nj = df[df['State'] == 'New Jersey']

# Step 3: Group by County and sum the LILATracts_1And10 values
summary = df_nj.groupby('County')['LILATracts_1And10'].sum().reset_index()

# Step 4: Sort counties by most food access issues
summary = summary.sort_values(by='LILATracts_1And10', ascending=False)

# Step 5: Display the summary in terminal (optional)
print(summary.head(10))

# Step 6: Create and show a bar chart
plt.figure(figsize=(12, 6))
plt.bar(summary['County'], summary['LILATracts_1And10'], color='maroon')
plt.xticks(rotation=45, ha='right')
plt.title('Low Income, Low Access Tracts per NJ County')
plt.xlabel('County')
plt.ylabel('Number of LILA Tracts')
plt.tight_layout()
plt.show()
