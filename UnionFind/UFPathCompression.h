#ifndef UF_PATH_COMPRESSION_H
#define UF_PATH_COMPRESSION_H

#include <vector>

#include "QuickUnion.h"

class UFPathCompression: public QuickUnion {
private:
	int root(int);
protected:
	std::vector<int> sizes;
public:
	UFPathCompression(int);

	virtual void connect(int, int) override;
	virtual int find(int) override;
};

#endif