#MakeFile A1
#Command One
A1: average.c main.c
	gcc -o A1 average.c main.c -std=c99
#Command Two
clean:
	-rm *.o
