#include <iostream>
#include <cmath>
using namespace std;

int combination(int n, int k)
{
        if(k>=n || k == 0)
                return 1;
        int res = 1, i;
        for(i = n; i > k; i--)
                res *= i;
        for(i = 1; i <= k; i++)
                res /= i;
        return res;
}

int catalan(int n)
{
        int m = combination(2*n, n);
        return m/(n+1);
}

int main()
{
        int N;
        cout << "Input catalan N: ";
        cin >> N;
        cout << catalan(N);
}

