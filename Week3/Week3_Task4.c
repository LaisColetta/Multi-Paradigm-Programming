//Write a Procedural C program that accepts two integers and returns true if either one is 5, or their sum, or difference, is 5.
// Reference: https://www.w3resource.com/c-programming-exercises/basic-algo/c-programming-basic-algorithm-exercises-18.php

#include <stdio.h>
#include <stdlib.h>


// Function to test if either of the two integers is 5 or if their sum or absolute difference is 5
int main(void){
    // Check if 'x' is equal to 5, 'y' is equal to 5, or their sum is equal to 5.
    // As explained in the class, the '||' operator represents logical OR, so if any of these conditions is true, the function returns 1 (true).
    // If none of these conditions is met, the function returns 0 (false).
    printf("%d",test(5, 4));
    printf("\n%d",test(4, 3));
    printf("\n%d",test(1, 4));
    }   

    // Call the 'test' function with different inputs and print the results
    int test(int x, int y)
         {
          return x == 5 || y == 5 || x + y == 5 || abs(x - y) == 5;
        
        }


// If x or y is equal to 5, the function returns true (1).
// If the sum of x and y is equal to 5, the function returns true.
// If the absolute difference between x and y is equal to 5, the function returns true.
// If none of the above conditions are met, the function returns false (0).
