/**
 * @file thread.cpp
 * @author your name (you@domain.com)
 * @brief windows create thread sum up
 * @version 0.1
 * @date 2021-10-14
 * 
 * @copyright Copyright (c) 2021
 * 
 */

#include<windows.h>
#include<stdio.h>
DWORD Sum;

DWORD WINAPI Summation(LPVOID Param){
   DWORD Upper=*(DWORD*)Param;
   for(DWORD i=0;i<=Upper;i++)
	   Sum+=i;
   return 0;
}

int main(int argc,char *argv[])
{
	DWORD ThreadId;
	HANDLE ThreadHandle;
	int Param;

	Param=100;
	ThreadHandle=CreateThread(
		NULL,0,Summation,&Param,0,&ThreadId);
	if(ThreadHandle !=NULL){
	 WaitForSingleObject(ThreadHandle,INFINITE);
	 CloseHandle(ThreadHandle);
	 printf("sum = %d\n",Sum);

	}
}