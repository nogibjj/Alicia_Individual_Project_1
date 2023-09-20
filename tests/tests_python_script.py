from src.python_script import run_statistics
import sys
sys.path.append("/workspaces/Alicia_Individual_Project_1")
sys.path.append("/workspaces/Alicia_Individual_Project_1/src")
import pandas as pd


def test_run_statistics():
    "Test the descriptive stats function in python script"
    data = pd.read_csv("/workspaces/Alicia_Individual_Project_1/src/population.csv")

    results = run_statistics(data)
    
    assert 'max' in results
    assert 'head' in results
    assert 'mean' in results
    assert 'std' in results
