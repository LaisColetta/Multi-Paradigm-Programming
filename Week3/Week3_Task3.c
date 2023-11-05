// Write a Procedural C program to compute the sum of the two given integers. If the sum is in the range 10..20 inclusive return 30
// I am unsure if the integers should be given by the user or not. If given by the user: 
//Reference: https://www.w3resource.com/c-programming-exercises/basic-declarations-and-expressions/c-programming-basic-exercises-9.php

#include <stdio.h>
int main() 
{
    int x, y, sum; // Declare variables for two integers and their sum
    
    // Prompt user for input and store in 'x'
    printf("\nInput the first integer: "); 
    scanf("%d", &x);
    
    // Prompt user for input and store in 'y'
    printf("\nInput the second integer: ");
    scanf("%d", &y);
    
    sum = x + y; // Calculate the sum of 'x' and 'y'

    // Check if the sum is in the range of 10 to 20 (inclusive) and return 30 if true
    if (sum >= 10 && sum <= 20) {
        printf("The sum is in the range of 10 to 20 inclusive. Returning 30.\n");
        return 30;
    }
    
    // Print the sum if it's not in the specified range

    printf("\nSum of the above two integers = %d\n", sum);
    
    return 0; // Indicate successful execution
}