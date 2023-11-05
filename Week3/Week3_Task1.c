//Write a Procedural C program to calculate the absolute difference between n and 51. If n is greater than 51 return triple the
//absolute difference. Listing 1 provides an example of determining the absolute value of a number.
// Note the use of an include statement.

// Function to calculate the absolute difference between n and 51, with a condition
#include <stdio.h>
#include <stdio.h>
int main(void){
    
    // Print the test function with different inputs and print the results
    printf("%d",test(53));
    printf("\n%d",test(30));
    printf("\n%d",test(51));
    }
    
   int test(int n)
        {
         const int x = 51; // Declare a constant variable x with a value of 51

            if (n > x)
            {
                return (n - x)*3; // If n is greater than 51, return three times the absolute difference
            }
            return x - n; // If n is not greater than 51, return the absolute difference
    
        }