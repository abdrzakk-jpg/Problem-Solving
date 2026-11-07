
#include <iostream>
#include <vector>

using namespace std;
vector<int> solution(vector<int> nums) {
    if(nums.size()==0){
        return {};
    }
    
    return nums;

}

int main(){
    for(int i : solution({1, 2, 10, 50, 5})){
        cout<<i<<"|";
    }
    cout<<"\n";
    return 0;
}