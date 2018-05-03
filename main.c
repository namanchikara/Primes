#include "stdio.h"
int main ()
{
  int n,m;
  int np=1;
  int primes[100004]={2};
  int prime[1300000]={0};
  prime[2]=1;
  
  for(n=3;n<1300001;n+=2) prime[n]=1; // odd maybe prime
  for(n=3;n<1141;n+=2) if(prime[n]) for(m=n*n;m<1300001;m+=(n+n)) prime[m]=0;
  for(n=3;n<1299722;n+=2) if(prime[n]) primes[np++]=n;
  
  for(n=0;n<10;n++)
    if(primes[3])
      printf("%d    %d\n",primes[n],n);
  
}
