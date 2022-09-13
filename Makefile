

all: output.out



output.out: main.o interpolation.o
	g++ main.o interpolation.o -o output.out
	clear # On bigger projects, comment this out
	./output.out # On bigger projects, comment this out
	rm *.out *.o # On bigger projects, comment this out

main.o: ./C++/main.cpp
	g++ -Wall -std=c++14 -c ./C++/main.cpp

interpolation.o: ./C++/interpolation.cpp ./C++/interpolation.h
	g++ -Wall -std=c++14 -c ./C++/interpolation.cpp


clean:
	rm *.o *.out
	clear