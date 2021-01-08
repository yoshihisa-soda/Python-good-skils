# 集合

a = {1, 2, 3, 4, 5}
b = {2, 3, 4}
print(a - b)

# 論理積
print(a & b)
# 論理和
print(a | b)
# 排他的論理和
print(a ^ b)

s = {1, 2, 3, 4, 5, 6}
s.add(7)
s.remove(7)
s.clear()

my_friends = {'A', 'B', 'C'}
A_friends = {'B', 'C', 'E', 'F'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)