import os

import pytest
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from models import LogisticModel



def test_logistic_model():
    model = LogisticModel({'solver': 'liblinear'})
    X, y = load_iris(return_X_y=True)
    xtrain, xtest, ytrain, ytest = train_test_split(X, y, random_state=1011, test_size=0.33)
    model.fit(xtrain, ytrain)
    
    assert accuracy_score(ytest, model.predict(xtest)) >= 0.9