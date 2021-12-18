#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<unistd.h>
#include<sys/wait.h>

void int_handler(int signum){
   printf("\n Bye Bye!\n");
   exit(0);
}

int main(){
   int pid=fork();
   if(pid==0){
      signal(SIGUSR1,int_handler);
      while(1){
         printf("go to sleep\n");
         sleep(10);
              }
         exit(0);
            }
   else{
        sleep(30); 
        kill(pid,SIGUSR1);
        wait(0);
        exit(0);
    }
   return 0;
}
