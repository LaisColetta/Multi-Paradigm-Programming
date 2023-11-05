// Create structs to represent an employee (name, age, salary, years worked, job title)
// Reference: https://www.simplilearn.com/tutorials/c-tutorial/structure-in-c

#include <stdio.h>
#include <string.h>

// Define a struct named "Employee" to represent an employee
struct Employee {
    char name[100];     
    int age;           
    int salary;      
    int yearsWorked;    
    char jobTitle[100];
};

int main(void) {
    // Create an employee struct
    struct Employee employee1;

    // Assign values to the attributes of the employee
    strcpy(employee1.name, "Lais Coletta");
    employee1.age = 31;
    employee1.salary = 50000.0;
    employee1.yearsWorked = 2;
    strcpy(employee1.jobTitle, "Analyst");

    // Print the employee's information
    printf("Employee Name: %s\n", employee1.name);
    printf("Employee Age: %d\n", employee1.age);
    printf("Employee Salary: %.2f\n", employee1.salary);
    printf("Years Worked: %d\n", employee1.yearsWorked);
    printf("Job Title: %s\n", employee1.jobTitle);

    // Create a second employee struct
    struct Employee employee2;

    // Assign values to the attributes of the employee 2
    strcpy(employee2.name, "Darwin Paz");
    employee2.age = 28;
    employee2.salary = 30000.0;
    employee2.yearsWorked = 0.5;
    strcpy(employee2.jobTitle, "Junior engineer"\n\n);

    // Print the employee's 2 information
    printf("Employee Name: %s\n", employee2.name);
    printf("Employee Age: %d\n", employee2.age);
    printf("Employee Salary: %.2f\n", employee2.salary);
    printf("Years Worked: %d\n", employee2.yearsWorked);
    printf("Job Title: %s\n", employee2.jobTitle);

    return 0;
}
