#include <bits/stdc++.h>
using namespace std;
int main()
{
    char arr[1000][1000];
    string str;cin>>str;
    int row=0,col=0,r=0,l=0,cnt=0;
    for(int i=0;i<str.size();i++)
    {
        if(str[i]=='R')
        {
            arr[row][col]=str[i];
            r++;
        }
        else
        {
            arr[row][col]=str[i];
            l++;
        }
        col++;

        if(r==l && r>0)
        {
            row++;
            col=0;
            r=0;l=0;
            cnt++;
        }
    }
    cout<<cnt<<endl;

    for(int i=0;i<1000;i++)
    {
        if(arr[i][0]!='R' && arr[i][0]!='L')
        {
            continue;
        }
        cout<<arr[i]<<endl;
    }

}