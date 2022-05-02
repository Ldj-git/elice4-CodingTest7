# 최적의 시간 = 시간이 적게 걸리는 심사대에서 최대한 많은 심사
# 시간을 기준으로 그 시간에 심사 받은 사람의 수를 구한다.

def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2  # 한 심사관에게 주어진 시간
        total = 0

        for t in times:  # 각 심사관마다 주어진 시간 동안 몇 명의 사람을 심사할 수 있는지
            total += mid // t

        if total >= n:  # 모든 사람을 심사할 수 있는 경우
            right = mid - 1  # 한 심사관에게 주어진 시간을 줄여본다
            answer = mid
        else:  # 모든 사람을 심사할 수 없는 경우
            left = mid + 1  # 한 심사관에게 주어진 시간을 늘려본다

    return answer


print(solution(6, [7, 10]))