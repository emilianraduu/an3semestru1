import os 

def search_by_content(target, to_search):
    target_file = open(target, 'r')
    files_containing_to_search = []
    if os.path.isfile(target):
        content = target_file.read()
        if to_search in content:
            if target_file.name not in files_containing_to_search:
                files_containing_to_search.append(target_file.name)
    else:
        print('idk')
    print(files_containing_to_search)
    target_file.close()

search_by_content('../Laborator 2/', 'input()')