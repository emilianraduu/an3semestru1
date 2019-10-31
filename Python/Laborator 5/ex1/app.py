from utils import process_item

if __name__ == '__main__':
    while True:
        try:
            x = input('Insert a number : ')
            if x=='q':
                break
            else:
                x=int(x)
                print(process_item(x))
        except:
            print('[ERROR] INSERT A VALID NUMBER')
else:
    print('[APP MODULE LOADED]')
