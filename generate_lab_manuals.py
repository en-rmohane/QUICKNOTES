# generate_lab_manuals.py
import json
import os

ds_programs = [
    {
        "id": 1,
        "title": "Create an Array of Integer Type and Print Its Elements",
        "aim": "To write a C program to declare, initialize, and traverse a one-dimensional array of integers and display its elements on the console.",
        "software": "GCC Compiler / Turbo C++ / VS Code",
        "theory": "An array is a collection of homogeneous (same type) data elements stored in contiguous memory locations. In C, elements are indexed from 0 to N-1. Traversal involves accessing each element exactly once using loops.",
        "algorithm": [
            "Start",
            "Declare an integer array arr of fixed size (e.g., 50) and integer variables n and i.",
            "Prompt the user to enter the number of elements n.",
            "Read n elements into the array using a for loop: for i = 0 to n-1, read arr[i].",
            "Display the elements using another for loop: for i = 0 to n-1, print arr[i].",
            "Stop"
        ],
        "code": """#include <stdio.h>

int main() {
    int arr[50], n, i;

    printf("=== PROGRAM 1: CREATE AND TRAVERSE 1D ARRAY ===\\n");
    printf("Enter number of elements (max 50): ");
    scanf("%d", &n);

    // Reading elements into array
    printf("Enter %d integer elements:\\n", n);
    for(i = 0; i < n; i++) {
        printf("Element [%d]: ", i);
        scanf("%d", &arr[i]);
    }

    // Displaying array elements
    printf("\\n--- Array Elements Display ---\\n");
    for(i = 0; i < n; i++) {
        printf("arr[%d] = %d (Address: %p)\\n", i, arr[i], (void*)&arr[i]);
    }

    return 0;
}""",
        "output": """=== PROGRAM 1: CREATE AND TRAVERSE 1D ARRAY ===
Enter number of elements (max 50): 5
Enter 5 integer elements:
Element [0]: 12
Element [1]: 45
Element [2]: 78
Element [3]: 23
Element [4]: 56

--- Array Elements Display ---
arr[0] = 12 (Address: 0x7ffd982c1a10)
arr[1] = 45 (Address: 0x7ffd982c1a14)
arr[2] = 78 (Address: 0x7ffd982c1a18)
arr[3] = 23 (Address: 0x7ffd982c1a1c)
arr[4] = 56 (Address: 0x7ffd982c1a20)""",
        "time_complexity": "O(N) for traversal",
        "space_complexity": "O(1) auxiliary space",
        "viva": [
            {"q": "What is an array in C?", "a": "An array is a derived data type consisting of a fixed-size sequential collection of elements of the same data type stored in contiguous memory."},
            {"q": "Why is array indexing zero-based in C?", "a": "Because index represents the memory offset (distance) from the base address. arr[i] = *(arr + i * sizeof(type))."},
            {"q": "What happens if we access an array out of bounds in C?", "a": "C does not perform bounds checking; it leads to undefined behavior or segmentation fault."}
        ]
    },
    {
        "id": 2,
        "title": "Count Even and Odd Numbers in an Integer Array",
        "aim": "To write a C program to count the total number of even and odd integers present in a user-provided array.",
        "software": "GCC Compiler / VS Code",
        "theory": "An integer is even if it is completely divisible by 2 (number % 2 == 0), otherwise it is odd. By iterating through each element and testing with modulus operator %, we increment respective counters.",
        "algorithm": [
            "Start",
            "Initialize evenCount = 0 and oddCount = 0.",
            "Read the size n and n integers into array arr.",
            "For each element arr[i] from 0 to n-1: if arr[i] % 2 == 0 then evenCount++, else oddCount++.",
            "Print evenCount and oddCount.",
            "Stop"
        ],
        "code": """#include <stdio.h>

int main() {
    int arr[100], n, i;
    int evenCount = 0, oddCount = 0;

    printf("=== PROGRAM 2: COUNT EVEN AND ODD NUMBERS ===\\n");
    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d integers:\\n", n);
    for(i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if(arr[i] % 2 == 0) {
            evenCount++;
        } else {
            oddCount++;
        }
    }

    printf("\\n--- Results ---\\n");
    printf("Total Elements : %d\\n", n);
    printf("Even Count     : %d\\n", evenCount);
    printf("Odd Count      : %d\\n", oddCount);

    return 0;
}""",
        "output": """=== PROGRAM 2: COUNT EVEN AND ODD NUMBERS ===
Enter number of elements: 6
Enter 6 integers:
14 27 38 49 50 63

--- Results ---
Total Elements : 6
Even Count     : 3
Odd Count      : 3""",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "How can you check if a number is even without using the modulo % operator?", "a": "Using bitwise AND operator: (n & 1) == 0 means even, else odd."},
            {"q": "Can 0 be classified as even or odd?", "a": "0 is classified as an even integer because 0 % 2 == 0."}
        ]
    },
    {
        "id": 3,
        "title": "Sum and Average of 1D Array Elements",
        "aim": "To write a C program demonstrating one-dimensional array processing to compute the sum and average of all elements.",
        "software": "GCC Compiler / VS Code",
        "theory": "Summation involves accumulating elements into an accumulator variable initialized to 0. The average is computed by dividing sum by total number of elements with typecasting to float.",
        "algorithm": [
            "Start",
            "Initialize sum = 0.",
            "Input size n and read n elements into array arr[].",
            "Loop i from 0 to n-1: sum = sum + arr[i].",
            "Calculate average = (float)sum / n.",
            "Display sum and average.",
            "Stop"
        ],
        "code": """#include <stdio.h>

int main() {
    int arr[100], n, i;
    int sum = 0;
    float average;

    printf("=== PROGRAM 3: SUM & AVERAGE OF ARRAY ELEMENTS ===\\n");
    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d integers:\\n", n);
    for(i = 0; i < n; i++) {
        printf("Element %d: ", i + 1);
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    average = (float)sum / n;

    printf("\\n--- Calculation Summary ---\\n");
    printf("Sum of Elements     = %d\\n", sum);
    printf("Average of Elements = %.2f\\n", average);

    return 0;
}""",
        "output": """=== PROGRAM 3: SUM & AVERAGE OF ARRAY ELEMENTS ===
Enter number of elements: 5
Enter 5 integers:
Element 1: 10
Element 2: 25
Element 3: 35
Element 4: 40
Element 5: 50

--- Calculation Summary ---
Sum of Elements     = 160
Average of Elements = 32.00""",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "Why is (float) typecasting necessary when computing average?", "a": "Because integer division in C truncates decimal parts; casting ensures floating-point precision."}
        ]
    },
    {
        "id": 4,
        "title": "Delete a Number From an Array at a Given Position",
        "aim": "To write a C program to delete an element from an array from a specified position and shift remaining elements.",
        "software": "GCC Compiler / VS Code",
        "theory": "Deleting an element requires locating its index, shifting all succeeding elements one position to the left (arr[i] = arr[i+1]), and decreasing the size count n by 1.",
        "algorithm": [
            "Start",
            "Input array size n and n elements.",
            "Input the position pos (1-based index) to delete.",
            "Check if pos is valid (1 <= pos <= n). If invalid, display error and exit.",
            "Loop i from pos-1 to n-2: arr[i] = arr[i+1].",
            "Decrement n = n - 1.",
            "Print the modified array.",
            "Stop"
        ],
        "code": """#include <stdio.h>

int main() {
    int arr[100], n, i, pos;

    printf("=== PROGRAM 4: DELETE AN ELEMENT FROM ARRAY ===\\n");
    printf("Enter size of array: ");
    scanf("%d", &n);

    printf("Enter %d elements:\\n", n);
    for(i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter position to delete (1 to %d): ", n);
    scanf("%d", &pos);

    if(pos < 1 || pos > n) {
        printf("Invalid position! Deletion failed.\\n");
    } else {
        // Shift elements left
        for(i = pos - 1; i < n - 1; i++) {
            arr[i] = arr[i + 1];
        }
        n--; // Reduce size

        printf("\\nArray after deletion of element at position %d:\\n", pos);
        for(i = 0; i < n; i++) {
            printf("%d ", arr[i]);
        }
        printf("\\n");
    }

    return 0;
}""",
        "output": """=== PROGRAM 4: DELETE AN ELEMENT FROM ARRAY ===
Enter size of array: 5
Enter 5 elements:
10 20 30 40 50
Enter position to delete (1 to 5): 3

Array after deletion of element at position 3:
10 20 40 50 """,
        "time_complexity": "Best Case: O(1) (last element), Worst Case: O(N) (first element)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "What is the time complexity of deleting the first element in an array of size N?", "a": "O(N), because N-1 elements must be shifted one position left."},
            {"q": "How does array deletion differ from linked list deletion?", "a": "In arrays, elements must be shifted in memory. In linked lists, deletion only requires updating pointer links in O(1) time once node is located."}
        ]
    },
    {
        "id": 5,
        "title": "Add Two Matrices A and B (2D Arrays)",
        "aim": "To write a C program to input two 2D matrices A and B of order R x C, perform matrix addition, and display the resultant matrix C.",
        "software": "GCC Compiler / VS Code",
        "theory": "Matrix addition is possible only when both matrices have identical dimensions (same number of rows and columns). Each element C[i][j] is the sum of A[i][j] + B[i][j].",
        "algorithm": [
            "Start",
            "Input row and column dimensions (r, c).",
            "Input elements of Matrix A[r][c] and Matrix B[r][c].",
            "Nested loops for i = 0 to r-1 and j = 0 to c-1: C[i][j] = A[i][j] + B[i][j].",
            "Display resultant matrix C.",
            "Stop"
        ],
        "code": """#include <stdio.h>

int main() {
    int A[10][10], B[10][10], C[10][10];
    int r, c, i, j;

    printf("=== PROGRAM 5: MATRIX ADDITION (A + B) ===\\n");
    printf("Enter number of rows and columns: ");
    scanf("%d %d", &r, &c);

    printf("\\nEnter elements of Matrix A (%d x %d):\\n", r, c);
    for(i = 0; i < r; i++) {
        for(j = 0; j < c; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    printf("\\nEnter elements of Matrix B (%d x %d):\\n", r, c);
    for(i = 0; i < r; i++) {
        for(j = 0; j < c; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    // Computing Sum
    for(i = 0; i < r; i++) {
        for(j = 0; j < c; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }

    printf("\\n--- Resultant Matrix (A + B) ---\\n");
    for(i = 0; i < r; i++) {
        for(j = 0; j < c; j++) {
            printf("%4d ", C[i][j]);
        }
        printf("\\n");
    }

    return 0;
}""",
        "output": """=== PROGRAM 5: MATRIX ADDITION (A + B) ===
Enter number of rows and columns: 2 3

Enter elements of Matrix A (2 x 3):
1 2 3
4 5 6

Enter elements of Matrix B (2 x 3):
7 8 9
1 2 3

--- Resultant Matrix (A + B) ---
   8   10   12 
   5    7    9 """,
        "time_complexity": "O(R * C)",
        "space_complexity": "O(R * C) for resultant matrix",
        "viva": [
            {"q": "What is the condition for matrix addition?", "a": "Both matrices must have the exact same dimensions (same number of rows and columns)."}
        ]
    },
    {
        "id": 6,
        "title": "Generate Fibonacci Series Using Recursive Function",
        "aim": "To write a C program to generate and display the Fibonacci sequence up to N terms using recursion.",
        "software": "GCC Compiler / VS Code",
        "theory": "The Fibonacci sequence is defined by F(0)=0, F(1)=1, and F(n) = F(n-1) + F(n-2) for n >= 2. Recursion solves a problem by having a function call itself with smaller sub-problems until base cases are met.",
        "algorithm": [
            "Start",
            "Define recursive function fibonacci(n):",
            "  If n == 0, return 0.",
            "  If n == 1, return 1.",
            "  Else return fibonacci(n-1) + fibonacci(n-2).",
            "In main(), input number of terms N.",
            "Loop i from 0 to N-1: print fibonacci(i).",
            "Stop"
        ],
        "code": """#include <stdio.h>

// Recursive function to calculate n-th Fibonacci number
int fibonacci(int n) {
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n, i;

    printf("=== PROGRAM 6: FIBONACCI SERIES USING RECURSION ===\\n");
    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printf("\\nFibonacci Series up to %d terms:\\n", n);
    for(i = 0; i < n; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\\n");

    return 0;
}""",
        "output": """=== PROGRAM 6: FIBONACCI SERIES USING RECURSION ===
Enter the number of terms: 8

Fibonacci Series up to 8 terms:
0 1 1 2 3 5 8 13 """,
        "time_complexity": "O(2^N) exponential without memoization",
        "space_complexity": "O(N) call stack space",
        "viva": [
            {"q": "What is a recursive function?", "a": "A function that calls itself directly or indirectly to solve smaller instances of the same problem until a base condition is reached."},
            {"q": "What happens if a recursive function does not have a base condition?", "a": "It causes infinite recursion resulting in Stack Overflow."}
        ]
    },
    {
        "id": 7,
        "title": "Implementation of Linear Queue Using Array",
        "aim": "To write a menu-driven C program to implement a linear Queue data structure using an array supporting Enqueue, Dequeue, Peek, and Display operations.",
        "software": "GCC Compiler / VS Code",
        "theory": "A Queue is a First-In-First-Out (FIFO) linear data structure. Elements are inserted at the REAR end and deleted from the FRONT end. Overflow occurs when rear reaches MAX-1; Underflow occurs when front > rear or front == -1.",
        "algorithm": [
            "Start",
            "Initialize front = -1, rear = -1, MAX = 5.",
            "Enqueue(val): If rear == MAX-1 -> Overflow. Else if front == -1, front=0; rear++; queue[rear]=val.",
            "Dequeue(): If front == -1 or front > rear -> Underflow. Else val = queue[front++]; If front > rear, reset front=rear=-1.",
            "Display(): Loop from front to rear and print elements.",
            "Stop"
        ],
        "code": """#include <stdio.h>
#include <stdlib.h>
#define MAX 5

int queue[MAX];
int front = -1, rear = -1;

void enqueue(int val) {
    if (rear == MAX - 1) {
        printf("[!] Queue Overflow! Cannot insert %d.\\n", val);
    } else {
        if (front == -1) front = 0;
        rear++;
        queue[rear] = val;
        printf("[+] Enqueued: %d\\n", val);
    }
}

void dequeue() {
    if (front == -1 || front > rear) {
        printf("[!] Queue Underflow! Queue is empty.\\n");
    } else {
        printf("[-] Dequeued element: %d\\n", queue[front]);
        front++;
        if (front > rear) { // Reset queue when all elements dequeued
            front = rear = -1;
        }
    }
}

void display() {
    if (front == -1 || front > rear) {
        printf("[*] Queue is EMPTY.\\n");
    } else {
        printf("[*] Current Queue Elements (Front -> Rear): ");
        for (int i = front; i <= rear; i++) {
            printf("%d ", queue[i]);
        }
        printf("\\n");
    }
}

int main() {
    int choice, val;
    printf("=== PROGRAM 7: LINEAR QUEUE USING ARRAY ===\\n");

    while(1) {
        printf("\\n1. Enqueue  2. Dequeue  3. Display  4. Exit\\nEnter Choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &val);
                enqueue(val);
                break;
            case 2:
                dequeue();
                break;
            case 3:
                display();
                break;
            case 4:
                printf("Exiting Queue Program.\\n");
                exit(0);
            default:
                printf("Invalid choice!\\n");
        }
    }
    return 0;
}""",
        "output": """=== PROGRAM 7: LINEAR QUEUE USING ARRAY ===

1. Enqueue  2. Dequeue  3. Display  4. Exit
Enter Choice: 1
Enter value to insert: 10
[+] Enqueued: 10

1. Enqueue  2. Dequeue  3. Display  4. Exit
Enter Choice: 1
Enter value to insert: 20
[+] Enqueued: 20

1. Enqueue  2. Dequeue  3. Display  4. Exit
Enter Choice: 3
[*] Current Queue Elements (Front -> Rear): 10 20 

1. Enqueue  2. Dequeue  3. Display  4. Exit
Enter Choice: 2
[-] Dequeued element: 10

1. Enqueue  2. Dequeue  3. Display  4. Exit
Enter Choice: 4
Exiting Queue Program.""",
        "time_complexity": "Enqueue: O(1), Dequeue: O(1), Display: O(N)",
        "space_complexity": "O(MAX)",
        "viva": [
            {"q": "What is the major drawback of a Linear Queue using array?", "a": "Memory wastage: even if spaces are freed at the front after dequeues, new elements cannot be inserted if rear has reached MAX-1."},
            {"q": "How is this limitation overcome?", "a": "By using a Circular Queue or dynamic Linked List implementation."}
        ]
    },
    {
        "id": 8,
        "title": "Implementation of Stack Using Array",
        "aim": "To write a menu-driven C program to implement a Stack data structure using an array supporting Push, Pop, Peek, and Display operations.",
        "software": "GCC Compiler / VS Code",
        "theory": "A Stack is a Last-In-First-Out (LIFO) linear data structure where insertions and deletions happen exclusively at one end called the TOP. Overflow occurs when top == MAX-1, Underflow occurs when top == -1.",
        "algorithm": [
            "Start",
            "Initialize top = -1, MAX = 5.",
            "Push(val): If top == MAX-1 -> Overflow. Else top = top + 1; stack[top] = val.",
            "Pop(): If top == -1 -> Underflow. Else val = stack[top]; top = top - 1; return val.",
            "Peek(): If top == -1 -> Empty. Else return stack[top].",
            "Display(): Loop from top down to 0 and print stack[i].",
            "Stop"
        ],
        "code": """#include <stdio.h>
#include <stdlib.h>
#define MAX 5

int stack[MAX];
int top = -1;

void push(int val) {
    if (top == MAX - 1) {
        printf("[!] Stack Overflow! Cannot push %d\\n", val);
    } else {
        top++;
        stack[top] = val;
        printf("[+] Pushed %d onto stack\\n", val);
    }
}

void pop() {
    if (top == -1) {
        printf("[!] Stack Underflow! Stack is empty\\n");
    } else {
        printf("[-] Popped element: %d\\n", stack[top]);
        top--;
    }
}

void peek() {
    if (top == -1) {
        printf("[*] Stack is empty!\\n");
    } else {
        printf("[*] Top element is: %d\\n", stack[top]);
    }
}

void display() {
    if (top == -1) {
        printf("[*] Stack is EMPTY.\\n");
    } else {
        printf("\\n--- Stack Contents (Top to Bottom) ---\\n");
        for (int i = top; i >= 0; i--) {
            printf("| %4d |%s\\n", stack[i], (i == top ? " <- TOP" : ""));
        }
        printf(" ------\\n");
    }
}

int main() {
    int choice, val;
    printf("=== PROGRAM 8: STACK IMPLEMENTATION USING ARRAY ===\\n");

    while (1) {
        printf("\\n1. Push  2. Pop  3. Peek  4. Display  5. Exit\\nEnter Choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to push: ");
                scanf("%d", &val);
                push(val);
                break;
            case 2:
                pop();
                break;
            case 3:
                peek();
                break;
            case 4:
                display();
                break;
            case 5:
                printf("Exiting Stack Program.\\n");
                exit(0);
            default:
                printf("Invalid choice! Please select 1-5.\\n");
        }
    }
    return 0;
}""",
        "output": """=== PROGRAM 8: STACK IMPLEMENTATION USING ARRAY ===

1. Push  2. Pop  3. Peek  4. Display  5. Exit
Enter Choice: 1
Enter value to push: 100
[+] Pushed 100 onto stack

1. Push  2. Pop  3. Peek  4. Display  5. Exit
Enter Choice: 1
Enter value to push: 200
[+] Pushed 200 onto stack

1. Push  2. Pop  3. Peek  4. Display  5. Exit
Enter Choice: 4

--- Stack Contents (Top to Bottom) ---
|  200 | <- TOP
|  100 |
 ------

1. Push  2. Pop  3. Peek  4. Display  5. Exit
Enter Choice: 2
[-] Popped element: 200

1. Push  2. Pop  3. Peek  4. Display  5. Exit
Enter Choice: 5
Exiting Stack Program.""",
        "time_complexity": "Push: O(1), Pop: O(1), Peek: O(1), Display: O(N)",
        "space_complexity": "O(MAX)",
        "viva": [
            {"q": "What are the real-world applications of a Stack?", "a": "Function call stack (recursion), expression evaluation/conversion (infix to postfix), undo-redo operations in editors, browser back navigation."},
            {"q": "What is Stack Overflow and Underflow?", "a": "Overflow occurs when pushing to a full stack; Underflow occurs when popping from an empty stack."}
        ]
    },
    {
        "id": 9,
        "title": "Implementation of Binary Search Tree (BST) Using Array",
        "aim": "To write a C program to implement sequential array-based representation of a Binary Search Tree (BST) and perform In-order Traversal.",
        "software": "GCC Compiler / VS Code",
        "theory": "In array representation of a binary tree: for a node at index i (1-based), Left Child is at 2*i and Right Child is at 2*i + 1. In a BST, all left subtree values < node value < all right subtree values. In-order traversal yields elements in ascending order.",
        "algorithm": [
            "Start",
            "Initialize tree array of size 100 with sentinel value -1 (indicating empty node).",
            "Insert(val): Start at root index 1.",
            "  While tree[index] != -1: if val < tree[index] go to left (index = 2*index), else go to right (index = 2*index + 1).",
            "  Place val at tree[index].",
            "Inorder(index): If index <= MAX and tree[index] != -1:",
            "  Inorder(2*index), Print tree[index], Inorder(2*index + 1).",
            "Stop"
        ],
        "code": """#include <stdio.h>
#define MAX 100

int tree[MAX];

void initTree() {
    for (int i = 0; i < MAX; i++) {
        tree[i] = -1; // -1 denotes empty node
    }
}

void insertBST(int val) {
    int index = 1; // 1-based indexing for standard binary tree mapping
    while (index < MAX && tree[index] != -1) {
        if (val < tree[index]) {
            index = 2 * index;     // Left child
        } else if (val > tree[index]) {
            index = 2 * index + 1; // Right child
        } else {
            printf("[!] Duplicate value %d not allowed in BST.\\n", val);
            return;
        }
    }
    if (index < MAX) {
        tree[index] = val;
        printf("[+] Inserted %d at tree index %d\\n", val, index);
    } else {
        printf("[!] Tree array capacity exceeded!\\n");
    }
}

void inorder(int index) {
    if (index < MAX && tree[index] != -1) {
        inorder(2 * index);              // Left subtree
        printf("%d ", tree[index]);      // Root node
        inorder(2 * index + 1);          // Right subtree
    }
}

int main() {
    initTree();
    int n, val;

    printf("=== PROGRAM 9: BINARY SEARCH TREE (ARRAY BASED) ===\\n");
    printf("Enter number of nodes to insert into BST: ");
    scanf("%d", &n);

    printf("Enter %d values:\\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &val);
        insertBST(val);
    }

    printf("\\nIn-order Traversal (Sorted BST elements):\\n");
    inorder(1);
    printf("\\n");

    return 0;
}""",
        "output": """=== PROGRAM 9: BINARY SEARCH TREE (ARRAY BASED) ===
Enter number of nodes to insert into BST: 6
Enter 6 values:
50 30 70 20 40 80
[+] Inserted 50 at tree index 1
[+] Inserted 30 at tree index 2
[+] Inserted 70 at tree index 3
[+] Inserted 20 at tree index 4
[+] Inserted 40 at tree index 5
[+] Inserted 80 at tree index 7

In-order Traversal (Sorted BST elements):
20 30 40 50 70 80 """,
        "time_complexity": "Average Insertion: O(log N), Traversal: O(N)",
        "space_complexity": "O(2^H) where H is tree height",
        "viva": [
            {"q": "What is the mathematical relationship for children in array-based binary tree?", "a": "For a node at index i (1-based): Left Child = 2*i, Right Child = 2*i + 1, Parent = floor(i/2)."},
            {"q": "Why does In-order traversal of a BST produce sorted order?", "a": "Because in-order visits Left Subtree (smaller) -> Root -> Right Subtree (larger)."}
        ]
    },
    {
        "id": 10,
        "title": "Implementation of Circular Queue Using Array",
        "aim": "To write a C program to implement a Circular Queue using an array to eliminate memory wastage of linear queues using modular arithmetic.",
        "software": "GCC Compiler / VS Code",
        "theory": "In a Circular Queue, the last position connects back to the first position forming a circle. Operations use modulo arithmetic: rear = (rear + 1) % MAX. Full condition is (rear + 1) % MAX == front.",
        "algorithm": [
            "Start",
            "Initialize front = -1, rear = -1, MAX = 5.",
            "Enqueue(val):",
            "  If (rear + 1) % MAX == front -> Queue Full.",
            "  If front == -1 -> front = rear = 0; else rear = (rear + 1) % MAX.",
            "  cqueue[rear] = val.",
            "Dequeue():",
            "  If front == -1 -> Queue Empty.",
            "  val = cqueue[front]. If front == rear -> front = rear = -1; else front = (front + 1) % MAX.",
            "Display():",
            "  Loop i from front to rear using (i + 1) % MAX.",
            "Stop"
        ],
        "code": """#include <stdio.h>
#include <stdlib.h>
#define MAX 5

int cqueue[MAX];
int front = -1, rear = -1;

void enqueue(int val) {
    if ((rear + 1) % MAX == front) {
        printf("[!] Circular Queue Overflow! Cannot insert %d\\n", val);
        return;
    }
    if (front == -1) {
        front = rear = 0;
    } else {
        rear = (rear + 1) % MAX;
    }
    cqueue[rear] = val;
    printf("[+] Enqueued: %d at index %d\\n", val, rear);
}

void dequeue() {
    if (front == -1) {
        printf("[!] Circular Queue Underflow! Queue is empty.\\n");
        return;
    }
    printf("[-] Dequeued: %d from index %d\\n", cqueue[front], front);
    if (front == rear) {
        front = rear = -1; // Reset to empty
    } else {
        front = (front + 1) % MAX;
    }
}

void display() {
    if (front == -1) {
        printf("[*] Circular Queue is EMPTY.\\n");
        return;
    }
    printf("[*] Circular Queue Elements: ");
    int i = front;
    while (1) {
        printf("%d (idx:%d) -> ", cqueue[i], i);
        if (i == rear) break;
        i = (i + 1) % MAX;
    }
    printf("WRAP\\n");
}

int main() {
    int choice, val;
    printf("=== PROGRAM 10: CIRCULAR QUEUE USING ARRAY ===\\n");

    while (1) {
        printf("\\n1. Enqueue  2. Dequeue  3. Display  4. Exit\\nEnter Choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &val);
                enqueue(val);
                break;
            case 2:
                dequeue();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
            default:
                printf("Invalid choice!\\n");
        }
    }
    return 0;
}""",
        "output": """=== PROGRAM 10: CIRCULAR QUEUE USING ARRAY ===

1. Enqueue  2. Dequeue  3. Display  4. Exit
Enter Choice: 1
Enter value: 10
[+] Enqueued: 10 at index 0

1. Enqueue  2. Dequeue  3. Display  4. Exit
Enter Choice: 1
Enter value: 20
[+] Enqueued: 20 at index 1

1. Enqueue  2. Dequeue  3. Display  4. Exit
Enter Choice: 3
[*] Circular Queue Elements: 10 (idx:0) -> 20 (idx:1) -> WRAP

1. Enqueue  2. Dequeue  3. Display  4. Exit
Enter Choice: 4""",
        "time_complexity": "Enqueue: O(1), Dequeue: O(1)",
        "space_complexity": "O(MAX)",
        "viva": [
            {"q": "What is the condition for a circular queue to be full?", "a": "(rear + 1) % MAX == front."},
            {"q": "How does circular queue prevent unused memory slots?", "a": "When rear reaches MAX-1, if front has advanced, new elements wrap around to index 0."}
        ]
    },
    {
        "id": 11,
        "title": "Search an Element Using Sequential (Linear) Search",
        "aim": "To write a C program to search for a target key in an array sequentially from beginning to end.",
        "software": "GCC Compiler / VS Code",
        "theory": "Linear search sequentially compares each element of the list with the target key until a match is found or the end of the array is reached. It does not require sorted data.",
        "algorithm": [
            "Start",
            "Read size n and elements of array arr[].",
            "Read target key to search.",
            "Initialize found = 0.",
            "For i = 0 to n-1: if arr[i] == key -> display match at position i+1, set found = 1, break.",
            "If found == 0, display 'Element not found'.",
            "Stop"
        ],
        "code": """#include <stdio.h>

int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            return i; // Found at index i
        }
    }
    return -1; // Not found
}

int main() {
    int arr[100], n, key, pos;

    printf("=== PROGRAM 11: LINEAR / SEQUENTIAL SEARCH ===\\n");
    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d integers:\\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter key element to search: ");
    scanf("%d", &key);

    pos = linearSearch(arr, n, key);

    if (pos != -1) {
        printf("\\n[SUCCESS] Element %d found at Index: %d (Position: %d)\\n", key, pos, pos + 1);
    } else {
        printf("\\n[FAILED] Element %d is NOT present in the array.\\n", key);
    }

    return 0;
}""",
        "output": """=== PROGRAM 11: LINEAR / SEQUENTIAL SEARCH ===
Enter number of elements: 5
Enter 5 integers:
64 34 25 12 22
Enter key element to search: 25

[SUCCESS] Element 25 found at Index: 2 (Position: 3)""",
        "time_complexity": "Best Case: O(1), Worst Case: O(N), Average: O(N)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "What is the main advantage of Linear Search over Binary Search?", "a": "Linear search works on unsorted datasets without requiring pre-sorting."},
            {"q": "What is the worst-case number of comparisons in linear search?", "a": "N comparisons (when element is at the end or absent)."}
        ]
    },
    {
        "id": 12,
        "title": "Search an Element Using Binary Search",
        "aim": "To write a C program to search for an element in a sorted array using the Divide and Conquer Binary Search algorithm.",
        "software": "GCC Compiler / VS Code",
        "theory": "Binary Search operates on sorted arrays by repeatedly dividing the search interval in half. Compare key with middle element: if equal, return; if key < mid, search left half; else search right half.",
        "algorithm": [
            "Start",
            "Read size n and sorted array arr[].",
            "Read target key.",
            "Initialize low = 0, high = n-1.",
            "While low <= high: mid = (low + high)/2.",
            "  If arr[mid] == key -> return mid.",
            "  Else if key < arr[mid] -> high = mid - 1.",
            "  Else -> low = mid + 1.",
            "If low > high -> return -1 (Not found).",
            "Stop"
        ],
        "code": """#include <stdio.h>

int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1, mid;

    while (low <= high) {
        mid = low + (high - low) / 2;

        if (arr[mid] == key)
            return mid;
        else if (key < arr[mid])
            high = mid - 1; // Left half
        else
            low = mid + 1;  // Right half
    }
    return -1;
}

int main() {
    int arr[100], n, key, pos;

    printf("=== PROGRAM 12: BINARY SEARCH (DIVIDE & CONQUER) ===\\n");
    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d sorted elements (Ascending Order):\\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter key element to search: ");
    scanf("%d", &key);

    pos = binarySearch(arr, n, key);

    if (pos != -1) {
        printf("\\n[SUCCESS] Element %d found at Index: %d (Position: %d)\\n", key, pos, pos + 1);
    } else {
        printf("\\n[FAILED] Element %d NOT found in the array.\\n", key);
    }

    return 0;
}""",
        "output": """=== PROGRAM 12: BINARY SEARCH (DIVIDE & CONQUER) ===
Enter number of elements: 6
Enter 6 sorted elements (Ascending Order):
11 22 33 44 55 66
Enter key element to search: 44

[SUCCESS] Element 44 found at Index: 3 (Position: 4)""",
        "time_complexity": "Best Case: O(1), Worst/Average Case: O(log2 N)",
        "space_complexity": "O(1) iterative",
        "viva": [
            {"q": "What is the mandatory prerequisite for Binary Search?", "a": "The array elements MUST be in sorted order."},
            {"q": "Why is mid calculated as low + (high - low)/2 instead of (low + high)/2?", "a": "To avoid potential integer overflow when low and high are very large positive numbers."}
        ]
    },
    {
        "id": 13,
        "title": "Sort Numbers in Ascending Order Using Bubble Sort",
        "aim": "To write a C program to sort an array of N integers in ascending order using the Bubble Sort algorithm with pass-by-pass tracing.",
        "software": "GCC Compiler / VS Code",
        "theory": "Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The largest unsorted element 'bubbles up' to its correct position at the end of each pass.",
        "algorithm": [
            "Start",
            "Read size n and array arr[].",
            "For i = 0 to n-2 (Passes):",
            "  For j = 0 to n-i-2 (Comparisons):",
            "    If arr[j] > arr[j+1] then swap(arr[j], arr[j+1]).",
            "Display sorted array.",
            "Stop"
        ],
        "code": """#include <stdio.h>

void bubbleSort(int arr[], int n) {
    int i, j, temp, swapped;
    for (i = 0; i < n - 1; i++) {
        swapped = 0;
        printf("Pass %d: ", i + 1);
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = 1;
            }
        }
        // Print array state after pass
        for (int k = 0; k < n; k++) printf("%d ", arr[k]);
        printf("\\n");
        if (swapped == 0) break; // Optimization: early exit if already sorted
    }
}

int main() {
    int arr[100], n;

    printf("=== PROGRAM 13: BUBBLE SORT ALGORITHM ===\\n");
    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d integers:\\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("\\n--- Tracing Bubble Sort Passes ---\\n");
    bubbleSort(arr, n);

    printf("\\nFinal Sorted Array (Ascending):\\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\\n");

    return 0;
}""",
        "output": """=== PROGRAM 13: BUBBLE SORT ALGORITHM ===
Enter number of elements: 5
Enter 5 integers:
64 34 25 12 22

--- Tracing Bubble Sort Passes ---
Pass 1: 34 25 12 22 64 
Pass 2: 25 12 22 34 64 
Pass 3: 12 22 25 34 64 
Pass 4: 12 22 25 34 64 

Final Sorted Array (Ascending):
12 22 25 34 64 """,
        "time_complexity": "Best Case: O(N) (optimized), Worst & Average: O(N^2)",
        "space_complexity": "O(1) in-place",
        "viva": [
            {"q": "Is Bubble Sort a stable sorting algorithm?", "a": "Yes, because it never swaps elements with equal keys."},
            {"q": "What is the maximum number of passes in Bubble sort for N elements?", "a": "N - 1 passes."}
        ]
    },
    {
        "id": 14,
        "title": "Sort Numbers in Ascending Order Using Insertion Sort",
        "aim": "To write a C program to sort an array of integers in ascending order using Insertion Sort.",
        "software": "GCC Compiler / VS Code",
        "theory": "Insertion sort builds the final sorted array one item at a time. It iterates through elements, picks the current element (key), and inserts it into its correct position among the already sorted sub-array on the left.",
        "algorithm": [
            "Start",
            "Read size n and array arr[].",
            "For i = 1 to n-1:",
            "  key = arr[i], j = i - 1.",
            "  While j >= 0 and arr[j] > key: arr[j+1] = arr[j], j = j - 1.",
            "  arr[j+1] = key.",
            "Display sorted array.",
            "Stop"
        ],
        "code": """#include <stdio.h>

void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        // Move elements greater than key to one position ahead
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int arr[100], n;

    printf("=== PROGRAM 14: INSERTION SORT ALGORITHM ===\\n");
    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d integers:\\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    insertionSort(arr, n);

    printf("\\nSorted Array in Ascending Order:\\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\\n");

    return 0;
}""",
        "output": """=== PROGRAM 14: INSERTION SORT ALGORITHM ===
Enter number of elements: 5
Enter 5 integers:
12 11 13 5 6

Sorted Array in Ascending Order:
5 6 11 12 13 """,
        "time_complexity": "Best Case: O(N) (when already sorted), Worst/Average: O(N^2)",
        "space_complexity": "O(1) in-place",
        "viva": [
            {"q": "Why is Insertion Sort preferred for small or nearly sorted arrays?", "a": "Because its best case time is linear O(N) with very low overhead and it is an online algorithm."},
            {"q": "How does insertion sort compare to card playing?", "a": "It mimics how a player arranges playing cards in hand one card at a time."}
        ]
    },
    {
        "id": 15,
        "title": "Implementation of Singly Linked List (Creation, Insertion, Deletion, Display)",
        "aim": "To write a menu-driven C program to create a Singly Linked List and perform Insertion, Deletion, and Display operations dynamically.",
        "software": "GCC Compiler / VS Code",
        "theory": "A Singly Linked List is a linear collection of data nodes dynamically allocated in heap memory. Each node contains a `data` field and a `next` pointer pointing to the successor node.",
        "algorithm": [
            "Start",
            "Define struct Node with int data and struct Node* next.",
            "Insert at Beginning: create node, temp->next = head, head = temp.",
            "Insert at End: create node, traverse to last node, last->next = temp.",
            "Delete from Beginning: if head==NULL underflow; else temp=head, head=head->next, free(temp).",
            "Display: traverse ptr from head till NULL printing ptr->data.",
            "Stop"
        ],
        "code": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* head = NULL;

void insertBeginning(int val) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = val;
    newNode->next = head;
    head = newNode;
    printf("[+] Inserted %d at beginning.\\n", val);
}

