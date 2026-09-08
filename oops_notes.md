# UNIT 1 — OBJECT-ORIENTED THINKING & OBJECT-ORIENTED PROGRAMMING

---

## 1. OBJECT-ORIENTED THINKING

### Definition
**Object-Oriented Thinking (OOT)** is a problem-solving approach in which a problem is analyzed and designed in terms of objects, their properties, their behaviors, and the relationships between them.

In simple words, object-oriented thinking means looking at a problem in the same way we look at the real world. In the real world, we interact with different entities or objects. Each object has some characteristics and performs certain actions.

For example, in a **College Management System**, we can identify objects such as:
- Student
- Teacher
- Course
- Classroom
- Department
- Examination

Each object has its own data and behavior.

For example, a **Student** may have:

**Properties (Data / Attributes):**
- Name
- Roll Number
- Age
- Course
- Marks

**Behaviors (Actions / Methods):**
- Attend class
- Study
- Give examination
- Pay fees

Thus, object-oriented thinking helps us identify the objects involved in a problem before writing the actual program.

---

### Real-World Example
Consider a **Banking System**.

Instead of thinking in a procedural step-by-step manner:
> *"First take account number, then take amount, then calculate balance..."*

We think in terms of **Objects & Entities**:

```text
Bank
 |
 ├── Customer
 |
 ├── Account
 |
 └── Transaction
```

An **Account** has:
- **Attributes:** Account Number, Account Holder, Balance, Account Type
- **Operations:** `deposit()`, `withdraw()`, `checkBalance()`

This is object-oriented thinking because we are identifying the entities involved and their responsibilities.

---

### C++ Example
```cpp
#include <iostream>
using namespace std;

class BankAccount
{
private:
    int accountNumber;
    double balance;

public:
    void deposit(double amount)
    {
        balance += amount;
    }

    void withdraw(double amount)
    {
        if (amount <= balance)
            balance -= amount;
    }

    void displayBalance()
    {
        cout << "Balance: " << balance << endl;
    }
};

int main()
{
    BankAccount account;

    account.deposit(5000);
    account.withdraw(1000);
    account.displayBalance();

    return 0;
}
```

**Explanation:**
Here, we first identified `BankAccount` as an object-oriented entity and then defined its data and behavior.

---

### Advantages
1. **Natural representation:** Real-world entities can be represented naturally as objects.
2. **Better problem understanding:** Breaking a problem into objects makes complex problems easier to understand.
3. **Easier design:** Objects and their relationships can be identified before programming.
4. **Supports reusability:** Once objects/classes are designed, they can be reused.
5. **Easier maintenance:** Each object generally has a specific responsibility, making changes easier.

### Disadvantages
1. **Requires proper analysis:** Incorrect identification of objects can result in poor program design.
2. **Can be complex:** Large systems may contain hundreds or thousands of interacting objects.
3. **More planning is required:** Object-oriented design generally requires more planning before coding.
4. **Not always necessary:** For very small programs, object-oriented thinking may introduce unnecessary complexity.

### Key Point
> **Key Point:** Object-Oriented Thinking is the process of understanding and designing a problem in terms of objects, their properties, behaviors, and relationships.

---
---

## 2. OBJECT-ORIENTED PROGRAMMING

### Definition
**Object-Oriented Programming (OOP)** is a programming paradigm in which software is designed and developed using objects and classes.

An object contains data and functions that operate on that data. OOP allows programmers to model real-world entities inside a computer program.

The main objective of OOP is to make programs:
- **Modular**
- **Reusable**
- **Secure**
- **Maintainable**
- **Flexible**
- **Easy to understand**

OOP is based on several important concepts such as:
- Class
- Object
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism
- Data hiding
- Message passing
- Dynamic binding

---

### Real-World Example
Consider a **Car**.

A car has properties such as:
- Color
- Model
- Speed
- Engine Number
- Fuel Level

It also performs actions:
- `start()`
- `stop()`
- `accelerate()`
- `brake()`

In OOP, we can represent this car as a class.

---

