from textblob import TextBlob
import GetTextSet
import re

def get_additional(user_list):
    temp_list = []
    index = 0
    for post_list in user_list:
        # 消极情感占比
        i1 = 0
        avarage1 = 0
        # 主观情感占比
        i2 = 0
        avarage2 = 0
        # 单词数量
        i3 = 0
        # 词汇量
        i4 = 0
        words = []
        # 临时列表
        temp = []

        for post in post_list:
            polarity = TextBlob(post)
            if(float(polarity.sentiment[0]) < 0):
                i1 = i1 + 1
            if(float(polarity.sentiment[1]) == 0):
                i2 = i2 + 1

            word_list = post.split(' ')
            i3 = (i3 + len(word_list)) / 2

            for word in post.split(" "):
                word = re.sub("[\s+\.\!?\/_,$%^*()+\"\']+|[+——！，。？、~@#￥%……&*（）]+".encode('utf-8').decode('utf-8'), "".encode('utf-8').decode('utf-8'), word)
                word = word.lower()
                words.append(word)
            map = {}
            for word in words:
                map[word] = map[word] + 1 if word in map.keys() else 1
            i4 = len(map)

        avarage1 = (i1/len(post_list))
        avarage2 = (i2/len(post_list))

        temp.append(avarage1)
        temp.append(avarage2)
        temp.append(i3)
        temp.append(i4)
        temp_list.append(temp)

        print(index)
        index = index + 1

    file = open('temp_list.txt', 'w')
    file.write(str(temp_list))
    file.close()

def main():
    negative = "D:\\Workspace\\textprocess\\docs\\negative"
    positive = "D:\\Workspace\\textprocess\\docs\\positive"
    user_label, user_list = GetTextSet.list_file(negative,positive)

    get_additional(user_list)

if __name__ == '__main__':
    main()