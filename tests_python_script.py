from python_script import run_statistics
import pandas as pd


def test_run_statistics():
    "Test the descriptive stats function in python script"
    data = pd.read_csv("population.csv")

    results = run_statistics(data)

    assert "max" in results
    assert "head" in results
    assert "mean" in results
    assert "std" in results