### C++ Example
```cpp
#include <iostream>
using namespace std;

class Car
{
public:
    string color;
    int speed;

    void start()
    {
        cout << "Car started" << endl;
    }

    void accelerate()
    {
        speed += 10;
        cout << "Speed: " << speed << endl;
    }

    void stop()
    {
        cout << "Car stopped" << endl;
    }
};

int main()
{
    Car c1;

    c1.color = "Black";
    c1.speed = 0;

    c1.start();
    c1.accelerate();
    c1.stop();

    return 0;
}
```

**Mapping Breakdown:**
- `Car`     → Class
- `c1`      → Object
- `color`   → Data
- `speed`   → Data
- `start()` → Behavior
- `stop()`  → Behavior

---

### Main Characteristics of OOP
1. **Class:** A class is a blueprint used to create objects.
2. **Object:** An object is an instance of a class.
3. **Encapsulation:** Data and functions are combined into one unit.
4. **Abstraction:** Unnecessary implementation details are hidden.
5. **Inheritance:** Existing classes can be reused to create new classes.
6. **Polymorphism:** One interface can have multiple forms.
7. **Data Hiding:** Internal data can be protected from direct access.

---

### Advantages
1. **Reusability:** Code can be reused through inheritance and classes.
2. **Security:** Encapsulation and data hiding improve data security.
3. **Maintainability:** Programs can be divided into independent classes.
4. **Modularity:** Large programs can be divided into smaller modules.
5. **Real-world modeling:** Real-world entities can be represented easily.
6. **Flexibility:** Polymorphism allows flexible program design.

### Disadvantages
1. **Complexity:** OOP contains many concepts that beginners need time to understand.
2. **Memory requirement:** Objects and additional OOP mechanisms may require more memory.
3. **Development time:** Designing classes and relationships can take additional time.
4. **Performance overhead:** Some OOP mechanisms can introduce additional processing overhead.
5. **Not suitable for every problem:** Small and simple problems may be easier to solve using procedural programming.

### Key Point
> **Key Point:** OOP organizes a program around objects that contain data and behavior, making software modular, reusable, maintainable, and easier to model.

---
---

## 3. PROCEDURAL PROGRAMMING

### Definition
**Procedural Programming** is a programming paradigm in which a program is organized as a sequence of functions or procedures that perform specific tasks.

The primary focus is on:
> **"What steps should be performed to solve the problem?"**

In procedural programming, the program is usually divided into several functions. Each function performs a particular operation.

Examples of procedural programming languages include:
- **C**
- **Pascal**
- **FORTRAN**
- **COBOL**

*C is one of the most commonly used procedural programming languages.*

---

### Real-World Example
Suppose we want to calculate a student's result.

The procedural approach may be:
1. Take student name
2. Take marks
3. Calculate total
4. Calculate percentage
5. Calculate grade
6. Display result

We can create separate functions:
- `input()`
- `calculateTotal()`
- `calculatePercentage()`
- `calculateGrade()`
- `display()`

The focus is on **functions** and the **sequence of operations**.

---

### C Example
```c
#include <stdio.h>

int calculateTotal(int a, int b, int c)
{
    return a + b + c;
}

float calculatePercentage(int total)
{
    return total / 3.0;
}

int main()
{
    int m1, m2, m3;
    int total;
    float percentage;

    printf("Enter marks: ");
    scanf("%d %d %d", &m1, &m2, &m3);

    total = calculateTotal(m1, m2, m3);
    percentage = calculatePercentage(total);

    printf("Total = %d\n", total);
    printf("Percentage = %.2f\n", percentage);

    return 0;
}
```

**Explanation:** The program is organized entirely around global/local data passed to functions.

---

### Characteristics
1. **Functions are the primary unit:** Programs are divided into functions.
2. **Top-down approach:** The problem is divided into smaller tasks from top to bottom.
3. **Data and functions are separate:** Data may be shared between functions and moved globally.
4. **Sequential execution:** Statements generally execute according to the defined flow.
5. **Limited data protection:** There is comparatively less support for data hiding.

---

### Advantages
1. **Simple for small programs:** Procedural programming is easy to understand for simple problems.
2. **Easy implementation:** Functions can be directly created for individual tasks.
3. **Efficient:** Procedural programs can be efficient because they generally have less abstraction overhead.
4. **Easy to learn:** Languages like C provide a relatively straightforward programming model.

