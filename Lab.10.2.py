file = open("output.txt", "w", encoding="utf-8")

text = ""

for i in range(1, 10):
    text = text + "а"
    file.write(text + "\n")

file.close()
