import sys
import json

with open(sys.argv[1], 'r') as values_file:
    values_cluster = json.loads(values_file.read())

with open(sys.argv[2], 'r') as tests_file:
    tests = json.loads(tests_file.read())

values = dict()
for pair in values_cluster['values']:
    values[pair['id']] = pair['value']

report = tests

def edit_tree(node):
    if isinstance(node, dict):
        if 'id' in node and 'value' in node:
            node['value'] = values.get(node['id'], '')
        if 'values' in node:
            edit_tree(node['values'])
    else:
        for subnode in node:
            edit_tree(subnode)

edit_tree(report['tests'])

with open(sys.argv[3], 'w') as report_file:
    report_file.write(json.dumps(report))

