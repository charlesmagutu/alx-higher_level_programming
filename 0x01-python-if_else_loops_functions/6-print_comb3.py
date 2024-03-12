#!/usr/bin/python3
print("01", end="")
for i in range(2, 10):
    for j in range(i + 1, 10):
        print(", {:02d}".format(int(str(i) + str(j))), end="")
print()
