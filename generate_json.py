import random

from config import n
from utils.generate_func import custom_dict
from utils.utils import TAGS
from utils.utils import IMAGE, CATEGORY, STATUS

body = {
    "id": 0,
    "category": {"id": 0, "name": "string"},
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [{"id": 0, "name": "string"}],
    "status": "available",
}
JSON = []
CUSTOM_JSON = []
for i in range(n):
    body = {
        "id": random.randint(1, 15),
        "category": random.choice(CATEGORY),
        "name": "doggie + " + str(i),
        "photoUrls": random.choice(IMAGE),
        "tags": random.choice(TAGS),
        "status": random.choice(STATUS),
    }
    JSON.append(body)

for i in range(n):
    body = custom_dict(
        id=random.randint(1, 15),
        category=random.choice(CATEGORY),
        name="doggie + " + str(i),
        photoUrls=random.choice(IMAGE),
        tags=random.choice(TAGS),
        status=random.choice(STATUS),
    )
    CUSTOM_JSON.append(body)
