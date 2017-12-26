#include "headers/move.h"
#include "headers/zeros.h"

using namespace std;

// OPTIMIZATION: Pass large variable by reference
vector<vector<float>> move(int dy, int dx, 
	vector < vector <float> > &beliefs) 
{
	int height, width;
	height = beliefs.size();
	width = beliefs[0].size();

	vector < vector <float> > newGrid;
  
  	// OPTIMIZATION: Use improved zeros function
	newGrid = zeros(height, width);

// OPTIMIZATION: Eliminate any variables that aren't needed
	dy=dy+height;
  	dx=dx+width;
  	for (int i=0; i<height; i++) {
		for (int j=0; j<width; j++) {
			newGrid[(i + dy ) % height][(j + dx)  % width] = beliefs[i][j];
		}
	}
	return newGrid;
}
