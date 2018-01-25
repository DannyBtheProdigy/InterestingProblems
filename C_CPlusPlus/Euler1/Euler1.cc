/*
 * Euler1.cc
 *
 *  Created on: Dec 18, 2017
 *      Author: DannyB
 */

#include <iostream>
#include <ctime>
using namespace std;

int main()
{
	clock_t start, stop;
	double elapsed_time;
	unsigned number;
	unsigned sum = 0;

	start = clock();

	for(number = 0; number < 1000; number++)
	{
		if(((number % 3) == 0) ||
		   ((number % 5) == 0))
		{
			sum = sum + number;
		}
	}

	stop = clock() - start;
	elapsed_time = (double(stop) / double(CLOCKS_PER_SEC));

	cout << sum << endl;
	cout << elapsed_time << endl;
}
