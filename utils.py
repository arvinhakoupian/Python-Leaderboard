def argument_error(command_name, args, expected_count):
    if len(args) != expected_count:
        raise ValueError(f"{command_name} expects {expected_count} argument(s)")


def parse_int(value, field_name):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"{field_name} must be an integer")
