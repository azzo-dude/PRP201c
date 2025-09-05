import json
import csv

'----------------Read from file-----------------'
def read_file_object_json(filepath: str):
  with open(path, 'r', encoding="utf-8") as file:
    return json.load(file)

def read_file_object_text(filepath: str):
  with open(path, 'r', encoding="utf-8") as file:
    return file.read()

def read_file_object_csv(filepath: str):
  with open(path, 'r', encoding="utf-8") as file:
    return csv.reader(file)
'-----------------------------------------------'
