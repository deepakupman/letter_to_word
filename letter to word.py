from itertools import permutations
import requests
import json
def is_word(word_id):
    """To verify word exists or not"""
    app_id = '0ff925b1'
    app_key = '485e9909480d5a4933185d19f61a4232'
    
    language = 'en'
    
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/search/' + language + '?q=' + word_id.lower() + '&prefix=true'
    
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    print('requests: ' + r)
    print("code {}\n".format(r.status_code))
    print("text \n" + r.text)
    print("json \n" + json.dumps(r.json()))

def main():
    letters = list(input().split(" "))
    
    wletters = list(permutations(letters))
    
    words = set()
    
    for i in wletters:
        word = ""
        for j in i:
            word += j
            words.add(word)
    print(words)
    
# main()
is_word("Hello")