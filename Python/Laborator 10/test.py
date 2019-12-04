from datetime import datetime
import sys


def problema1():
    d1 = datetime.strptime(sys.argv[1], "%m/%d/%Y")
    d2 = datetime.strptime(sys.argv[2], "%m/%d/%Y")
    return (d1 - d2).days


def problema2():
    sorted_date_list = []
    for i in range(1,len(sys.argv)):
        d = datetime.strptime(sys.argv[i],'%m/%d/%Y_%H.%M.%S')
        d= d.strftime('%Y-%m-%d %H:%M:%S')
        sorted_date_list.append(d)
    sorted_date_list = sorted(sorted_date_list,reverse=True)
    min = datetime.strptime(sorted_date_list[len(sorted_date_list)-1],'%Y-%m-%d %H:%M:%S')
    max = datetime.strptime(sorted_date_list[0],'%Y-%m-%d %H:%M:%S')
    return(sorted_date_list, int((max-min).total_seconds()))


