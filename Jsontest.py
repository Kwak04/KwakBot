import json

item = ["a", "b"]

data = {
    item[0]: {
        "name": "kwak",
        "bot": "kwakbot"
    },
    item[1]: {
        "name": "choi",
        "bot": "thinkingbot"
    }
}

with open("testJson.json", "w") as write:
    json.dump(data, write, ensure_ascii=False)

with open("testJson.json", "r") as read:
    datafile = json.load(read)

print(datafile)

for i in range(2):
    print(datafile[item[i]]["name"])