void insertEnd(int val) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = val;
    newNode->next = NULL;

    if (head == NULL) {
        head = newNode;
    } else {
        struct Node* temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
    printf("[+] Inserted %d at end.\\n", val);
}

void deleteBeginning() {
    if (head == NULL) {
        printf("[!] List is empty! Deletion not possible.\\n");
        return;
    }
    struct Node* temp = head;
    printf("[-] Deleted %d from beginning.\\n", temp->data);
    head = head->next;
    free(temp);
}

void displayList() {
    if (head == NULL) {
        printf("[*] Linked List is EMPTY.\\n");
        return;
    }
    struct Node* temp = head;
    printf("[*] Linked List: ");
    while (temp != NULL) {
        printf("[%d] -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\\n");
}

int main() {
    int choice, val;
    printf("=== PROGRAM 15: SINGLY LINKED LIST OPERATIONS ===\\n");

    while (1) {
        printf("\\n1. Insert at Beginning\\n2. Insert at End\\n3. Delete from Beginning\\n4. Display\\n5. Exit\\nEnter Choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &val);
                insertBeginning(val);
                break;
            case 2:
                printf("Enter value: ");
                scanf("%d", &val);
                insertEnd(val);
                break;
            case 3:
                deleteBeginning();
                break;
            case 4:
                displayList();
                break;
            case 5:
                printf("Exiting Linked List Program.\\n");
                exit(0);
            default:
                printf("Invalid Choice!\\n");
        }
    }
    return 0;
}""",
        "output": """=== PROGRAM 15: SINGLY LINKED LIST OPERATIONS ===

1. Insert at Beginning
2. Insert at End
3. Delete from Beginning
4. Display
5. Exit
Enter Choice: 1
Enter value: 30
[+] Inserted 30 at beginning.

1. Insert at Beginning
2. Insert at End
3. Delete from Beginning
4. Display
5. Exit
Enter Choice: 1
Enter value: 20
[+] Inserted 20 at beginning.

1. Insert at Beginning
2. Insert at End
3. Delete from Beginning
4. Display
5. Exit
Enter Choice: 2
Enter value: 50
[+] Inserted 50 at end.

1. Insert at Beginning
2. Insert at End
3. Delete from Beginning
4. Display
5. Exit
Enter Choice: 4
[*] Linked List: [20] -> [30] -> [50] -> NULL

1. Insert at Beginning
2. Insert at End
3. Delete from Beginning
4. Display
5. Exit
Enter Choice: 5
Exiting Linked List Program.""",
        "time_complexity": "Insert at Head: O(1), Insert at Tail: O(N), Delete Head: O(1)",
        "space_complexity": "O(N) dynamic heap memory",
        "viva": [
            {"q": "What is the advantage of a Linked List over an Array?", "a": "Dynamic sizing without fixed allocation, and efficient O(1) insertions/deletions without shifting elements."},
            {"q": "What is malloc() in C?", "a": "A standard library function in <stdlib.h> that allocates a specified number of bytes in heap memory and returns a void pointer."}
        ]
    }
]

cpp_programs = [
    {
        "id": 1,
        "title": "Class and Object Implementation (Student Record)",
        "aim": "To write a C++ program to create a class named `Student` with data members (Roll Number, Name, Marks in 3 subjects) and member functions to input data, calculate total & percentage, and display student grade card.",
        "software": "G++ / Clang / VS Code / Dev-C++",
        "theory": "Object-Oriented Programming models real-world entities into Classes (blueprints) and Objects (instances). Encapsulation bundles data (attributes) and methods (functions) inside a class while enforcing access specifiers (private, public).",
        "algorithm": [
            "Start",
            "Define class Student with private data members: rollNo, name, marks[3], total, percentage.",
            "Define public member functions: inputData(), calculate(), and displayData().",
            "In main(), instantiate an object of Student class.",
            "Call member functions using dot (.) operator.",
            "Display output formatted on console.",
            "Stop"
        ],
        "code": """#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

class Student {
private:
    int rollNo;
    string name;
    float marks[3];
    float total;
    float percentage;

public:
    void inputData() {
        cout << "Enter Roll Number: ";
        cin >> rollNo;
        cin.ignore();
        cout << "Enter Student Name: ";
        getline(cin, name);
        cout << "Enter Marks in 3 Subjects (out of 100):\\n";
        total = 0;
        for (int i = 0; i < 3; i++) {
            cout << "  Subject " << i + 1 << ": ";
            cin >> marks[i];
            total += marks[i];
        }
        percentage = total / 3.0;
    }

    void displayData() const {
        cout << "\\n========================================\\n";
        cout << "           STUDENT GRADE REPORT          \\n";
        cout << "========================================\\n";
        cout << "Roll Number : " << rollNo << endl;
        cout << "Name        : " << name << endl;
        cout << "----------------------------------------\\n";
        for (int i = 0; i < 3; i++) {
            cout << "Subject " << i + 1 << "   : " << marks[i] << " / 100" << endl;
        }
        cout << "----------------------------------------\\n";
        cout << "Total Marks : " << total << " / 300" << endl;
        cout << fixed << setprecision(2);
        cout << "Percentage  : " << percentage << "%" << endl;
        cout << "Result      : " << (percentage >= 40.0 ? "PASSED" : "FAILED") << endl;
        cout << "========================================\\n";
    }
};

int main() {
    Student s1;
    cout << "=== PROGRAM 1: C++ CLASS & OBJECT DEMONSTRATION ===\\n";
    s1.inputData();
    s1.displayData();
    return 0;
}""",
        "output": """=== PROGRAM 1: C++ CLASS & OBJECT DEMONSTRATION ===
Enter Roll Number: 101
Enter Student Name: Rahul Sharma
Enter Marks in 3 Subjects (out of 100):
  Subject 1: 85
  Subject 2: 90
  Subject 3: 88

========================================
           STUDENT GRADE REPORT          
========================================
Roll Number : 101
Name        : Rahul Sharma
----------------------------------------
Subject 1   : 85 / 100
Subject 2   : 90 / 100
Subject 3   : 88 / 100
----------------------------------------
Total Marks : 263 / 300
Percentage  : 87.67%
Result      : PASSED
======================================== """,
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "What is the difference between a class and an object?", "a": "A class is a user-defined blueprint/type without memory allocation; an object is an instantiated instance of a class that occupies memory."},
            {"q": "What is data encapsulation?", "a": "Wrapping data members and member functions into a single unit (class) while restricting direct outside access via private access specifiers."}
        ]
    },
    {
        "id": 2,
        "title": "Largest of Three Numbers Using Inline Functions",
        "aim": "To write a C++ program to find the largest of three numbers using an `inline` member function.",
        "software": "G++ / Clang / VS Code",
        "theory": "An `inline` function suggests to the compiler to substitute the function body at each call site during compilation, eliminating the overhead of function call stack frames (pushing arguments, jump, return) for small, performance-critical code.",
        "algorithm": [
            "Start",
            "Define inline function findMax(a, b, c) returning the largest integer.",
            "Use nested ternary conditional operators or if-else.",
            "In main(), prompt the user for three numbers.",
            "Call findMax() and display the maximum value.",
            "Stop"
        ],
        "code": """#include <iostream>
using namespace std;

// Inline function definition
inline int findMax(int a, int b, int c) {
    return (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
}

int main() {
    int num1, num2, num3;

    cout << "=== PROGRAM 2: INLINE FUNCTION DEMONSTRATION ===\\n";
    cout << "Enter three integers: ";
    cin >> num1 >> num2 >> num3;

    int maxVal = findMax(num1, num2, num3);

    cout << "\\nAmong [" << num1 << ", " << num2 << ", " << num3 << "]\\n";
    cout << "The Largest Number is: " << maxVal << endl;

    return 0;
}""",
        "output": """=== PROGRAM 2: INLINE FUNCTION DEMONSTRATION ===
Enter three integers: 45 92 67

Among [45, 92, 67]
The Largest Number is: 92 """,
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "What is an inline function?", "a": "A function that is expanded in-line at the point of each call by the compiler, avoiding function call overhead."},
            {"q": "When does compiler ignore the inline request?", "a": "If function contains loops, switch statements, recursive calls, or large code blocks."}
        ]
    },
    {
        "id": 3,
        "title": "Swap Private Data Members of Two Classes Using Friend Function",
        "aim": "To write a C++ program to swap the private data values of two distinct classes using a common `friend` function.",
        "software": "G++ / Clang / VS Code",
        "theory": "A `friend` function is a non-member function granted access to private and protected members of a class. When swapping data between two classes, pass-by-reference allows in-place modifications.",
        "algorithm": [
            "Start",
            "Forward declare ClassB.",
            "Define ClassA with private member valA and declare friend function swapValues().",
            "Define ClassB with private member valB and declare friend function swapValues().",
            "Implement swapValues(ClassA &a, ClassB &b) to swap using a temp variable.",
            "Instantiate objects, display before swap, call swapValues(), and display after swap.",
            "Stop"
        ],
        "code": """#include <iostream>
using namespace std;

class ClassB; // Forward declaration

class ClassA {
private:
    int valA;
public:
    ClassA(int v) : valA(v) {}
    void display() const { cout << "ClassA valA = " << valA << endl; }
    friend void swapValues(ClassA &a, ClassB &b);
};

class ClassB {
private:
    int valB;
public:
    ClassB(int v) : valB(v) {}
    void display() const { cout << "ClassB valB = " << valB << endl; }
    friend void swapValues(ClassA &a, ClassB &b);
};

// Friend function definition
void swapValues(ClassA &a, ClassB &b) {
    int temp = a.valA;
    a.valA = b.valB;
    b.valB = temp;
}

int main() {
    int x, y;
    cout << "=== PROGRAM 3: FRIEND FUNCTION SWAPPING ===\\n";
    cout << "Enter value for Class A: ";
    cin >> x;
    cout << "Enter value for Class B: ";
    cin >> y;

    ClassA objA(x);
    ClassB objB(y);

    cout << "\\n--- Before Swapping ---\\n";
    objA.display();
    objB.display();

    swapValues(objA, objB);

    cout << "\\n--- After Swapping (via Friend Function) ---\\n";
    objA.display();
    objB.display();

    return 0;
}""",
        "output": """=== PROGRAM 3: FRIEND FUNCTION SWAPPING ===
Enter value for Class A: 100
Enter value for Class B: 500

--- Before Swapping ---
ClassA valA = 100
ClassB valB = 500

--- After Swapping (via Friend Function) ---
ClassA valA = 500
ClassB valB = 100 """,
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "What is a Friend Function in C++?", "a": "A non-member function defined outside class scope that has full access to private and protected members of the class."},
            {"q": "Is friendship mutual or inherited in C++?", "a": "No, friendship is neither symmetric/mutual nor inherited."}
        ]
    },
    {
        "id": 4,
        "title": "Function Overloading (Area of Geometric Shapes)",
        "aim": "To write a C++ program to calculate the area of a Circle, Rectangle, and Triangle using Function Overloading (Compile-Time Polymorphism).",
        "software": "G++ / Clang / VS Code",
        "theory": "Function Overloading allows multiple functions in the same scope to share the same name with different parameter signatures (number, order, or data types of parameters). The compiler binds the call based on arguments passed at compile time.",
        "algorithm": [
            "Start",
            "Define overloaded area() functions:",
            "  1. double area(double radius) -> PI * r * r (Circle)",
            "  2. double area(double length, double breadth) -> l * b (Rectangle)",
            "  3. double area(double base, double height, int isTriangle) -> 0.5 * b * h (Triangle)",
            "Prompt user with menu choices.",
            "Invoke corresponding overloaded function and print area.",
            "Stop"
        ],
        "code": """#include <iostream>
#include <cmath>
using namespace std;

const double PI = 3.141592653589793;

// Overload 1: Circle
double area(double radius) {
    return PI * radius * radius;
}

// Overload 2: Rectangle
double area(double length, double breadth) {
    return length * breadth;
}

// Overload 3: Triangle
double area(double base, double height, bool isTriangle) {
    if (isTriangle) return 0.5 * base * height;
    return 0;
}

int main() {
    int choice;
    cout << "=== PROGRAM 4: FUNCTION OVERLOADING (AREA CALCULATOR) ===\\n";
    cout << "1. Area of Circle\\n2. Area of Rectangle\\n3. Area of Triangle\\nEnter choice (1-3): ";
    cin >> choice;

    switch (choice) {
        case 1: {
            double r;
            cout << "Enter radius of Circle: ";
            cin >> r;
            cout << "=> Area of Circle = " << area(r) << " sq units\\n";
            break;
        }
        case 2: {
            double l, b;
            cout << "Enter length and breadth of Rectangle: ";
            cin >> l >> b;
            cout << "=> Area of Rectangle = " << area(l, b) << " sq units\\n";
            break;
        }
        case 3: {
            double base, height;
            cout << "Enter base and height of Triangle: ";
            cin >> base >> height;
            cout << "=> Area of Triangle = " << area(base, height, true) << " sq units\\n";
            break;
        }
        default:
            cout << "Invalid choice!\\n";
    }

    return 0;
}""",
        "output": """=== PROGRAM 4: FUNCTION OVERLOADING (AREA CALCULATOR) ===
1. Area of Circle
2. Area of Rectangle
3. Area of Triangle
Enter choice (1-3): 2
Enter length and breadth of Rectangle: 12.5 8.0
=> Area of Rectangle = 100 sq units""",
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "What is Compile-Time Polymorphism?", "a": "Polymorphism resolved during compilation via Function Overloading and Operator Overloading (also called static/early binding)."},
            {"q": "Can function overloading be achieved by changing only the return type?", "a": "No, return type alone is not sufficient to distinguish overloaded functions."}
        ]
    },
    {
        "id": 5,
        "title": "Constructors (Default, Parameterized, Copy) & Destructor",
        "aim": "To write a C++ program demonstrating Default Constructor, Parameterized Constructor, Copy Constructor, and Destructor lifecycle of objects.",
        "software": "G++ / Clang / VS Code",
        "theory": "A Constructor is a special member function having the same name as the class invoked automatically upon object creation to initialize state. A Destructor (~ClassName) is invoked automatically when an object goes out of scope to reclaim resources.",
        "algorithm": [
            "Start",
            "Define class Account with account number and balance.",
            "Implement Default Constructor (initialize to default 0).",
            "Implement Parameterized Constructor (initialize with arguments).",
            "Implement Copy Constructor (deep copy another object's state).",
            "Implement Destructor to print deallocation message.",
            "Create objects in main() and observe invocation orders.",
            "Stop"
        ],
        "code": """#include <iostream>
#include <string>
using namespace std;

class Account {
private:
    int accNo;
    string holderName;
    double balance;

public:
    // 1. Default Constructor
    Account() {
        accNo = 0;
        holderName = "Unknown";
        balance = 0.0;
        cout << "[*] Default Constructor Called (Acc: " << accNo << ")\\n";
    }

    // 2. Parameterized Constructor
    Account(int no, string name, double bal) {
        accNo = no;
        holderName = name;
        balance = bal;
        cout << "[*] Parameterized Constructor Called for " << holderName << " (Acc: " << accNo << ")\\n";
    }

    // 3. Copy Constructor
    Account(const Account &other) {
        accNo = other.accNo + 1; // new cloned account
        holderName = other.holderName + " (Joint)";
        balance = other.balance;
        cout << "[*] Copy Constructor Called (Copied from Acc " << other.accNo << " to Acc " << accNo << ")\\n";
    }

    // Member display function
    void display() const {
        cout << "   [Account " << accNo << "] " << holderName << " | Balance: $" << balance << endl;
    }

    // Destructor
    ~Account() {
        cout << "[~] Destructor Called: Reclaiming Account " << accNo << " (" << holderName << ")\\n";
    }
};

int main() {
    cout << "=== PROGRAM 5: CONSTRUCTORS & DESTRUCTOR LIFECYCLE ===\\n\\n";
    {
        cout << "--- 1. Creating default object ---\\n";
        Account acc1;
        acc1.display();

        cout << "\\n--- 2. Creating parameterized object ---\\n";
        Account acc2(1001, "Amit Verma", 75000.50);
        acc2.display();

        cout << "\\n--- 3. Creating object using Copy Constructor ---\\n";
        Account acc3 = acc2; // Copy constructor invocation
        acc3.display();

        cout << "\\n--- Leaving Inner Scope (Destructors will trigger in reverse order) ---\\n";
    }
    cout << "\\nAll accounts destroyed successfully.\\n";
    return 0;
}""",
        "output": """=== PROGRAM 5: CONSTRUCTORS & DESTRUCTOR LIFECYCLE ===

--- 1. Creating default object ---
[*] Default Constructor Called (Acc: 0)
   [Account 0] Unknown | Balance: $0

--- 2. Creating parameterized object ---
[*] Parameterized Constructor Called for Amit Verma (Acc: 1001)
   [Account 1001] Amit Verma | Balance: $75000.5

--- 3. Creating object using Copy Constructor ---
[*] Copy Constructor Called (Copied from Acc 1001 to Acc 1002)
   [Account 1002] Amit Verma (Joint) | Balance: $75000.5

--- Leaving Inner Scope (Destructors will trigger in reverse order) ---
[~] Destructor Called: Reclaiming Account 1002 (Amit Verma (Joint))
[~] Destructor Called: Reclaiming Account 1001 (Amit Verma)
[~] Destructor Called: Reclaiming Account 0 (Unknown)

All accounts destroyed successfully.""",
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "Why is the parameter to a copy constructor passed by reference (const ClassName &obj)?", "a": "If passed by value, passing the argument would itself call the copy constructor, causing infinite recursive calls and stack overflow."},
            {"q": "Can a destructor be overloaded in C++?", "a": "No, a class has exactly one destructor with no parameters and no return type."}
        ]
    },
    {
        "id": 6,
        "title": "Constructor Overloading and Dynamic Memory Allocation",
        "aim": "To write a C++ program demonstrating Constructor Overloading and Dynamic Array allocation using `new` and `delete` operators.",
        "software": "G++ / Clang / VS Code",
        "theory": "Constructor Overloading occurs when a class has multiple constructors with different argument lists. Dynamic memory allocation allocates heap memory at runtime using `new[]` and releases it using `delete[]` in destructor preventing memory leaks.",
        "algorithm": [
            "Start",
            "Define class DynamicVector with pointer int *arr and size n.",
            "Constructor 1 (DynamicVector()): allocates default size 3.",
            "Constructor 2 (DynamicVector(int size)): dynamically allocates array of custom size.",
            "Constructor 3 (DynamicVector(int size, int initVal)): allocates and fills with initVal.",
            "Destructor ~DynamicVector(): executes delete[] arr.",
            "In main(), test all constructors and display contents.",
            "Stop"
        ],
        "code": """#include <iostream>
using namespace std;

class DynamicVector {
private:
    int* arr;
    int size;

public:
    // Overloaded Constructor 1: Default
    DynamicVector() {
        size = 3;
        arr = new int[size]{10, 20, 30};
        cout << "[*] Default Constructor: Allocated array of size " << size << endl;
    }

    // Overloaded Constructor 2: Parameterized (Size only)
    DynamicVector(int s) {
        size = s;
        arr = new int[size];
        for (int i = 0; i < size; i++) arr[i] = (i + 1) * 100;
        cout << "[*] Parameterized Constructor: Allocated custom size " << size << endl;
    }

    // Overloaded Constructor 3: Parameterized (Size and default fill value)
    DynamicVector(int s, int fillVal) {
        size = s;
        arr = new int[size];
        for (int i = 0; i < size; i++) arr[i] = fillVal;
        cout << "[*] Parameterized Constructor: Allocated size " << size << " filled with " << fillVal << endl;
    }

    void display() const {
        cout << "Vector Elements: [ ";
        for (int i = 0; i < size; i++) {
            cout << arr[i] << " ";
        }
        cout << "]\\n";
    }

    // Destructor to free heap memory
    ~DynamicVector() {
        delete[] arr;
        cout << "[~] Destructor: Dynamically allocated memory freed.\\n";
    }
};

int main() {
    cout << "=== PROGRAM 6: CONSTRUCTOR OVERLOADING & DYNAMIC MEMORY ===\\n\\n";
    
    cout << "1. Object V1 (Default):\\n";
    DynamicVector v1;
    v1.display();

    cout << "\\n2. Object V2 (Custom size 4):\\n";
    DynamicVector v2(4);
    v2.display();

    cout << "\\n3. Object V3 (Custom size 5 filled with 77):\\n";
    DynamicVector v3(5, 77);
    v3.display();

    cout << "\\n--- Scope Exit ---\\n";
    return 0;
}""",
        "output": """=== PROGRAM 6: CONSTRUCTOR OVERLOADING & DYNAMIC MEMORY ===

1. Object V1 (Default):
[*] Default Constructor: Allocated array of size 3
Vector Elements: [ 10 20 30 ]

2. Object V2 (Custom size 4):
[*] Parameterized Constructor: Allocated custom size 4
Vector Elements: [ 100 200 300 400 ]

3. Object V3 (Custom size 5 filled with 77):
[*] Parameterized Constructor: Allocated size 5 filled with 77
Vector Elements: [ 77 77 77 77 77 ]

--- Scope Exit ---
[~] Destructor: Dynamically allocated memory freed.
[~] Destructor: Dynamically allocated memory freed.
[~] Destructor: Dynamically allocated memory freed.""",
        "time_complexity": "O(N) for initialization",
        "space_complexity": "O(N) heap allocation",
        "viva": [
            {"q": "What is the difference between malloc() and new in C++?", "a": "malloc() allocates raw uninitialized memory bytes and doesn't call constructors; new allocates memory with proper type and automatically calls object constructor."},
            {"q": "What is a memory leak?", "a": "Failing to release dynamically allocated heap memory before pointers are lost or program terminates."}
        ]
    },
    {
        "id": 7,
        "title": "Unary Operator Overloading (Overload - and ++ Operators)",
        "aim": "To write a C++ program to overload Unary Minus (`-`) and Prefix/Postfix Increment (`++`) operators.",
        "software": "G++ / Clang / VS Code",
        "theory": "Operator Overloading allows C++ operators to be given special user-defined meanings when applied to user-defined class objects. Unary operators operate on a single operand (the calling object `*this`).",
        "algorithm": [
            "Start",
            "Define class Point with x and y coordinates.",
            "Overload Unary Minus: Point operator-() const -> returns Point(-x, -y).",
            "Overload Prefix ++: Point& operator++() -> increments ++x, ++y, returns *this.",
            "Overload Postfix ++: Point operator++(int) -> saves old state, increments, returns old state.",
            "In main(), create Point and apply unary operators.",
            "Stop"
        ],
        "code": """#include <iostream>
using namespace std;

class Point {
private:
    int x, y;

public:
    Point(int x = 0, int y = 0) : x(x), y(y) {}

    void display() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }

    // 1. Overloading Unary Minus (-)
    Point operator-() const {
        return Point(-x, -y);
    }

    // 2. Overloading Prefix Increment (++p)
    Point& operator++() {
        ++x;
        ++y;
        return *this;
    }

    // 3. Overloading Postfix Increment (p++)
    Point operator++(int) {
        Point temp = *this; // save old state
        x++;
        y++;
        return temp;        // return old state
    }
};

int main() {
    Point p1(15, -25);

    cout << "=== PROGRAM 7: UNARY OPERATOR OVERLOADING ===\\n";
    cout << "Original Point P1: ";
    p1.display();

    // Applying Unary Minus
    Point pNeg = -p1;
    cout << "Negated Point (-P1): ";
    pNeg.display();

    // Applying Prefix ++
    cout << "\\nApplying Prefix ++ (++P1): ";
    (++p1).display();

    // Applying Postfix ++
    cout << "Applying Postfix ++ (P1++): ";
    (p1++).display();
    cout << "Point P1 after Postfix Increment: ";
    p1.display();

    return 0;
}""",
        "output": """=== PROGRAM 7: UNARY OPERATOR OVERLOADING ===
Original Point P1: (15, -25)
Negated Point (-P1): (-15, 25)

Applying Prefix ++ (++P1): (16, -24)
Applying Postfix ++ (P1++): (16, -24)
Point P1 after Postfix Increment: (17, -23)""",
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "How does compiler differentiate between prefix and postfix operator++ in overloading?", "a": "Postfix takes a dummy `int` argument in its signature: operator++(int)."},
            {"q": "Which operators cannot be overloaded in C++?", "a": "Scope resolution (::), Member selection (.), Member selection via pointer (.*), Ternary (?:), and sizeof."}
        ]
    },
    {
        "id": 8,
        "title": "Binary Operator Overloading (Complex Number Addition)",
        "aim": "To write a C++ program to overload the Binary Plus (`+`) operator to add two Complex numbers.",
        "software": "G++ / Clang / VS Code",
        "theory": "Binary operators take two operands. When overloaded as a member function, the left operand is the invoking object (`*this`) and the right operand is passed as a constant reference argument `const Complex &other`.",
        "algorithm": [
            "Start",
            "Define class Complex with real and imag parts.",
            "Overload binary operator+: Complex operator+(const Complex &c) const:",
            "  result.real = real + c.real",
            "  result.imag = imag + c.imag",
            "  return result.",
            "In main(), read two complex numbers C1 and C2.",
            "Execute C3 = C1 + C2 and display C3.",
            "Stop"
        ],
        "code": """#include <iostream>
using namespace std;

class Complex {
private:
    float real;
    float imag;

public:
    Complex(float r = 0.0, float i = 0.0) : real(r), imag(i) {}

    void input() {
        cout << "Enter Real and Imaginary parts: ";
        cin >> real >> imag;
    }

    void display() const {
        if (imag >= 0)
            cout << real << " + " << imag << "i" << endl;
        else
            cout << real << " - " << -imag << "i" << endl;
    }

    // Overloading Binary + Operator
    Complex operator+(const Complex &c) const {
        Complex temp;
        temp.real = this->real + c.real;
        temp.imag = this->imag + c.imag;
        return temp;
    }
};

int main() {
    Complex c1, c2, c3;

    cout << "=== PROGRAM 8: BINARY OPERATOR OVERLOADING (+) ===\\n";
    cout << "Enter Complex Number 1:\\n";
    c1.input();

    cout << "\\nEnter Complex Number 2:\\n";
    c2.input();

    // Adding using overloaded + operator
    c3 = c1 + c2; // Equivalent to c1.operator+(c2)

    cout << "\\n--- Results ---\\n";
    cout << "C1 = "; c1.display();
    cout << "C2 = "; c2.display();
    cout << "C3 (C1 + C2) = "; c3.display();

    return 0;
}""",
        "output": """=== PROGRAM 8: BINARY OPERATOR OVERLOADING (+) ===
Enter Complex Number 1:
Enter Real and Imaginary parts: 4.5 3.2

Enter Complex Number 2:
Enter Real and Imaginary parts: 2.5 -1.2

--- Results ---
C1 = 4.5 + 3.2i
C2 = 2.5 - 1.2i
C3 (C1 + C2) = 7 + 2i""",
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "Can binary operators be overloaded using friend functions?", "a": "Yes, a friend function takes both operands explicitly: friend Complex operator+(const Complex &c1, const Complex &c2)."}
        ]
    },
    {
        "id": 9,
        "title": "Single and Multilevel Inheritance",
        "aim": "To write a C++ program demonstrating Multilevel Inheritance where class `Result` is derived from `Marks`, which is derived from `Student`.",
        "software": "G++ / Clang / VS Code",
        "theory": "Inheritance promotes code reuse. In Single Inheritance, a derived class inherits from one base class. In Multilevel Inheritance, a class is derived from another derived class forming an inheritance chain (A -> B -> C).",
        "algorithm": [
            "Start",
            "Define Base Class Student (rollNo, name).",
            "Define Intermediate Class Marks inheriting Student (marks1, marks2).",
            "Define Derived Class Result inheriting Marks (computes total = marks1 + marks2 and displays result).",
            "In main(), create Result object, invoke input methods and display final card.",
            "Stop"
        ],
        "code": """#include <iostream>
#include <string>
using namespace std;

// Base Class
class Student {
protected:
    int rollNo;
    string name;

public:
    void getStudentDetails() {
        cout << "Enter Roll Number: ";
        cin >> rollNo;
        cin.ignore();
        cout << "Enter Student Name: ";
        getline(cin, name);
    }
    void putStudentDetails() const {
        cout << "Roll Number : " << rollNo << endl;
        cout << "Name        : " << name << endl;
    }
};

// Intermediate Derived Class (Single Inheritance from Student)
class Marks : public Student {
protected:
    float m1, m2;

public:
    void getMarks() {
        getStudentDetails();
        cout << "Enter Marks in Subject 1: ";
        cin >> m1;
        cout << "Enter Marks in Subject 2: ";
        cin >> m2;
    }
    void putMarks() const {
        putStudentDetails();
        cout << "Subject 1 Marks : " << m1 << endl;
        cout << "Subject 2 Marks : " << m2 << endl;
    }
};

// Final Derived Class (Multilevel Inheritance from Marks)
class Result : public Marks {
private:
    float totalScore;

public:
    void calculateResult() {
        getMarks();
        totalScore = m1 + m2;
    }
    void displayResultCard() const {
        cout << "\\n========================================\\n";
        cout << "       MULTILEVEL INHERITANCE REPORT     \\n";
        cout << "========================================\\n";
        putMarks();
        cout << "----------------------------------------\\n";
        cout << "Total Marks Score: " << totalScore << " / 200\\n";
        cout << "Status           : " << (totalScore >= 80 ? "PASSED" : "FAILED") << endl;
        cout << "========================================\\n";
    }
};

int main() {
    Result res;
    cout << "=== PROGRAM 9: MULTILEVEL INHERITANCE (STUDENT -> MARKS -> RESULT) ===\\n";
    res.calculateResult();
    res.displayResultCard();
    return 0;
}""",
        "output": """=== PROGRAM 9: MULTILEVEL INHERITANCE (STUDENT -> MARKS -> RESULT) ===
Enter Roll Number: 202
Enter Student Name: Anjali Gupta
Enter Marks in Subject 1: 88
Enter Marks in Subject 2: 94

========================================
       MULTILEVEL INHERITANCE REPORT     
========================================
Roll Number : 202
Name        : Anjali Gupta
Subject 1 Marks : 88
Subject 2 Marks : 94
----------------------------------------
Total Marks Score: 182 / 200
Status           : PASSED
======================================== """,
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "What is the protected access specifier in C++?", "a": "Protected members are inaccessible from outside classes, but accessible within the class and its derived child classes."},
            {"q": "In what order are constructors executed in multilevel inheritance?", "a": "Base class constructor executes first, followed by intermediate, and finally derived class constructor."}
        ]
    },
    {
        "id": 10,
        "title": "Multiple and Hierarchical Inheritance",
        "aim": "To write a C++ program demonstrating Multiple Inheritance (derived class inheriting from two base classes: `AcademicMarks` and `SportsScore`).",
        "software": "G++ / Clang / VS Code",
        "theory": "Multiple Inheritance occurs when a child class inherits simultaneously from more than one base class (e.g., class Hybrid : public BaseA, public BaseB).",
        "algorithm": [
            "Start",
            "Define Base Class 1: Academic (theory marks).",
            "Define Base Class 2: Sports (sports score/grace points).",
            "Define Derived Class: FinalScore inheriting both Academic and Sports.",
            "Calculate combined score = academic + sports.",
            "Display comprehensive score sheet in main().",
            "Stop"
        ],
        "code": """#include <iostream>
using namespace std;

// Base Class 1
class Academic {
protected:
    float academicScore;
public:
    void getAcademic(float score) {
        academicScore = score;
    }
    void showAcademic() const {
        cout << "Academic Score : " << academicScore << " / 100" << endl;
    }
};

// Base Class 2
class Sports {
protected:
    float sportsScore;
public:
    void getSports(float score) {
        sportsScore = score;
    }
    void showSports() const {
        cout << "Sports Score   : " << sportsScore << " / 20" << endl;
    }
};

// Derived Class demonstrating Multiple Inheritance
class OverallPerformance : public Academic, public Sports {
private:
    float totalAggregate;

public:
    void calculateAggregate(float acad, float sport) {
        getAcademic(acad);
        getSports(sport);
        totalAggregate = academicScore + sportsScore;
    }

    void displayReport() const {
        cout << "\\n========================================\\n";
        cout << "     MULTIPLE INHERITANCE PERFORMANCE   \\n";
        cout << "========================================\\n";
        showAcademic();
        showSports();
        cout << "----------------------------------------\\n";
        cout << "Total Aggregate: " << totalAggregate << " / 120\\n";
        cout << "========================================\\n";
    }
};

int main() {
    OverallPerformance studentPerf;
    float acad, sport;

    cout << "=== PROGRAM 10: MULTIPLE INHERITANCE DEMONSTRATION ===\\n";
    cout << "Enter Academic Score (0-100): ";
    cin >> acad;
    cout << "Enter Sports Grace Score (0-20): ";
    cin >> sport;

    studentPerf.calculateAggregate(acad, sport);
    studentPerf.displayReport();

    return 0;
}""",
        "output": """=== PROGRAM 10: MULTIPLE INHERITANCE DEMONSTRATION ===
Enter Academic Score (0-100): 89.5
Enter Sports Grace Score (0-20): 18.0

========================================
     MULTIPLE INHERITANCE PERFORMANCE   
========================================
Academic Score : 89.5 / 100
Sports Score   : 18 / 20
----------------------------------------
Total Aggregate: 107.5 / 120
======================================== """,
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "What is Multiple Inheritance?", "a": "A mechanism in C++ where a class can inherit from more than one parent base class."},
            {"q": "What is the Diamond problem that can occur in multiple inheritance?", "a": "When a derived class inherits two classes that both inherit from a single grandparent base class, creating duplicate copies of the grandparent's members."}
        ]
    },
    {
        "id": 11,
        "title": "Virtual Base Class (Resolving Diamond Problem Ambiguity)",
        "aim": "To write a C++ program to demonstrate Virtual Base Class in multipath inheritance to prevent duplicate inheritance of base class members.",
        "software": "G++ / Clang / VS Code",
        "theory": "In Multipath Inheritance (Diamond shape A -> B, A -> C, and B, C -> D), derived class D receives two copies of base class A. Declaring base class as `virtual` (e.g., `class B : virtual public A`) ensures only a single shared copy of A is inherited.",
        "algorithm": [
            "Start",
            "Define Base Class Person with id and name.",
            "Define Faculty inheriting `virtual public Person`.",
            "Define Student inheriting `virtual public Person`.",
            "Define TeachingAssistant inheriting both Faculty and Student.",
            "In main(), instantiate TeachingAssistant and verify unambiguous access.",
            "Stop"
        ],
        "code": """#include <iostream>
#include <string>
using namespace std;

// Grandparent Base Class
class Person {
public:
    int personId;
    void setPerson(int id) {
        personId = id;
    }
    void showPerson() const {
        cout << "Person ID: " << personId << endl;
    }
};

// Intermediate Class 1: Virtual inheritance
class Faculty : virtual public Person {
public:
    string department;
    void setFaculty(string dept) { department = dept; }
};

// Intermediate Class 2: Virtual inheritance
class StudentRole : virtual public Person {
public:
    float cgpa;
    void setStudent(float c) { cgpa = c; }
};

// Derived Class inheriting both (Diamond structure resolved)
class TeachingAssistant : public Faculty, public StudentRole {
public:
    void setTA(int id, string dept, float c) {
        setPerson(id); // Unambiguous because of virtual inheritance!
        setFaculty(dept);
        setStudent(c);
    }

    void displayTA() const {
        cout << "\\n========================================\\n";
        cout << "      TEACHING ASSISTANT DETAILS (VBC)   \\n";
        cout << "========================================\\n";
        showPerson();
        cout << "Department : " << department << endl;
        cout << "CGPA       : " << cgpa << endl;
        cout << "========================================\\n";
    }
};

int main() {
    TeachingAssistant ta;
    cout << "=== PROGRAM 11: VIRTUAL BASE CLASS (DIAMOND PROBLEM) ===\\n";
    ta.setTA(501, "Computer Science & Engineering", 9.4);
    ta.displayTA();
    return 0;
}""",
        "output": """=== PROGRAM 11: VIRTUAL BASE CLASS (DIAMOND PROBLEM) ===

========================================
      TEACHING ASSISTANT DETAILS (VBC)   
========================================
Person ID: 501
Department : Computer Science & Engineering
CGPA       : 9.4
======================================== """,
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "What is the purpose of a Virtual Base Class?", "a": "To eliminate duplicate copies and ambiguity when a class inherits from two classes that have a common base class."},
            {"q": "How does compiler implement virtual base class internally?", "a": "Using Virtual Table (vtable) and Virtual Base Pointer (vbptr) offsets."}
        ]
    },
    {
        "id": 12,
        "title": "Runtime Polymorphism Using Virtual Functions & Pure Virtual Class",
        "aim": "To write a C++ program to demonstrate Runtime Polymorphism using Pure Virtual Functions and Abstract Base Class (`Shape` -> `Circle`, `Rectangle`).",
        "software": "G++ / Clang / VS Code",
        "theory": "Runtime (Dynamic) Polymorphism is achieved via Virtual Functions. A base class pointer pointing to derived class objects invokes the overridden derived method at runtime through dynamic dispatch (VTABLE mechanism).",
        "algorithm": [
            "Start",
            "Define abstract base class Shape with pure virtual function: virtual void calculateArea() = 0.",
            "Define derived class Circle overriding calculateArea().",
            "Define derived class Rectangle overriding calculateArea().",
            "Create base class pointer Shape *ptr and dynamically assign derived objects.",
            "Invoke calculateArea() polymorphically.",
            "Stop"
        ],
        "code": """#include <iostream>
using namespace std;

// Abstract Base Class
class Shape {
public:
    // Pure Virtual Function
    virtual void calculateArea() = 0;
    virtual void displayInfo() const = 0;

    // Virtual Destructor for safe polymorphic destruction
    virtual ~Shape() {
        cout << "[~] Shape Base Destructor\\n";
    }
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) : radius(r) {}
    void calculateArea() override {
        cout << "Circle Area: " << (3.14159 * radius * radius) << " sq units\\n";
    }
    void displayInfo() const override {
        cout << "[Circle] Radius = " << radius << endl;
    }
    ~Circle() { cout << "[~] Circle Destructor\\n"; }
};

