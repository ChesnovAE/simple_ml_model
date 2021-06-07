import os
import yaml

import pytest

from models import LogisticModel
from ._utils import ModelMapper, DatasetMapper, get_model_params


TEST_CONFIG_YAML = {
    'params': {
        'solver': 'liblinear',
        'max_iter': 100
    }
}


def test_model_mapper():
    model = ModelMapper.get_model('logistic')()
    assert isinstance(model, LogisticModel) == True


def test_correct_load_config_yml(tmpdir):
    yaml_path = os.path.join(tmpdir, 'tst_config.yml')
    with open(yaml_path, 'w') as f:
        yaml.dump(TEST_CONFIG_YAML, f)
    config = get_model_params(yaml_path)
    
    assert 'para' in config
    assert 'solver' in config['params']
    assert 'max_iter' in config['params']
    assert config['params']['solver'] == 'liblinear'
    assert config['params']['max_iter'] == 100


def test_save_model_by_path(tmpdir):
    pass
