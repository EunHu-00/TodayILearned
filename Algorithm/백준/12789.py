N = int(input())
num = list(map(int, input().split()))

ST = []
now = 1

for number in num:
    while ST and ST[-1] == now:  
        ST.pop()
        now += 1
    if number == now:
        now += 1
    else:
        ST.append(number)

while ST and ST[-1] == now:
    ST.pop()
    now += 1

if now == N + 1:
    print("Nice")
else:
    print("Sad")
