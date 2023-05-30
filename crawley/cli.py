from argparse import ArgumentParser


def main(args):
    pass


if __name__ == "__main__":

    cli_parser = ArgumentParser()
    cli_parser.add_argument(
        'outuput', choices=['print', 'save json', 'save csv'])

    args = cli_parser.parse_args()
    main(args)
