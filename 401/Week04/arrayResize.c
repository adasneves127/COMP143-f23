#include <stdlib.h>
#include <stdio.h>


int getArrSize(int* arr){
    int arraySize = 0;
    for(int* x = arr; *x != '\0'; x++){
        arraySize++;
    }
    return arraySize;
}

void insert(int* oldArray, int idx, int data){
    
    int arraySize = getArrSize(oldArray);

    // Allocate a new arrau
    int* newArray = (int*)malloc((arraySize + 1) * sizeof(int));

    for(int i = 0; i < idx; i++){
        newArray[i] = oldArray[i];
    }
    newArray[idx] = data;
    for(int i = idx; i < arraySize + 1; i++){
        newArray[i] = oldArray[i - 1];
    }
    free(oldArray);
    oldArray = newArray;


}

int main(void){
    int* initialArray = (int*)malloc(5 * sizeof(int));

    initialArray[0] = 2;
    initialArray[1] = 3;
    initialArray[2] = 4;
    initialArray[3] = 5;
    initialArray[4] = 6;

    insert(initialArray, 3, 0);

    for(int i = 0; i < getArrSize(initialArray); i++){
        printf("%i\n", initialArray[i]);
    }

}