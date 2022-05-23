from collections import deque
from re import A

n, k = list(map(int, input().split()))

arrow = [(0, 0) for _ in range(n + 1)]

for i in range(n):
    l, r = list(map(int, input().split()))
    arrow[i + 1] = (l, r)

q = deque([1])
while q:
    current = q.popleft()
    
    l, r = arrow[current]
    if l > 0:
        q.append(l)
        arrow[current] = (0, r)
    elif r > 0:
        q.append(r)
        arrow[current] = (l, 0)

result = 0
for l, r in arrow:
    if l > 0 and r > 0:
        result += 1
print(result)