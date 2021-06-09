import logging
import argparse
from textwrap import dedent

from utils import ModelMapper, DatasetMapper, save_model, get_model_params

# TODO: дописать применение модели
def run_train(args):
    if args.params_path is not None:
        params = get_model_params(args.params_path)['params']
    else:
        params = None
    model = ModelMapper.get_model(args.model_type)(params)
    logging.info('Load model %s', model)
    X, y = DatasetMapper.get_data('iris')
    logging.info('Fit model')
    model.fit(X, y)
    
    if args.save_model_path is not None:
        logging.info('Save %s to %s', model, args.save_model_path)
        save_model(args.save_model_path, model)


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
        '--save-model-path',
        help='path to save model',
        dest='save_model_path',
        type=str,
        required=False,
        default=None
    )
    train_parser.set_defaults(callback=run_train)


def main():
    parser = argparse.ArgumentParser('Simple ML project')
    setup_parser(parser)
    args = parser.parse_args()
    args.callback(args)


if __name__ == '__main__':
    main()
