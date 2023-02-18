import re


class partOne():


    def __init__(self):
        pass


if __name__ == "__main__":

    name = "pg100.txt"
    handle = open(name)
    dic = dict()

    for lines in handle:
        for line in lines.split():
            y = re.sub('[^A-Za-z0-9]+', '', line)

            if y in dic.keys():
                dic[y] += 1
            else:
                dic[y] = 1

    sortedDic= sorted(dic.items(), key=lambda x:x[1], reverse=True)[:10]

    for word, count in sortedDic:
        print (word + " -> " + str(count) + " times")



   


