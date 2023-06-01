import os
import json
import csv
from pprint import pprint


def get_output(input_type, output_dir):
    if input_type == 'print':
        return _print
    elif input_type == 'save_json':
        return lambda results: _save_json(results, output_dir)
    elif input_type == 'save_csv':
        return lambda results: _save_csv(results, output_dir)


def _print(results, *args):
    pprint(results)


def _save_json(results, output_dir):
    filename = os.path.join(output_dir, 'output.json')
    with open(filename, 'w') as json_file:
        json.dump(results, json_file, indent=4)


def _save_csv(results, output_dir):
    filename = os.path.join(output_dir, 'output.csv')
    keys = results[0].keys() if results else []
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)
