"We will use pytest to test our functions from src/lib.py"
from lib import head, mean, max
import pandas as pd

def test_head():
    """Test function for the get_mean"""
    data = pd.read_csv("population.csv")
    test_result = head(data)
    # assert the test
    assert test_result.iloc[3,5] == 2.115789118

def test_mean():
    data = pd.read_csv("population.csv")
    test_result2 = mean(data)
    assert test_result2.iloc[4] == 2.3040175788371213

def test_max():
    data = pd.read_csv("population.csv")
    test_result3 = max(data)
    assert test_result3.iloc[7] == 12.11486066


if __name__ == '__main__':
    test_head()
    test_mean()
    test_max()
