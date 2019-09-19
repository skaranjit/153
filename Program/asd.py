l = [1, 2, 3, '', 4, '', '', 5]
y = []
x = l
for i in l:
    if i != '':
        y.append(i)
    else:
        print(i)

    print(x)
print(l)
print(y)
