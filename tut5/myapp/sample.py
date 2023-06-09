import json


def save_dict(_dcit, filepath):
    json.dump(_dcit, open(filepath, 'w', encoding='UTF-8'))
    print("saved")
