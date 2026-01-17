import json
from datetime import datetime
from tripdata import get_trip

trips = [
    get_trip("Paris", "15-05-2023", "Visited the Eiffel Tower"),
    get_trip("Rome", "20-06-2023", "Explored the Colosseum"),
    get_trip("Tokyo", "10-07-2023", "Enjoyed sushi and cherry blossoms")
]

for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")

json_output = json.dumps(trips, indent=4)
print(json_output)