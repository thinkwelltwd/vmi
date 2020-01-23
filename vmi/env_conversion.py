from decimal import Decimal


TRUE_LIST = [1, "1", "true", "True", "TRUE", "YES", "Yes", "yes", True]
FALSE_LIST = [0, "0", "False", "FALSE", "false", "NO", "No", "no", False]


def bool_env(env_val=None):
    """ check for boolean values """

    if env_val:
        if env_val in TRUE_LIST:
            return True
        else:
            if isinstance(env_val, str):
                if env_val.lower() in TRUE_LIST:
                    return True
            return False
    else:
        return False


def int_env(env_val):
    """ convert to integer from String """
    try:
        return int(Decimal(float(env_val)))
    except ValueError:
        return

def filter_list_to_tuple(env_val, source_list, blank_option=None):
    """ filter list using env_val to create tuple
        Split is performed on space so need to pass empty tuple
        in as optional blank_option parameter
        eg. ('', 'No Identity Assurance Evidence')
    """

    if env_val != "":
        pi = env_val.split(" ")

        list_for_tupling = []

        for i in pi:
            for c in source_list:
                if i == c[0]:
                    list_for_tupling.append((c[0], c[1]))
        if blank_option:
            list_for_tupling.append(blank_option)

    else:
        list_for_tupling = source_list

    return tuple(list_for_tupling)
