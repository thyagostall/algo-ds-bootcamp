#include <iostream>

#include "unionfind/QuickUnion.h"

using namespace std;

int main() {
	QuickUnion qu {10};

	cout << "Count: ";
	cout << qu.count() << endl;
}