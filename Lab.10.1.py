B = [3, -1, 5, 0, -4, 0.5, 7, -2, 16, -9]

last_positive_index = -1
for i in range(len(B)):
    if B[i] > 0:
        last_positive_index = i

if last_positive_index == -1:
    print("There are no positive elements in the list.")
else:
    result = sum(B[:last_positive_index + 1])
    print("List:", B)
    print("Index of the last positive element:", last_positive_index)
    print("Sum of elements up to it (inclusive) =", result)
    