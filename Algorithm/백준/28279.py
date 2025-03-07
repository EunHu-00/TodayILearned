from collections import deque
import sys

que = deque()

for _ in range(int(input())):
    com = sys.stdin.readline().split()

    if com[0] == '1':
        que.appendleft(int(com[1]))
    
    if com[0] == '2':
        que.append(int(com[1]))

    if com[0] == '3':
        if len(que) > 0:
            print(que.popleft())
        else:
            print(-1)
    
    if com[0] == '4':
        if len(que) > 0:
            print(que.pop())
        else:
            print(-1)
    
    if com[0] == '5':
        print(len(que))
    
    if com[0] == '6':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    
    if com[0] == '7':
        if len(que) > 0:
            print(que[0])
        else:
            print(-1)
    
    if com[0] == '8':
        if len(que) > 0:
            print(que[-1])
        else:
            print(-1)