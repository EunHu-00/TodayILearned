import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque([i for i in range(1, N+1)])

while( len(que) > 1):
    que.popleft()
    num = que.popleft()
    que.append(num)


print(que[0])