class Rectangle : public Shape {
private:
    double length, width;
public:
    Rectangle(double l, double w) : length(l), width(w) {}
    void calculateArea() override {
        cout << "Rectangle Area: " << (length * width) << " sq units\\n";
    }
    void displayInfo() const override {
        cout << "[Rectangle] Length = " << length << ", Width = " << width << endl;
    }
    ~Rectangle() { cout << "[~] Rectangle Destructor\\n"; }
};

int main() {
    cout << "=== PROGRAM 12: RUNTIME POLYMORPHISM (VIRTUAL FUNCTIONS) ===\\n\\n";

    // Polymorphic Base Class Pointer
    Shape* shapePtr = nullptr;

    cout << "--- 1. Dynamic Dispatch with Circle ---\\n";
    shapePtr = new Circle(7.0);
    shapePtr->displayInfo();
    shapePtr->calculateArea();
    delete shapePtr;

    cout << "\\n--- 2. Dynamic Dispatch with Rectangle ---\\n";
    shapePtr = new Rectangle(10.0, 5.0);
    shapePtr->displayInfo();
    shapePtr->calculateArea();
    delete shapePtr;

    return 0;
}""",
        "output": """=== PROGRAM 12: RUNTIME POLYMORPHISM (VIRTUAL FUNCTIONS) ===

