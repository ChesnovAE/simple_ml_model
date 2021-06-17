import logging
import argparse
from textwrap import dedent

import mlflow
from sklearn.pipeline import Pipeline
from dotenv import load_dotenv

from utils import ModelMapper, DatasetMapper, save_model, get_model_params

# TODO: дописать применение модели
def run_train(args):
    if args.params_path is not None:
        params = get_model_params(args.params_path)['params']
    else:
        params = None
    model = ModelMapper.get_model(args.model_type)(params)
    
    model = Pipeline([
        ('estimator', model)
    ])
    
    logging.info('Load model %s', model)
    X, y = DatasetMapper.get_data('iris')
    logging.info('Fit model')
    mlflow.set_tracking_uri("http://194.67.111.68:5000")
    mlflow.set_experiment(args.exp_name)
    with mlflow.start_run() as run:
        model.fit(X, y)
        if params:
            mlflow.log_params(params)
        mlflow.sklearn.log_model(model, artifact_path="model")
    
    if args.model_name is not None:
        logging.info('Save %s to %s', model, args.model_name)
        save_model(args.model_name, model)


def setup_parser(parser: argparse.ArgumentParser):
    subparsers = parser.add_subparsers(
        help='Choose command. Type <command> -h for more help'
    )
    train_parser = subparsers.add_parser(
        'train',
        help='train choosen model',
        formatter_class=argparse.RawTextHelpFormatter,
    )
    train_parser.add_argument(
        '--model',
        help=dedent('''
            Choose model type
            Available types:
                - logistic: sklearn.linear_models.LogisticRegression
        '''),
        dest='model_type',
        type=str,
        required=True
    )
    train_parser.add_argument(
        '--config-params-path',
        help='path to model params .yml file',
        dest='params_path',
        type=str,
        required=False,
        default=None
    )
    train_parser.add_argument(
        '--model-name',
        help='name of model',
        dest='model_name',
        type=str,
        required=False,
        default=None
    )
    train_parser.add_argument(
        '--exp-name',
        help='name of experiment',
        dest='exp_name',
        type=str,
        required=False,
        default='test_exp'
    )
    train_parser.set_defaults(callback=run_train)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser('Simple ML project')
    setup_parser(parser)
    args = parser.parse_args()
    args.callback(args)


if __name__ == '__main__':
    main()
