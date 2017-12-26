#include "headers/initialize_beliefs.h"

using namespace std;

// OPTIMIZATION: pass large variables by reference
vector< vector <float> > initialize_beliefs(int height, int width, float prob_per_cell) {
	return vector< vector <float> > (height,vector<float>(width, prob_per_cell));
}