#기계 학습 대상 만듬
clf=svm.SVC()
#데이터와 답을 넣기 -> 어떤 형태로 데이터를 가공할 것인가?
clf.fit(data, label)
#예측
predict=clf.predict()
#정답률을 구하기 위함
score=metrics.accuracy_score()
print("정답률:", score)

# 150p
# XOR 연산을 학습하는 프로그램

# 152p
# 프레임워크

# 155p
# 붓꽃 품종 분류하기

# 163p
# CSV파일 만들기
# 모르겠뜸...
import struct

def to_csv(name, maxdata):
    lbl_f = open("./mnist/" + name + "-labels-idx1-ubyte", "rb")
    img_f = open("./mnist/" + name + "-images-idx3-ubyte", "rb")
    csv_f = open("./mnist/" + name + ".csv", "w", encoding="utf-8")

    mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
    mag, img_count = struct.unpack(">II", img_f.read(8))
    rows, cols = struct.unpack(">II", img_f.read(8))
    pixels = rows * cols
    res = []
    for idx in range(lbl_count):
        if idx > maxdata:
            break
        label = struct.unpack("B", lbl_f.read(1))[0]
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(str(label)+",")
        csv_f.write(",".join(sdata)+"\r\n")

        if idx < 10:
            s = "P2 28 28 255\n"
            s += " ".join(sdata)
            iname = "./mnist/{0}-{1}-{2}.pgm".format(name,idx,label)

            with open(iname, "w", encoding="utf-8") as f:
                f.write(s)

    csv_f.close()
    lbl_f.close()
    img_f.close()


to_csv("train", 1000)
to_csv("t10k", 500)



# 165P
from sklearn import svm, metrics
import pandas

train_csv=pandas.read_csv("./mnist/train.csv", header=None)
tk_csv=pandas.read_csv("./mnist/t10k.csv",  header=None)

# map(함수, 데이터)이라는 함수에서 함수는 0부터 1사이의 숫자만 나와야해.
# test()라는 함수를 거치면 0부터 1사이의 숫자만 나와야해.
def test(l) :
    output=[]
    for i in l:
        output.append(float(i)/256)
    return output

#iloc -> 선택하고자 하는 범위 설정
#이터러블(반복문 등으로 가능한 여러 개의 values) 이기 때문에 list로 강제 변환해야함
train_csv_data=list(map(test, train_csv.iloc[:,1:].values)) # [:(== 모든 row) , 1:(==1번째 이후에 있는 데이터)]
tk_csv_data=list(map(test, tk_csv.iloc[:,1:].values))

#첫번째 열 = 정답
train_csv_label=train_csv[0].values
tk_csv_label= tk_csv[0].values

# 진영이가 보내준 사진 파일 보고 코드짜기
# 세개씩 묶으면 정답이 코드로 보여

# print(tk_csv_data)

clf=svm.SVC(gamma='auto')
#vector표현 시 fit method의 첫번째 매개변수는 0과 1사이여야 함 -> map 이용!!
clf.fit(train_csv_data, train_csv_label)
predict=clf.predict(tk_csv_data)
score=metrics.accuracy_score(tk_csv_label, predict)
print("정답률:", score)


