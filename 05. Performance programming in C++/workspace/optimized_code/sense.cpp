#include "headers/sense.h"

using namespace std;

// OPTIMIZATION: Pass larger variables by reference
void sense(char color, vector< vector <char> > &grid, vector< vector <float> > &beliefs,  float p_hit, float p_miss) 
{
	for (int i=0; i<grid.size(); i++) {
		for (int j=0; j<grid[0].size(); j++) {
          	beliefs[i][j]=beliefs[i][j]*(p_hit*(grid[i][j] == color) + p_miss*(grid[i][j] != color));
    	}
	}
}
