def solution(numbers, target):
    answer = 0
    
    def DFS(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            DFS(idx+1, result+numbers[idx])
            DFS(idx+1, result-numbers[idx])
    
    DFS(0, 0)
    return answer


