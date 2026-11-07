
#include <iostream> 
#include <string>
#include <vector>

using namespace std; 

vector<string> split(string arg){
    //* "This is an Example !"
    vector<string> rslt;
    string currentWord;
    for(int i = 0; i < arg.size(); i++){
        if(arg[i] == ' '){
            rslt.push_back(currentWord);
            currentWord = "";
        }else{
            currentWord += arg[i];
        }
    }
    return rslt;
}

string reverse(string arg){
    // ! This -> sihT
    /*
    * for-loop simulate
    * T:0= 0-3 = arg[3] = s
    * h:1= 1-3 = arg[2] = i
    * i:2= 2-3 = arg[1] = h
    * s:3= 3-3 = arg[0] = T
    */
    string reversed;
    for(int i = 0; i < arg.size()+1; i++){
        reversed += arg[arg.size()-i];
    }
    return reversed;
}
int main(){
    string rslt;
    vector<string> splitedText = split("This is an Example !");
    for(string item : splitedText){
        rslt += reverse(item)+" ";
    }
    cout <<"Reversed Text: " << rslt<<endl;
    return 0;
}
