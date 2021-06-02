import argparse
from textwrap import dedent

from utils import ModelMapper


def run_train(args):
    model = ModelMapper.get_model(args.model_type)()


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
    train_parser.set_defaults(callback=run_train)


def main():
    parser = argparse.ArgumentParser('Simple ML project')
    setup_parser(parser)
    args = parser.parse_args()
    args.callback(args)


if __name__ == '__main__':
    main()
