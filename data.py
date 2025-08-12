
import requests


dictionary = {
    "amount" : 10,
    "type" : "boolean"
}
ew = requests.get(url="https://opentdb.com/api.php",params=dictionary)
ew.raise_for_status()
question_data = ew.json()["results"]



