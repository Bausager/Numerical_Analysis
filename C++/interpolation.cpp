
#include "interpolation.h"




std::vector<double> lagrange_interp(const std::vector<double> *const X,
									const std::vector<double> *const Y, 
									const std::vector<double> *const x, 
									uint8_t order)
{

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


std::vector<double> cubic_spine_interp(const std::vector<double> *const X,
											const std::vector<double> *const Y,
											const std::vector<double> *const x,
											const double alpha,
											const double beta)
{

	
	uint64_t N_points = (*X).size();
	uint64_t n_points = (*x).size();



	std::vector<double> y;
	y.reserve(n_points);

	double delta[N_points-1] = {0.0};

	Eigen::MatrixXd A(N_points-2, N_points-2);
	A.setZero();
	Eigen::VectorXd b(N_points-2);
	b.setZero();
	Eigen::VectorXd c(N_points-2);
	c.setZero();
	Eigen::VectorXd g(N_points);
	g.setZero();

	// std::cout << A << std::endl;

	for (uint64_t i = 0; i < N_points-1; ++i)
	{
		delta[i] = (*X).at(i+1) - (*X).at(i);
		//printf("%f\n", delta[i]);
	}

	for (uint64_t i = 0; i < N_points-2; ++i)
	{
		if (i == 0) // start condetion
		{
			A(i,i) = ((delta[i])/6.0)*alpha + ((delta[i] + delta[i+1])/3.0); // b_tilde
			A(i,i+1) = delta[i+1]/6.0; // c
		}
		else if (i == static_cast<uint64_t>(A.rows()) -1) // end condetion
		{
	 		A(i,i-1) = delta[i]/6.0; // a
            A(i,i) = ((delta[i] + delta[i+1])/3.0) + (beta*(delta[i+1]/6.0)); // b_tilde_tilde   
	 	}
	 	else
	 	{

	 		A(i,i-1) = delta[i]/6.0; // a
            A(i,i) = (delta[i] + delta[i+1])/3.0; // b
            A(i,i+1) = delta[i+1]/6.0; // c
	 	}

	 	b(i) = (((*Y).at(i+2) - (*Y).at(i+1))/delta[i+1]) - (((*Y).at(i+1) - (*Y).at(i))/delta[i]); 
	}
	//std::cout << A << std::endl;

	c = A.inverse()*b;

	g(0) = c(0)*alpha;
	g(N_points-1) = c(N_points-3)*beta;



	for (uint64_t i = 1; i < N_points-1; ++i)
	{
		g(i) = c(i-1);
	}
 	//std::cout << g << std::endl;

	for (uint64_t i = 0; i < n_points; ++i)
	{
		for (uint64_t j = 0; j < N_points-1; ++j)
		{

			if (((*X).at(j) <= (*x).at(i)) && ((*x).at(i) <= (*X).at(j+1)))
			{
			// std::cout << j << std::endl;
			y.push_back(
				((g(j)/6.0) * ((pow(((*X).at(j+1) - (*x).at(i)), 3)/delta[j]) - (delta[j]*((*X).at(j+1) - (*x).at(i)))))
				+ ((g(j+1)/6.0) * ((pow(((*x).at(i) - (*X).at(j)),3)/delta[j]) - (delta[j]*((*x).at(i) - (*X).at(j)))))
				+ (((*Y).at(j) * ((*X).at(j+1) - (*x).at(i))/delta[j]) + ((*Y).at(j+1) * ((*x).at(i) - (*X).at(j))/delta[j]))
				);
			}
		}
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







