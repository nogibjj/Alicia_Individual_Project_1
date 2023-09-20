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
Both these files containes tests for their respective python scripts. This ensures the code in functionally performs well.

### 5. Understanding the statistics functions
The objective is to analyze the relationship between Insulin, Glucose, BMI, and diabetes status (1 for diabetic, 0 for not diabetic). The functions defined calculate maximum, minimum, mean, median, and standard deviation for these key variables, aiding in a descriptive analysis of their association with diabetes.

### 6. Understanding the Data Visualization functions
In this code, count plots offer a glimpse into the distribution of data types, especially the prevalence of diabetic and non-diabetic cases. Understanding this distribution is vital for addressing class imbalance and potential biases in a diabetes prediction scenario. On the other hand, bar plots help visually compare predictor variables like Glucose, Insulin, and BMI against diabetes status, revealing insights into their association with the outcome. These visualizations aid in identifying patterns and trends, such as higher Glucose levels being more common among diabetic patients. Overall, count and bar plots provide valuable visual context, enabling informed decisions in diabetes research and predictive modeling.

## Results

![After executing the code, the following descriptive statistics are for Glucose, Insulin, and BMI](https://user-images.githubusercontent.com/141798228/268531816-2f9924ab-d11c-422a-b509-bb3cb042a723.jpg)

These statistics offer insights into the central tendency and spread of the diabetes patients, contributing to a better understanding of its distribution.

The visualization below illustrates the relationship between the predictor variable (Insulin, Glucose, BMI) and the Outcome variable (Whether a patient has diabetes or doesn't have diabetes)

![Countplot](https://user-images.githubusercontent.com/141798228/268531789-4ee528a7-c91f-4281-b2e6-ea15daa89a42.png)
![Barplot](https://user-images.githubusercontent.com/141798228/268531736-b20fb998-b839-4c6a-b8af-3749b5ed8f4b.png)

## Conclusion
This script serves as a valuable tool for investigating the interplay between crucial predictor variables—Glucose, Insulin, and BMI—and the diabetes status indicator within the context of the Pima Indian female patient dataset. By offering essential descriptive statistics and intuitive visualizations like count plots and bar plots, it allows for a deeper understanding of how these variables are linked to the likelihood of diabetes. These insights provide a solid foundation for conducting more advanced analyses and informed decision-making in the domain of diabetes research and prediction
