# 처음에 모의코테로 쳐본 풀이!!

# def main():
#     n,m,k = map(int,input().split())
#     x=[]
#     y=[]
#     for i in range(k):
#         a,b=map(int,input().split())
#         x.append(a)
#         y.append(b)
        
#     sum_x=((max(x)+1)-(min(x)-1))*2
#     sum_y=((max(y)+1)-(min(y)-1))*2
    
#     print(sum_x+sum_y)

# if __name__=="__main__":
#     main()


# 이전에 풀었는데 다시 풀어본 풀이!
# 당근 위치가 0 혹은 n,m 길이만큼 있을 수 있다는 생각에 if문으로 예외처리를 했는데
# 제한사항에 이미 1<=x<=m-1 이라고 적혀있어서 필요없었다.

def main():
    n,m,k = map(int,input().split())
    
    carrot_x=[]
    carrot_y=[]
    
    for i in range(k):
        a,b=map(int,input().split())
        carrot_x.append(a)
        carrot_y.append(b)
    
    hor=2*(max(carrot_x)-min(carrot_x)+2)
    ver=2*(max(carrot_y)-min(carrot_y)+2)
        
    # if min(carrot_x)==0:
    #     hor-=2
    # if max(carrot_x)==n:
    #     ver-=2
    # if min(carrot_y)==0:
    #     hor-=2
    # if max(carrot_y)==m:
    #     ver-=2
    
    print(hor+ver)

if __name__=="__main__":
    main()
