

all: output.out outputC.out



output.out: main.o OwnLib.o
	g++ main.o OwnLib.o -o output.out
	#./output

main.o: main.cpp
	g++ -Wall -std=c++14 -c main.cpp

OwnLib.o: OwnLib.cpp OwnLib.h
	g++ -Wall -std=c++14 -c OwnLib.cpp





outputC.out: mainC.o OwnLibC.o
	gcc -O mainC.o OwnLibC.o -o outputC.out 
	#rm *.o # On bigger projects, comment this out
	#clear # On bigger projects, comment this out
	./outputC.out

mainC.o: mainC.c
	gcc -c mainC.c

OwnLibC.o: OwnLibC.c OwnLibC.h
	gcc -c OwnLibC.c



clean:
	rm *.o *.out
	clear