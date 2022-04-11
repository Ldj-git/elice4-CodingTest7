from collections import deque


def solution(numbers, target):
    answer = 0

    queue = deque()
    queue.append((0, 0))  # current number, index

    while queue:
        curNum, idx = queue.popleft()

        if idx == len(numbers):
            if curNum == target:
                answer += 1
        else:
            queue.append((curNum + numbers[idx], idx + 1))
            queue.append((curNum - numbers[idx], idx + 1))

    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
