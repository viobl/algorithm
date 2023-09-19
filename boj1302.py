import sys
input = sys.stdin.readline
n = int(input())
bookList = dict()

for _ in range(n):
    title = input().rstrip()
    if title in bookList:
        bookList[title] += 1
    else:
        bookList[title] = 1

cnt = 0
sortBook = dict(sorted(bookList.items()))
for i in sortBook:
    if sortBook[i] > cnt:
        cnt =sortBook[i]
        max = i

print(max)