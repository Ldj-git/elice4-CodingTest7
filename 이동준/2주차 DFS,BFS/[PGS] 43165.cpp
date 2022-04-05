#include <vector>
#include <queue>
#include <utility>
// #include <bitset>
// #include <cmath>
using namespace std;

//[PGS] 43165. 타겟 넘버 / 레벨 2 / 15분

int solution(vector<int> numbers, int target) {
    int answer = 0;
    
    //모든 경우를 다 보는건데 방법을 bfs로다가
    //생각해보면 구지 bfs로 안해도 되긴함 비트마스킹?? 해보니까 bfs가 훨 빠르긴 하네.. 근데 메모리 더씀
    //0000~1111 까지 인거 0이면 -, 1이면 +
    // 테스트 1 〉	통과 (12.86ms, 11.5MB)
    // 테스트 2 〉	통과 (12.29ms, 11.5MB)
    // 테스트 3 〉	통과 (0.02ms, 4.11MB)
    // 테스트 4 〉	통과 (0.06ms, 4.17MB)
    // 테스트 5 〉	통과 (0.41ms, 4.18MB)
    // 테스트 6 〉	통과 (0.03ms, 4.04MB)
    // 테스트 7 〉	통과 (0.02ms, 4.18MB)
    // 테스트 8 〉	통과 (0.10ms, 4.1MB)
    
    queue<pair<int,int>>q; //현재 위치, 현재 위치까지 계산값
    q.push(make_pair(0,numbers[0])); //+
    q.push(make_pair(0,-numbers[0])); //-
    while(!q.empty()){
        pair<int,int>here=q.front();
        q.pop();
        if(here.first==numbers.size()-1){ //끝까지옴
            if(here.second==target)
                answer++;
        }else{
            q.push(make_pair(here.first+1,here.second+numbers[here.first+1])); //+
            q.push(make_pair(here.first+1,here.second-numbers[here.first+1])); //-
        }
    }
    
    return answer;
}

// int solution(vector<int> numbers, int target) {
//     int answer = 0;
    
//     //비트마스킹 버전
//     //0000~1111 까지 인거 0이면 -, 1이면 +
//     // 테스트 1 〉	통과 (39.45ms, 4.17MB)
//     // 테스트 2 〉	통과 (43.31ms, 4.1MB)
//     // 테스트 3 〉	통과 (0.04ms, 4.05MB)
//     // 테스트 4 〉	통과 (0.13ms, 4.18MB)
//     // 테스트 5 〉	통과 (0.95ms, 3.77MB)
//     // 테스트 6 〉	통과 (0.07ms, 4.18MB)
//     // 테스트 7 〉	통과 (0.04ms, 3.67MB)
//     // 테스트 8 〉	통과 (0.25ms, 4.18MB)
//     for(int i=0;i<pow(2,numbers.size());i++){
//         bitset<20> here(i);
//         int res=0;
//         for(int j=0;j<numbers.size();j++){
//             if(here[j])
//                 res+=numbers[j];
//             else
//                 res+=numbers[j]*-1;
//         }
//         if(res==target)
//             answer++;        
//     }
//     return answer;
// }