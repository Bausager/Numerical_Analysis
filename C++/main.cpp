//#include <iostream>
#include <stdio.h>
#include <vector>
#include <cmath>

#include <fstream>

#include <chrono>


#include "interpolation.h"

using std::cout;
using std::cin;
using std::endl;

using std::vector;


int main()
{

    
	uint64_t m = 11;
    vector<double> a1 = linspace(-3.1415/2, 3.1415/2, m);
    vector<double> X;
    for (uint64_t i = 0; i < m; ++i)
    {
        X.push_back(sin(a1.at(i)));
    }



    vector<double> Y;
    for (uint64_t i = 0; i < m; ++i)
    {
    	Y.push_back(1.0 / (1 + 25 * pow(X.at(i), 2)));
    }

    uint64_t n = 1000;
    vector<double> a2 = linspace(-3.1415/2, 3.1415/2, n);
    vector<double> x;
     for (uint64_t i = 0; i < n; ++i)
    {
        x.push_back(sin(a2.at(i)));
    }

    

    vector<double> lagrange_int = lagrange_interp(&X, &Y, &x);
    vector<double> cubic_spine_int = cubic_spine_interp(&X, &Y, &x);


    FILE *f1 = fopen("GroundTruth.csv", "w");
    if(f1)
    {
        fprintf(f1, "X,Y\n");
        for (uint64_t i = 0; i < Y.size(); ++i)
        {
            fprintf(f1, "%f,%f\n", X.at(i), Y.at(i));
        }
        
        fclose(f1);
    }
    else printf("Unable to open the target file\n");

    FILE *f2 = fopen("lagrange_interp.csv", "w");
    if(f2)
    {
        fprintf(f2, "x,y\n");
        for (uint64_t i = 0; i < lagrange_int.size(); ++i)
        {
            fprintf(f2, "%f,%f\n", x.at(i), lagrange_int.at(i));
        }
        
        fclose(f2);
    }
    else printf("Unable to open the target file\n");


    FILE *f3 = fopen("cubic_spine_interp.csv", "w");
    if(f3)
    {
        fprintf(f3, "x,y\n");
        for (uint64_t i = 0; i < cubic_spine_int.size(); ++i)
        {
            fprintf(f3, "%f,%f\n", x.at(i), cubic_spine_int.at(i));
        }
        
        fclose(f3);
    }
    else printf("Unable to open the target file\n");






	return 0;
}