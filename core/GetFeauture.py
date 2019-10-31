from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csc_matrix
import scipy.sparse
import numpy as np

# 工具
def gather(user_list, user_label):
    user_list_gather = []
    for post_list in user_list:
        temp = ""
        for post in post_list:
            temp = temp + post
        user_list_gather.append(temp)

    x_train, x_test, y_train, y_test = train_test_split(user_list_gather, user_label, test_size=0.25, random_state = 0)
    return x_train, x_test, y_train, y_test

def organize(original_list):
    data = []
    for original in original_list:
        data_list = []
        original = original[0:-1]
        temp_list = original.split(',')
        for temp in temp_list:
            temp = float(temp)
            data_list.append(temp)
        data.append(data_list)

    data_nd = np.array(data)
    data_csr = scipy.sparse.csr.csr_matrix(data_nd)
    return data_csr

def count_vec(user_list, user_label):
    x_train, x_test, y_train, y_test = gather(user_list, user_label)

    count = CountVectorizer(stop_words='english')
    x_train = count.fit_transform(x_train)
    x_test = count.transform(x_test)

    return x_train, x_test, y_train, y_test

def tf_idf(user_list,user_label):
    x_train, x_test, y_train, y_test = gather(user_list, user_label)

    tfidf = TfidfVectorizer(stop_words='english')
    x_train = tfidf.fit_transform(x_train)
    x_test = tfidf.transform(x_test)

    return x_train, x_test, y_train, y_test

def additional(user_label):
    text = open("D:\\Workspace\\textprocess\\docs\\temp_list.txt", 'r', encoding='UTF-8')
    line = text.readline()

    user_list = line.split(', [')
    x_train, x_test, y_train, y_test = train_test_split(user_list[1:], user_label, test_size=0.25, random_state = 0)
    x_train = organize(x_train)
    x_test = organize(x_test)

    return x_train, x_test, y_train, y_test

# 组合
def count_tfidf(user_list, user_label):
    x_train, x_test, y_train, y_test = gather(user_list, user_label)

    count = CountVectorizer(stop_words='english')
    train_count = count.fit_transform(x_train)
    test_count = count.transform(x_test)

    tfidf = TfidfVectorizer(stop_words='english')
    train_tfidf = tfidf.fit_transform(x_train)
    tes_tfidf = tfidf.transform(x_test)

    x_train = scipy.sparse.hstack([train_count, train_tfidf])
    x_test = scipy.sparse.hstack([test_count, tes_tfidf])

    return x_train, x_test, y_train, y_test
