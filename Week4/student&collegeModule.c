// Create structs to represent: 1 - Student (name, age, an array of their college modules) 2 - A college module (module name, credits it is worth)

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Define a structure named "Module" 
struct Module {
    char name[50];    
    int credits;     
};

// Define a structure named "Student" to represent a student with name, age, and an array of modules
struct Student {
    char name[100];     
    int age;            
    struct Module modules[10]; // An array of Module structures to store a student's modules (up to 10 modules)
};

// Function to print the name and credits of a module
void printModule(struct Module module) {
    printf("Module name: %s\n", module.name);
    printf("Module credits: %d\n", module.credits);
}

int main(void) {
    // Create Module structures for the modules the student is taking, including credits
    struct Module modules[] = {
        {"Multi - paradigm Programming", 5},
        {"Introduction to Programming", 5},
        {"Data Representation", 5},
    };
    
    // Create a Student structure named "student" 
    struct Student student = {
        .name = "John Doe", 
        .age = 20,          
    };

    // Copy the modules with credits into the student's module array
    for (int i = 0; i < 10 && i < sizeof(modules) / sizeof(modules[0]); i++) {
        strcpy(student.modules[i].name, modules[i].name);
        student.modules[i].credits = modules[i].credits;
    }

    // Print the student's name and age
    printf("Student Name: %s\n", student.name);
    printf("Student Age: %d\n", student.age);
    
    // Print the modules the student is taking, including credits
    printf("Modules the student is taking:\n");
    for (int i = 0; i < 10; i++) {
        if (strlen(student.modules[i].name) > 0) {
            printModule(student.modules[i]);
        }
    }

    return 0; // Return 0 to indicate successful execution
}
