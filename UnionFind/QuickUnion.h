#ifndef QUICKUNION_H
#define QUICKUNION_H

#include <vector>

#include "UnionFind.h"

class QuickUnion: public UnionFind {
public:
	QuickUnion(int);

	void connect(int, int);
	int find(int);
};

#endif