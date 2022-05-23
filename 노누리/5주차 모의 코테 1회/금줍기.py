# 이전에 코테 치면서 풀었던 풀이!

# def main():
#     n = int(input())
#     lst=list(map(int,input().split()))
#     temp=[]
    
#     for i in range(1,n-2):
#         temp.append((lst[i-1]+lst[i]+lst[i+1],i))
    
#     temp=sorted(temp)
#     for i in range(len(temp)-1,1,-1):
#         for j in range(len(temp)-2,0,-1):
#             if abs(temp[i][1]-temp[j][1])>=3:
#                 print(temp[i][0]+temp[j][0])
#                 exit()
    
# if __name__=="__main__":
#     main()
    
    
# 왼손, 오른손 겹쳐서 금을 주우면 안되기 때문에 금을 잡은 거리가 3이상 차이나는지 확인해야한다!
# 최대한 가장 maximum 값을 고정하고 2순위의 금 무게를 조정하는 것이 좋기 때문에 for문 순서를 그렇게 만들어뒀음. 
# (j==제일 무거운 금 무게,k==2번째로 무거운 금 무게)

def main():
    n = int(input())
    gold=list(map(int,input().split()))
    weight=[]
    
    for i in range(1,n-1):
        weight.append((gold[i-1]+gold[i]+gold[i+1],i))
    
    weight=sorted(weight,key=lambda x:x[0],reverse=True)
    for j in range(len(weight)):
        for k in range(1,len(weight)):
            if abs(weight[j][1]-weight[k][1])>=3:
                print(weight[j][0]+weight[k][0])
                exit(0)
    print(weight)

if __name__=="__main__":
    main()
