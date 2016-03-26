#ifndef QUICKUNION_H
#define QUICKUNION_H

#include <vector>

#include "UnionFind.h"

class QuickUnion: public UnionFind {
private:
	std::vector<int> parents;
public:
	QuickUnion(int);

	void connect(int, int);
	int find(int);
	bool connected(int, int);
	int count();
};

#endif