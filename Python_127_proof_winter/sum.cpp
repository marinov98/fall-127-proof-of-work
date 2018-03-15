#include <iostream>
using namespace std;
int main()
{
  int stnum, endnum;
  int sum=0;
  cout<<'Type starting number'<<endl;
  cin>>stnum;
  cout<<'Put your last number'<<endl;
  cin>>endnum;
  if (stnum<0)
  cout<<'please put in a positive integer!'<<endl;
  cin>>stnum;
  if (endnum<stnum)
  cout<<"Number must be bigger than the initial value!"<<endl;
  for (int num=stnum; num<=endnum, num++;){
  sum+=num;
}
cout<<sum<<endl;
return 0 
