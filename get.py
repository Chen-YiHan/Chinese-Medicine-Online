import json
from pathlib import Path
import time

with open("./data.json", "r") as f:
    dic = json.load(f)
d_list = []
name_list = []
for k, v in dic.items():
    d_list.append([k, v])
    name_list.append(k)


with open("./questions.json", "r") as f:
    ques = json.load(f)


def get_page(page):
    page = abs(page % len(d_list))
    content = d_list[page]
    name = content[0]
    cont = content[1]
    # print(page, name)
    return (name, cont["种植"], cont["炮制"], cont["药性"], cont["主治"])

def get_len():
    return len(dic)

def get_dic():
    return dic

def get_value(name):
    return dic[name]

def get_name_list():
    return name_list

def checkin(idx, name):
    if Path(f"./time.json").exists():
        with open("./time.json", "r") as idf:
            iddic = json.load(idf)
            if idx in iddic and iddic[idx]["name"] == name: return True
            else: return False
    else:
        with open("./time.json", "w") as idf:
            json.dump({idx : { "name" : name, "time" : 0}}, idf)
            return True

def conflict_check(idx, name):
    with open("./time.json", "r") as idf:
        iddic = json.load(idf)
        if idx in iddic: return False
        else:
            iddic[idx] = { "name" : name, "time" : 0}
    with open("./time.json", "w") as idf:
        json.dump(iddic, idf)
        return True

def get_time(idx):
    with open("./time.json", "r") as idf:
        iddic = json.load(idf)
        return iddic[idx]["time"]

def save_time(idx, time):
    with open("./time.json", "r") as idf:
        iddic = json.load(idf)
    iddic[idx]["time"] = time
    with open("./time.json", "w") as idf:
        json.dump(iddic, idf)

def get_idx_time():
    with open("./time.json", "r") as idf:
        iddic = json.load(idf)
    return iddic

def get_ques(idx):
    return ques[idx]

def save_score(id, score):
    if Path(f"./examination.json").exists():
        with open("./examination.json", "r") as exf:
            exdic = json.load(exf)
        exdic[time.asctime(time.localtime(time.time()))] = {"id" : id, "score" : score}
        with open("./examination.json", "w") as exf:
            json.dump(exdic, exf)
            return
    else:
        exdic = {}
        exdic[time.asctime(time.localtime(time.time()))] = {"id" : id, "score" : score}
        with open("./examination.json", "w") as exf:
            json.dump(exdic, exf)
            return

def get_exam():
    with open("./examination.json", "r") as exf:
        exdic = json.load(exf)
    return exdic