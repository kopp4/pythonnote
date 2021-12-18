#include<signal.h>
#include<stdio.h>
#include<stdlib.h>

void int_handler(int signum)
{
printf("\n Bye Bye!\n");
exit(-1);
}

int main()
{
   signal(SIGINT,int_handler);
   printf("int_handleer at SIGINT\n");

   while(1){
      printf("go to sleep.\n");
      sleep(10);
}
    return 0;
}
