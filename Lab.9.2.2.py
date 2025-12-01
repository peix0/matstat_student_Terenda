n = input()
d = input()

pos = n[::-1].find(d)

if pos == -1:
    print(0)
else:
    print(pos + 1)