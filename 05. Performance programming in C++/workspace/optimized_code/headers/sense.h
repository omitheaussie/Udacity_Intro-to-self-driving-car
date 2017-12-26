#ifndef SENSE_H
#define SENSE_H

#include <vector>
#include <iostream>

void sense(char color, std::vector< std::vector <char> > &grid, std::vector< std::vector <float> > &beliefs,  float p_hit, float p_miss);

#endif /* SENSE.H */