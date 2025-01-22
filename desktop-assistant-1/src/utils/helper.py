def format_time(time_obj):
    return time_obj.strftime("%H:%M:%S")

def format_date(date_obj):
    return date_obj.strftime("%Y-%m-%d")

def load_config(file_path):
    import json
    with open(file_path, 'r') as f:
        return json.load(f)

def save_config(file_path, config_data):
    import json
    with open(file_path, 'w') as f:
        json.dump(config_data, f, indent=4)

def validate_url(url):
    import re
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None