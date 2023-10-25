#include<bits/stdc++.h>
using namespace std;

int main()
{
    int mnt = INT_MAX;
    int n;cin>>n;
    while(n--)
    {
        int cnt =0;
        int k;cin>>k;
        while(k!=0)
        {
            if(k%2==1)
            {
                break;
            }
            k/=2;
            cnt++;
            
        }
        mnt = min(mnt,cnt);
    }
    cout<<mnt<<endl;
}