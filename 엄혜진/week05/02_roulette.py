n, k, p, l = map(int, input().split())

rounds = [[0] * k for i in range(l)]

for player in range(k):
    play = list(map(int, input().split()))
    for i in range(l):
        rounds[i][player] = play[i]

result_player = -1
result_round = 0
roulette = list(range(n, 0, -1))
roulette_idx = n - 1

for i in range(l):
    for j in range(k):
        # 문제에는 시계방향이라고 언급되어 있는데, 그림은 시계 반대방향이다...
        for _ in range(rounds[i][j]):
            roulette_idx += 1
            if roulette_idx >= len(roulette):
                roulette_idx = 0

        if roulette[roulette_idx] == p:
            result_player = j + 1
            result_round = i + 1
            break

if result_player == -1:
    print(-1)
else:
    print(result_player, result_round)
