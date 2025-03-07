import sys

ST=[]
K = int(sys.stdin.readline())

for _ in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        ST.pop(-1)
    else:
        ST.append(num)

print(sum(ST))