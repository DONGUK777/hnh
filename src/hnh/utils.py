import requests
import json

def get_max_label(p):
    max_score = 0
    max_label = ""
    #data = get_api()
    for i in p:
        if i['score'] > max_score:
            max_score = i['score']
            max_label = i['label']
    return max_label

def get_max_score(p):
    max_score = 0
    max_label = ""
    #data = get_api()
    for i in p:
        if i['score'] > max_score:
            max_score = i['score']
            max_label = i['label']
    return max_score

def get_label(p):
    win_label = get_max_label(p)
    win_score = get_max_score(p)
    
    if win_label == "hot dog" and win_score >= 0.8:
        last_label = "hot dog"
        return {"label" : last_label, "score": win_score}
    else:
        last_label = "not hot dog"
        return {"label": last_label, "score": win_score}

#def get_max_score2():
#    max_p = max(p, key=get_score)
#    return max_p
#
#def get_max_score3():
#    max_p = max(p, key=lambda x: x['score'])
#    print(max_p)
#    return max_p

