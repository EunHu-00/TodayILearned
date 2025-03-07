import sys

T = int(sys.stdin.readline())

for _ in range(T):
    ST=[]
    text = sys.stdin.readline().strip()
    char = list(text)
    i=0
    
    
    while( i < len(char)):
        if char[i] == '(':
            ST.append(char[i])
            i += 1
        elif char[i] == ')':
            if not ST:
                print("NO")
                break
            ST.pop(-1)
            i+=1

    if not ST and i >= len(char):
        print("YES")
    elif ST:
        print("NO")