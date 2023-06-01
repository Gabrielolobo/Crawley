import json
import csv
from pprint import pprint


def get_output(input_type):
    if input_type == 'print':
        return _print
    elif input_type == 'save_json':
        return _save_json
    elif input_type == 'save_csv':
        return _save_csv


def _print(results, *args):
    pprint(results)


def _serialize_result(result):
    serialized_result = {
        'cpu': result.cpu,
        'monthly_cost': result.monthly_cost,
        'memory': result.memory,
        'storage': result.storage,
        'bandwidth': result.bandwidth
    }
    return serialized_result


def _save_json(results, *args):
    if len(args) > 0:
        filename = args[0]
    else:
        filename = 'output.json'
    serialized_results = [_serialize_result(result) for result in results]
    with open(filename, 'w') as file:
        json.dump(serialized_results, file)


def _save_csv(results, *args):
    if len(args) > 0:
        filename = args[0]
    else:
        filename = 'output.csv'
    if isinstance(results, list) and len(results) > 0 and isinstance(results[0], dict):
        keys = results[0].keys()
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(results)
    else:
        print("Invalid data format. Results should be a list of dictionaries.")
