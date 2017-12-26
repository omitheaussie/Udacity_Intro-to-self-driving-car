#include "headers/blur.h"
#include "headers/zeros.h"

using namespace std;

// OPTIMIZATION: Pass large variable by reference
vector < vector < float> > blur(vector < vector < float> > &grid, float blurring,int height, int width) {

	float center = 1.0 - blurring;
	float corner = blurring / 12.0;
	float adjacent = blurring / 6.0;
	static vector < vector <float> > window={{corner,adjacent,corner},{adjacent,center,adjacent},{corner,adjacent,corner}};

	static vector <int> DX={-1,0,1};
	static vector <int> DY={-1,0,1};

	float newVal;

	vector < vector <float> >newGrid=zeros(height,width);
  	
	for (int i=0; i< height; i++ ) {
		for (int j=0; j<width; j++ ) { 
			newVal = grid[i][j];
			for (int ii=0; ii<3; ii++) {
				for (int jj=0; jj<3; jj++) {
					newGrid[(i + DY[ii] + height) % height][(j + DX[jj] + width) % width] += newVal * window[ii][jj];
				}
			}
		}
	}

	return newGrid;
}
