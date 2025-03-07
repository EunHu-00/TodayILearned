'''
기능 직접 구현
import sys

queue=[]
 
def push(num):
    queue.append(num)

def pop():
    if not queue:
        print(-1)
    else:
        N = queue.pop(0)
        print(N)

def size():
    print(len(queue))

def empty():
    if not queue:
        print(1)
    else:
        print(0)

def front():
    if not queue:
        print(-1)
    else:
        print(queue[0])

def back():
    if not queue:
        print(-1)
    else:
        print(queue[-1])


for _ in range(int(input())):
    op = sys.stdin.readline().split()

    if op[0] == 'push':
        push(op[1])
    
    if op[0] == 'pop':
        pop()
    
    if op[0] == 'size':
        size()

    if op[0] == 'empty':
        empty()

    if op[0] == 'front':
        front()
    
    if op[0] == 'back':
        back()
'''

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

q = deque([])

for _ in range(n):
    order = input().split()
    if order[0] == 'push':
            q.append(order[1])
            
    elif order[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
            
    elif order[0] == 'size':
        print(len(q))
        
    elif order[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
            
    elif order[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
            
    elif order[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)