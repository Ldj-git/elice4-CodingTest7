# 사다리꼴 넓이 구하는 공식
def calc_area(left_side, right_side, down_side):
    return (left_side + right_side) * down_side / 2

n = int(input())
nails_pos = dict()

for _ in range(n):
    x, y = list(map(int, input().split()))
    # 이미 x에 대한 값이 있으면 크기를 비교해서 업데이트
    if x in nails_pos:
        current_value = nails_pos[x]
        nails_pos[x] = y if current_value < y else current_value
    else:
        nails_pos[x] = y

nails_x = sorted(nails_pos)
result = 0

for i in range(len(nails_x) - 1):
    current_x = nails_x[i]
    next_x = nails_x[i + 1]

    result += calc_area(nails_pos[current_x], nails_pos[next_x], next_x - current_x)

# 정수면 정수로 변환
if result % 1 == 0:
    result = int(result)

# 결과 출력
print(result)