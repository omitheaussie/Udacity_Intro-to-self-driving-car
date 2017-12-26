#include "headers/normalize.h"
using namespace std;

// OPTIMIZATION: Pass variable by reference
void normalize(vector< vector <float> > &grid, int height, int width) {

  	// OPTIMIZATION: Avoid declaring and defining 				// intermediate variables that are not needed.
	float total = 0.0;

	for (int i = 0; i < height; i++)
	{
		for (int j=0; j< width; j++)
		{
			total += grid[i][j];
		}
	}
	/*for (int i=0; i<(height*width); i++) 
	{
      	 total+=grid[i % width][i / width];
	}*/
  	for (int i = 0; i < height; i++) {
		for (int j=0; j< width; j++) {
          	grid[i][j]=grid[i][j]/total;
		}
	}

}
