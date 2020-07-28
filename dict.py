import json

data = json.load(open("data.json"))


word = input("Enter word here: ")

def translate(word):
    if word in data:
        return data[word]


print(translate(word))
