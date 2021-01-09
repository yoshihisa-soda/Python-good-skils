y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')


a = 1
b = 1
# あまり使わない
if not a == b:
    print('Not equal')

if a != b:
    print('Not equal')

# notはboolean型の時に良く使う
# False : False, 0, 0.0, '', [], (), {}, set()

is_ok = True
is_ok = 1

if not is_ok:
    print('No')
else:
    print('OK')


