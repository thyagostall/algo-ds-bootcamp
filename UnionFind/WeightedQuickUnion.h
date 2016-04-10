#ifndef WEIGHTEDQUICKUNION_H
#define WEIGHTEDQUICKUNION_H

#include <vector>

#include "QuickUnion.h"

class WeightedQuickUnion: public QuickUnion {
protected:
	std::vector<int> sizes;
public:
	WeightedQuickUnion(int);

	virtual void connect(int, int) override;
	virtual int find(int) override;
};

#endif