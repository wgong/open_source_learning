# coding: utf-8
def sort_dict_by_key(d, reverse=False):
    return [(k, d[k]) for k in sorted(d, reverse=reverse)]
        
def sort_dict_by_val(d, reverse=False):
    return [(d[k], k) for k in sorted(d, key=d.get, reverse=reverse)]

def dict2list(d):
    return [(k,v) for k,v in d.items()]

if __name__ == '__main__':
    dic = {'system': 4, 'time': 5, 'computer': 2, 'survey': 7, 'response': 6, 'eps': 8, 'graph': 10, 'user': 3, 'human': 1, 'trees': 9, 'minors': 11, 'interface': 0}
    print(dict2list(dic))
    print(sort_dict_by_key(dic, True))
    print(sort_dict_by_val(dic))


