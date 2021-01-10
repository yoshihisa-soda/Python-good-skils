# input()はwhileと一緒によく使用する

while True:
    word = input('Enter')
    num = int(word)
    if num == 100:
        break
    print('next')

