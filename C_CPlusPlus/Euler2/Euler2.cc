/*
 * Euler2.cc
 *
 *  Created on: Dec 19, 2017
 *      Author: DannyB
 */



#include <iostream>
#include <ctime>
using namespace std;

int main()
{
	clock_t start, stop;
	double elapsed_time;
	unsigned fibonacci1 = 1;
	unsigned fibonacci2 = 2;
	unsigned next_fibonacci, sum;

	start = clock();

	next_fibonacci = fibonacci1 + fibonacci2;
	sum = 2;
	while(next_fibonacci < 4000000)
	{
		if((next_fibonacci % 2) == 0)
		{
			sum = sum + next_fibonacci;
		}
		fibonacci1 = fibonacci2;
		fibonacci2 = next_fibonacci;
		next_fibonacci = fibonacci1 + fibonacci2;
	}

	stop = clock() - start;
	elapsed_time = (double(stop) / double(CLOCKS_PER_SEC));

	cout << sum << endl;
	cout << elapsed_time << endl;
}
