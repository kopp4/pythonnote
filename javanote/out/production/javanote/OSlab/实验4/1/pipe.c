#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>


int main(){
int fd[2];
int pid;

pipe(fd);
pid=fork();

if(pid==0){
  char *str="I am child.\n";
  write(fd[1],str,30);
   }
else{
    wait(0);
  char buf[30];
  read(fd[0],buf,30);
  printf("In parent.\n");
  printf("%s",buf);
    }
return 0;

}

