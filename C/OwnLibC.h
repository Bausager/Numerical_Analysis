#ifndef _OwnLibC_H_
#define _OwnLibC_H_

#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>

bool lagrange_interp(const double *const X,
					const double *const Y,
					const uint64_t m, 
					const double *const x,
					double *const y,
					const uint64_t n,
					uint8_t order);


bool linspace(const double start,
	 		 	const double stop, 
			 	double *const y,
			 	const uint64_t num);

//uint64_t search_closest(const std::vector<double> *const sorted_array, const double *const x);




#endif // _OwnLibC_H_