### Disadvantages
1. **Difficult to maintain large programs:** Large programs can contain hundreds of functions and global variables.
2. **Less data security:** Data can be accessed and modified by multiple functions.
3. **Limited reusability:** Code reuse is less powerful compared with OOP inheritance and class-based reuse.
4. **Difficult real-world modeling:** Representing real-world entities is less natural.
5. **Changes can affect multiple functions:** A change in shared data structure may require modifications across several functions.

---
---

## 4. COMPARISON OF PROCEDURAL AND OBJECT-ORIENTED PROGRAMMING

### Definition
Procedural and Object-Oriented Programming are two different approaches to software development.
- **Procedural programming** focuses primarily on functions and procedures.
- **OOP** focuses primarily on objects and classes.

---

### Real-World Example
Consider a **Banking Application**:

- **Procedural approach:**
  We create separate functions:
  - `createAccount()`
  - `deposit()`
  - `withdraw()`
  - `checkBalance()`
  - `closeAccount()`
  *(Data is stored in separate structures and passed into functions).*

- **Object-oriented approach:**
  We create an `Account` class binding data and behavior:
  ```text
  Account
   |
   ├── accountNumber
   ├── balance
   |
   ├── deposit()
   ├── withdraw()
   └── checkBalance()
  ```

---

### Comparison Table

| Feature | Procedural Programming (POP) | Object-Oriented Programming (OOP) |
| :--- | :--- | :--- |
| **Main unit** | Function | Object / Class |
| **Approach** | Top-down | Bottom-up |
| **Main focus** | Procedures (Algorithms & Functions) | Objects (Data + Behavior) |
| **Data & functions** | Separate | Combined / Bound together |
| **Data hiding** | Limited / Not present | Strong (via access specifiers) |
| **Security** | Lower | Higher |
| **Reusability** | Limited | High (Inheritance, Polymorphism) |
| **Inheritance** | Not supported as a core feature | Supported |
| **Polymorphism** | Not a core feature | Supported |
| **Real-world modeling** | Difficult | Easy & Intuitive |
| **Large programs** | Difficult to manage | Easier to manage |
| **Maintenance** | Difficult | Easier |
| **Examples** | C, Pascal, FORTRAN | C++, Java, C#, Python |

---

### Advantages of OOP over Procedural Programming
- Better data security
- Better code reusability
- Easier maintenance
- Better real-world modeling
- Supports inheritance
- Supports polymorphism
- Better modularity

### Disadvantages of OOP
- More complex
- Requires more planning
- May use additional memory
- Can have performance overhead
- Not always necessary for simple programs

---
---

## 5. FEATURES OF OBJECT-ORIENTED PARADIGM

### Definition
The **Object-Oriented Paradigm** is a programming approach that organizes software around objects rather than only functions.

The important features are:
1. **Objects**
2. **Classes**
3. **Encapsulation**
4. **Abstraction**
5. **Inheritance**
6. **Polymorphism**
7. **Data hiding**
8. **Message passing**
9. **Dynamic binding**
10. **Reusability**

---

### Detailed Features

#### 1. Objects
Objects represent entities.
```cpp
Student s1;
```

#### 2. Classes
Classes define the structure and behavior of objects.
```cpp
class Student
{
    // data members and member functions
};
```

#### 3. Encapsulation
Combining data and functions into one single unit (class).

#### 4. Abstraction
Showing essential information and hiding background implementation details.

#### 5. Inheritance
Creating a new class from an existing class.
```cpp
class Dog : public Animal
{
    // inherits properties of Animal
};
```

#### 6. Polymorphism
Allowing the same interface/name to behave differently depending on the context.

#### 7. Data Hiding
Protecting internal data from unauthorized external access using access control specifiers (`private`, `protected`).

#### 8. Message Passing
Objects communicate with each other through method calls.
```cpp
student.display();
```

#### 9. Dynamic Binding
The method code to execute in response to a call is determined at runtime.

#### 10. Reusability
Existing code and classes can be reused in new programs without rewriting.

---

### Real-World Example
A **University Management System** can contain:
```text
University
 |
 ├── Student
 ├── Teacher
 ├── Course
 ├── Department
 └── Examination
```
Each object has its own properties and behavior.

