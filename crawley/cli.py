from argparse import ArgumentParser


def main(args):
    pass


if __name__ == "__main__":

    cli_parser = ArgumentParser()
    cli_parser.add_argument('outuput', choices=[

        '((1) Print html',
        '(2) Save in JSON',
        '(3)) Save in CSV'])

    args = cli_parser.parse_args()
    main(args)
