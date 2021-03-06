def solution(new_id):
    special_characters = "~!@#$%^&*()=+[{]}:?,<>/"
    
    # step 1
    new_id = new_id.lower()
    
    # step 2
    for c in range(len(special_characters)):
        new_id = new_id.replace(special_characters[c], "")
    
    # step 3
    while ".." in new_id:
        new_id = new_id.replace("..", ".")    
    
    # step 4
    new_id = new_id.strip(".")
    # if len(new_id) >= 1 and new_id[-1] == ".": new_id = new_id.rstrip(".")
    # if len(new_id) >= 1 and new_id[0] == ".": new_id = new_id.lstrip(".")
    
    # step 5
    if len(new_id) == 0: new_id = "a"
    
    # step 6
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    if new_id[-1] == ".":
        new_id = new_id[0:-1]
    
    # step 7
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id

# 정규 표현식 활용
'''
import re

def solution(new_id):
    id = new_id
    
    id = id.lower()                         # 1
    id = re.sub("[^a-z0-9-_.]", "", id)     # 2
    id = re.sub("\.{2,}", ".", id)          # 3
    # id = re.sub("\.+", ".", id)           # 3
    id = re.sub("^[.]|[.]$", "", id)        # 4
    id = "a" if len(id) == 0 else id[:15]   # 5, 6-1
    id = re.sub("[.]$", "", id)             # 6-2
    id = id if len(id) > 2 else id + "".join(id[-1] for _ in range(3 - len(id))) # 7
    
    return id
'''