---

### Advantages
- Modularity
- Reusability
- Security
- Maintainability
- Flexibility
- Real-world representation
- Reduced duplication
- Easier extension

### Disadvantages
- More complex than simple procedural programs
- Requires proper design
- May require more memory
- Development can take longer
- Some mechanisms introduce overhead

---
---

## 6. MERITS AND DEMERITS OF OBJECT-ORIENTED METHODOLOGY

### Definition
**Object-oriented methodology** is a systematic approach to software development where systems are analyzed, designed, and implemented using objects and their relationships.

---

### Merits
1. **Modularity:** The system can be divided into independent classes and objects.
2. **Reusability:** Existing classes can be reused across different projects.
3. **Data Security:** Data hiding protects internal information from accidental modification.
4. **Easy Maintenance:** Changes can often be made within individual classes without breaking the entire program.
5. **Extensibility:** New features can easily be added using inheritance and polymorphism.
6. **Real-world modeling:** Real-world entities can be represented naturally.
7. **Reduced duplication:** Reusable classes reduce repeated boilerplate code.
8. **Better scalability:** OOP is highly suitable for large and enterprise software systems.

### Demerits
1. **Complexity:** The concepts can be difficult for beginners to grasp initially.
2. **More development time:** Designing proper class hierarchies requires upfront planning.
3. **Memory usage:** Objects and virtual table mechanisms can require additional memory.
4. **Performance:** Some OOP mechanisms (like dynamic dispatch) introduce slight runtime overhead.
5. **Poor design can cause problems:** Incorrect relationships between classes can make the program needlessly complicated.

---

### Real-World Example
Consider an **E-commerce Application**:
Objects might be:
- `Customer`
- `Product`
- `Cart`
- `Order`
- `Payment`
- `Delivery`

Each class handles its own responsibility.

If we want to add a new payment method (e.g., Crypto or UPI), we can extend the payment system without rewriting the entire application. This demonstrates the **maintainability** and **extensibility** advantages of OOP.

---
---

## 7. OBJECT MODEL

### Definition
An **Object Model** is a conceptual model that represents a software system as a collection of objects, classes, attributes, operations, and relationships.

It describes how objects are structured and how they interact with one another. An object model helps developers understand the architecture and structure of a system before implementation.

---

### Main Elements of Object Model
1. **Object:** Represents an individual entity.
2. **Class:** Defines a group/type of similar objects.
3. **Attributes:** Represent object data and state.
4. **Operations:** Represent object behavior and methods.
5. **Relationships:** Represent connections and associations between objects.

---

### Real-World Example
Consider a **Library Management System**:

**Objects:**
- Student
- Book
- Librarian
- Library
- Issue
- Return

A **Book** may have:
- **Attributes:** Book ID, Title, Author, Price, Availability
- **Operations:** `issueBook()`, `returnBook()`, `displayDetails()`

**Relationship:**
```text
Student ---- borrows ----> Book
```

---

### C++ Representation
```cpp
#include <string>
using namespace std;

class Book
{
private:
    int bookId;
    string title;
    bool available;

public:
    void issueBook()
    {
        available = false;
    }

    void returnBook()
    {
        available = true;
    }
};
```
*This class represents the object model of a book.*

---

### Advantages
- Helps understand system structure
- Makes design easier
- Helps identify relationships
- Supports modular development
- Makes complex systems easier to visualize
- Helps before actual implementation

### Disadvantages
- Designing a detailed object model takes time
- Poor modeling can lead to poor implementation
- Large systems can have complicated object relationships
- Requires knowledge of object-oriented design

---
---

## 8. ELEMENTS OF OOPS

The major elements of Object-Oriented Programming are:
1. **Class**
2. **Object**
3. **Encapsulation**
4. **Abstraction**
5. **Inheritance**
6. **Polymorphism**
7. **Data Hiding**
8. **Message Passing**
9. **Dynamic Binding**
10. **Reusability**

### Summary of Elements:
1. **Class:** A class is a blueprint for objects.
   ```cpp
   class Student { };
   ```
2. **Object:** An object is an instance of a class.
   ```cpp
   Student s1;
   ```
