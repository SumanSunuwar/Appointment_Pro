import yaml


def yaml_coerce(value):
    # YAML file/values into a Python list of dictionaries
    if isinstance(value, str):
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']
    return value
