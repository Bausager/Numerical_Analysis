
#include "OwnLib.h"




std::vector<double> lagrange_interp(const std::vector<double> *const X,
									const std::vector<double> *const Y, 
									const std::vector<double> *const x, 
									uint8_t order){

	std::vector<double> y;
	y.reserve((*x).size());
	uint64_t idx_i;
	double p = 0.0;
	double yi = 0.0;

	for (uint64_t n = 0; n < (*x).size(); ++n)
	{	
		uint64_t idx = search_closest(X, &x->at(n));
		
		// Lower Bound Conditions
		if (idx <= (order/2.0))
		{
			idx_i = 0;
		}
		// Upper Bound Conditions
		else if (((*X).size()-1 - (order/2.0)) <= idx)
		{
			idx_i = (*X).size()-1 - order;
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
					p *= ((*x).at(n) - (*X).at(idx_i+i)) / ((*X).at(idx_i+j) - (*X).at(idx_i+i));
				}
			}
			yi += (*Y).at(idx_i+j) * p;
		}
		y.push_back(yi);		
	}
	return y;
}



std::vector<double> linspace(const double start,
							 	const double stop,
							 	const uint64_t num){

	//std::vector<double> vec(num);
	std::vector<double> vec;
	vec.reserve(num);

	if (num == 0)
	{
		return vec;
	}
	else if (num == 1)
	{
		//vec.at(0) = start;
		vec.push_back(start);
	}
	else
	{
		double delta = (stop - start) / (num - 1);

		for (uint64_t i = 0; i < num - 1; ++i)
		{
			//vec.at(0) = start + delta * i;
			vec.push_back(start + delta * i);

			//std::cout << vec.at(0) << "\t" << i << std::endl;
		}
		//vec.at(num-1) = stop;
		vec.push_back(stop);
	}

	
	return vec;
}


uint64_t search_closest(const std::vector<double> *const sorted_array, const double *const x) {

    auto iter_geq = std::lower_bound(
        (*sorted_array).begin(), 
        (*sorted_array).end(), 
        (*x)
    );

    if (iter_geq == (*sorted_array).begin()) {
        return 0;
    }

    double a = *(iter_geq - 1);
    double b = *(iter_geq);

    if (fabs((*x) - a) < fabs((*x) - b)) {
        return iter_geq - (*sorted_array).begin() - 1;
    }

    return iter_geq - (*sorted_array).begin();
}







