#!/usr/bin/python3
result = ""
for i in range(65, 91):
    if i % 2 == 0:
        i += 32
        result += chr(i)
    else:
        result += chr(i)
print(result[::-1], end="")
