#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * infinite_while - a loop infinite
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
 * main - main
 * Return: nothing
 */
int main(void)
{
	int i = 0;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			sleep(1);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
