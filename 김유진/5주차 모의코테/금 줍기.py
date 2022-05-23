

def main():
    num = int(input())
    gold = list(map(int, input().split(' ')))
    # print(gold)
    hand = dict()
    for i in range(0, num-2):
        # print(gold[i], gold[i+1], gold[i+2])
        add = gold[i] + gold[i+1] + gold[i+2]
        if add not in hand:
            hand[add] = [gold[i], gold[i+1], gold[i+2]]
    
    result = sorted(hand.items(), reverse=True)
    
    if len(result) == 1:
        print(sum(result[0][1])*2)
    else:
        print(sum(result[0][1])+sum(result[1][1]))
    
if __name__=="__main__":
    main()

'''
왜 그렇지?ㅠㅠ

채점을 시작합니다...
================================
Case 1. 오답입니다. (+0)
Case 2. 오답입니다. (+0)
Case 3. 오답입니다. (+0)
Case 4. 오답입니다. (+0)
Case 5. 정답입니다! (+5)
Case 6. 정답입니다! (+5)
Case 7. 오답입니다. (+0)
Case 8. 정답입니다! (+5)
Case 9. 오답입니다. (+0)
Case 10. 정답입니다! (+5)
Case 11. 정답입니다! (+5)
Case 12. 정답입니다! (+5)
Case 13. 정답입니다! (+5)
Case 14. 오답입니다. (+0)
Case 15. 정답입니다! (+5)
Case 16. 정답입니다! (+5)
Case 17. 정답입니다! (+5)
Case 18. 정답입니다! (+5)
Case 19. 정답입니다! (+5)
Case 20. 정답입니다! (+5)
================================
채점을 마쳤습니다. 코드 실행이 완료될 때까지 잠시만 기다려주세요.
총 점수: 65 / 100
Finished running the code.
'''