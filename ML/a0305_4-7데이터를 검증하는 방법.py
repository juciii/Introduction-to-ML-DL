# 크로스 밸리데이션 => 교차검증
from sklearn import svm, metrics
import random, re

# 붓꽃의 CSV 파일 읽어 들이기
lines = open('iris.csv','r',encoding='utf-8').read().split("\n")
f_tonum = lambda n: float(n) if re.match(r'^[0-9\.]+$', n) else n
f_cols = lambda li: list(map(f_tonum,li.strip().split(',')))
csv = list(map(f_cols, lines))
del csv[0] # 헤어 제거하기
random.shuffle(csv) # 데이터 섞기

# 데이터를 k개로 분할하기
k=5
csvk = [ [] for i in range(k)]
#print(len(csv)) #150
for i in range(len(csv)):
    csvk[i % k].append(csv[i])
# print(csvk) # 30개의 list가 있는 list가 5개 형성된다.
# 리스트를 훈련 전용 데이터와 테스트 전용 데이터로 분할하는 함수
def split_data_label(rows):
    data = []; label = []
    for row in rows:
        data.append(row[0:4])
        label.append(row[4])
    return(data, label)

# 정답률 구하기
def calc_score(test, train):
    test_f, test_l = split_data_label(test)
    train_f, train_l = split_data_label(train)
    # 학습시키고 정답률 구하기
    clf = svm.SVC()
    clf.fit(train_f, train_l)
    pre = clf.predict(test_f)
    return metrics.accuracy_score(test_l, pre)

# k개로 분할해서 정답률 구하기
score_list = []
for testc in csvk:
    # testc 이외의 데이ㅓ를 훈련 전용 데이터로 사용하기
    trainc = []
    for i in csvk:
        if i != testc: trainc += i
    sc = calc_score(testc, trainc)
    score_list.append(sc)
print("각각의 정답률 =", score_list)
print("평균 정답률 =", sum(score_list) / len(score_list))

####################################
# scikit-learn의 크로스 밸리데이션
import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re

# 붓꽃의 csv 읽어들이기
csv = pd.read_csv("iris.csv")

# 리스트를 훈련 전용 데이터와 테스트 전용 데이터로 분할하기
data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
label = csv["Name"]

# 크로스 밸리데이션하기
clf = svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("각각의 정답률=", scores)
print("평균 정답률=", scores.mean())

########################################
import pandas as pd
from sklearn import model_selection, svm, metrics
from sklearn.grid_search import GridSearchCV

# MNIST 학습 데이터 읽어들이기
train_csv = pd.read_csv("./mnist/train.csv")
test_csv = pd.read_csv("./mnist/t10k.csv")

# 필요한 열 추출하기
train_label = train_csv.ix[:, 0]
train_data = train_csv.ox[:, 1:]
test_label = test_csv.ix[:, 0]
test_data = test_csv.ix[:, 1:]
print("학습 데이터의 수 =", len(train_label))

# 그리드 서치 매개변수 설정
params = [
    {"C": [1,10,100,1000], "kernel":["linear"]},
    {"C": [1,10,100,1000], "kernel":["rbf"], "gamma":[0.001, 0.0001]}
]

# 그리드 서치 수행
clf = GridSearchCV( svm.SVC(), params, n_jobs=-1)
clf.fit(train_data, train_label)
print("학습기 =", clf.best_estimator_)

# 테스트 데이터 확인하기
pre = clf.predict(test_data)
ac_score = metrics.accuracy_score(pre, test_label)
print("정답률=", ac_score)



