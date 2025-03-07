from collections import deque

N, K = map(int, input().split())
que=deque(range(1, N+1))

result = []

while que:
    que.rotate(-(K-1))
    result.append(que.popleft())

print("<" + ", ".join(map(str, result)) + ">")