3. **Encapsulation:** Binding data and methods together into a single unit.
4. **Abstraction:** Hiding unnecessary implementation details and exposing essentials.
5. **Inheritance:** Acquiring properties and behavior from another class.
6. **Polymorphism:** One interface with multiple forms.
7. **Data Hiding:** Restricting direct access to internal data.
8. **Message Passing:** Communication between objects.
   ```cpp
   s1.display();
   ```
9. **Dynamic Binding:** Selecting the appropriate method during runtime.
10. **Reusability:** Using existing code and structures again.

---
---

## 9. CLASS

### Definition
A **class** is a user-defined data type and a blueprint or template for creating objects.

A class can contain:
- Data members (Variables)
- Member functions (Methods)
- Constructors
- Destructors
- Access specifiers (`private`, `public`, `protected`)

### Example:
```cpp
#include <iostream>
#include <string>
using namespace std;

class Student
{
private:
    string name;
    int age;

public:
    void display()
    {
        cout << name << " " << age;
    }
};
```

---

### Real-World Example
Think of a class as a **blueprint of a house**.

The blueprint specifies:
- Number of rooms
- Doors
- Windows
- Kitchen
- Bathroom

But the blueprint itself is not an actual house; it occupies no physical ground.

Similarly:
- **Class** → Blueprint (No memory allocated for variables)
- **Object** → Actual entity (Memory is allocated)

One class can create many objects:
```cpp
Student s1;
Student s2;
Student s3;
```

---

### Advantages
- Provides structure
- Supports encapsulation
- Allows multiple objects
- Supports reusability
- Makes programs organized
- Makes maintenance easier

### Disadvantages
- Requires additional design
- Can be unnecessary for very small programs
- Large class hierarchies can become complicated

---
---

## 10. OBJECT

### Definition
An **object** is an instance of a class.

An object represents a specific entity and contains its own state while using the behavior defined by its class.

```cpp
Student s1;
```
Here:
- `Student` → Class
- `s1`      → Object

---

### Real-World Example
Consider a class: `Car`

Actual cars are objects:
- `Car 1` → Black BMW
- `Car 2` → White BMW
- `Car 3` → Red BMW

All belong to the same general category (Class), but each has a different state (color, license plate, speed).

---

### C++ Example
```cpp
#include <iostream>
#include <string>
using namespace std;

class Student
{
public:
    string name;
    int age;

    void display()
    {
        cout << name << " " << age << endl;
    }
};

int main()
{
    Student s1;

    s1.name = "Ravi";
    s1.age = 20;

    s1.display();

    return 0;
}
```
*Here `s1` is an object.*

---

### Characteristics of Objects
1. **State:** Data and attributes stored inside the object (e.g., `name = "Ravi"`, `age = 20`).
2. **Behavior:** Operations and methods performed by the object (e.g., `display()`).
3. **Identity:** A unique address or identifier distinguishing it from all other objects in memory.

---

### Advantages
- Represents real-world entities
- Supports modularity
- Makes programs easier to understand
- Provides object-level organization
- Allows multiple instances

### Disadvantages
- Large numbers of objects may consume memory
- Object interactions can become complex
- Requires proper class design

---
---

## 11. ENCAPSULATION

### Definition
**Encapsulation** is the process of combining data and the functions that operate on that data into a single unit called a **class**.

It also commonly involves controlling access to the internal state of an object (Data Hiding).

---

### Real-World Example
Consider an **ATM Machine**.

The user interacts with a clean interface:
- Withdraw
- Deposit
- Check Balance

The internal banking ledger, database transactions, and hardware vaults are not directly accessible. The ATM encapsulates all internal operations.

---

### C++ Example
```cpp
class BankAccount
{
private:
    double balance; // Data hidden from external access

public:
    void deposit(double amount)
    {
        if (amount > 0)
            balance += amount;
    }

    double getBalance()
    {
        return balance;
    }
};
```

**Breakdown:**
- **Data:** `balance` (Private)
- **Functions:** `deposit()`, `getBalance()` (Public)
Both are bundled together inside the same class.

---

### Advantages
1. **Data protection:** Internal data can be protected from unauthorized/accidental modification.
2. **Modularity:** Data and behavior stay bundled together cleanly.
3. **Maintenance:** Internal implementation can be changed without altering how users interact with the class.
4. **Control:** Access can be precisely controlled using access specifiers (`private`, `protected`, `public`).

