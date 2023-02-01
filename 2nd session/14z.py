num = [1, 2, 3, 4]
name = ['satya', 'krishna', 'siva', 'sunil']
zl= zip(num, name)
zl = list(zl)
print(zl)
num, name = zip(*zl)
print(num)
print(name)