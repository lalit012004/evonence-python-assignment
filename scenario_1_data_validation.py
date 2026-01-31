def validate_data(data):
    invalid_entries = []
    for item in data:
        if "age" not in item or not isinstance(item["age"], int):
            invalid_entries.append(item)
    return invalid_entries
