// Write a Procedural C program to check if two or more non-negative given integers have the same rightmost digit.
#include <stdio.h>
#include <stdlib.h>

// Function to test if any two of the three integers have the same last digit
int test(int x, int y, int z) {
    // The function returns 1 (true) if any two of the three integers have the same last digit.
    // It checks if the last digit of 'x', 'y', or 'z' (obtained using x % 10, y % 10, or z % 10) is the same as any of the other two.
    // If the condition is met, the function returns 1; otherwise, it returns 0 (false).
    return x % 10 == y % 10 || x % 10 == z % 10 || y % 10 == z % 10;
}

int main(void) {
    // Call the 'test' function with different inputs and print the results
    printf("Result for test(11, 21, 31): %d\n", test(11, 21, 31)); // Call 'test' with x=11, y=21, and z=31
    printf("Result for test(11, 22, 31): %d\n", test(11, 22, 31)); // Call 'test' with x=11, y=22, and z=31
    printf("Result for test(11, 22, 33): %d\n", test(11, 22, 33)); // Call 'test' with x=11, y=22, and z=33

    return 0; // Return 0 to indicate successful execution
}
