import urllib.request as req
import gzip, os, os.path

savepath = "./mnist"
baseurl = "http://yann.lecun.com/exdb/mnist"
files = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz"
]

# 다운로드
if not os.path.exists(savepath): os.mkdir(savepath)
for f in files:
    url = baseurl + "/" + f
    loc = savepath + "/" + f
    print("download:", url)
    if not os.path.exists(loc): req.urlretrieve(url, loc)

# GZip 압축 해제
for f in files:
    gz_file = savepath + "/" + f
    raw_file = savepath + "/" + f.replace(".gz", "")
    print("gzip:", f)
    with gzip.open(gz_file, "rb") as fp:
        body = fp.read()
        with open(raw_file, "wb") as w:
            w.write(body)
    print("ok")

# CSV 파일로 변환
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

