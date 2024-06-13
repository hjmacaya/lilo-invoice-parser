from pprint import pprint
import json

with open("backup.json", "r") as json_file:
    result_dict = json.load(json_file)
    pprint(result_dict)
