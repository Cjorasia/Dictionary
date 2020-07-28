import json

data = json.load(open("data.json"))


word = input("Enter word here: ")

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]

output = translate(word)
print("meaning-->")
if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)
