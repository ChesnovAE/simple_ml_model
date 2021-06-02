from sklearn.datasets import load_iris

from models import LogisticModel


class ModelMapper:
    mapper = {
        'logistic': LogisticModel
    }
    @staticmethod
    def get_model(name):
        return ModelMapper.mapper[name]


class DatasetMapper:
    mapper = {
        'iris': _get_iris
    }
    @staticmethod
    def get_data(name):
        return DatasetMapper.mapper[name]


def _get_iris():
    pass
