#!/usr/bin/python

import sys
import json
import requests
from prettytable import PrettyTable
import html
import unicodedata
from itertools import count
import textwrap

def get_json(url):
    #resp = requests.get(url, proxies={ 'https' : '134.238.252.143:8080'})
    resp = requests.get(url, verify=False)
    #json_resp = json.dumps(resp.json())
    return resp.json()

def unicode_len(s):
    try :
        return len([unicodedata.name(ch) for ch in s])
    except ValueError as e:
        return len(s)

def print_tabular(*args):
    tbl = PrettyTable()
    columns = ['Dev.','grammar','IAST','En. Word','En. Add']
    for idx, col, arg in zip(count(), columns, args):
        arg = [textwrap.fill(tokens, 35) for tokens in arg]
        tbl.add_column(col, arg)
        word_len = [unicode_len(word) for word in arg]
        max_len = max(word_len)
        #print(max_len)
        tbl._min_width[f'Column {idx}'] = max_len
    tbl.align[""] = "r"    
    #breakpoint()
    print(tbl)

def get_values(json, key, count, entity_code):
    val = []
    filtered_values = []
    word = sys.argv[2]
    for idx, x in enumerate(json["values"]):       
        if x['sk_grammar'].strip() != 'sent.' and x['en_word'].strip() == word:
            filtered_values.append(x)
    for idx, x in enumerate(filtered_values):
        if idx+1 <= count:
            if entity_code:
                word = html.unescape(x[key])
                val.append(word.strip())
            else:
                val.append(x[key])
    return val

def main():
    requests.packages.urllib3.disable_warnings()
    
    # if len(sys.argv) < 4:
    #     print("Usage: python script.py <count> <word> <exact>")
    #     sys.exit(1)

    count = sys.argv[1]
    count = int(count)
    word = sys.argv[2]
    try: 
        exact = sys.argv[3] 
    except:
        exact = 'false'
        
    URL = 'https://www.learnsanskrit.cc/getdata/word/gettranslation?word={word}&direction=au&{count}=0&exact=false'

    # URL = f'https://www.learnsanskrit.cc/getdata/word/gettranslation?word={word}&direction=au&count=0&exact={exact}'
    json_resp = get_json(URL)
    #breakpoint()
    dv_words = get_values(json_resp, 'dv_word', count, entity_code=True)
    iast_words = get_values(json_resp, 'ia_word', count, entity_code=True)
    sk_grammar = get_values(json_resp, 'sk_grammar', count, entity_code=False)
    en_words = get_values(json_resp, 'en_word', count, entity_code=False)
    en_adds = get_values(json_resp, 'en_add', count, entity_code=False)
    
    if dv_words or iast_words or sk_grammar or en_words:
        print_tabular(dv_words, sk_grammar, iast_words, en_words, en_adds)
    else:
        print("No matching results found for the given word.")
if __name__ == "__main__":
    main()
