# Data Analysis: Analyze 266 countries population growth in 67 years.

## Data Source
The dataset is composed of 266 countries' 62 years population growth in annual percentage.
You can access the data from the following URL: [population.csv] https://data.worldbank.org/indicator/SP.POP.GROW

## Code Overview

### 1. Library of my shared functions
In the library I created 'head
  1. head()
  2. mean()
  3. std()
  4. summary()
  5. countries_interest()
  6. viz_population()

### 2. Jupyter Notebook and Python Script.py
My jupyter notebook helps to scratch my overall thought about how to analyze my data and it provides visualized result of each line of code.

### 3. MakeFile and Workflows
I seperated my Makefile into 4 individual .yml files to seperately automate 4 workflows
Install: runs the packages indicated in my requirements.txt
Lint: Lints the code with Ruff to make sure code doesn't have syntex problem or unused lines.
Format: Formats code with Python black formatter
Test: Runs tests on notebook, script, and library

### 4. Test_script.py and Test_lib.py
I tested my main script and also my functions in library to make sure they work properly.

### 5. Understanding the statistics functions
The main purpose of this project is to have a peak of dataset with function I created 'head' to have a peak on the data firstly and generated basic statistics insight from the population data. So I generated a function 'mean','max','std', calculating mean, max, standard deviation. Then, I pulled out four interested countries population growth percentages to have look at my data.

### 6. Understanding the Data Visualization functions


## Results




## Conclusion
This script serves as a valuable tool for investigating the interplay between crucial predictor variables—Glucose, Insulin, and BMI—and the diabetes status indicator within the context of the Pima Indian female patient dataset. By offering essential descriptive statistics and intuitive visualizations like count plots and bar plots, it allows for a deeper understanding of how these variables are linked to the likelihood of diabetes. These insights provide a solid foundation for conducting more advanced analyses and informed decision-making in the domain of diabetes research and prediction
