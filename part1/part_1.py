import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

with open("forecast_5days_a.json") as json_file:
    reader = json.reader(json_file)
    for line in reader:
        DEGREE_SYBMOL.append(line)
