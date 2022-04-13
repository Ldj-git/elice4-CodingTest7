#include <string>
#include <vector>
#include <algorithm>

using namespace std;

//[PGS] 43236. 징검다리 / 레벨 4 / 1시간 반 삽질 + 답지 이해 30분 + 직접 구현 30분 = 대충 3시간

bool possible(int min_dist, vector<int>rocks, int n){
    //n개 바위를 지워서 최소 구간길이를 min_dist로 맞출수 있냐?? 를 반환하는 함수
    
    //초반에 이 부분을 어떻게 구현할지 생각이 안나서 지울 바위를 고르는 방법을 생각하다가 
    //구간길이가 가장 짧은 곳에 포함된 바위를 지우자라고 생각해서 그리디로 쌉가능인가??? 해서 그리디로 삽질 1시간 반하고 답지 봄...
    
    //그니까 n개의 바위를 지울 때 최소 구간길이가 얼마가 될 수 있냐? 라고하면 구현 방법이 잘 생각 안나지만
    //최소 구간길이를 고정해두고 몇개의 바위를 지워야되나? 라고하면 구현 쉬움 (내가 정한 최소 구간길이 보다 작은 구간의 바위는 지워버리는 식)
    //완전 씽크빅인데...  답지보면 그렇구나 하는데 내가 하려면 생각 안남..

    //min_dist 가 최소 구간길이가 되게끔 바위 제거했을때 n개보다 많이 제거했으면 false 아니면 true
    int del_rock=0,prev=0;
    for(int i=0;i<rocks.size();i++){
        if(rocks[i]-prev<min_dist){ //구간 길이가 min_dist보다 작다면 바위 제거
            del_rock++;
        }else{
            prev=rocks[i];
        }
    }
    if(del_rock>n){
        return false;
    }else{
        return true;
    }
}

int solution(int distance, vector<int> rocks, int n) {
    //이 문제에서 탐색할 대상은 최소 구간 길이
    int answer = 0;
    rocks.push_back(distance); //마지막 지점까지 구간 길이 확인용 마지막 바위 임의로 추가
    sort(rocks.begin(), rocks.end());

    int l = 0, r = distance;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (possible(mid, rocks, n)) {
            l = mid + 1; answer = mid;
        }
        else {
            r = mid - 1;
        }
    }
    return answer;
}

//삽질 기록 (실패)
//그리디로 접근해봤음.. 예제 케이스는 다 되긴하는데 제출하면 1개만 맞고 다틀림.. 시간도 1000ms 넘어가긴함 ㅋㅋ
//매 순간마다 모든 바위를 확인하면서 최소 구간길이에 포함된 바위 중 하나를 지워주는 방식
//구현은 바위기준으로 하지 않고 구간을 리스트로 만들어서 구간 기준으로 함
//가장 작은 구간을 찾아 양옆에 있는 구간중 더 짧은 구간에 합쳐줌 (그래야 남아있는 구간중 최소값이 커짐)
//중간에 있는 구간을 지울일이 있어서 링크드리스트 자료구조를 써먹으려다 이터레이터 사용법 익히느라 시간 오래씀..

// #include <string>
// #include <vector>
// #include <iostream>
// #include <algorithm>
// #include <list>

// using namespace std;

// //[PGS] 43236. 징검다리 / 레벨 4 / 10'25 ~ 

// int solution(int distance, vector<int> rocks, int n) {
//    int answer = distance;

//    sort(rocks.begin(), rocks.end());
//    list <int> between; between.push_back(rocks[0]);
//    for (int i = 0; i < rocks.size() - 1; i++) {
//        between.push_back(rocks[i + 1] - rocks[i]);
//    }
//    between.push_back(distance - rocks[rocks.size() - 1]);
//    //그냥 각 바위사이 거리를 계속 합쳐주되 항상 최소값 기준 더 작은쪽으로 합쳐주기
//    //최소값 여러개면 가장 작은쪽 찾아서 그거먼저?
//    for (int k = 0; k < n; k++) {
//        auto min = between.begin(), del = between.begin();
//        del++;
//        for (auto i = between.begin(); i != between.end(); i++) {
//            if (*i <= *min) {
//                if (i == between.begin()) {
//                    continue;
//                }
//                if (i == --between.end()) {
//                    auto l = i; l--; 
//                    if (*del >= *l) {
//                        del = l;
//                        min = i;
//                    }
//                }
//                else {
//                    auto l = i, r = i; l--; r++;
//                    if (*del >= *r || *del >= *l) {
//                        if (*r > *l)
//                            del = l;
//                        else
//                            del = r;
//                        min = i;
//                    }
//                }
//            }
//        }
//        *min = *min + *del;
//        between.erase(del);
//    }
//    for (auto i = between.begin(); i != between.end(); i++) {
//        if (answer > *i)
//            answer = *i;
//    }
//    return answer;
// }