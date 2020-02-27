from urllib import request
import json
import os
import hashlib


def problema1(sir):
    list = []
    for i in sir:
        try:
            int(i)
            list.append(i)
        except:
            print(i)
    print(len(list))
    return len(list)


def problema2(url):
    try:
        response = request.urlopen(url).read()
        text = json.loads(response.decode('utf-8'))
        list = text.keys()
        return len(list)
    except:
        print('here')


def problema3(url):
    list = []
    try:
        response = request.urlopen(url).read()
        text = str(response.decode('utf-8'))
        src = text.split('src')
        for index, text in enumerate(src):
            if 'img' in src[index - 1]:
                tag = src[index].split('="')
                for i in tag:
                    new_src = i.split('" ')
                    for new_i in new_src:
                        if 'http' in new_i:
                            list.append(new_i)
        return list

    except:
        print('here')


def problema4(my_path):
    for (root, directories, files) in os.walk(my_path):
        for fileName in files:
            full_fileName = os.path.join(root, fileName)
            file = os.open(full_fileName, os.O_RDONLY)
            print(file.to_bytes(100))


# problema4("./")

# problema3("https://pastebin.com/raw/QkBS3h4J")
