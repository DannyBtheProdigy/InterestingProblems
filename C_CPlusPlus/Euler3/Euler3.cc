/*
 * Euler3.cc
 *
 *  Created on: Dec 20, 2017
 *      Author: DannyB
 */

#include <iostream>
#include <ctime>
using namespace std;

int main()
{
	clock_t start, stop;
	double elapsed_time;
	long long number = 600851475143;
	unsigned half = number / 2;
	unsigned test = 2;

	start = clock();

	while(test < half)
	{
		if((number % test) == 0)
		{
			number = number / test;
			half = number / 2;
			test = 2;
		}
		else
		{
			test = test + 1;
		}
	}

	stop = clock() - start;
	elapsed_time = (double(stop) / double(CLOCKS_PER_SEC));

	cout << number << endl;
	cout << elapsed_time << endl;
}



