import random
import requests
import urllib3

from config import n, BASE_URL
from generate_json import JSON

urllib3.disable_warnings()
CREATE_ID = []
for i in random.sample(JSON, n):
    create = requests.post(url=BASE_URL, json=i, verify=False)
    CREATE_ID.append(str(create.json()["id"]))
with open("delete.txt", "a") as f:
    f.write(",".join(CREATE_ID))
