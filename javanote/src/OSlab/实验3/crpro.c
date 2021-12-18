#include<sys/types.h>
#include<stdio.h>
#include<unistd.h>


void main(int argc,char *argv[])
{
 pid_t pid;
 
 pid=fork();
 if(pid<0){/*error occurred*/
   fprintf(stderr,"Fork Failed");
   exit(-1);
}
 else if(pid==0){/*child process*/
   execlp("/bin/ls","ls",NULL);
}
else{/*parent process*/
  wait(NULL);
  printf("Child Complete\n");
  exit(0);


}

}