--- 1. Dynamic Dispatch with Circle ---
[Circle] Radius = 7
Circle Area: 153.938 sq units
[~] Circle Destructor
[~] Shape Base Destructor

--- 2. Dynamic Dispatch with Rectangle ---
[Rectangle] Length = 10, Width = 5
Rectangle Area: 50 sq units
[~] Rectangle Destructor
[~] Shape Base Destructor""",
        "time_complexity": "O(1) with one vtable pointer indirection",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "What is a Pure Virtual Function?", "a": "A virtual function declared with `= 0` in base class having no definition in base class, forcing derived classes to provide an implementation."},
            {"q": "What is an Abstract Class?", "a": "A class containing at least one pure virtual function. Abstract classes cannot be directly instantiated."}
        ]
    },
    {
        "id": 13,
        "title": "File Handling in C++ (Writing and Reading Records)",
        "aim": "To write a C++ program to write student records to a text file using `ofstream` and retrieve/display them using `ifstream`.",
        "software": "G++ / Clang / VS Code",
        "theory": "File handling in C++ utilizes classes from `<fstream>`: `ofstream` (output file stream for writing), `ifstream` (input file stream for reading), and `fstream` (both read/write).",
        "algorithm": [
            "Start",
            "Open file 'students.txt' using ofstream in write mode.",
            "Write student records (ID, Name, GPA) to file.",
            "Close ofstream.",
            "Open 'students.txt' using ifstream in read mode.",
            "Read file line by line and print on console.",
            "Close ifstream.",
            "Stop"
        ],
        "code": """#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    string filename = "students_record.txt";

    cout << "=== PROGRAM 13: FILE HANDLING IN C++ ===\\n";

    // 1. Writing to File
    ofstream outFile(filename);
    if (!outFile) {
        cerr << "[!] Error opening file for writing!\\n";
        return 1;
    }

    cout << "[+] Writing student records to '" << filename << "'...\\n";
    outFile << "101,Vikram_Singh,8.8\\n";
    outFile << "102,Priya_Sharma,9.2\\n";
    outFile << "103,Rohan_Verma,7.9\\n";
    outFile.close();
    cout << "[✓] File written and closed successfully.\\n";

    // 2. Reading from File
    ifstream inFile(filename);
    if (!inFile) {
        cerr << "[!] Error opening file for reading!\\n";
        return 1;
    }

    cout << "\\n--- Reading Records from File ---\\n";
    string line;
    int recordCount = 0;
    while (getline(inFile, line)) {
        recordCount++;
        cout << "Record " << recordCount << ": " << line << endl;
    }
    inFile.close();

    cout << "\\n[✓] Total records read: " << recordCount << endl;
    return 0;
}""",
        "output": """=== PROGRAM 13: FILE HANDLING IN C++ ===
