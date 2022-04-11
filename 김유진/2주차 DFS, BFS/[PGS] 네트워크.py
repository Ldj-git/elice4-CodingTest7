def solution(n, computers):            
    answer = 0
    visited = [0 for i in range(n)] # [0, 0, 0]
    
    def DFS(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] and not visited[j]:
                DFS(j)
                
    
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
        
    return answer