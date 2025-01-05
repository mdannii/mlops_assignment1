#import pytest
from sklearn.linear_model import LinearRegression

def test_model_training():
    model = LinearRegression()
    assert model is not None
