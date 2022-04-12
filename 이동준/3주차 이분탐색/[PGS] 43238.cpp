#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// [PGS] 43238. 입국심사 / 레벨 3 / 1시간

bool possible(long long t, long long n, vector<int>times){
    //t분 이 가능한 시간인지 판별, 모든 심사관은 쉬지 않고 일해야됨
    for(int i=0;i<times.size();i++)
        n-=t/times[i]; //t랑 n을 같은 longlong으로 안하면 int에대가 long을 빼는 경우가 되버려서 계산이 이상하게됨

    if(n<=0)
        return true;
    else
        return false;
}

long long solution(int n, vector<int> times) {
    long long answer = 0;

    //가능한 시간 범위를 잡아놓고 이분탐색
    //최소 l - 귀찮아서 그냥 0, 최대 r - 가장 오래걸리는놈한테 다 받기
    sort(times.begin(),times.end());
    long long l=0;
    long long r=(long long) times[times.size()-1]*n;
    long long nn=(long long)n; //이거 안해줘서 30분 날림... 근데 예전에 풀었을때도 이거랑 똑같은 실수함 ㅋㅋ
    
    while(l<r){
        answer=(l+r)/2;
        if(possible(answer,nn,times)){
            r=answer;
        }else{
            l=answer+1;
        }
    }
    return l;
    
    //임시방편 코든데 좋은 방법은 아닌거 같아서 다른코드 봤는데 그냥 l을 리턴하면 되는거였음.. 개멍청했네 ㅋㅋㅋ
//위에 대충 근사치 구해놓고 한칸한칸내려가면서 최소치 확인용
//     while(possible(answer,nn,times)){
//         answer--;
//     }
//     answer++;
    
//     return answer;
}