[+] Writing student records to 'students_record.txt'...
[✓] File written and closed successfully.

--- Reading Records from File ---
Record 1: 101,Vikram_Singh,8.8
Record 2: 102,Priya_Sharma,9.2
Record 3: 103,Rohan_Verma,7.9

[✓] Total records read: 3""",
        "time_complexity": "O(N) where N is file size",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "Which header file is required for file stream handling in C++?", "a": "#include <fstream>"},
            {"q": "What is the difference between ios::app and ios::out file modes?", "a": "ios::out overwrites existing content, whereas ios::app appends new data to the end of file."}
        ]
    },
    {
        "id": 14,
        "title": "Templates (Function Template & Generic Stack Class Template)",
        "aim": "To write a C++ program implementing Generic Function Template for Swapping and Generic Class Template for Stack.",
        "software": "G++ / Clang / VS Code",
        "theory": "Templates enable Generic Programming, allowing functions and classes to operate with generic data types `template <typename T>` without duplicating code for int, float, string, etc.",
        "algorithm": [
            "Start",
            "Define template function customSwap(T &a, T &b).",
            "Define template class GenericStack<T> with push(), pop(), and display().",
            "Instantiate GenericStack<int> and GenericStack<string> in main().",
            "Test operations on both types.",
            "Stop"
        ],
        "code": """#include <iostream>
