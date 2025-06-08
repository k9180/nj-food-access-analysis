# NJ Food Access Analysis

This project analyzes USDA's Food Access Research Atlas to explore food access challenges
in NJ.

## What It Does

- Loads USDA 2019 food access data (CSV)
- Filters for the state of NJ
- Aggregates by county to find areas with low-income, low access census tracts
- Visualizes results in a bar chart using 'matplotlib'

## Tools Used
 
- Python
- pandas
- matplotlib
- Real-world USDA data 

## Files

- 'nj_food_access.py' - Python script for loading and analyzing the data 
- 'Food Access Research Atlas.csv' - USDA data (2019)
- 'VariableLookup.csv' -  Key to column definitions 

## Why This Matters 

Food deserts and access issue affect public health and policy decisions. This project
takes a look at how data analysis can support equity, awareness, and better decision-making.

## Run It Yourself

1. Install required packages
'''bash
pip install pandas matplotlib

2. Run the script 
python nj_food_access.py