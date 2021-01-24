# ファイルの書き込みモード

s="""\
AAA
BBB
CCC
DDD
"""

# 'w' : 書き込み, 'w+' : 書き込み+読み込み
with open('test.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f,read())

# 'r' : 読み込み, 'r+' : 読み込み+書き込み
with open('test.txt', 'r+') as f:
    print(f, read())
    f.seek(0)
    f.write(s)

