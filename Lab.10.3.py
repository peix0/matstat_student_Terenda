import matplotlib.pyplot as plt

file = open("lab.txt", "r", encoding="utf-8")
text = file.read()
file.close()

vowels = "aeiou"

counts = {}
text = text.lower()

for ch in text:
    if ch in vowels:
        if ch not in counts:
            counts[ch] = 0
        counts[ch] += 1

plt.bar(counts.keys(), counts.values())
plt.xlabel("Vowels")
plt.ylabel("Count")
plt.title("Frequency of Vowels in Text")

plt.savefig("histogram.png")
