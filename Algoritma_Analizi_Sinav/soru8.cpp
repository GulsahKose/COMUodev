#include <iostream>
#include <ctime>
#include <stdlib.h>
using namespace std;



int main() {

	int size = 10;
	int* arr = new int[size];

	srand((unsigned)time(NULL));
		for (int i = 1; i < 26; i++)
		{
			if (i>size){
				size = size * 2;
		        int* newArr = new int[size];

				for(int i=0; i<size/2; i++){
				   	newArr[i]=arr[i];
				}
				delete [] arr;
				arr = newArr;
			}
			arr[i] = 1+ rand() % 10;
	    }

	return 0;
}

