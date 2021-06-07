import yaml
import pickle

from sklearn.datasets import load_iris

from models import LogisticModel


def _get_iris():
    return load_iris(return_X_y=True)


def save_model(path, model):
    with open(path, 'wb') as f:
        pickle.dump(model, f)


def get_model_params(path):
    with open(path, 'r') as cfg:
        config = yaml.load(cfg)
    return config


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
        return DatasetMapper.mapper[name]()