#include <string>
using namespace std;

// 1. Generic Function Template
template <typename T>
void customSwap(T &a, T &b) {
    T temp = a;
    a = b;
    b = temp;
}

// 2. Generic Class Template (Stack)
template <typename T>
class GenericStack {
private:
    T arr[10];
    int top;
public:
    GenericStack() : top(-1) {}

    void push(T val) {
        if (top == 9) {
            cout << "[!] Stack Overflow\\n";
        } else {
            arr[++top] = val;
        }
    }

    T pop() {
        if (top == -1) {
            cout << "[!] Stack Underflow\\n";
            return T();
        }
        return arr[top--];
    }

    void display() const {
        cout << "[Stack]: ";
        for (int i = 0; i <= top; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    cout << "=== PROGRAM 14: FUNCTION & CLASS TEMPLATES ===\\n\\n";

    // Testing Function Template
    int x = 10, y = 20;
    cout << "Before Swap: x=" << x << ", y=" << y << endl;
    customSwap(x, y);
    cout << "After Swap:  x=" << x << ", y=" << y << endl;

    string s1 = "Hello", s2 = "World";
    cout << "\\nBefore String Swap: s1=" << s1 << ", s2=" << s2 << endl;
    customSwap(s1, s2);
    cout << "After String Swap:  s1=" << s1 << ", s2=" << s2 << endl;

    // Testing Class Template with Int
    cout << "\\n--- Testing GenericStack<int> ---\\n";
    GenericStack<int> intStack;
    intStack.push(100);
    intStack.push(200);
    intStack.display();

    // Testing Class Template with String
    cout << "\\n--- Testing GenericStack<string> ---\\n";
    GenericStack<string> strStack;
    strStack.push("DataStructures");
    strStack.push("Algorithms");
    strStack.display();

    return 0;
}""",
        "output": """=== PROGRAM 14: FUNCTION & CLASS TEMPLATES ===

Before Swap: x=10, y=20
After Swap:  x=20, y=10

Before String Swap: s1=Hello, s2=World
After String Swap:  s1=World, s2=Hello

--- Testing GenericStack<int> ---
[Stack]: 100 200 

--- Testing GenericStack<string> ---
[Stack]: DataStructures Algorithms """,
        "time_complexity": "O(1)",
        "space_complexity": "O(N)",
        "viva": [
            {"q": "What is Generic Programming?", "a": "An approach where code is written in terms of types to-be-specified-later that are then instantiated when needed for specific types."},
            {"q": "What is the difference between typename and class in template header?", "a": "Both `template <class T>` and `template <typename T>` are completely identical and interchangeable."}
        ]
    },
    {
        "id": 15,
        "title": "Exception Handling in C++ (try, catch, throw)",
        "aim": "To write a C++ program demonstrating Exception Handling to catch Division by Zero and Array Index Out of Bounds errors.",
        "software": "G++ / Clang / VS Code",
        "theory": "Exception handling transfers control from a point where an exceptional error condition occurs (`throw`) to a handler block (`catch`) inside a monitored block (`try`), preventing program crash.",
        "algorithm": [
            "Start",
            "In function safeDivide(a, b): if b == 0 throw runtime_error or custom error.",
            "In main(), wrap function call in try block.",
            "Catch exception in catch(const exception &e) block.",
            "Display clean user-friendly error message without crashing.",
            "Stop"
        ],
        "code": """#include <iostream>
#include <stdexcept>
using namespace std;

double safeDivide(double numerator, double denominator) {
    if (denominator == 0.0) {
        throw runtime_error("Division by zero error: Denominator cannot be 0!");
    }
    return numerator / denominator;
}

int main() {
    double a, b;
    cout << "=== PROGRAM 15: EXCEPTION HANDLING IN C++ ===\\n";

    // Test Case 1: Valid Division
    try {
        cout << "\\nEnter numerator and denominator: ";
        cin >> a >> b;
        double result = safeDivide(a, b);
        cout << "[✓] Result: " << a << " / " << b << " = " << result << endl;
    }
    catch (const runtime_error &e) {
        cout << "[!] CAUGHT EXCEPTION: " << e.what() << endl;
    }
    catch (...) {
        cout << "[!] CAUGHT UNKNOWN EXCEPTION!\\n";
    }

    // Test Case 2: Intentional Zero Division
    cout << "\\n--- Triggering Zero Division Exception ---\\n";
    try {
        cout << "Attempting: safeDivide(50, 0)...\\n";
        double res = safeDivide(50, 0);
        cout << "Result: " << res << endl;
    }
    catch (const exception &e) {
        cout << "[!] EXCEPTION HANDLED SAFELY: " << e.what() << endl;
    }

    cout << "\\nProgram continued execution and terminated normally!\\n";
    return 0;
}""",
        "output": """=== PROGRAM 15: EXCEPTION HANDLING IN C++ ===

Enter numerator and denominator: 25 5
[✓] Result: 25 / 5 = 5

--- Triggering Zero Division Exception ---
Attempting: safeDivide(50, 0)...
[!] EXCEPTION HANDLED SAFELY: Division by zero error: Denominator cannot be 0!

Program continued execution and terminated normally!""",
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "viva": [
            {"q": "What are the three keywords used for exception handling in C++?", "a": "try (encloses monitored code), throw (raises an exception), catch (handles the exception)."},
            {"q": "What does catch(...) signify?", "a": "It is a catch-all block that handles any type of thrown exception."}
        ]
    }
]

# Generate standalone HTML & Jinja templates
def build_html(manual_title, course_code, branch, programs, subject_key):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{manual_title} - Laboratory Manual</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <!-- FontAwesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {{
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --primary-light: #eff6ff;
            --secondary: #0f172a;
            --accent: #f59e0b;
            --bg-base: #f8fafc;
            --bg-card: #ffffff;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --border-color: #e2e8f0;
            --code-bg: #0f172a;
            --code-text: #e2e8f0;
            --terminal-bg: #030712;
            --terminal-green: #22c55e;
            --radius-lg: 14px;
            --radius-md: 8px;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
            --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
            --shadow-lg: 0 12px 24px -4px rgba(0,0,0,0.1);
        }}

        [data-theme="dark"] {{
            --bg-base: #0b0f19;
            --bg-card: #131c2e;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border-color: #1e293b;
            --primary-light: rgba(37, 99, 235, 0.15);
            --shadow-md: 0 4px 20px rgba(0,0,0,0.4);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            scroll-behavior: smooth;
        }}

        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-base);
            color: var(--text-main);
            line-height: 1.6;
            transition: background 0.3s, color 0.3s;
        }}

        /* Navbar */
        .navbar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: var(--bg-card);
            border-bottom: 1px solid var(--border-color);
            padding: 14px 36px;
            position: sticky;
            top: 0;
            z-index: 1000;
            backdrop-filter: blur(8px);
            box-shadow: var(--shadow-sm);
        }}

        .navbar-brand {{
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: var(--primary);
            font-weight: 800;
            font-size: 1.25rem;
        }}

        .navbar-actions {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .nav-btn {{
            background: none;
            border: 1px solid var(--border-color);
            padding: 8px 16px;
            border-radius: var(--radius-md);
            cursor: pointer;
            color: var(--text-main);
            font-weight: 600;
            font-size: 0.85rem;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
            text-decoration: none;
        }}

        .nav-btn:hover {{
            background: var(--primary-light);
            border-color: var(--primary);
            color: var(--primary);
        }}

        .nav-btn.primary {{
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }}
        .nav-btn.primary:hover {{
            background: var(--primary-dark);
        }}

        /* Layout */
        .main-container {{
            max-width: 1300px;
            margin: 30px auto;
            padding: 0 24px;
            display: grid;
            grid-template-columns: 280px 1fr;
            gap: 30px;
            align-items: start;
        }}

        /* Sidebar Index */
        .sidebar {{
            position: sticky;
            top: 85px;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 20px;
            box-shadow: var(--shadow-sm);
            max-height: calc(100vh - 110px);
            overflow-y: auto;
        }}

        .sidebar-title {{
            font-size: 0.95rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text-muted);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .sidebar-search {{
            width: 100%;
            padding: 8px 12px;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            font-size: 0.85rem;
            margin-bottom: 15px;
            background: var(--bg-base);
            color: var(--text-main);
            outline: none;
        }}

        .sidebar-search:focus {{
            border-color: var(--primary);
        }}

        .index-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}

        .index-item a {{
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 8px 12px;
            border-radius: var(--radius-md);
            text-decoration: none;
            color: var(--text-main);
            font-size: 0.85rem;
            font-weight: 500;
            transition: all 0.2s;
        }}

        .index-item a:hover, .index-item.active a {{
            background: var(--primary-light);
            color: var(--primary);
            font-weight: 600;
        }}

        .exp-badge {{
            background: var(--primary);
            color: white;
            font-size: 0.7rem;
            font-weight: 700;
            padding: 2px 7px;
            border-radius: 20px;
            flex-shrink: 0;
        }}

        /* Content Area */
        .content-area {{
            display: flex;
            flex-direction: column;
            gap: 30px;
        }}

        /* College Header Card */
        .record-card {{
            background: var(--bg-card);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 30px;
            box-shadow: var(--shadow-md);
            position: relative;
            overflow: hidden;
        }}

        .record-card::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 6px;
            background: linear-gradient(90deg, #2563eb, #38bdf8, #22c55e);
        }}

        .college-header {{
            text-align: center;
            border-bottom: 2px dashed var(--border-color);
            padding-bottom: 20px;
            margin-bottom: 24px;
        }}

        .college-name {{
            font-size: 1.6rem;
            font-weight: 800;
            color: var(--primary);
            letter-spacing: -0.5px;
            margin-bottom: 4px;
        }}

        .college-sub {{
            font-size: 0.95rem;
            color: var(--text-muted);
            font-weight: 500;
        }}

        .manual-name {{
            font-size: 1.3rem;
            font-weight: 700;
            margin-top: 12px;
            color: var(--text-main);
            background: var(--primary-light);
            display: inline-block;
            padding: 6px 20px;
            border-radius: 30px;
            border: 1px solid var(--border-color);
        }}

        .student-meta-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            background: var(--bg-base);
            padding: 20px;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            margin-bottom: 20px;
        }}

        .meta-field {{
            display: flex;
            flex-direction: column;
        }}

        .meta-label {{
            font-size: 0.75rem;
            text-transform: uppercase;
            font-weight: 700;
            color: var(--text-muted);
            margin-bottom: 2px;
        }}

        .meta-val {{
            font-size: 0.95rem;
            font-weight: 600;
            color: var(--text-main);
        }}

        /* Index Table */
        .index-table-container {{
            overflow-x: auto;
            margin-top: 20px;
        }}

        .index-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85rem;
            text-align: left;
        }}

        .index-table th {{
            background: var(--bg-base);
            padding: 10px 14px;
            border: 1px solid var(--border-color);
            font-weight: 700;
            color: var(--text-main);
        }}

        .index-table td {{
            padding: 9px 14px;
            border: 1px solid var(--border-color);
            color: var(--text-main);
        }}

        .index-table tr:hover {{
            background: var(--primary-light);
        }}

        /* Experiment Card */
        .exp-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 30px;
            box-shadow: var(--shadow-sm);
            scroll-margin-top: 90px;
            transition: box-shadow 0.2s;
        }}

        .exp-card:hover {{
            box-shadow: var(--shadow-md);
        }}

        .exp-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 16px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 16px;
            margin-bottom: 20px;
        }}

        .exp-title-wrap {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}

        .exp-tag {{
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .exp-title {{
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--text-main);
        }}

        .exp-section {{
            margin-bottom: 24px;
        }}

        .section-heading {{
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .section-heading i {{
            color: var(--primary);
            font-size: 0.95rem;
        }}

        .text-box {{
            background: var(--bg-base);
            padding: 14px 18px;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            font-size: 0.92rem;
            color: var(--text-main);
        }}

        /* Algorithm List */
        .algo-steps {{
            list-style: none;
            counter-reset: algo-counter;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}

        .algo-steps li {{
            counter-increment: algo-counter;
            display: flex;
            align-items: flex-start;
            gap: 12px;
            background: var(--bg-base);
            padding: 10px 14px;
            border-radius: var(--radius-md);
            font-size: 0.9rem;
            border-left: 3px solid var(--primary);
        }}

        .algo-steps li::before {{
            content: "Step " counter(algo-counter) ":";
            font-weight: 700;
            color: var(--primary);
            flex-shrink: 0;
        }}

        /* Code Box */
        .code-box-wrapper {{
            position: relative;
            border-radius: var(--radius-md);
            overflow: hidden;
            background: var(--code-bg);
            border: 1px solid #334155;
            margin-top: 10px;
        }}

        .code-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 16px;
            background: #1e293b;
            color: #94a3b8;
            font-size: 0.75rem;
            font-family: 'JetBrains Mono', monospace;
            border-bottom: 1px solid #334155;
        }}

        .copy-btn {{
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            color: #f8fafc;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.75rem;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 5px;
        }}

        .copy-btn:hover {{
            background: var(--primary);
            border-color: var(--primary);
        }}

        pre code {{
            display: block;
            padding: 16px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            color: var(--code-text);
            line-height: 1.5;
            overflow-x: auto;
        }}

        /* Terminal Output Box */
        .terminal-box {{
            background: var(--terminal-bg);
            border: 1px solid #1f2937;
            border-radius: var(--radius-md);
            overflow: hidden;
            margin-top: 10px;
            font-family: 'JetBrains Mono', monospace;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }}

        .terminal-header {{
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 8px 12px;
            background: #111827;
            border-bottom: 1px solid #1f2937;
        }}

        .terminal-dot {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
        }}
        .dot-red {{ background: #ef4444; }}
        .dot-yellow {{ background: #eab308; }}
        .dot-green {{ background: #22c55e; }}

        .terminal-title {{
            font-size: 0.75rem;
            color: #9ca3af;
            margin-left: 6px;
            font-weight: 500;
        }}

        .terminal-body {{
            padding: 14px 16px;
            color: var(--terminal-green);
            font-size: 0.83rem;
            white-space: pre-wrap;
            line-height: 1.45;
        }}

        /* Complexity & Viva */
        .complexity-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-top: 10px;
        }}

        .complexity-box {{
            background: var(--bg-base);
            padding: 12px 16px;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            font-size: 0.88rem;
        }}

        .viva-list {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-top: 10px;
        }}

        .viva-item {{
            background: var(--bg-base);
            padding: 12px 16px;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            font-size: 0.9rem;
        }}

        .viva-q {{
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .viva-a {{
            color: var(--text-muted);
            line-height: 1.5;
        }}

        /* Sign Box */
        .sign-box {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px dashed var(--border-color);
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-muted);
        }}

        /* Print Styles */
        @media print {{
            .navbar, .sidebar, .copy-btn, .navbar-actions {{
                display: none !important;
            }}
            .main-container {{
                max-width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
                display: block !important;
            }}
            .exp-card {{
                page-break-before: always;
                border: 1px solid #ccc !important;
                box-shadow: none !important;
                margin-bottom: 30px;
            }}
            body {{
                background: white !important;
                color: black !important;
            }}
            pre code, .terminal-body {{
                white-space: pre-wrap !important;
                font-size: 9pt !important;
            }}
            .code-box-wrapper, .terminal-box {{
                border: 1px solid #333 !important;
                background: #f4f4f4 !important;
            }}
            pre code {{
                color: #111 !important;
            }}
            .terminal-body {{
                color: #000 !important;
            }}
        }}

        @media (max-width: 900px) {{
            .main-container {{
                grid-template-columns: 1fr;
            }}
            .sidebar {{
                display: none;
            }}
        }}
    </style>
</head>
<body>

    <!-- Sticky Navbar -->
    <header class="navbar">
        <a href="/" class="navbar-brand">
            <i class="fa-solid fa-graduation-cap"></i>
            <span>LAB MANUAL PORTAL</span>
        </a>
        <div class="navbar-actions">
            <a href="/lab-manuals" class="nav-btn">
                <i class="fa-solid fa-list-check"></i> All Manuals
            </a>
            <a href="{'/' if subject_key == 'ds' else '/ds-lab-manual'}" class="nav-btn">
                <i class="fa-solid fa-code"></i> DS in C
            </a>
            <a href="{'/' if subject_key == 'cpp' else '/cpp-lab-manual'}" class="nav-btn">
                <i class="fa-solid fa-cube"></i> OOPs in C++
            </a>
            <button class="nav-btn" onclick="toggleTheme()" title="Toggle Dark/Light Mode">
                <i class="fa-solid fa-moon" id="themeIcon"></i>
            </button>
            <button class="nav-btn primary" onclick="window.print()" title="Print / Save PDF">
                <i class="fa-solid fa-print"></i> Print Record
            </button>
        </div>
    </header>

    <div class="main-container">
        <!-- Sidebar Jump Index -->
        <aside class="sidebar">
            <div class="sidebar-title">
                <i class="fa-solid fa-bars-staggered"></i> Experiments Index
            </div>
            <input type="text" class="sidebar-search" id="searchExp" placeholder="Filter experiments..." onkeyup="filterIndex()">
            <ul class="index-list" id="indexList">
'''
    for p in programs:
        html += f'''                <li class="index-item">
                    <a href="#exp-{p['id']}">
                        <span class="exp-badge">Exp {p['id']}</span>
                        <span class="exp-nav-title">{p['title']}</span>
                    </a>
                </li>
'''
    html += f'''            </ul>
        </aside>

        <!-- Main Content Area -->
        <main class="content-area">
            
            <!-- College Record Title Card -->
            <section class="record-card">
                <div class="college-header">
                    <h1 class="college-name">DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING</h1>
                    <p class="college-sub">Laboratory Practical Record & Manual</p>
                    <div class="manual-name">{manual_title}</div>
                </div>

                <div class="student-meta-grid">
                    <div class="meta-field">
                        <span class="meta-label">Course Code</span>
                        <span class="meta-val">{course_code}</span>
                    </div>
                    <div class="meta-field">
                        <span class="meta-label">Target Branch</span>
                        <span class="meta-val">{branch}</span>
                    </div>
                    <div class="meta-field">
                        <span class="meta-label">Academic Year</span>
                        <span class="meta-val">2026 - 2027</span>
                    </div>
                    <div class="meta-field">
                        <span class="meta-label">Total Experiments</span>
                        <span class="meta-val">{len(programs)} Practical Programs</span>
                    </div>
                </div>

                <!-- Complete Record Index Table -->
                <h3 style="font-size: 1.05rem; font-weight: 700; margin-top: 20px; display: flex; align-items: center; gap: 8px;">
                    <i class="fa-solid fa-table-list" style="color: var(--primary);"></i> Practical Index / Syllabus Record Sheet
                </h3>
                <div class="index-table-container">
                    <table class="index-table">
                        <thead>
                            <tr>
                                <th style="width: 60px;">Exp No.</th>
                                <th>Name of the Experiment</th>
                                <th style="width: 110px;">Date</th>
                                <th style="width: 70px;">Page No.</th>
                                <th style="width: 100px;">Faculty Sign</th>
                            </tr>
                        </thead>
                        <tbody>
'''
    for p in programs:
        html += f'''                            <tr>
                                <td style="text-align: center; font-weight: 700;">{p['id']}</td>
                                <td><a href="#exp-{p['id']}" style="color: inherit; text-decoration: none; font-weight: 500;">{p['title']}</a></td>
                                <td>____/____</td>
                                <td style="text-align: center;">{p['id'] * 2 - 1}</td>
                                <td></td>
                            </tr>
'''
    html += '''                        </tbody>
                    </table>
                </div>
            </section>
'''

    # Detailed Experiment Cards
    for p in programs:
        code_escaped = p['code'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        output_escaped = p['output'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

        html += f'''
            <!-- EXPERIMENT {p['id']} -->
            <article class="exp-card" id="exp-{p['id']}">
                <div class="exp-header">
                    <div class="exp-title-wrap">
                        <span class="exp-tag">Experiment No. {p['id']}</span>
                        <h2 class="exp-title">{p['title']}</h2>
                    </div>
                </div>

                <!-- Aim -->
                <div class="exp-section">
                    <div class="section-heading"><i class="fa-solid fa-bullseye"></i> AIM / OBJECTIVE</div>
                    <div class="text-box">{p['aim']}</div>
                </div>

                <!-- Software / Hardware Requirements -->
                <div class="exp-section">
                    <div class="section-heading"><i class="fa-solid fa-laptop-code"></i> SOFTWARE / ENVIRONMENT</div>
                    <div class="text-box">{p['software']}</div>
                </div>

                <!-- Theory -->
                <div class="exp-section">
                    <div class="section-heading"><i class="fa-solid fa-book-open"></i> THEORETICAL BACKGROUND / PREREQUISITES</div>
                    <div class="text-box">{p['theory']}</div>
                </div>

                <!-- Algorithm -->
                <div class="exp-section">
                    <div class="section-heading"><i class="fa-solid fa-diagram-project"></i> STEP-BY-STEP ALGORITHM</div>
                    <ol class="algo-steps">
'''
        for step in p['algorithm']:
            html += f'''                        <li>{step}</li>
'''
        html += f'''                    </ol>
                </div>

                <!-- Source Code -->
                <div class="exp-section">
                    <div class="section-heading"><i class="fa-solid fa-code"></i> SOURCE CODE (C/C++)</div>
                    <div class="code-box-wrapper">
                        <div class="code-header">
                            <span>program_{p['id']}.{'c' if subject_key == 'ds' else 'cpp'}</span>
                            <button class="copy-btn" onclick="copyCode('code-{p['id']}', this)">
                                <i class="fa-regular fa-copy"></i> Copy Code
                            </button>
                        </div>
                        <pre><code id="code-{p['id']}">{code_escaped}</code></pre>
                    </div>
                </div>

                <!-- Terminal Output -->
                <div class="exp-section">
                    <div class="section-heading"><i class="fa-solid fa-terminal"></i> SAMPLE INPUT & EXECUTION OUTPUT</div>
                    <div class="terminal-box">
                        <div class="terminal-header">
                            <span class="terminal-dot dot-red"></span>
                            <span class="terminal-dot dot-yellow"></span>
                            <span class="terminal-dot dot-green"></span>
                            <span class="terminal-title">Terminal - gcc program_{p['id']}.{'c' if subject_key == 'ds' else 'cpp'} &amp;&amp; ./a.out</span>
                        </div>
                        <div class="terminal-body">{output_escaped}</div>
                    </div>
                </div>

                <!-- Complexity -->
                <div class="exp-section">
                    <div class="section-heading"><i class="fa-solid fa-gauge-high"></i> COMPLEXITY ANALYSIS</div>
                    <div class="complexity-grid">
                        <div class="complexity-box"><strong>Time Complexity:</strong> {p['time_complexity']}</div>
                        <div class="complexity-box"><strong>Space Complexity:</strong> {p['space_complexity']}</div>
                    </div>
                </div>

                <!-- Viva-Voce Questions -->
                <div class="exp-section">
                    <div class="section-heading"><i class="fa-solid fa-comments"></i> VIVA-VOCE QUESTIONS & ANSWERS</div>
                    <div class="viva-list">
'''
        for v in p['viva']:
            html += f'''                        <div class="viva-item">
                            <div class="viva-q"><i class="fa-solid fa-circle-question" style="color: var(--primary);"></i> Q: {v['q']}</div>
                            <div class="viva-a"><strong>Ans:</strong> {v['a']}</div>
                        </div>
'''
        html += f'''                    </div>
                </div>

                <!-- Result / Signature -->
                <div class="sign-box">
                    <div>
                        <strong>Result:</strong> Program successfully implemented, compiled, and verified.
                    </div>
                    <div style="text-align: right;">
                        <div>Faculty Signature: __________________</div>
                        <div style="margin-top: 4px; font-size: 0.75rem;">Grade / Marks: [ &nbsp; &nbsp; &nbsp; &nbsp; / 10 ]</div>
                    </div>
                </div>
            </article>
'''

    html += '''
        </main>
    </div>

    <!-- Scripts -->
    <script>
        function toggleTheme() {
            const current = document.documentElement.getAttribute('data-theme');
            const newTheme = current === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            const icon = document.getElementById('themeIcon');
            icon.className = newTheme === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
        }

        // Apply saved theme
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            document.documentElement.setAttribute('data-theme', savedTheme);
            const icon = document.getElementById('themeIcon');
            if (icon) icon.className = savedTheme === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
        }

        function copyCode(id, btn) {
            const codeEl = document.getElementById(id);
            if (!codeEl) return;
            const text = codeEl.innerText;
            navigator.clipboard.writeText(text).then(() => {
                const origHtml = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
                btn.style.background = '#22c55e';
                setTimeout(() => {
                    btn.innerHTML = origHtml;
                    btn.style.background = '';
                }, 2000);
            });
        }

        function filterIndex() {
            const q = document.getElementById('searchExp').value.toLowerCase();
            const items = document.querySelectorAll('#indexList .index-item');
            items.forEach(it => {
                const text = it.innerText.toLowerCase();
                it.style.display = text.includes(q) ? 'block' : 'none';
            });
        }
    </script>
</body>
</html>'''
    return html

# Build unified portal HTML
def build_portal_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Computer Science Laboratory Manuals Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --primary-light: #eff6ff;
            --bg-base: #f8fafc;
            --bg-card: #ffffff;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --border-color: #e2e8f0;
            --radius-lg: 16px;
            --radius-md: 10px;
            --shadow-md: 0 4px 15px rgba(0,0,0,0.06);
            --shadow-lg: 0 12px 30px rgba(0,0,0,0.08);
        }
        [data-theme="dark"] {
            --bg-base: #0b0f19;
            --bg-card: #131c2e;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border-color: #1e293b;
            --primary-light: rgba(37, 99, 235, 0.15);
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-base);
            color: var(--text-main);
            line-height: 1.6;
            min-height: 100vh;
        }
        .hero {
            text-align: center;
            padding: 60px 20px 40px;
            max-width: 900px;
            margin: 0 auto;
        }
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: var(--primary-light);
            color: var(--primary);
            padding: 6px 16px;
            border-radius: 30px;
            font-weight: 700;
            font-size: 0.85rem;
            margin-bottom: 16px;
            border: 1px solid var(--border-color);
        }
        .hero-title {
            font-size: 2.5rem;
            font-weight: 800;
            letter-spacing: -0.5px;
            margin-bottom: 12px;
            background: linear-gradient(135deg, #1e293b 0%, #2563eb 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        [data-theme="dark"] .hero-title {
            background: linear-gradient(135deg, #f8fafc 0%, #60a5fa 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-sub {
            font-size: 1.1rem;
            color: var(--text-muted);
            line-height: 1.6;
        }
        .manual-grid {
            max-width: 1100px;
            margin: 30px auto 60px;
            padding: 0 20px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 30px;
        }
        .card {
            background: var(--bg-card);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 35px;
            box-shadow: var(--shadow-md);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-lg);
            border-color: var(--primary);
        }
        .card-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .card-icon {
            width: 55px;
            height: 55px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        }
        .icon-ds {
            background: #eff6ff;
            color: #2563eb;
        }
        .icon-cpp {
            background: #fdf4ff;
            color: #c026d3;
        }
        .icon-cd {
            background: #ecfdf5;
            color: #059669;
        }
        .card-tag {
            font-size: 0.75rem;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .tag-c { background: #dbeafe; color: #1e40af; }
        .tag-cpp { background: #fae8ff; color: #86198f; }
        .tag-cd { background: #d1fae5; color: #065f46; }

        .card-title {
            font-size: 1.4rem;
            font-weight: 800;
            margin-bottom: 10px;
        }
        .card-desc {
            color: var(--text-muted);
            font-size: 0.92rem;
            margin-bottom: 24px;
        }
        .feature-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-bottom: 25px;
            font-size: 0.88rem;
        }
        .feature-list li {
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--text-main);
        }
        .feature-list li i {
            color: #22c55e;
            font-size: 0.85rem;
        }
        .btn-launch {
            display: block;
            text-align: center;
            background: var(--primary);
            color: white;
            padding: 12px 24px;
            border-radius: var(--radius-md);
            text-decoration: none;
            font-weight: 700;
            transition: background 0.2s;
        }
        .btn-launch:hover {
            background: var(--primary-dark);
        }
    </style>
</head>
<body>
    <div class="hero">
        <div class="hero-badge">
            <i class="fa-solid fa-graduation-cap"></i> Official College Laboratory Manuals
        </div>
        <h1 class="hero-title">Engineering Practical Records Portal</h1>
        <p class="hero-sub">Complete college-ready lab manuals with Aim, Algorithm, Source Code, Sample Input/Output, Viva-Voce Questions, and Print-ready A4 Record Sheets.</p>
    </div>

    <div class="manual-grid">
        <!-- Manual 1: DS in C -->
        <div class="card">
            <div>
                <div class="card-top">
                    <div class="card-icon icon-ds"><i class="fa-solid fa-sitemap"></i></div>
                    <span class="card-tag tag-c">15 Programs in C</span>
                </div>
                <h2 class="card-title">Data Structures Using C</h2>
                <p class="card-desc">Comprehensive manual covering 1D/2D Arrays, Matrices, Recursion, Stacks, Linear & Circular Queues, Binary Search Tree, Sequential & Binary Search, Bubble & Insertion Sort, and Singly Linked Lists.</p>
                <ul class="feature-list">
                    <li><i class="fa-solid fa-check"></i> 15 Full Working C Programs with Output</li>
                    <li><i class="fa-solid fa-check"></i> Stack, Queue, Circular Queue, BST & Linked List</li>
                    <li><i class="fa-solid fa-check"></i> Step-by-Step Algorithm & Time Complexity</li>
                    <li><i class="fa-solid fa-check"></i> College Print Sheet & Viva Voce Q&A</li>
                </ul>
            </div>
            <a href="/ds-lab-manual" class="btn-launch">Open DS Lab Manual</a>
        </div>

        <!-- Manual 2: OOPs with C++ -->
        <div class="card">
            <div>
                <div class="card-top">
                    <div class="card-icon icon-cpp"><i class="fa-solid fa-cubes"></i></div>
                    <span class="card-tag tag-cpp">15 Programs in C++</span>
                </div>
                <h2 class="card-title">Object-Oriented Programming (C++)</h2>
                <p class="card-desc">Complete OOP manual covering Classes & Objects, Inline & Friend Functions, Overloading, Constructors & Destructors, Single/Multilevel/Multiple/Virtual Base Inheritance, Virtual Functions, File Handling, Templates, and Exceptions.</p>
                <ul class="feature-list">
                    <li><i class="fa-solid fa-check"></i> 15 Full Working C++ Programs with Output</li>
                    <li><i class="fa-solid fa-check"></i> Unary/Binary Operator & Function Overloading</li>
                    <li><i class="fa-solid fa-check"></i> Diamond Problem & Runtime Polymorphism</li>
                    <li><i class="fa-solid fa-check"></i> Templates, Exception Handling & File I/O</li>
                </ul>
            </div>
            <a href="/cpp-lab-manual" class="btn-launch" style="background: #c026d3;">Open OOPs Lab Manual</a>
        </div>

        <!-- Manual 3: Compiler Design -->
        <div class="card">
            <div>
                <div class="card-top">
                    <div class="card-icon icon-cd"><i class="fa-solid fa-flask"></i></div>
                    <span class="card-tag tag-cd">SBITM Betul</span>
                </div>
                <h2 class="card-title">Compiler Design Lab</h2>
                <p class="card-desc">Official AD-604 Lab Manual for SBITM Betul (Branch: AI & DS, Year: III Yr B.E, Sem: 6) with Lexical Analysis, Tokenization, Parsing, and Code Generation.</p>
                <ul class="feature-list">
                    <li><i class="fa-solid fa-check"></i> Lexical Analyzer & Token Classifier</li>
                    <li><i class="fa-solid fa-check"></i> LL(1) & Recursive Descent Parsers</li>
                    <li><i class="fa-solid fa-check"></i> 3-Address Code Generation</li>
                </ul>
            </div>
            <a href="/compiler-lab-manual" class="btn-launch" style="background: #059669;">Open Compiler Manual</a>
        </div>
    </div>
</body>
</html>'''

if __name__ == '__main__':
    # 1. Build DS Manual
    ds_html = build_html("DATA STRUCTURES LABORATORY MANUAL (USING C)", "CS-304", "Computer Science & Engineering (B.E / B.Tech)", ds_programs, "ds")
    with open("templates/ds_lab_manual.html", "w", encoding="utf-8") as f:
        f.write(ds_html)
    with open("ds_lab_manual.html", "w", encoding="utf-8") as f:
        f.write(ds_html)
    print("Created templates/ds_lab_manual.html & ds_lab_manual.html successfully!")

    # 2. Build C++ OOPs Manual
    cpp_html = build_html("OBJECT-ORIENTED PROGRAMMING LABORATORY MANUAL (USING C++)", "CS-305", "Computer Science & Engineering / AI & DS", cpp_programs, "cpp")
    with open("templates/cpp_lab_manual.html", "w", encoding="utf-8") as f:
        f.write(cpp_html)
    with open("cpp_lab_manual.html", "w", encoding="utf-8") as f:
        f.write(cpp_html)
    print("Created templates/cpp_lab_manual.html & cpp_lab_manual.html successfully!")

    # 3. Build Lab Manuals Portal
    portal_html = build_portal_html()
    with open("templates/lab_manuals.html", "w", encoding="utf-8") as f:
        f.write(portal_html)
    with open("lab_manuals.html", "w", encoding="utf-8") as f:
        f.write(portal_html)
    print("Created templates/lab_manuals.html & lab_manuals.html successfully!")
