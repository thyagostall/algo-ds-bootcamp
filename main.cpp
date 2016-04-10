#include <iostream>

#include "unionfind/UFPathCompression.h"

using namespace std;

int main() {
	UFPathCompression qu {30};

	qu.connect(1, 2);
	qu.connect(2, 3);
	qu.connect(3, 4);
	qu.connect(5, 6);
	qu.connect(4, 6);
}