### Disadvantages
- May increase code complexity
- Requires proper access design
- Excessive encapsulation can sometimes make simple code unnecessarily complicated

---
---

## 12. ABSTRACTION

### Definition
**Abstraction** is the process of representing only the essential features of an object while hiding unnecessary implementation details.

The user focuses on **what** an object does, rather than **how** it does it internally.

---

### Real-World Example
When using a **Mobile Phone**, you can:
- Make Calls
- Send Messages
- Take Photos
- Play Music

You don't need to understand the internal electronic circuits, DSP algorithms, or RF transceivers to use these functions. That is **abstraction**.

---

### C++ Example
```cpp
class ATM
{
public:
    void withdraw(int amount)
    {
        verifyAccount();
        checkBalance();
        processTransaction();
        dispenseCash();
    }

private:
    void verifyAccount()
    {
        // Internal implementation hidden
    }

    void checkBalance()
    {
        // Internal implementation hidden
    }

    void processTransaction()
    {
        // Internal implementation hidden
    }

    void dispenseCash()
    {
        // Internal implementation hidden
    }
};
```

The user only needs:
```cpp
atm.withdraw(500);
```
The complex four-step implementation remains hidden from the outside world.

---

### Advantages
- Reduces complexity
- Improves usability
- Protects implementation details
- Makes software easier to understand
- Improves maintainability

### Disadvantages
- Designing abstraction properly can be difficult
- Too much abstraction can make debugging harder
- Requires additional design effort

---
---

## 13. INHERITANCE

### Definition
**Inheritance** is an OOP mechanism in which a new class acquires the properties and behaviors of an existing class.

- The existing class is called the: **Base / Parent / Super Class**
- The new class is called the: **Derived / Child / Sub Class**

---

### Real-World Example
```text
             Vehicle
                |
        -----------------
        |       |       |
       Car     Bus     Truck
```
All vehicles have common features:
- `start()`
- `stop()`
- `speed`

Instead of writing these features repeatedly for every class, they can be placed once in the `Vehicle` base class.

---

### C++ Example
```cpp
#include <iostream>
using namespace std;

class Vehicle
{
public:
    void start()
    {
        cout << "Vehicle started" << endl;
    }
};

class Car : public Vehicle
{
public:
    void drive()
    {
        cout << "Car is driving" << endl;
    }
};

int main()
{
    Car c;

    c.start(); // Inherited from Vehicle
    c.drive(); // Defined in Car

    return 0;
}
```
*`Car` inherits `start()` from `Vehicle`.*

---

### Types of Inheritance

#### 1. Single Inheritance
One derived class inherits from one base class.
```text
  [ A ]  (Base)
    |
    v
  [ B ]  (Derived)
```

#### 2. Multiple Inheritance
One class inherits from multiple base classes.
```text
  [ A ]     [ B ]  (Base classes)
     \       /
      v     v
       [ C ]       (Derived class)
```

#### 3. Multilevel Inheritance
Inheritance occurs across multiple hierarchical levels.
```text
  [ A ]  (Grandparent)
    |
    v
  [ B ]  (Parent)
    |
    v
  [ C ]  (Child)
```

#### 4. Hierarchical Inheritance
Multiple classes inherit from a single base class.
```text
        [ A ]       (Base)
       /  |  \
      v   v   v
    [ B ][ C ][ D ] (Derived classes)
```

#### 5. Hybrid Inheritance
A combination of two or more types of inheritance (e.g., Hierarchical + Multiple).
```text
        [ A ]
       /     \
      v       v
    [ B ]   [ C ]
      \       /
       v     v
        [ D ]
```

---

### Advantages
- Code reuse
- Reduces duplication
- Easy extension
- Supports hierarchical classification
- Easier maintenance

### Disadvantages
- Creates dependency/coupling between classes
- Deep inheritance hierarchies can become complicated
- Changes in base classes may affect derived classes unexpectedly
- Multiple inheritance can create ambiguity (e.g., Diamond Problem)

---
---

## 14. POLYMORPHISM

