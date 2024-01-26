#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
/**
* infinite_while - infinite while loop for zombie
* Return: 0
*/
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}
/**
* main - create 5 zombie process
* Return: 0
*/
int main(void)
{
int ps_num;
pid_t pid_of_zombie;
ps_num = 0;
while (ps_num < 5)
{
pid_of_zombie = fork();
if (pid_of_zombie > 0)
{
printf("Zombie process created, PID: %d\n", pid_of_zombie);
}
else
exit(0);
ps_num++;
}
infinite_while();
return (0);
}
