#How would you read and write YAML files in Python

import yaml

from yaml.loader import SafeLoader

with open(r'C:\Users\lenovo\OneDrive\Documents\2nd session\output.yaml', 'r') as f:
    data = list(yaml.load_all(f, Loader=SafeLoader))
    print(data)
user_details = {'UserName': 'Alice',
                'Password': 'star123*',
                'phone': 3256,
                'AccessKeys': ['EmployeeTable',
                               'SoftwaresList',
                               'HardwareList']}

with open(r'C:\Users\lenovo\OneDrive\Documents\2nd session\output.yaml', 'w') as f:
    data = yaml.dump(user_details, f, sort_keys=False, default_flow_style=False)
    print(data)