### Definition
**Polymorphism** means **"many forms"** (*Poly* = Many, *Morph* = Form).

In OOP, polymorphism allows the same function, interface, or operator to behave differently depending on the context.

For example:
```text
Animal
 |
 ├── Dog → sound() -> "Dog barks"
 └── Cat → sound() -> "Cat meows"
```
Both have `sound()`, but their behavior is different.

---

### Types of Polymorphism

```text
                     POLYMORPHISM
                          |
        -------------------------------------
        |                                   |
Compile-Time (Static)               Run-Time (Dynamic)
        |                                   |
  ├── Function Overloading            ├── Function Overriding
  └── Operator Overloading            └── Virtual Functions
```

---

### 1. Compile-Time Polymorphism (Static Binding)
The decision of which function to call is made during compilation.

**Common techniques:**
- Function overloading
- Operator overloading

**Example (Function Overloading):**
```cpp
class Calculator
{
public:
    int add(int a, int b)
    {
        return a + b;
    }

    double add(double a, double b)
    {
        return a + b;
    }
};
```
*The compiler determines which `add()` function to call based on argument types.*

---

### 2. Run-Time Polymorphism (Dynamic Binding)
The decision of which function to execute is made during program execution at runtime.

It is commonly achieved using:
- Function overriding
- `virtual` functions

**Example:**
```cpp
#include <iostream>
using namespace std;

class Animal
{
public:
    virtual void sound()
    {
        cout << "Animal sound" << endl;
    }
};

class Dog : public Animal
{
public:
    void sound() override
    {
        cout << "Dog barks" << endl;
    }
};
```

---

### Real-World Example
A person may use a single word: **"Pay"**

Payment can happen through multiple forms:
- Cash
- Credit/Debit Card
- UPI
- Net Banking

The operation is conceptually the same, but the underlying implementation differs.

---

### Advantages
- Flexibility
- Code reuse
- Extensibility
- Supports loose coupling
- Makes programs easier to expand

### Disadvantages
- Can make programs more difficult to trace
- Runtime polymorphism can introduce slight overhead (via vtable lookup)
- Requires proper class design
- Debugging can sometimes be more difficult

---
---

## 15. MESSAGE PASSING

### Definition
**Message Passing** is a mechanism through which objects communicate with one another by sending requests or calling methods.

In OOP, an object may request another object to perform a particular operation.

```cpp
student.display();
```
*Here, the object `student` receives a request/message to execute `display()`.*

---

### Real-World Example
Consider a **Restaurant**:
```text
Customer
   |
   | (1. Order food)
   v
 Waiter
   |
   | (2. Request dish)
   v
Kitchen
```
The customer does not directly prepare the food in the kitchen. A request is passed through another entity (the waiter). Similarly, objects communicate by sending messages and requests.

---

### C++ Example
```cpp
#include <iostream>
using namespace std;

class Printer
{
public:
    void print()
    {
        cout << "Printing document" << endl;
    }
};

class Computer
{
public:
    void sendToPrinter(Printer &p)
    {
        p.print(); // Message passed from Computer to Printer
    }
};
```
*The `Computer` object sends a print request to the `Printer` object.*

---

### Advantages
- Supports object communication
- Improves modularity
- Reduces direct dependency
- Supports distributed systems
- Makes responsibilities clear

### Disadvantages
- Too many messages can make a system complex
- Communication overhead may occur
- Incorrect object relationships can cause design problems

---
---

## 16. DYNAMIC BINDING

### Definition
**Dynamic Binding** (also known as Late Binding) is the process in which the method to be executed is determined at runtime rather than at compile time.

It is strongly associated with **runtime polymorphism** and **virtual functions**.

---

### Real-World Example
Suppose you have a **Universal Remote Control**.

You press the **Power** button. The actual action depends on which device the remote is currently paired with:
- `TV` → TV turns on
- `AC` → AC turns on
- `Projector` → Projector turns on

The same operation produces different behavior depending on the actual object present at runtime.

---

