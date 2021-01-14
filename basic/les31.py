# 独自例外の作成

class UppercaseError(Exception):
    pass

def check():
    words = ['apple', 'banana', 'orange']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')