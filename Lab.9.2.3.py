s = input()

if len(s) <= 3:
    print(s)
else:
    parts = []
    while s:
        parts.append(s[-3:])
        s = s[:-3]
    print(" ".join(parts[::-1]))