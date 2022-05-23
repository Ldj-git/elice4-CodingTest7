result_x = -1
result_count = 0

n, h = map(int, input().split())

boards = [(0, 0) for i in range(n + 1)]

for _ in range(n):
    x, s, k = map(int, input().split())
    
    # 판자가 띄워져 있는 경우
    if len(boards) <= x:
        for _ in range(len(boards), x + 1):
            boards.append((0, 0))
    # 판자 정보 저장
    boards[x] = (s, k)

for i in range(1, len(boards)):
    s, k =  boards[i]
    
    # 강철 재질인 경우
    if k == 3 and s > h:
        result_x = i
        break

    # 뚫리는 경우
    if k == 1 and s > h:
        result_count += 1

            
print(result_x, result_count)