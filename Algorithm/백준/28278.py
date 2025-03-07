stack=[-1]*1000000
i = 0

def push(num):
    global stack, i
    stack[i]=num
    i+=1

def pop():
    global stack, i
    if i == 0:
        print(-1)
        return
    else:
        popnum = stack[i-1]
        stack[i-1] = -1
        i-=1
        print(popnum)

def count():
    global i
    print(i)

def empty():
    global i
    if i == 0: print(1)
    else: print(0)

def exist():
    global stack, i
    if i == 0:
        print(-1)
        return
    else: print(stack[i-1])



for _ in range(int(input())):
    command = input().split()
    if command[0] == '1':
        push(int(command[1]))
    elif command[0] == '2':
        pop()
    elif command[0] == '3':
        count()
    elif command[0] == '4':
        empty()
    elif command[0] == '5':
        exist()

"""
시간 줄이는 코드

import sys

N = int(sys.stdin.readline())
ST=[]
for i in range(N):
    op = sys.stdin.readline().split()
    if op[0] == '1':
        ST.append(int(op[-1]))
    elif op[0] == '2':
        if ST:
            print(ST.pop(-1))
            continue
        print(-1)
    elif op[0] == '3':
        print(len(ST))
    elif op[0] == '4':
        if ST:
            print(0)
            continue
        print(1)
    elif op[0] == '5':
        if ST:
            print(ST[-1])
            continue
        print(-1)
"""