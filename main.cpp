//#include <iostream>
#include <stdio.h>
#include <vector>
#include <cmath>

#include <fstream>

#include <chrono>


#include "OwnLib.h"

using std::cout;
using std::cin;
using std::endl;

using std::vector;

using namespace std::chrono;

std::ofstream myfile;
std::ofstream myfile1;
std::ofstream myfileT;

int main()
{

    

	uint64_t m = 11;
    vector<double> X = linspace(-1, 1, m);
    vector<double> Y;
    for (uint64_t i = 0; i < m; ++i)
    {
    	Y.push_back(1.0 / (1 + 25 * pow(X.at(i), 2)));
    }

    uint64_t n = 1000;
    vector<double> x = linspace(-1, 1, n);

    auto start = high_resolution_clock::now();

    vector<double> y = lagrange_interp(&X, &Y, &x);

    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<microseconds>(stop - start);

    printf("Time taken by function: %f seconds\n", duration.count()/1e+6);



    FILE *f = fopen("time.csv", "w");
    if(f)
    {
        fprintf(f, "points,time\n");
        fprintf(f, "%ld,%f\n", n, duration.count()/1e+6);
        fclose(f);
    }
    else printf("Unable to open the target file\n");

    FILE *f1 = fopen("GroundTruth.csv", "w");
    if(f1)
    {
        fprintf(f1, "X,Y\n");
        for (uint64_t i = 0; i < Y.size(); ++i)
        {
            fprintf(f1, "%f,%f\n", X.at(i), Y.at(i));
            //myfile1 << X.at(i) << ',' << Y.at(i) << endl;
        }
        
        fclose(f1);
    }
    else printf("Unable to open the target file\n");

    FILE *f2 = fopen("Inter.csv", "w");
    if(f2)
    {
        fprintf(f2, "x,y\n");
        for (uint64_t i = 0; i < y.size(); ++i)
        {
            fprintf(f2, "%f,%f\n", x.at(i), y.at(i));
            //myfile1 << X.at(i) << ',' << Y.at(i) << endl;
        }
        
        fclose(f2);
    }
    else printf("Unable to open the target file\n");

	return 0;
}