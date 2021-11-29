data = input()
list = [0] * 2 # 0과 1이 붙어있는 그룹 개수

for i in range(1, len(data)):
    if data[i - 1] != data[i] or i == len(data) - 1:
        list[int(data[i - 1])] += 1

if list[0] > list[1]:
    print(list[1])
else:
    print(list[0])

