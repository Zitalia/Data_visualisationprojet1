import unidecode

def normalize_label(s):
    s = s.split(' ')[0]
    s = s.split('/')[0]
    s = s.lower()
    s = unidecode.unidecode(s)
    s = s.replace('[', '')
    s = s.replace(']', '')
    s = s.replace(':', '')
    return s.strip()

def add_to_dict(_dict, key, value, add_if_not_exist=True):
    if key not in _dict.keys() and add_if_not_exist:
        _dict.update({key : 0})
        _dict[key] += value
    else:
        _dict[key] += value

