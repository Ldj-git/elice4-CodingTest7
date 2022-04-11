global answer
answer = 0

def solution(numbers, target):
    
    dfs(numbers, numbers[0], target, 0)
    dfs(numbers, numbers[0] * (-1), target, 0)
    
    return answer

def dfs(lst, num, target, depth):
    
    global answer

    if depth == len(lst) - 1:
        if num == target:
            answer += 1
        return
    
    else:
        dfs(lst, num + lst[depth + 1], target, depth + 1)
        dfs(lst, num - lst[depth + 1], target, depth + 1)