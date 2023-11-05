//Write a Procedural C program to check two given integers, and return true if one of them is 30 or if their sum is 30. 
//C doesn’t have booleans built-in, so you can use the snippet in Listing 2 or use the values 1 and 0.
//Reference: https://www.w3resource.com/c-programming-exercises/basic-algo/c-programming-basic-algorithm-exercises-3.php

#include <stdio.h>
#include <stdbool.h>

bool test(int x, int y) {
    return x == 30 || y == 30 || (x + y == 30);
}

int main(void) {
    bool x = false;

    printf("%d", test(10, 5));
    printf("\n%d", test(10, 30));
    printf("\n%d", test(20, 25));

    return 0;
}

// 1 = true, 0 =false






