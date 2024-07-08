import json
import sys


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def fill_values(tests, values_map):
    for test in tests:
        test_id = test.get('id')
        if test_id in values_map:
            test['value'] = values_map[test_id]
        if 'values' in test:
            fill_values(test['values'], values_map)


def main():
    tests_file = 'tests.json'
    values_file = 'values.json'
    report_file = 'report.json'
    tests_data = load_json(tests_file)
    values_data = load_json(values_file)
    values_map = {entry['id']: entry['value'] for entry in values_data['values']}
    fill_values(tests_data['tests'], values_map)
    save_json(tests_data, report_file)


if __name__ == "__main__":
    main()
