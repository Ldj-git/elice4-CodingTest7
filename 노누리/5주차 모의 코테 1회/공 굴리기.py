# 테스트케이스에서 오답이 많이 나온 풀이 (65점)

# def main():
#     n,m = map(int,input().split())
#     graph=[]
    
#     for _ in range(n):
#         graph.append(list(map(int,input().split())))
    
#     x,y=map(int,input().split())
#     x-=1
#     y-=1
    
#     visited=[(x,y)]
#     route=[]
#     cnt=0
    
#     while True:
#         if x<0 or x>=n or y<0 or y>=m:
#             print(-1)
#             break
#         if graph[x][y]==1:
#             x-=1
#         elif graph[x][y]==2:
#             y-=1
#         elif graph[x][y]==3:
#             y+=1
#         elif graph[x][y]==4:
#             x+=1
        
#         if (x,y) in visited:
#             cnt+=1
#             route.append((x,y))
#         elif (x,y) not in visited:
#             cnt=0
#             route=[]
        
#         visited.append((x,y))
        
#         if len(route)!=0 and (x,y)==route[0]:
#             print(cnt+1)
#             break
    
# if __name__=="__main__":
#     main()


# 풀이를 조금 참고해서 푼 풀이!
# 이전에는 반복되는 경로를 구하는 방식을 visited에 좌표를 넣고 이미 visited에 있는 좌표라면 route에 값을 넣어
# 경로의 길이를 계산하는 방식을 이용했는데
# 풀이에서 visited를 배열로 만들어서 방문했을 때 값을 1 추가해줘서 2번이상 방문한 경로를 체크해주는 방식을 썼다.
# 그 점을 참고해서 풀이를 고쳤음.

def main():
    n,m = map(int,input().split())
    graph=[]
    
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    
    x,y=map(int,input().split())
    x-=1
    y-=1
    
    visited=[[0]*m for _ in range(n)]
    cnt=0
    
    while True:
            
        visited[x][y]+=1
        
        if graph[x][y]==1:
            x-=1
        elif graph[x][y]==2:
            y-=1
        elif graph[x][y]==3:
            y+=1
        elif graph[x][y]==4:
            x+=1
            
        if x<0 or x>=n or y<0 or y>=m:
            print(-1)
            exit()
        
        if visited[x][y]>2:
            for i in range(n):
                for j in range(m):
                    if visited[i][j]>=2:
                        cnt+=1
            break
            
    print(cnt)
    
if __name__=="__main__":
    main()
