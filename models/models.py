"""Models class"""
from abc import ABC, abstractmethod
from typing import Union, Dict

from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd


class BaseModel(ABC):
    """abstract model class"""
    def __init__(self, params=None):
        """init func"""
        if params is not None:
            self.params = params
        else:
            params = {}

    @abstractmethod
    def fit(self, xtrain, ytrain):
        """fit method"""
        raise NotImplementedError

    @abstractmethod
    def predict(self, xtest):
        """predict method"""
        raise NotImplementedError


class LogisticModel(BaseModel):
    """logistic model class"""
    def __init__(self, params: Dict = None) -> None:
        """init method"""
        super().__init__(params)
        self.model = LogisticRegression(**params)

    def fit(self,
            xtrain: Union[pd.DataFrame, np.array],
            ytrain: Union[pd.DataFrame, np.array]) -> None:
        """fit method"""
        self.model.fit(xtrain, ytrain)

    def predict(self,
                xtest: Union[pd.DataFrame, np.array]) -> np.array:

        return self.model.predict(xtest)
