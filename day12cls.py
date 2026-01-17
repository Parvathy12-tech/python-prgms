import json
from datetime import datetime
from tracker import create_record

records = [
    create_record("Paris", "Saw the Eiffel Tower", "05-06-2022"),
    create_record("Rome", "Visited the Colosseum", "15-07-2023"),
    create_record("Tokyo", "Enjoyed sushi and cherry blossoms", "10-04-2024")
]


for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")


json_data = json.dumps(records, indent=4)
print("JSON Output:\n", json_data)


parsed_records = json.loads(json_data)

print("\nParsed Records:")
for rec in parsed_records:
    print(rec)