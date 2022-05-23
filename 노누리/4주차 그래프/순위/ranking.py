#플로이드-워셜 방식 이용

def solution(n, results):
    answer = 0
    graph=[['N']*n for _ in range(n)]
    
    for i in range(len(results)):
        x,y=results[i]
        graph[x-1][y-1]=1
        graph[y-1][x-1]=-1
        
    for k in range(n):
        graph[k][k]=0
        for i in range(n):
            for j in range(n):
                if graph[i][k]!='N' and graph[k][j]!='N':
                    if graph[i][k]+graph[k][j]<0:
                        graph[i][j]=-1
                    elif graph[i][k]+graph[k][j]>0:
                        graph[i][j]=1
    
    for i in range(n):
        cnt=0
        for j in range(n):
            if type(graph[i][j])!=int:
                cnt+=1
                break
        if cnt==0:
            answer+=1
    return answer
