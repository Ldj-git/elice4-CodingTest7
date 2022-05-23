# 50% 정답... 이유를 모르겠다...
n, m = list(map(int, input().split()))

guidance = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    guidance.append(list(map(int, input().split())))

x, y = list(map(int, input().split()))
x -= 1
y -= 1
circuit_cnt = 0

while True:
    if x < 0 or y < 0 or x > (m - 1) or y > (n - 1):
        circuit_cnt = -1
        break

    current = guidance[x][y]
    
    if visited[x][y] == 1: # 두 번째 방문
        circuit_cnt += 1
        visited[x][y] = 2
    elif visited[x][y] == 2: # 세 번째 방문, 순환 카운트 완료
        break
    elif visited[x][y] == 0: # 첫 번째 방문
        visited[x][y] = 1 
    
    if current == 1: # 상
        x -= 1
    elif current == 2: # 좌
        y -= 1
    elif current == 3: # 우
        y += 1
    else: # 하
        x += 1

    
print(circuit_cnt)