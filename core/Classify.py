from xgboost.sklearn import XGBClassifier
from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.naive_bayes import MultinomialNB

def naive_bayes(x_train, x_test, y_train, y_test):
    mlt = MultinomialNB()
    mlt.fit(x_train, y_train)
    y_predict = mlt.predict(x_test)

    print("精确率为：", precision_score(y_test, y_predict))
    print("召回率为：", recall_score(y_test, y_predict))
    print("F1值为：", f1_score(y_test, y_predict))

def support_vector(x_train, x_test, y_train, y_test):
    svc = SVC()
    svc.fit(x_train, y_train)
    y_predict = svc.predict(x_test)

    print("精确率为：", precision_score(y_test, y_predict))
    print("召回率为：", recall_score(y_test, y_predict))
    print("F1值为：", f1_score(y_test, y_predict))

def xg_boost(x_train, x_test, y_train, y_test):
    xgb = XGBClassifier()
    xgb.fit(x_train, y_train)
    y_predict = xgb.predict(x_test)
    predictions = [round(value) for value in y_predict]

    print("精确率为：", precision_score(y_test, y_predict))
    print("召回率为：", recall_score(y_test, predictions))
    print("F1值为：", f1_score(y_test, predictions))