### C++ Example
```cpp
#include <iostream>
using namespace std;

class Animal
{
public:
    virtual void sound()
    {
        cout << "Animal sound" << endl;
    }
};

class Dog : public Animal
{
public:
    void sound() override
    {
        cout << "Dog barks" << endl;
    }
};

class Cat : public Animal
{
public:
    void sound() override
    {
        cout << "Cat meows" << endl;
    }
};

int main()
{
    Animal *a;

    Dog d;
    Cat c;

    a = &d;
    a->sound(); // Calls Dog's sound at runtime

    a = &c;
    a->sound(); // Calls Cat's sound at runtime

    return 0;
}
```

**Output:**
```text
Dog barks
Cat meows
```

**Explanation:** The method selected depends on the actual object pointed to at runtime.

---

### Advantages
- Supports runtime polymorphism
- Provides immense flexibility
- Makes systems easily extensible
- Reduces dependency on specific implementations

### Disadvantages
- Can introduce slight runtime overhead
- Debugging can be harder
- Requires proper inheritance and virtual function design

---
---

## 17. I/O PROCESSING

### Definition
**I/O Processing** stands for **Input/Output Processing**.

It refers to the process through which a program receives data from external sources, processes that data, and produces results for external devices or destinations.

### Basic Flow:
```text
[ INPUT ] ──────> [ PROCESSING ] ──────> [ OUTPUT ]
```

- **Input:** Data provided to the program (Keyboard, Mouse, File, Sensor, Network).
- **Output:** Information produced by the program (Monitor, Printer, File, Network).

---

### Real-World Example
Suppose you enter two numbers into a calculator:
- **Input:** `10`, `20`
- **Processing:** `10 + 20`
- **Output:** `30`

---

### C++ I/O System
C++ provides console I/O through the `<iostream>` standard library.

```cpp
#include <iostream>
using namespace std;
```

The two most commonly used stream objects are:
- `cin`  → Standard Input Stream
- `cout` → Standard Output Stream

#### `cin`
`cin` is used to receive input from the standard input device, normally the keyboard.
```cpp
int age;
cin >> age;
```

#### `cout`
`cout` is used to display output to the standard output device (screen).
```cpp
cout << age;
```

---

### Example
```cpp
#include <iostream>
using namespace std;

int main()
{
    int a, b;

    cout << "Enter two numbers: ";
    cin >> a >> b;

    cout << "Sum = " << a + b << endl;

    return 0;
}
```

**Input:**
```text
10 20
```

**Output:**
```text
Enter two numbers: Sum = 30
```

---

### I/O Operators & Functions

#### 1. Extraction Operator (`>>`)
Used with `cin` to extract data from the input stream.
```cpp
cin >> a;
```

#### 2. Insertion Operator (`<<`)
Used with `cout` to insert data into the output stream.
```cpp
cout << a;
```

#### 3. `getline()`
`getline()` is used to read a complete line of text including spaces.
```cpp
string name;
getline(cin, name);
```
If the input is `Ravi Kumar`, the entire string including the space is stored.

---

### Advantages of I/O Processing
- Allows interaction with users
- Allows programs to receive data dynamically
- Allows results to be displayed
- Supports file and device communication
- Essential for interactive applications

### Disadvantages
- Input errors can cause incorrect results
- I/O operations can be slower than CPU/memory operations
- Improper input handling can cause program crashes or buffer errors
- Large amounts of unbuffered I/O can affect performance

---
---

## IMPORTANT: FOUR PILLARS OF OOP

> [!IMPORTANT]
> **The Four Pillars of OOP (Crucial for Exams):**
>
> Remember the acronym: **E - A - I - P**
>
> 1. **E → Encapsulation:** Binding data and methods together into a single unit & protecting internal state.
> 2. **A → Abstraction:** Showing essential features and hiding complex background implementation details.
> 3. **I → Inheritance:** Acquiring properties and behaviors from an existing base class.
> 4. **P → Polymorphism:** One interface / name having multiple forms (Compile-time & Run-time).

---

## MOST IMPORTANT DIFFERENCE SUMMARY

### Procedural Programming Flow
```text
Problem ──> Functions ──> Operations ──> Data
```
**Focus:** *"What steps should be performed?"*

---

### Object-Oriented Programming Flow
```text
Problem ──> Objects ──> Classes ──> Data + Behavior ──> Interaction
```
**Focus:** *"What objects are involved and how do they interact?"*
