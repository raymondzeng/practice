#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

void main()
{
char x = 'a';
char *p = &x;
p++;
printf("%c\n", *p);
}
