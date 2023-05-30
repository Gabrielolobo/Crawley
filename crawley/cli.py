from argparse import ArgumentParser

from .output import get_output


def main(args):
    output_callable = get_output(args.output)


if __name__ == "__main__":

    cli_parser = ArgumentParser()
    cli_parser.add_argument(
        'outuput', choices=['print', 'save json', 'save csv'])

    args = cli_parser.parse_args()
    main(args)
