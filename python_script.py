"""This Script is used to deploy descriptive statistics 
on the population dataset using function 
already defined by the lib.py"""
import lib
import pandas as pd


def run_statistics(data):
    result = {
        "head": lib.max(data),
        "mean": lib.mean(data),
        "std": lib.std(data),
        "summary": lib.summary(data),
    }

    return result


def run_visualizations(data):
    "Runs visualizations on the passed dataset"
    lib.viz_population(data, jupyter=True)
    lib.countries_interest(data)


if __name__ == "__main__":
    data = pd.read_csv("/workspaces/Alicia_Individual_Project_1/population.csv")
    results = run_statistics(data)
    run_visualizations(data)
