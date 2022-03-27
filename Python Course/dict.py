# Mariah	first_name
# Carey	last_name
# 27.03.1970 (מחרוזת)	birth_date
# Sing, Compose, Act(רשימה)	hobbies
import time

from functools import cached_property
from typing import Dict, Match

Dict = {"first_name": "Mariah",
        "last_name": "Carey",
        "birth_date": "27.03.1970",
        "hobbies": ["Sing", 'Compose', 'Act']
        }

while True:
    choice = int(input("choose an option "))
    if choice == 1:
        print(Dict["last_name"])
    elif choice == 2:
        print(Dict["birth_date"][3:5])
    elif choice == 3:
        print(len(Dict["hobbies"]))
    elif choice == 4:
        print(Dict["hobbies"][-1])
    elif choice == 5:
        Dict['hobbies'] += ['Cooking']
    elif choice == 6:
        new_tuple = tuple((Dict['birth_date'].split('.')))
        # new_tuple = tuple(new_tuple)
        print(new_tuple)
    elif choice == 7:
        new_key = 2021 - int(new_tuple[-1])
        Dict['Age'] = new_key
        print(Dict['Age'])
