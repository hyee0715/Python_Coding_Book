n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0

for i in range(0, len(data) - 1):
    for j in range(i, len(data)):
        if data[i] != data[j]:
            result += 1
print(result)