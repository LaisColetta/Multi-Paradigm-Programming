// Write a Procedural C program to check if y is greater than x, and z is greater than y from three given integers x, y, z. Print appropriate messages using printf().

#include <stdio.h>
#include <stdlib.h>
int main(void){

// Call the 'test' function with different inputs and print the results
    printf("%d",test(1, 2, 3));
    }   

    //Function to test if x is less than y and y is less than z
    int test(int x, int y, int z)
         {
        // The function returns 1 (true) if x is less than y and y is less than z.
        // It returns 0 (false) if the condition is not met
           return x < y && y < z;
         }