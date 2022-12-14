#ifndef _interpolation_H_
#define _interpolation_H_

#include <string>
#include <iostream>
#include <vector>
#include <cmath>
#include "Eigen/Dense"

std::vector<double> lagrange_interp(const std::vector<double> *const X,
									const std::vector<double> *const Y, 
									const std::vector<double> *const x, 
									uint8_t order=10);

std::vector<double> cubic_spine_interp(const std::vector<double> *const X,
										const std::vector<double> *const Y,
										const std::vector<double> *const x,
										const double alpha=0.0,
										const double beta=0.0);


std::vector<double> linspace(const double start,
							 	const double stop,
							 	const uint64_t num=100);

uint64_t search_closest(const std::vector<double> *const sorted_array, const double *const x);




#endif // _interpolation_H_