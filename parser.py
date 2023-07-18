import json
import re
import sys

# Open the JSON file
with open(sys.argv[1]) as file:
    # Load the JSON data into a Python object
    data = json.load(file)

# Access the data

rules = data["runs"][0]["tool"]["driver"]["rules"]
results = data["runs"][0]["results"]

map = {}
for res in results:
	map[res["ruleId"]] = ""

for rule in rules:
	sd = rule["shortDescription"]["text"]
	sd = re.sub(r".*\(","", sd)
	sd = re.sub(r"\)", "", sd)
	map[rule["id"]] = sd

for res in data["runs"][0]["results"]:
	id = res["ruleId"]
	if id in map:
		res["level"] = map[id]
print(json.dumps(data))
