numbers = list(map(int, input()))
result = 0
for number in numbers:
    if result * number > result + number:
        result = result * number
    else:
        result = result + number
print(result)
