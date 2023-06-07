import requests

from config import BASE_URL

f = open("delete.txt", "r")
line = f.readline()
f.close()
delete_lst = line.split(",")
for i in set(delete_lst):
    delete = requests.delete(url=BASE_URL + f"/{i}")
