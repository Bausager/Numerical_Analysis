#ifndef _OwnLib_H_
#define _OwnLib_H_

#include <string>
#include <iostream>
#include <vector>
#include <cmath>


std::vector<double> lagrange_interp(const std::vector<double> *const X,
									const std::vector<double> *const Y, 
									const std::vector<double> *const x, 
									uint8_t order=4);


std::vector<double> linspace(const double start,
							 	const double stop,
							 	const uint64_t num=100);

uint64_t search_closest(const std::vector<double> *const sorted_array, const double *const x);




#endif // _OwnLib_H_