# Data Analysis: Analyze 266 countries population growth in 67 years.
---Youtube video link here: https://youtu.be/U7vApAowVO4
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
Installs code via:  pip install -r requirements.txt

### 4. Test_script.py and Test_lib.py
I tested my main 'script.py' with 'test_python_script.py' and also 'lib.py' with 'test_lib.py' to make sure my functions in library works and also the main script of my code works as well.

### 5. Understanding the statistics functions
The main purpose of this project is to make a glance of the dataset with function I created, 'head' and generated basic statistics insight from the population data. So I generated a function 'mean','max','std', calculating mean, max, standard deviation. Then, I pulled out four interested countries population growth percentages to have look at my data.
<img width="1360" alt="head_result" src="https://github.com/nogibjj/Alicia_Individual_Project_1/assets/143651934/a0eb25ae-e391-4081-830d-a363b936446a">
<img width="133" alt="max_result" src="https://github.com/nogibjj/Alicia_Individual_Project_1/assets/143651934/d16f8321-7174-413e-8940-4355e3df3338">

### 6. Visualization
With function 'viz_population', I generated a line plot that visualized mean, median, and standard deviation of each year to see each year how population growth will change. the plot is as follow:
<img width="790" alt="line_plot" src="https://github.com/nogibjj/Alicia_Individual_Project_1/assets/143651934/685c3da5-e018-4a12-80fd-9fb83d0b38be">
## Results
Out of the four countries showing interest, India consistently exhibited the highest percentage of growth over the entire span of 63 years. Meanwhile, in 1961, China experienced a negative growth percentage. As time progressed, all four countries witnessed a decline in their population growth rates. A line plot graphically illustrates this downward trend in population growth rates year by year.
<img width="1389" alt="countries_table" src="https://github.com/nogibjj/Alicia_Individual_Project_1/assets/143651934/07a93685-469a-4fe3-93b8-4260de13376b">
## Conclusion
Different countries exhibit diverse population growth rates. Some nations may experience rapid population expansion, while others might have slower growth or even negative growth rates.Some countries might experience negative population growth in specific years. This could be due to factors like declining birth rates, increased emigration, or other demographic shifts.Developed nations tend to have more stable and consistent population growth rates over time, while developing nations may experience more significant fluctuations.
