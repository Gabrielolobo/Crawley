
def get_output(input_type):
    if input_type == 'print':
        return _print
    elif input_type == 'save_json':
        return _save_json
    elif input_type == 'save_csv':
        return _save_csv


def _print():
    pass


def _save_json():
    pass


def _save_csv():
    pass
