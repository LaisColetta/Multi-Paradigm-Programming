// Create structs to represent manager (name, age, salary, an array of the employees they manage)
// Reference: https://www.shiksha.com/online-courses/articles/structure-in-c-programming/

#include <stdio.h>
#include <string.h>


// Define a struct named "Manager"
struct Manager {
    char name[100];                
    int age;                        
    double salary;                  
    struct Employee employees[10]; 
    int numEmployees;               
};

// Define a struct named "Employee" 
struct Employee {
    char name[100];     
    int age;           
    double salary;      
    int yearsWorked;    
    char jobTitle[100]; 
};

int main(void) {

    struct Employee employee1;
    strcpy(employee1.name, "John Doe");
    employee1.age = 30;
    employee1.salary = 50000.0;
    employee1.yearsWorked = 5;
    strcpy(employee1.jobTitle, "Software Engineer");
    
    struct Employee employee2;
    strcpy(employee2.name, "Alice Park");
    employee1.age = 45;
    employee1.salary = 70000.0;
    employee1.yearsWorked = 4;
    strcpy(employee1.jobTitle, "Developer");
    
    struct Employee employee3;
    strcpy(employee2.name, "Robert Mass");
    employee1.age = 37;
    employee1.salary = 60000.0;
    employee1.yearsWorked = 4;
    strcpy(employee1.jobTitle, "Project Analyst");

    struct Manager manager1;
    strcpy(manager1.name, "Alice Smith");
    manager1.age = 40;
    manager1.salary = 75000.0;

    // Add employees to the manager's array
    manager1.employees[0] = employee1;
    manager1.employees[1] = employee2;
    manager1.numEmployees = 2; // Indicate managing two employees

    // Print the manager's information
    printf("Manager Name: %s\n", manager1.name);
    printf("Manager Age: %d\n", manager1.age);
    printf("Manager Salary: %.2f\n", manager1.salary);

    // Print the information of the employees managed by the manager
    for (int i = 0; i < manager1.numEmployees; i++) {
        printf("Employee %d:\n", i + 1);
        printf("Name: %s\n", manager1.employees[i].name);
        printf("Age: %d\n", manager1.employees[i].age);
        printf("Salary: %.2f\n", manager1.employees[i].salary);
    }

    return 0;
}
