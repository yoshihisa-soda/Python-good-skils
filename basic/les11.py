count = 0

while count < 5:
    print(count)
    count += 1

while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue
    # ここは実行されない
    print(count)
    count += 1

