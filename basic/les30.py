# 例外処理

l = [1, 2, 3]
i = 5


try:
    l[i]

# エラーをキャッチ
except IndexError as ex:
    print("Don't worry : {}".format(ex))

else:
    print('done')

# 必ず最後に実行される
finally:
    print('clean up')