import json

def Custom(filename, userid, a, b):
    with open(f"{filename}.json", 'r', encoding="UTF8") as f:
        Data = json.load(f)
    Data[str(userid)] = {
        str(a) : str(b)
    }
    def save(data):
        with open(f'{filename}.json', 'w', encoding='utf-8') as t:
            json.dump(data, t, indent="\t", ensure_ascii=False)
    save(Data)