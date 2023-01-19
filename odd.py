import sys
input = sys.stdin.readline()

list = []

for i in range(7):
    number = int(input())

    if number %2 == 1:
        list.append(number)

    if list:
        print(sum(list))
        print(min(list))

    else:
        print(-1)