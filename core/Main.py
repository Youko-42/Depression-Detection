import GetTextSet
import GetFeauture
import Classify
import time

user_label = [] # 用户标签
user_list = []  # 训练用户全体

def main():
    start = time.time()

    # depression2017
    negative = "D:\\Workspace\\textprocess\\docs\\negative"
    positive = "D:\\Workspace\\textprocess\\docs\\positive"
    user_label, user_list = GetTextSet.list_file(negative,positive)

    # RSDD
    #train = "D:\\Workspace\\textprocess\\docs\\RSDD"
    #user_label, user_list = GetTextSet.read_text_r(train)

    x_train, x_test, y_train, y_test = GetFeauture.count_vec(user_list, user_label)
    #x_train, x_test, y_train, y_test = GetFeauture.tf_idf(user_list, user_label)
    #x_train, x_test, y_train, y_test = GetFeauture.count_tfidf(user_list, user_label)
    #x_train, x_test, y_train, y_test = GetFeauture.additional(user_label)

    Classify.naive_bayes(x_train, x_test, y_train, y_test)
    #Classify.support_vector(x_train, x_test, y_train, y_test)
    #Classify.xg_boost(x_train, x_test, y_train, y_test)

    end = time.time()
    print("运行时间：", (end - start))

if __name__ == '__main__':
    main()