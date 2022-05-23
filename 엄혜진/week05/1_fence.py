# 20분 고민하다가 해설 참조... 이렇게 간단할 수가....

n, m, k = list(map(int, input().split()))

carrot_x = []
carrot_y = []

for _ in range(k):
    x, y = list(map(int, input().split()))
    carrot_x.append(x)
    carrot_y.append(y)

width = max(carrot_x) - min(carrot_x) + 2
height = max(carrot_y) - min(carrot_y) + 2

print((width * 2) + (height * 2))