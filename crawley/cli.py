from argparse import ArgumentParser

from .output import get_output
from .crawlers import AVAILABLE_CRAWLERS


# Calls crawler results
def main(args):
    output_callable = get_output(args.output)

    all_results = []
    for crawler in AVAILABLE_CRAWLERS.values():
        results = crawler.run()
        all_results.extend(results)

    output_callable(all_results)


if __name__ == "__main__":
    cli_parser = ArgumentParser()
    cli_parser.add_argument(
        'crawler', choices=list(AVAILABLE_CRAWLERS.keys()),
        help='Crawler choice: ' + ','.join(AVAILABLE_CRAWLERS.keys())
    )

    cli_parser.add_argument(
        'output', choices=['print', 'save json', 'save csv'])

    args = cli_parser.parse_args()
    main(args)
