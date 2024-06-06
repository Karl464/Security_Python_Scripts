
/*	
compile code without stack protection:
	gcc -fno-stack-protector -z  execstack -o buff buff.c
change privileges of binary:
	chmod +x buff
execute binary code: 
	./buff

Be aware that stack App protection have been disable on code compilation.
But also u need to disable OS protection, check and verify if this protection is disabled:
	$ sudo sysctl kernel.randomize_va_space 
	kernel.randomize_va_space = 2
	$ sudo sysctl -w kernel.randomize_va_space=0
	kernel.randomize_va_space = 0
*/

#include <stdio.h> 
#include <unistd.h>

int vuln() {
	char arr[400];
	int return_status;

	printf("What's your name?\n"); 
	return_status = read (0, arr, 400);

	printf("Hello %s", arr);

	return 0;
}

int main(int argc, char *argv[]) {
	vuln();
	return 0;
}

ssize_t read (int fildes, void *buf, size_t nbytes);
