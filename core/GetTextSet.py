import os
import json

user_label = [] # 用户标签
user_list = []  # 用户全体
index = 0       # 标记用户序号

# depression2017
# 遍历文件
def list_file(folder_path_1, folder_path_2):
    global index

    for file_name in os.listdir(folder_path_1):
        user_label.append(-1)

        post_list = [] # 用户发言
        user_list.append(post_list)

        read_text(folder_path_1 + "\\" + file_name)

        index = index + 1
    for file_name in os.listdir(folder_path_2):
        user_label.append(1)

        post_list = []
        user_list.append(post_list)

        read_text(folder_path_2 + "\\" + file_name)

        index = index + 1

    return user_label, user_list

# 读取文本
def read_text(file_path):
    text = open(file_path, 'r', encoding='UTF-8')
    line = text.readline()
    while line:
        if (len(line.strip()) != 0):
            user_list[index].append(line)
        line = text.readline()
    text.close()

# RSDD
# 读取文本
def read_text_r(file_path):
    text = open(file_path, 'r', encoding='UTF-8')
    line = text.readline()
    global index
    while line:
        if (len(line.strip()) != 0):
            setting = json.loads(line[1:-2])
            posts = setting['posts']
            label = setting['label']

            lable_r(label, posts)

            index = index + 1
            line = text.readline()

        if (index == 1000):
            break

    return user_label, user_list

# 添加至标签
def lable_r(label, posts):
    if (label == "control"):
        user_label.append(-1)
        list_r(posts)
    elif (label == "depression"):
        user_label.append(1)
        list_r(posts)

# 添加至全体
def list_r(posts):
    post_list = []
    for post in posts:
        post_list.append(post[1])
    user_list.append(post_list)

