from itertools import permutations
import requests
import json

def is_word(word_id):
    """To verify word exists or not"""
    app_id = '0ff925b1'
    app_key = '485e9909480d5a4933185d19f61a4232'
    language = 'en'
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/inflections/' + language + '/' + word_id.lower()
    
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    # print("code {}\n".format(r.status_code))
    # print("text \n" + r.text)
    result = r.json()
    print("request: " + r.text)
    #return result["metadata"]["total"]
    

def main():
    letters = list(input().split(" "))
    wletters = list(permutations(letters))
    print(wletters)
    words = set()
    for i in wletters:
        word = ""
        for j in i:
            word += j
            if is_word(word) > 0:
                words.add(word)
    print("Words Found:" + len(words))
    print(words)
    
main()
# print(is_word("ab"))