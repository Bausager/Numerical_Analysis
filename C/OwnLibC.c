
#include "OwnLibC.h"



bool lagrange_interp(const double *const X,
					const double *const Y,
					const uint64_t M, 
					const double *const x,
					double *const y,
					const uint64_t N,
					uint8_t order){

	uint64_t idx_i;
	double p = 0.0;
	double yi = 0.0;

	for (uint64_t n = 0; n < N; ++n)
	{	
		uint64_t idx = search_closest(X, M, &x->at(n));
		uint64_t idx;
		// Lower Bound Conditions
		if (idx <= (order/2.0))
		{
			idx_i = 0;
		}
		// Upper Bound Conditions
		else if ((M-1 - (order/2.0)) <= idx)
		{
			idx_i = M-1 - order;
		}
		// Middle
		else
		{
			idx_i = idx - (order/2.0);
		}

		// For Loop
		yi = 0;
		for (uint8_t j = 0; j <= order; ++j)
		{
			p = 1.0;
			for (uint8_t i = 0; i <= order; ++i)
			{	
				if(j != i)
				{
					p *= (x[n] - X[idx_i+i]) / (X[idx_i+j] - X[idx_i+i]);
				}
			}
			yi += Y[idx_i+j] * p;
		}
		y[n] = yi;		
	}
	return 0;
}


bool linspace(const double start,
	 		 	const double stop, 
			 	double *const y,
			 	const uint64_t num){
	if (num == 0)
	{
		return 1;
	}
	else if (num == 1)
	{
		y[0] = start;
	}
	else
	{
		double delta = (stop - start) / (num - 1);
		for (uint64_t i = 0; i < num; ++i)
		{
			y[i] = (start + (delta * i));
		}
	}
	return 0;
}


uint64_t search_closest(const double *const sorted_array, const uint64_t N, const double x) {

	uint64_t idx = 0;

	for (uint64_t i = 0; i < N; ++i)
	{
		if (abs(x - sorted_array[i]) < abs(x - sorted_array[idx]))
		{
			idx = i;
		}
	}

    return idx;
}




