

#all: output.out outputC.out



output.out: main.o OwnLib.o
	g++ main.o OwnLib.o -o output.out
	clear # On bigger projects, comment this out
	./output.out # On bigger projects, comment this out
	rm *.out *.o # On bigger projects, comment this out

main.o: ./C++/main.cpp
	g++ -Wall -std=c++14 -c ./C++/main.cpp

OwnLib.o: ./C++/OwnLib.cpp ./C++/OwnLib.h
	g++ -Wall -std=c++14 -c ./C++/OwnLib.cpp





# outputC.out: mainC.o OwnLibC.o
# 	gcc -O mainC.o OwnLibC.o -o outputC.out 
# 	#rm *.o # On bigger projects, comment this out
# 	#clear # On bigger projects, comment this out
# 	./outputC.out

# mainC.o: mainC.c
# 	gcc -c ./C/mainC.c

# OwnLibC.o: OwnLibC.c OwnLibC.h
# 	gcc -c ./C/OwnLibC.c



clean:
	rm *.o *.out
	clear