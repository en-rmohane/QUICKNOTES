# -*- coding: utf-8 -*-
"""
OOP & C++ Complete Master Curriculum (Parts I through XI, Chapters 1 to 28)
Comprehensive textbook & lecture manual formatted in simplified, student-friendly English.
Includes exam-oriented theory, real-world analogies, Mermaid diagrams, clean C++ code,
and terminal outputs.
"""

cpp_oop_data = [
    # =========================================================================
    # UNIT 1: OBJECT-ORIENTED THINKING & OBJECT-ORIENTED PROGRAMMING
    # =========================================================================
    {
        "unit": "UNIT 1",
        "title": "Object-Oriented Thinking & Object-Oriented Programming",
        "topics": [
            {
                "slug": "unit-1-object-oriented-thinking-and-oop",
                "title": "Unit 1: Object-Oriented Thinking & OOP (Complete Notes)",
                "subtopics": [
                    "1. Object-Oriented Thinking (Definition, Real-World Examples, C++ Code, Advantages & Disadvantages)",
                    "2. Object-Oriented Programming (Definition, Objectives, Car Example, Characteristics, Advantages & Disadvantages)",
                    "3. Procedural Programming (Definition, Student Result C Code, Characteristics, Advantages & Disadvantages)",
                    "4. Comparison of Procedural and Object-Oriented Programming (Comparison Table, Flow Differences)",
                    "5. Features of Object-Oriented Paradigm (All 10 Features with Code)",
                    "6. Merits and Demerits of Object-Oriented Methodology (E-commerce Real-World Scenario)",
                    "7. Object Model (Elements, Library Management System, C++ Class)",
                    "8. Elements of OOPs (10 Core Elements Summary)",
                    "9. Class (Definition, House Blueprint Analogy, C++ Syntax)",
                    "10. Object (Definition, BMW Analogy, State/Behavior/Identity, C++ Code)",
                    "11. Encapsulation (ATM Analogy, Data Hiding, C++ BankAccount)",
                    "12. Abstraction (Mobile Phone Analogy, C++ ATM Class)",
                    "13. Inheritance (Vehicle Analogy, C++ Code, 5 Types: Single, Multiple, Multilevel, Hierarchical, Hybrid)",
                    "14. Polymorphism (Compile-Time vs. Run-Time, Payment Analogy, Overloading & Overriding Code)",
                    "15. Message Passing (Restaurant Analogy, Printer & Computer C++ Code)",
                    "16. Dynamic Binding (Universal Remote Analogy, Virtual Functions & Base Pointer Code)",
                    "17. I/O Processing (Input/Processing/Output Flow, cin, cout, >>, <<, getline())",
                    "18. Important: Four Pillars of OOP (E-A-I-P) & Procedural vs OOP Flow Chart"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🌟 UNIT 1 — OBJECT-ORIENTED THINKING & OBJECT-ORIENTED PROGRAMMING</h1>
        <p style="font-size: 1.15rem; margin: 0;">Comprehensive Notes covering Object-Oriented Thinking, Procedural vs OOP, Object Model, The Four Pillars (E-A-I-P), Dynamic Binding, and I/O Streams</p>
    </div>

    <!-- 1. OBJECT-ORIENTED THINKING -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">1. OBJECT-ORIENTED THINKING</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>Object-Oriented Thinking (OOT)</strong> is a problem-solving approach in which a problem is analyzed and designed in terms of objects, their properties, their behaviors, and the relationships between them.
        </p>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            In simple words, object-oriented thinking means looking at a problem in the same way we look at the real world. In the real world, we interact with different entities or objects. Each object has some characteristics and performs certain actions.
        </p>
        
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            For example, in a <strong>college management system</strong>, we can identify objects such as:
        </p>
        <ul style="color: #334155; line-height: 1.8; font-size: 1rem; margin-left: 20px;">
            <li>Student</li>
            <li>Teacher</li>
            <li>Course</li>
            <li>Classroom</li>
            <li>Department</li>
            <li>Examination</li>
        </ul>

        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            Each object has its own data and behavior. For example, a <strong>Student</strong> may have:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin: 15px 0;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">Properties (Data / Attributes)</h4>
                <ul style="margin: 0; padding-left: 20px; color: #475569; line-height: 1.6;">
                    <li>Name</li>
                    <li>Roll Number</li>
                    <li>Age</li>
                    <li>Course</li>
                    <li>Marks</li>
                </ul>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">Behaviors (Actions / Methods)</h4>
                <ul style="margin: 0; padding-left: 20px; color: #475569; line-height: 1.6;">
                    <li>Attend class</li>
                    <li>Study</li>
                    <li>Give examination</li>
                    <li>Pay fees</li>
                </ul>
            </div>
        </div>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            Thus, object-oriented thinking helps us identify the objects involved in a problem before writing the actual program.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            Consider a <strong>Banking System</strong>.
        </p>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            Instead of thinking: <em>"First take account number, then take amount, then calculate balance..."</em>, we think in terms of objects:
        </p>
        <div class="mermaid" style="text-align: center; margin: 15px 0;">
graph TD
    B["<b>Bank</b>"] --> C["Customer"]
    B --> A["Account"]
    B --> T["Transaction"]
        </div>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            An <strong>Account</strong> has:
        </p>
        <ul style="color: #334155; line-height: 1.8; font-size: 1rem; margin-left: 20px;">
            <li>Account Number</li>
            <li>Account Holder</li>
            <li>Balance</li>
            <li>Account Type</li>
        </ul>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            and performs:
        </p>
        <ul style="color: #334155; line-height: 1.8; font-size: 1rem; margin-left: 20px;">
            <li><code>deposit()</code></li>
            <li><code>withdraw()</code></li>
            <li><code>checkBalance()</code></li>
        </ul>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            This is object-oriented thinking because we are identifying the entities involved and their responsibilities.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">C++ Example</h3>
        <pre><code class="language-cpp">#include &lt;iostream&gt;
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
        if (amount &lt;= balance)
            balance -= amount;
    }

    void displayBalance()
    {
        cout &lt;&lt; "Balance: " &lt;&lt; balance &lt;&lt; endl;
    }
};

int main()
{
    BankAccount account;

    account.deposit(5000);
    account.withdraw(1000);
    account.displayBalance();

    return 0;
}</code></pre>
        <p style="font-size: 1rem; color: #475569; margin-top: 10px;">
            Here, we first identified <code>BankAccount</code> as an object-oriented entity and then defined its data and behavior.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ol style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li><strong>Natural representation:</strong> Real-world entities can be represented naturally as objects.</li>
                    <li><strong>Better problem understanding:</strong> Breaking a problem into objects makes complex problems easier to understand.</li>
                    <li><strong>Easier design:</strong> Objects and their relationships can be identified before programming.</li>
                    <li><strong>Supports reusability:</strong> Once objects/classes are designed, they can be reused.</li>
                    <li><strong>Easier maintenance:</strong> Each object generally has a specific responsibility, making changes easier.</li>
                </ol>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ol style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li><strong>Requires proper analysis:</strong> Incorrect identification of objects can result in poor program design.</li>
                    <li><strong>Can be complex:</strong> Large systems may contain hundreds or thousands of interacting objects.</li>
                    <li><strong>More planning is required:</strong> Object-oriented design generally requires more planning before coding.</li>
                    <li><strong>Not always necessary:</strong> For very small programs, object-oriented thinking may introduce unnecessary complexity.</li>
                </ol>
            </div>
        </div>

        <div style="background: #eff6ff; padding: 15px; border-radius: 8px; border-left: 5px solid #2563eb; margin-top: 20px;">
            <strong>📌 Key Point:</strong> Object-Oriented Thinking is the process of understanding and designing a problem in terms of objects, their properties, behaviors, and relationships.
        </div>
    </div>

    <!-- 2. OBJECT-ORIENTED PROGRAMMING -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">2. OBJECT-ORIENTED PROGRAMMING</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>Object-Oriented Programming (OOP)</strong> is a programming paradigm in which software is designed and developed using objects and classes.
        </p>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            An object contains data and functions that operate on that data. OOP allows programmers to model real-world entities inside a computer program.
        </p>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            The main objective of OOP is to make programs:
        </p>
        <ul style="color: #334155; line-height: 1.8; font-size: 1rem; margin-left: 20px;">
            <li>Modular</li>
            <li>Reusable</li>
            <li>Secure</li>
            <li>Maintainable</li>
            <li>Flexible</li>
            <li>Easy to understand</li>
        </ul>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            OOP is based on several important concepts such as: <strong>Class, Object, Encapsulation, Abstraction, Inheritance, Polymorphism, Data hiding, Message passing, Dynamic binding</strong>.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            Consider a <strong>Car</strong>. A car has properties such as: <em>Color, Model, Speed, Engine Number, Fuel Level</em>. It also performs actions: <em>start(), stop(), accelerate(), brake()</em>. In OOP, we can represent this car as a class.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">C++ Example</h3>
        <pre><code class="language-cpp">#include &lt;iostream&gt;
using namespace std;

class Car
{
public:
    string color;
    int speed;

    void start()
    {
        cout &lt;&lt; "Car started" &lt;&lt; endl;
    }

    void accelerate()
    {
        speed += 10;
        cout &lt;&lt; "Speed: " &lt;&lt; speed &lt;&lt; endl;
    }

    void stop()
    {
        cout &lt;&lt; "Car stopped" &lt;&lt; endl;
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
}</code></pre>
        
        <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px; margin: 15px 0;">
            <strong>Breakdown:</strong><br/>
            <code>Car</code> &rarr; Class<br/>
            <code>c1</code> &rarr; Object<br/>
            <code>color</code> &rarr; Data<br/>
            <code>speed</code> &rarr; Data<br/>
            <code>start()</code> &rarr; Behavior<br/>
            <code>stop()</code> &rarr; Behavior
        </div>

        <h3 style="color: #1e40af; margin-top: 20px;">Main Characteristics of OOP</h3>
        <ol style="color: #334155; line-height: 1.8; font-size: 1rem; margin-left: 20px;">
            <li><strong>Class:</strong> A class is a blueprint used to create objects.</li>
            <li><strong>Object:</strong> An object is an instance of a class.</li>
            <li><strong>Encapsulation:</strong> Data and functions are combined into one unit.</li>
            <li><strong>Abstraction:</strong> Unnecessary implementation details are hidden.</li>
            <li><strong>Inheritance:</strong> Existing classes can be reused to create new classes.</li>
            <li><strong>Polymorphism:</strong> One interface can have multiple forms.</li>
            <li><strong>Data Hiding:</strong> Internal data can be protected from direct access.</li>
        </ol>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ol style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li><strong>Reusability:</strong> Code can be reused through inheritance and classes.</li>
                    <li><strong>Security:</strong> Encapsulation and data hiding improve data security.</li>
                    <li><strong>Maintainability:</strong> Programs can be divided into independent classes.</li>
                    <li><strong>Modularity:</strong> Large programs can be divided into smaller modules.</li>
                    <li><strong>Real-world modeling:</strong> Real-world entities can be represented easily.</li>
                    <li><strong>Flexibility:</strong> Polymorphism allows flexible program design.</li>
                </ol>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ol style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li><strong>Complexity:</strong> OOP contains many concepts that beginners need time to understand.</li>
                    <li><strong>Memory requirement:</strong> Objects and additional OOP mechanisms may require more memory.</li>
                    <li><strong>Development time:</strong> Designing classes and relationships can take additional time.</li>
                    <li><strong>Performance overhead:</strong> Some OOP mechanisms can introduce additional processing overhead.</li>
                    <li><strong>Not suitable for every problem:</strong> Small and simple problems may be easier to solve using procedural programming.</li>
                </ol>
            </div>
        </div>

        <div style="background: #eff6ff; padding: 15px; border-radius: 8px; border-left: 5px solid #2563eb; margin-top: 20px;">
            <strong>📌 Key Point:</strong> OOP organizes a program around objects that contain data and behavior, making software modular, reusable, maintainable, and easier to model.
        </div>
    </div>

    <!-- 3. PROCEDURAL PROGRAMMING -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">3. PROCEDURAL PROGRAMMING</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>Procedural Programming</strong> is a programming paradigm in which a program is organized as a sequence of functions or procedures that perform specific tasks.
        </p>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            The primary focus is on: <strong>"What steps should be performed to solve the problem?"</strong>
        </p>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            In procedural programming, the program is usually divided into several functions. Each function performs a particular operation.
            Examples of procedural programming languages include: <strong>C, Pascal, FORTRAN, COBOL</strong>. <em>C is one of the most commonly used procedural programming languages.</em>
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            Suppose we want to calculate a student's result. The procedural approach may be:
        </p>
        <ol style="color: #334155; line-height: 1.8; font-size: 1rem; margin-left: 20px;">
            <li>Take student name</li>
            <li>Take marks</li>
            <li>Calculate total</li>
            <li>Calculate percentage</li>
            <li>Calculate grade</li>
            <li>Display result</li>
        </ol>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            We can create separate functions: <code>input()</code>, <code>calculateTotal()</code>, <code>calculatePercentage()</code>, <code>calculateGrade()</code>, <code>display()</code>. The focus is on functions and the sequence of operations.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">C Example</h3>
        <pre><code class="language-c">#include &lt;stdio.h&gt;

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

    printf("Total = %d\\n", total);
    printf("Percentage = %.2f\\n", percentage);

    return 0;
}</code></pre>

        <h3 style="color: #1e40af; margin-top: 20px;">Characteristics</h3>
        <ol style="color: #334155; line-height: 1.8; font-size: 1rem; margin-left: 20px;">
            <li><strong>Functions are the primary unit:</strong> Programs are divided into functions.</li>
            <li><strong>Top-down approach:</strong> The problem is divided into smaller tasks.</li>
            <li><strong>Data and functions are separate:</strong> Data may be shared between functions.</li>
            <li><strong>Sequential execution:</strong> Statements generally execute according to the defined flow.</li>
            <li><strong>Limited data protection:</strong> There is comparatively less support for data hiding.</li>
        </ol>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ol style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li><strong>Simple for small programs:</strong> Procedural programming is easy to understand for simple problems.</li>
                    <li><strong>Easy implementation:</strong> Functions can be directly created for individual tasks.</li>
                    <li><strong>Efficient:</strong> Procedural programs can be efficient because they generally have less abstraction overhead.</li>
                    <li><strong>Easy to learn:</strong> Languages like C provide a relatively straightforward programming model.</li>
                </ol>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ol style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li><strong>Difficult to maintain large programs:</strong> Large programs can contain hundreds of functions.</li>
                    <li><strong>Less data security:</strong> Data can be accessed by multiple functions.</li>
                    <li><strong>Limited reusability:</strong> Code reuse is less powerful compared with OOP inheritance and class-based reuse.</li>
                    <li><strong>Difficult real-world modeling:</strong> Representing real-world entities is less natural.</li>
                    <li><strong>Changes can affect multiple functions:</strong> A change in shared data may require modifications in several functions.</li>
                </ol>
            </div>
        </div>
    </div>

    <!-- 4. COMPARISON -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">4. COMPARISON OF PROCEDURAL AND OBJECT-ORIENTED PROGRAMMING</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            Procedural and Object-Oriented Programming are two different approaches to software development. Procedural programming focuses primarily on functions and procedures, whereas OOP focuses primarily on objects and classes.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example (Banking Application)</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin: 15px 0;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">Procedural approach</h4>
                <p style="color: #475569; font-size: 0.95rem;">We may create separate functions where data is stored separately:</p>
                <ul style="color: #475569; font-size: 0.95rem; margin: 0; padding-left: 20px;">
                    <li><code>createAccount()</code></li>
                    <li><code>deposit()</code></li>
                    <li><code>withdraw()</code></li>
                    <li><code>checkBalance()</code></li>
                    <li><code>closeAccount()</code></li>
                </ul>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">Object-oriented approach</h4>
                <p style="color: #475569; font-size: 0.95rem;">We create an <code>Account</code> class combining data & behavior:</p>
                <div class="mermaid" style="text-align: center;">
graph TD
    Acc["<b>Account</b>"] --> D["Data: accountNumber, balance"]
    Acc --> B["Behavior: deposit(), withdraw(), checkBalance()"]
                </div>
            </div>
        </div>

        <h3 style="color: #1e40af; margin-top: 20px;">Comparison Table</h3>
        <table style="width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 1rem;">
            <thead>
                <tr style="background: #1e3a8a; color: white;">
                    <th style="padding: 10px; border: 1px solid #cbd5e1;">Feature</th>
                    <th style="padding: 10px; border: 1px solid #cbd5e1;">Procedural Programming</th>
                    <th style="padding: 10px; border: 1px solid #cbd5e1;">OOP</th>
                </tr>
            </thead>
            <tbody>
                <tr style="background: #f8fafc;">
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Main unit</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Function</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold; color: #16a34a;">Object/Class</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Approach</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Top-down</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold; color: #16a34a;">Bottom-up</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Main focus</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Procedures</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Objects</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Data & functions</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Separate</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Combined</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Data hiding</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Limited</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Strong</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Security</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Lower</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1; color: #16a34a; font-weight: bold;">Higher</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Reusability</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Limited</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">High</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Inheritance</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Not supported as a core feature</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Supported</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Polymorphism</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Not a core feature</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Supported</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Real-world modeling</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Difficult</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Easy</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Large programs</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Difficult</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Easier</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Maintenance</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Difficult</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">Easier</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Examples</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">C, Pascal</td>
                    <td style="padding: 10px; border: 1px solid #cbd5e1;">C++, Java, C#</td>
                </tr>
            </tbody>
        </table>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages of OOP over Procedural Programming</h4>
                <ul style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li>Better data security</li>
                    <li>Better code reusability</li>
                    <li>Easier maintenance</li>
                    <li>Better real-world modeling</li>
                    <li>Supports inheritance</li>
                    <li>Supports polymorphism</li>
                    <li>Better modularity</li>
                </ul>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages of OOP</h4>
                <ul style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li>More complex</li>
                    <li>Requires more planning</li>
                    <li>May use additional memory</li>
                    <li>Can have performance overhead</li>
                    <li>Not always necessary for simple programs</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 5. FEATURES OF OOP PARADIGM -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">5. FEATURES OF OBJECT-ORIENTED PARADIGM</h2>
        
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            The <strong>Object-Oriented Paradigm</strong> is a programming approach that organizes software around objects rather than only functions.
        </p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin: 20px 0;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">1. Objects</h4>
                <p style="color: #475569; font-size: 0.95rem; margin-bottom: 5px;">Objects represent entities.</p>
                <code>Student s1;</code>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">2. Classes</h4>
                <p style="color: #475569; font-size: 0.95rem; margin-bottom: 5px;">Classes define structure & behavior.</p>
                <code>class Student { };</code>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">3. Encapsulation</h4>
                <p style="color: #475569; font-size: 0.95rem; margin: 0;">Combining data and functions into one class.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">4. Abstraction</h4>
                <p style="color: #475569; font-size: 0.95rem; margin: 0;">Showing essential information and hiding implementation details.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">5. Inheritance</h4>
                <p style="color: #475569; font-size: 0.95rem; margin-bottom: 5px;">Creating a new class from an existing class.</p>
                <code>class Dog : public Animal { };</code>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">6. Polymorphism</h4>
                <p style="color: #475569; font-size: 0.95rem; margin: 0;">Allowing the same interface/name to behave differently.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">7. Data Hiding</h4>
                <p style="color: #475569; font-size: 0.95rem; margin: 0;">Protecting internal data using access control.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">8. Message Passing</h4>
                <p style="color: #475569; font-size: 0.95rem; margin-bottom: 5px;">Objects communicate through method calls.</p>
                <code>student.display();</code>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">9. Dynamic Binding</h4>
                <p style="color: #475569; font-size: 0.95rem; margin: 0;">The method to execute can be determined at runtime.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">10. Reusability</h4>
                <p style="color: #475569; font-size: 0.95rem; margin: 0;">Existing code can be reused in new programs.</p>
            </div>
        </div>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            A <strong>University Management System</strong> can contain:
        </p>
        <div class="mermaid" style="text-align: center; margin: 15px 0;">
graph TD
    U["<b>University</b>"] --> S["Student"]
    U --> T["Teacher"]
    U --> C["Course"]
    U --> D["Department"]
    U --> E["Examination"]
        </div>
        <p style="font-size: 1rem; color: #475569;">Each object has its own properties and behavior.</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li>Modularity</li>
                    <li>Reusability</li>
                    <li>Security</li>
                    <li>Maintainability</li>
                    <li>Flexibility</li>
                    <li>Real-world representation</li>
                    <li>Reduced duplication</li>
                    <li>Easier extension</li>
                </ul>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li>More complex than simple procedural programs</li>
                    <li>Requires proper design</li>
                    <li>May require more memory</li>
                    <li>Development can take longer</li>
                    <li>Some mechanisms introduce overhead</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 6. MERITS AND DEMERITS OF OO METHODOLOGY -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">6. MERITS AND DEMERITS OF OBJECT-ORIENTED METHODOLOGY</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>Object-oriented methodology</strong> is a systematic approach to software development where systems are analyzed, designed, and implemented using objects and their relationships.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin: 20px 0;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Merits</h4>
                <ol style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li><strong>Modularity:</strong> The system can be divided into classes and objects.</li>
                    <li><strong>Reusability:</strong> Existing classes can be reused.</li>
                    <li><strong>Data Security:</strong> Data hiding protects internal information.</li>
                    <li><strong>Easy Maintenance:</strong> Changes can often be made within individual classes.</li>
                    <li><strong>Extensibility:</strong> New features can be added using inheritance and polymorphism.</li>
                    <li><strong>Real-world modeling:</strong> Real-world entities can be represented naturally.</li>
                    <li><strong>Reduced duplication:</strong> Reusable classes reduce repeated code.</li>
                    <li><strong>Better scalability:</strong> OOP is suitable for large software systems.</li>
                </ol>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Demerits</h4>
                <ol style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li><strong>Complexity:</strong> The concepts can be difficult initially.</li>
                    <li><strong>More development time:</strong> Designing classes requires planning.</li>
                    <li><strong>Memory usage:</strong> Objects can require additional memory.</li>
                    <li><strong>Performance:</strong> Some OOP mechanisms introduce overhead.</li>
                    <li><strong>Poor design can cause problems:</strong> Incorrect relationships between classes can make the program complicated.</li>
                </ol>
            </div>
        </div>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example (E-commerce Application)</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            Objects might be: <strong>Customer, Product, Cart, Order, Payment, Delivery</strong>. Each class handles its own responsibility. If we want to add a new payment method, we can extend the payment system without rewriting the entire application. This demonstrates the <em>maintainability</em> and <em>extensibility</em> advantages of OOP.
        </p>
    </div>

    <!-- 7. OBJECT MODEL -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">7. OBJECT MODEL</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            An <strong>Object Model</strong> is a conceptual model that represents a software system as a collection of objects, classes, attributes, operations, and relationships. It describes how objects are structured and how they interact with one another. An object model helps developers understand the structure of a system before implementation.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">Main Elements of Object Model</h3>
        <ol style="color: #334155; line-height: 1.8; font-size: 1rem; margin-left: 20px;">
            <li><strong>Object:</strong> Represents an entity.</li>
            <li><strong>Class:</strong> Defines a group/type of similar objects.</li>
            <li><strong>Attributes:</strong> Represent object data.</li>
            <li><strong>Operations:</strong> Represent object behavior.</li>
            <li><strong>Relationships:</strong> Represent connections between objects.</li>
        </ol>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example (Library Management System)</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>Objects:</strong> Student, Book, Librarian, Library, Issue, Return.<br/>
            A <strong>Book</strong> may have attributes (<em>Book ID, Title, Author, Price, Availability</em>) and operations (<em>issue(), returnBook(), displayDetails()</em>).<br/>
            <strong>Relationship:</strong> <code>Student ---- borrows ----&gt; Book</code>
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">C++ Representation</h3>
        <pre><code class="language-cpp">class Book
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
};</code></pre>
        <p style="font-size: 1rem; color: #475569;">This class represents the object model of a book.</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li>Helps understand system structure</li>
                    <li>Makes design easier</li>
                    <li>Helps identify relationships</li>
                    <li>Supports modular development</li>
                    <li>Makes complex systems easier to visualize</li>
                    <li>Helps before actual implementation</li>
                </ul>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li>Designing a detailed object model takes time</li>
                    <li>Poor modeling can lead to poor implementation</li>
                    <li>Large systems can have complicated object relationships</li>
                    <li>Requires knowledge of object-oriented design</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 8. ELEMENTS OF OOPS -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">8. ELEMENTS OF OOPS</h2>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            The major elements of Object-Oriented Programming are:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; margin: 15px 0;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 6px;"><strong>1. Class:</strong> A blueprint for objects. (<code>class Student { };</code>)</div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 6px;"><strong>2. Object:</strong> An instance of a class. (<code>Student s1;</code>)</div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 6px;"><strong>3. Encapsulation:</strong> Binding data and methods together.</div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 6px;"><strong>4. Abstraction:</strong> Hiding unnecessary implementation details.</div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 6px;"><strong>5. Inheritance:</strong> Acquiring properties and behavior from another class.</div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 6px;"><strong>6. Polymorphism:</strong> One interface with multiple forms.</div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 6px;"><strong>7. Data Hiding:</strong> Restricting direct access to internal data.</div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 6px;"><strong>8. Message Passing:</strong> Communication between objects. (<code>s1.display();</code>)</div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 6px;"><strong>9. Dynamic Binding:</strong> Selecting the appropriate method during runtime.</div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 6px;"><strong>10. Reusability:</strong> Using existing code again.</div>
        </div>
    </div>

    <!-- 9. CLASS -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">9. CLASS</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            A <strong>class</strong> is a user-defined data type and a blueprint or template for creating objects.
            A class can contain: <em>Data members, Member functions, Constructors, Destructors, Access specifiers</em>.
        </p>

        <pre><code class="language-cpp">class Student
{
private:
    string name;
    int age;

public:
    void display()
    {
        cout &lt;&lt; name &lt;&lt; " " &lt;&lt; age;
    }
};</code></pre>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            Think of a class as a <strong>blueprint of a house</strong>. The blueprint specifies: <em>Number of rooms, Doors, Windows, Kitchen, Bathroom</em>. But the blueprint itself is not an actual house.
        </p>
        <p style="font-size: 1rem; color: #334155;">
            Similarly: <code>Class &rarr; Blueprint</code> and <code>Object &rarr; Actual entity</code>. One class can create many objects:
        </p>
        <pre><code class="language-cpp">Student s1;
Student s2;
Student s3;</code></pre>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li>Provides structure</li>
                    <li>Supports encapsulation</li>
                    <li>Allows multiple objects</li>
                    <li>Supports reusability</li>
                    <li>Makes programs organized</li>
                    <li>Makes maintenance easier</li>
                </ul>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li>Requires additional design</li>
                    <li>Can be unnecessary for very small programs</li>
                    <li>Large class hierarchies can become complicated</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 10. OBJECT -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">10. OBJECT</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            An <strong>object</strong> is an instance of a class. An object represents a specific entity and contains its own state while using the behavior defined by its class.
        </p>
        <code>Student s1; // Student -&gt; Class, s1 -&gt; Object</code>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            Consider a class <code>Car</code>. Actual cars are objects: <em>Car 1 &rarr; Black BMW, Car 2 &rarr; White BMW, Car 3 &rarr; Red BMW</em>. All belong to the same general category but have different states.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">C++ Example</h3>
        <pre><code class="language-cpp">class Student
{
public:
    string name;
    int age;

    void display()
    {
        cout &lt;&lt; name &lt;&lt; " " &lt;&lt; age;
    }
};

int main()
{
    Student s1;

    s1.name = "Ravi";
    s1.age = 20;

    s1.display();

    return 0;
}</code></pre>
        <p style="font-size: 1rem; color: #475569;">Here <code>s1</code> is an object.</p>

        <h3 style="color: #1e40af; margin-top: 20px;">Characteristics of Objects</h3>
        <ul style="color: #334155; line-height: 1.8; font-size: 1rem; margin-left: 20px;">
            <li><strong>State:</strong> Data stored in the object.</li>
            <li><strong>Behavior:</strong> Operations performed by the object.</li>
            <li><strong>Identity:</strong> Unique existence of the object.</li>
        </ul>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li>Represents real-world entities</li>
                    <li>Supports modularity</li>
                    <li>Makes programs easier to understand</li>
                    <li>Provides object-level organization</li>
                    <li>Allows multiple instances</li>
                </ul>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li>Large numbers of objects may consume memory</li>
                    <li>Object interactions can become complex</li>
                    <li>Requires proper class design</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 11. ENCAPSULATION -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">11. ENCAPSULATION</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>Encapsulation</strong> is the process of combining data and the functions that operate on that data into a single unit called a class. It also commonly involves controlling access to the internal state of an object.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            Consider an <strong>ATM</strong>. The user interacts with: <em>Withdraw, Deposit, Check Balance</em>. The internal banking process is not directly accessible. The ATM encapsulates the internal operations.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">C++ Example</h3>
        <pre><code class="language-cpp">class BankAccount
{
private:
    double balance;

public:
    void deposit(double amount)
    {
        if (amount &gt; 0)
            balance += amount;
    }

    double getBalance()
    {
        return balance;
    }
};</code></pre>
        <p style="font-size: 1rem; color: #475569;">
            Here, Data (<code>balance</code>) and Functions (<code>deposit()</code>, <code>getBalance()</code>) are inside the same class. Access can be controlled using: <code>private</code>, <code>protected</code>, <code>public</code>.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ol style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li><strong>Data protection:</strong> Internal data can be protected.</li>
                    <li><strong>Modularity:</strong> Data and behavior stay together.</li>
                    <li><strong>Maintenance:</strong> Internal implementation can be changed without changing how users interact with the class.</li>
                    <li><strong>Control:</strong> Access can be controlled using private/protected/public.</li>
                </ol>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li>May increase code complexity</li>
                    <li>Requires proper access design</li>
                    <li>Excessive encapsulation can sometimes make simple code unnecessarily complicated</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 12. ABSTRACTION -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">12. ABSTRACTION</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>Abstraction</strong> is the process of representing only the essential features of an object while hiding unnecessary implementation details. The user focuses on <em>what</em> an object does, rather than <em>how</em> it does it internally.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            When using a <strong>mobile phone</strong>, you can: <em>Call, Message, Take Photo, Play Music</em>. You don't need to understand the internal electronic circuits and software algorithms to use these functions. That is abstraction.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">C++ Example</h3>
        <pre><code class="language-cpp">class ATM
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
        // Internal implementation
    }

    void checkBalance()
    {
        // Internal implementation
    }

    void processTransaction()
    {
        // Internal implementation
    }

    void dispenseCash()
    {
        // Internal implementation
    }
};</code></pre>
        <p style="font-size: 1rem; color: #475569;">
            The user only needs: <code>atm.withdraw(500);</code>. The complex implementation remains hidden.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li>Reduces complexity</li>
                    <li>Improves usability</li>
                    <li>Protects implementation details</li>
                    <li>Makes software easier to understand</li>
                    <li>Improves maintainability</li>
                </ul>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li>Designing abstraction properly can be difficult</li>
                    <li>Too much abstraction can make debugging harder</li>
                    <li>Requires additional design effort</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 13. INHERITANCE -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">13. INHERITANCE</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>Inheritance</strong> is an OOP mechanism in which a new class acquires the properties and behaviors of an existing class.
            The existing class is called the <strong>Base / Parent / Super Class</strong>. The new class is called the <strong>Derived / Child / Sub Class</strong>.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example</h3>
        <div class="mermaid" style="text-align: center; margin: 15px 0;">
graph TD
    V["<b>Vehicle</b><br/>start(), stop(), speed"] --> C["Car"]
    V --> B["Bus"]
    V --> T["Truck"]
        </div>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            All vehicles have common features: <code>start()</code>, <code>stop()</code>, <code>speed</code>. Instead of writing these features separately for every class, they can be placed in <code>Vehicle</code>.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">C++ Example</h3>
        <pre><code class="language-cpp">#include &lt;iostream&gt;
using namespace std;

class Vehicle
{
public:
    void start()
    {
        cout &lt;&lt; "Vehicle started" &lt;&lt; endl;
    }
};

class Car : public Vehicle
{
public:
    void drive()
    {
        cout &lt;&lt; "Car is driving" &lt;&lt; endl;
    }
};

int main()
{
    Car c;

    c.start();
    c.drive();

    return 0;
}</code></pre>
        <p style="font-size: 1rem; color: #475569;"><code>Car</code> inherits <code>start()</code> from <code>Vehicle</code>.</p>

        <h3 style="color: #1e40af; margin-top: 20px;">Types of Inheritance</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; margin: 15px 0;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">1. Single</h4>
                <p style="font-size: 0.9rem; color: #475569;">One derived class inherits from one base class (A &rarr; B).</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">2. Multiple</h4>
                <p style="font-size: 0.9rem; color: #475569;">One class inherits from multiple base classes (A, B &rarr; C).</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">3. Multilevel</h4>
                <p style="font-size: 0.9rem; color: #475569;">Inheritance occurs in multiple levels (A &rarr; B &rarr; C).</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">4. Hierarchical</h4>
                <p style="font-size: 0.9rem; color: #475569;">Multiple classes inherit from one base class (A &rarr; B, C, D).</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 12px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">5. Hybrid</h4>
                <p style="font-size: 0.9rem; color: #475569;">Combination of two or more types of inheritance.</p>
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li>Code reuse</li>
                    <li>Reduces duplication</li>
                    <li>Easy extension</li>
                    <li>Supports hierarchical classification</li>
                    <li>Easier maintenance</li>
                </ul>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li>Creates dependency between classes</li>
                    <li>Deep inheritance can become complicated</li>
                    <li>Changes in base classes may affect derived classes</li>
                    <li>Multiple inheritance can create ambiguity</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 14. POLYMORPHISM -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">14. POLYMORPHISM</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>Polymorphism</strong> means "many forms." In OOP, polymorphism allows the same function, interface, or operation to behave differently depending on the context.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">Types of Polymorphism</h3>
        
        <h4 style="color: #1e40af;">1. Compile-Time Polymorphism</h4>
        <p style="font-size: 1rem; color: #334155;">The decision is made during compilation. Common techniques: <em>Function overloading, Operator overloading</em>.</p>
        <pre><code class="language-cpp">class Calculator
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
};</code></pre>

        <h4 style="color: #1e40af; margin-top: 15px;">2. Run-Time Polymorphism</h4>
        <p style="font-size: 1rem; color: #334155;">The decision is made during program execution. Commonly achieved using: <em>Function overriding, Virtual functions</em>.</p>
        <pre><code class="language-cpp">class Animal
{
public:
    virtual void sound()
    {
        cout &lt;&lt; "Animal sound";
    }
};

class Dog : public Animal
{
public:
    void sound() override
    {
        cout &lt;&lt; "Dog barks";
    }
};</code></pre>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            A person may use a single word: <strong>"Pay"</strong>. But payment can happen through: <em>Cash, Card, UPI, Net Banking</em>. The operation is conceptually the same, but implementation differs.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li>Flexibility</li>
                    <li>Code reuse</li>
                    <li>Extensibility</li>
                    <li>Supports loose coupling</li>
                    <li>Makes programs easier to expand</li>
                </ul>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li>Can make programs more difficult to understand</li>
                    <li>Runtime polymorphism can introduce overhead</li>
                    <li>Requires proper class design</li>
                    <li>Debugging can sometimes be more difficult</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 15. MESSAGE PASSING -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">15. MESSAGE PASSING</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>Message Passing</strong> is a mechanism through which objects communicate with one another by sending requests or calling methods. In OOP, an object may request another object to perform a particular operation.
        </p>
        <code>student.display(); // student receives request to execute display()</code>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example (Restaurant)</h3>
        <div class="mermaid" style="text-align: center; margin: 15px 0;">
graph LR
    C["Customer"] -- "Order food" --> W["Waiter"]
    W -- "Request" --> K["Kitchen"]
        </div>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            The customer does not directly prepare the food. A request is passed through another entity. Similarly, objects communicate by sending requests.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">C++ Example</h3>
        <pre><code class="language-cpp">class Printer
{
public:
    void print()
    {
        cout &lt;&lt; "Printing document";
    }
};

class Computer
{
public:
    void sendToPrinter(Printer &p)
    {
        p.print();
    }
};</code></pre>
        <p style="font-size: 1rem; color: #475569;">The <code>Computer</code> object sends a request to the <code>Printer</code> object.</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li>Supports object communication</li>
                    <li>Improves modularity</li>
                    <li>Reduces direct dependency</li>
                    <li>Supports distributed systems</li>
                    <li>Makes responsibilities clear</li>
                </ul>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li>Too many messages can make a system complex</li>
                    <li>Communication overhead may occur</li>
                    <li>Incorrect object relationships can cause design problems</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 16. DYNAMIC BINDING -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">16. DYNAMIC BINDING</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>Dynamic Binding</strong> is the process in which the method to be executed is determined at runtime rather than at compile time. It is strongly associated with runtime polymorphism.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">Real-World Example</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            Suppose you have a <strong>universal remote control</strong>. You press: <em>Power</em>. The actual action depends on the device: <em>TV &rarr; TV turns on, AC &rarr; AC turns on, Projector &rarr; Projector turns on</em>. The same operation produces different behavior depending on the actual object.
        </p>

        <h3 style="color: #1e40af; margin-top: 20px;">C++ Example</h3>
        <pre><code class="language-cpp">#include &lt;iostream&gt;
using namespace std;

class Animal
{
public:
    virtual void sound()
    {
        cout &lt;&lt; "Animal sound" &lt;&lt; endl;
    }
};

class Dog : public Animal
{
public:
    void sound() override
    {
        cout &lt;&lt; "Dog barks" &lt;&lt; endl;
    }
};

class Cat : public Animal
{
public:
    void sound() override
    {
        cout &lt;&lt; "Cat meows" &lt;&lt; endl;
    }
};

int main()
{
    Animal *a;

    Dog d;
    Cat c;

    a = &d;
    a-&gt;sound();

    a = &c;
    a-&gt;sound();

    return 0;
}</code></pre>
        <div style="background: #1e293b; color: #38bdf8; padding: 12px; border-radius: 6px; margin-top: 10px; font-family: monospace;">
            <strong>Output:</strong><br/>
            Dog barks<br/>
            Cat meows
        </div>
        <p style="font-size: 1rem; color: #475569; margin-top: 8px;">The method selected depends on the actual object at runtime.</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li>Supports runtime polymorphism</li>
                    <li>Provides flexibility</li>
                    <li>Makes systems extensible</li>
                    <li>Reduces dependency on specific implementations</li>
                </ul>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li>Can introduce runtime overhead</li>
                    <li>Debugging can be harder</li>
                    <li>Requires proper inheritance and virtual function design</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 17. I/O PROCESSING -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">17. I/O PROCESSING</h2>
        
        <h3 style="color: #1e40af; margin-top: 15px;">Definition</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>I/O Processing</strong> means Input/Output Processing. It refers to the process through which a program receives data from external sources, processes that data, and produces results for external devices or destinations.
        </p>

        <div class="mermaid" style="text-align: center; margin: 15px 0;">
graph LR
    I["<b>INPUT</b><br/>Keyboard, File, Network"] --> P["<b>PROCESSING</b><br/>CPU / Logic"] --> O["<b>OUTPUT</b><br/>Monitor, Printer, File"]
        </div>

        <h3 style="color: #1e40af; margin-top: 20px;">C++ I/O (<iostream>)</h3>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            C++ provides console I/O through the <code>&lt;iostream&gt;</code> library. The two most commonly used objects are:
        </p>
        <ul style="color: #334155; line-height: 1.8; font-size: 1rem; margin-left: 20px;">
            <li><code>cin</code> &rarr; Standard Input (reads from keyboard)</li>
            <li><code>cout</code> &rarr; Standard Output (displays on screen)</li>
        </ul>

        <h3 style="color: #1e40af; margin-top: 20px;">Example</h3>
        <pre><code class="language-cpp">#include &lt;iostream&gt;
using namespace std;

int main()
{
    int a, b;

    cout &lt;&lt; "Enter two numbers: ";
    cin &gt;&gt; a &gt;&gt; b;

    cout &lt;&lt; "Sum = " &lt;&lt; a + b;

    return 0;
}</code></pre>
        <div style="background: #1e293b; color: #38bdf8; padding: 12px; border-radius: 6px; margin-top: 10px; font-family: monospace;">
            <strong>Input:</strong> 10 20<br/>
            <strong>Output:</strong> Sum = 30
        </div>

        <h3 style="color: #1e40af; margin-top: 20px;">I/O Operators</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin: 15px 0;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">Extraction Operator <code>&gt;&gt;</code></h4>
                <p style="color: #475569; font-size: 0.95rem; margin-bottom: 5px;">Used with <code>cin</code>.</p>
                <code>cin &gt;&gt; a;</code>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">Insertion Operator <code>&lt;&lt;</code></h4>
                <p style="color: #475569; font-size: 0.95rem; margin-bottom: 5px;">Used with <code>cout</code>.</p>
                <code>cout &lt;&lt; a;</code>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;"><code>getline()</code></h4>
                <p style="color: #475569; font-size: 0.95rem; margin-bottom: 5px;">Reads complete line including spaces.</p>
                <code>string name;<br/>getline(cin, name);</code>
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 15px; border-radius: 8px;">
                <h4 style="color: #166534; margin-top: 0;">Advantages of I/O Processing</h4>
                <ul style="margin: 0; padding-left: 20px; color: #15803d; line-height: 1.6;">
                    <li>Allows interaction with users</li>
                    <li>Allows programs to receive data</li>
                    <li>Allows results to be displayed</li>
                    <li>Supports file and device communication</li>
                    <li>Essential for interactive applications</li>
                </ul>
            </div>
            <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 8px;">
                <h4 style="color: #991b1b; margin-top: 0;">Disadvantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #b91c1c; line-height: 1.6;">
                    <li>Input errors can cause incorrect results</li>
                    <li>I/O operations can be slower than memory operations</li>
                    <li>Improper input handling can cause program errors</li>
                    <li>Large amounts of I/O can affect performance</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- IMPORTANT EXAM RECAP: FOUR PILLARS & CORE DIFFERENCE -->
    <div class="concept-section" style="background: #eff6ff; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 2px solid #3b82f6;">
        <h2 style="color: #1e3a8a; border-bottom: 2px solid #bfdbfe; padding-bottom: 8px;">IMPORTANT: FOUR PILLARS OF OOP</h2>
        <p style="font-size: 1.1rem; font-weight: bold; color: #1e40af;">These are extremely important for exams. Remember: E-A-I-P</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; margin: 15px 0;">
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 5px solid #2563eb;">
                <h4 style="color: #1e40af; margin-top: 0;">1. Encapsulation (E)</h4>
                <p style="color: #334155; font-size: 0.95rem; margin: 0;">Binding data and methods together into a single unit.</p>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 5px solid #2563eb;">
                <h4 style="color: #1e40af; margin-top: 0;">2. Abstraction (A)</h4>
                <p style="color: #334155; font-size: 0.95rem; margin: 0;">Showing essential features and hiding implementation details.</p>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 5px solid #2563eb;">
                <h4 style="color: #1e40af; margin-top: 0;">3. Inheritance (I)</h4>
                <p style="color: #334155; font-size: 0.95rem; margin: 0;">Acquiring properties and behaviors from an existing class.</p>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 5px solid #2563eb;">
                <h4 style="color: #1e40af; margin-top: 0;">4. Polymorphism (P)</h4>
                <p style="color: #334155; font-size: 0.95rem; margin: 0;">One interface/name having multiple forms.</p>
            </div>
        </div>

        <h3 style="color: #1e40af; margin-top: 25px;">MOST IMPORTANT DIFFERENCE</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 15px;">
            <div style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #cbd5e1;">
                <h4 style="color: #dc2626; margin-top: 0;">PROCEDURAL PROGRAMMING</h4>
                <p style="color: #475569; font-size: 0.95rem;">Problem &rarr; Functions &rarr; Operations &rarr; Data</p>
                <p style="color: #1e293b; font-weight: bold; margin-bottom: 0;">Focus &rarr; "What steps should be performed?"</p>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #cbd5e1;">
                <h4 style="color: #16a34a; margin-top: 0;">OBJECT-ORIENTED PROGRAMMING</h4>
                <p style="color: #475569; font-size: 0.95rem;">Problem &rarr; Objects &rarr; Classes &rarr; Data + Behavior &rarr; Interaction</p>
                <p style="color: #1e293b; font-weight: bold; margin-bottom: 0;">Focus &rarr; "What objects are involved and how do they interact?"</p>
            </div>
        </div>
    </div>
</div>
"""
            }
        ]
    },
    # =========================================================================
    # PART I: FOUNDATIONS OF OBJECT-ORIENTED PROGRAMMING (Chapters 1 - 4)
    # =========================================================================
    {
        "unit": "Part I: Foundations of OOP",
        "title": "Foundations & Core Class Architecture",
        "topics": [
            {
                "slug": "chapter-1-introduction-to-oop",
                "title": "Chapter 1: Introduction to Object-Oriented Programming",
                "subtopics": [
                    "1. Evolution of Programming Languages (Machine -> Assembly -> Procedural -> OOP)",
                    "2. The Crisis of Large Procedural Programs (Spaghetti Code & Global State)",
                    "3. History of Simula, Smalltalk, and Bjarne Stroustrup's C with Classes",
                    "4. Procedural Programming vs. Object-Oriented Programming",
                    "5. Core Principles, Benefits, and Limitations of OOP"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🌟 Chapter 1: Introduction to Object-Oriented Programming</h1>
        <p style="font-size: 1.15rem; margin: 0;">History, Evolution, The Procedural Crisis, and Paradigm Comparison</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a;">1. Evolution of Programming Languages</h2>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            To understand why Object-Oriented Programming (OOP) exists, we must trace how programming paradigms evolved over decades to manage rising software complexity:
        </p>

        <div class="mermaid" style="text-align: center; margin: 20px 0;">
graph LR
    ML["<b>1. Machine Language (1940s)</b><br/>Raw Binary (0s & 1s)"] --> AL["<b>2. Assembly Language (1950s)</b><br/>Mnemonics (MOV, ADD)"]
    AL --> PL["<b>3. Procedural Language (1960s)</b><br/>Functions & Routines (C, Pascal)"]
    PL --> OOP["<b>4. Object-Oriented (1980s+)</b><br/>Encapsulated Objects (C++, Java)"]
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px; margin: 20px 0;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">1. Machine Language</h4>
                <p style="color: #475569; font-size: 0.95rem; margin: 0;">Written purely in binary bits (0s and 1s). Fast for hardware, but nearly impossible for humans to write, debug, or maintain.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">2. Assembly Language</h4>
                <p style="color: #475569; font-size: 0.95rem; margin: 0;">Introduced human-readable mnemonics (<code>ADD</code>, <code>MOV</code>, <code>JMP</code>). Still tied to specific CPU registers and hardware architectures.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 15px; border-radius: 8px;">
                <h4 style="color: #1e40af; margin-top: 0;">3. Procedural / Structured</h4>
                <p style="color: #475569; font-size: 0.95rem; margin: 0;">Introduced functions, loops, and modules (C, Pascal). However, data moved freely across global variables, leading to security and scale bottlenecks.</p>
            </div>
        </div>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a;">2. Why Large Procedural Programs Failed (The Crisis)</h2>
        <ul style="color: #334155; line-height: 1.8; font-size: 1rem; margin-left: 20px;">
            <li><strong>Global Data Vulnerability:</strong> In procedural code, data is open and accessible to all functions. A single unintended modification in one function corrupts the state across the entire application.</li>
            <li><strong>Top-Down Spaghetti Flow:</strong> Adding new features requires altering dozens of existing routines, causing unexpected cascading bugs.</li>
            <li><strong>No Natural Real-World Mapping:</strong> Procedural code models operations (verbs), whereas real-world problems consist of entities (nouns) with state and behavior.</li>
        </ul>

        <div style="background: #eff6ff; padding: 15px; border-radius: 8px; border-left: 5px solid #2563eb; margin: 15px 0;">
            <strong>📜 History of C++:</strong> In 1979, <strong>Bjarne Stroustrup</strong> at Bell Labs created <em>"C with Classes"</em> by combining the speed and system efficiency of <strong>C</strong> with the object-oriented abstractions of <strong>Simula67</strong>. In 1983, it was officially renamed to <strong>C++</strong> (the <code>++</code> indicating an increment/evolution of C).
        </div>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a;">3. Procedural Programming vs. Object-Oriented Programming</h2>
        <table style="width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 1rem;">
            <thead>
                <tr style="background: #1e3a8a; color: white;">
                    <th style="padding: 12px; border: 1px solid #cbd5e1;">Comparison Parameter</th>
                    <th style="padding: 12px; border: 1px solid #cbd5e1; width: 40%;">Procedural Programming (e.g. C)</th>
                    <th style="padding: 12px; border: 1px solid #cbd5e1; width: 40%;">Object-Oriented Programming (e.g. C++)</th>
                </tr>
            </thead>
            <tbody>
                <tr style="background: #f8fafc;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">Design Approach</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">Top-Down Approach</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1; color: #16a34a; font-weight: bold;">Bottom-Up Approach</td>
                </tr>
                <tr style="background: #ffffff;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">Primary Focus</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">Functions & Step-by-Step Logic</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">Data Security & Encapsulation</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">Data Security</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1; color: #dc2626;">Low (Data moves freely)</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1; color: #16a34a; font-weight: bold;">High (Access Specifiers protect data)</td>
                </tr>
                <tr style="background: #ffffff;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">Code Reusability</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">Limited to function calls</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">High via Inheritance & Polymorphism</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
"""
            },
            {
                "slug": "chapter-2-classes-and-objects",
                "title": "Chapter 2: Classes and Objects Architecture",
                "subtopics": [
                    "1. Definition of Class and Object",
                    "2. Memory Allocation of Objects (Stack vs. Heap)",
                    "3. Arrays of Objects and Nested Classes",
                    "4. Passing and Returning Objects (By Value, Reference, Pointer)",
                    "5. Complete C++ Code Example & Output"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🏛️ Chapter 2: Classes and Objects Architecture</h1>
        <p style="font-size: 1.15rem; margin: 0;">Blueprint Declarations, Memory Layouts, Arrays of Objects, and Function Transfers</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a;">1. What is a Class and an Object?</h2>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            • <strong>Class:</strong> An abstract user-defined blueprint that binds member variables (data) and member functions together. It occupies 0 bytes until instantiated.
            <br>• <strong>Object:</strong> A physical instance of a class allocated in memory.
        </p>

        <h4 style="color: #1e3a8a; margin-top: 20px;">💻 C++ Implementation: Class, Array of Objects & Method Calls</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

class Student {
private:
    int rollNo;
    string name;
    float marks;

public:
    // Parameterized Setter Method
    void setDetails(int r, string n, float m) {
        rollNo = r;
        name = n;
        marks = m;
    }

    // Display Method
    void display() const {
        cout &lt;&lt; "Roll No: " &lt;&lt; rollNo &lt;&lt; " | Name: " &lt;&lt; name &lt;&lt; " | Marks: " &lt;&lt; marks &lt;&lt; "%\n";
    }
};

int main() {
    // Array of Objects
    Student batch[2];
    batch[0].setDetails(101, "Ravi Kumar", 94.5);
    batch[1].setDetails(102, "Aman Verma", 89.0);

    cout &lt;&lt; "--- Student Batch Records ---\n";
    for(int i = 0; i &lt; 2; i++) {
        batch[i].display();
    }

    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            --- Student Batch Records ---<br>
            Roll No: 101 | Name: Ravi Kumar | Marks: 94.5%<br>
            Roll No: 102 | Name: Aman Verma | Marks: 89%
        </div>
    </div>
</div>
"""
            },
            {
                "slug": "chapter-3-access-specifiers",
                "title": "Chapter 3: Access Specifiers & Data Security",
                "subtopics": [
                    "1. Why Data Protection is Necessary",
                    "2. Public, Private, and Protected Explained",
                    "3. Access Table through Inheritance",
                    "4. Struct vs. Class Default Access Rules"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🔒 Chapter 3: Access Specifiers & Data Protection</h1>
        <p style="font-size: 1.15rem; margin: 0;">Public, Private, Protected and Inheritance Access Matrix</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a;">1. The 3 Access Specifiers in C++</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 15px; margin: 20px 0;">
            <div style="background: #f8fafc; border-left: 5px solid #ef4444; padding: 16px; border-radius: 8px;">
                <h4 style="color: #dc2626; margin: 0 0 6px 0;">1. private (Default in Class)</h4>
                <p style="color: #475569; font-size: 0.95rem; margin: 0;">Accessible <strong>ONLY</strong> within the same class member functions and declared friend functions.</p>
            </div>
            <div style="background: #f8fafc; border-left: 5px solid #f59e0b; padding: 16px; border-radius: 8px;">
                <h4 style="color: #d97706; margin: 0 0 6px 0;">2. protected</h4>
                <p style="color: #475569; font-size: 0.95rem; margin: 0;">Accessible within the same class <strong>AND</strong> its derived (child) classes. Hidden from outside users.</p>
            </div>
            <div style="background: #f8fafc; border-left: 5px solid #10b981; padding: 16px; border-radius: 8px;">
                <h4 style="color: #059669; margin: 0 0 6px 0;">3. public (Default in Struct)</h4>
                <p style="color: #475569; font-size: 0.95rem; margin: 0;">Accessible openly by any function or object across the entire program.</p>
            </div>
        </div>

        <h3 style="color: #1e3a8a; margin-top: 25px;">2. Access Specifier Inheritance Matrix</h3>
        <table style="width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 1rem;">
            <thead>
                <tr style="background: #1e3a8a; color: white;">
                    <th style="padding: 12px; border: 1px solid #cbd5e1;">Base Class Member</th>
                    <th style="padding: 12px; border: 1px solid #cbd5e1;">public Inheritance</th>
                    <th style="padding: 12px; border: 1px solid #cbd5e1;">protected Inheritance</th>
                    <th style="padding: 12px; border: 1px solid #cbd5e1;">private Inheritance</th>
                </tr>
            </thead>
            <tbody>
                <tr style="background: #f8fafc;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">public</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1; color: #16a34a; font-weight: bold;">public</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">protected</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1; color: #dc2626;">private</td>
                </tr>
                <tr style="background: #ffffff;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">protected</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">protected</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">protected</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1; color: #dc2626;">private</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">private</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1; color: #94a3b8;">Inaccessible</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1; color: #94a3b8;">Inaccessible</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1; color: #94a3b8;">Inaccessible</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
"""
            },
            {
                "slug": "chapter-4-member-functions-scope",
                "title": "Chapter 4: Member Functions & Scope Resolution",
                "subtopics": [
                    "1. Declaring vs. Defining Member Functions",
                    "2. Scope Resolution Operator (::) 5 Use Cases",
                    "3. Inline Functions & Compiler Rejection Rules",
                    "4. Const Member Functions & Static Functions"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">⚡ Chapter 4: Member Functions & Scope Rules</h1>
        <p style="font-size: 1.15rem; margin: 0;">Scope Resolution Operator (::), Inline Mechanics, and Const Methods</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a;">1. The Scope Resolution Operator (::)</h2>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            The <code>::</code> operator resolves ambiguities and determines which namespace or class scope an identifier belongs to.
        </p>

        <h4 style="color: #1e3a8a;">💻 C++ Implementation: External Definition & Scope Resolution</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

int globalCount = 100; // Global Variable

class Calculator {
public:
    // Defined inside class (Implicitly inline)
    int add(int a, int b) { return a + b; }

    // Declared inside class, defined outside via ::
    int multiply(int a, int b);
};

// Defining function outside using Scope Resolution Operator
int Calculator::multiply(int a, int b) {
    return a * b;
}

int main() {
    int globalCount = 10; // Local Variable shadows global

    cout &lt;&lt; "Local Count: " &lt;&lt; globalCount &lt;&lt; endl;
    cout &lt;&lt; "Global Count (via ::): " &lt;&lt; ::globalCount &lt;&lt; endl;

    Calculator calc;
    cout &lt;&lt; "Multiplication Result: " &lt;&lt; calc.multiply(6, 7) &lt;&lt; endl;

    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            Local Count: 10<br>
            Global Count (via ::): 100<br>
            Multiplication Result: 42
        </div>
    </div>
</div>
"""
            }
        ]
    },

    # =========================================================================
    # PART II: OBJECT LIFECYCLE (Chapters 5 - 6)
    # =========================================================================
    {
        "unit": "Part II: Object Lifecycle",
        "title": "Constructors, Destructors & RAII",
        "topics": [
            {
                "slug": "chapter-5-constructors-mastery",
                "title": "Chapter 5: Constructors in Depth",
                "subtopics": [
                    "1. Why Constructors are Needed (Car Color Analogy)",
                    "2. Default, Parameterized, Copy, and Explicit Constructors",
                    "3. Constructor Member Initializer Lists (MIL)",
                    "4. Delegating Constructors & Constructor Chaining",
                    "5. Execution Order with Inheritance"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #065f46 0%, #10b981 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">⚙️ Chapter 5: Complete Constructors Mastery</h1>
        <p style="font-size: 1.15rem; margin: 0;">Initialization Lists, Delegating Constructors, Deep Copies, and Chaining</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #065f46;">1. The Philosophy of Constructors</h2>
        <div class="analogy-box" style="background: #fefce8; border: 2px solid #ca8a04; border-radius: 8px; padding: 18px; margin: 15px 0;">
            <strong style="color: #854d0e; font-size: 1.1rem;">🚗 The White Scorpio / Fortuner Showroom Analogy:</strong>
            <p style="color: #713f12; margin: 6px 0 0 0; font-size: 1rem; line-height: 1.7;">
                Instantiating an object without a constructor is like purchasing a car manufactured with <em>no color</em> and painting it afterwards. When placing an order for a Scorpio or Fortuner, you state: <strong>"White Color" at manufacturing time</strong>. Constructors guarantee that an object is born fully initialized and valid in RAM!
            </p>
        </div>

        <h4 style="color: #065f46; margin-top: 20px;">💻 C++ Implementation: Delegating Constructor & Initializer List</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

class Vehicle {
private:
    string brand;
    int topSpeed;
    const int registrationYear; // Const members MUST use Member Initializer List

public:
    // Primary Parameterized Constructor using Member Initializer List
    Vehicle(string b, int s, int yr) : brand(b), topSpeed(s), registrationYear(yr) {
        cout &lt;&lt; "[Primary Constructor] " &lt;&lt; brand &lt;&lt; " initialized.\n";
    }

    // Delegating Constructor (Calls primary constructor)
    Vehicle(string b) : Vehicle(b, 120, 2026) {
        cout &lt;&lt; "[Delegating Constructor] Assigned default speed & year.\n";
    }

    void display() const {
        cout &lt;&lt; "Vehicle: " &lt;&lt; brand &lt;&lt; " | Speed: " &lt;&lt; topSpeed &lt;&lt; " km/h | Year: " &lt;&lt; registrationYear &lt;&lt; endl;
    }
};

int main() {
    Vehicle v1("Fortuner"); // Calls delegating constructor
    v1.display();
    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            [Primary Constructor] Fortuner initialized.<br>
            [Delegating Constructor] Assigned default speed & year.<br>
            Vehicle: Fortuner | Speed: 120 km/h | Year: 2026
        </div>
    </div>
</div>
"""
            },
            {
                "slug": "chapter-6-destructors-and-raii",
                "title": "Chapter 6: Destructors, Virtual Cleanups & RAII",
                "subtopics": [
                    "1. Destructor Purpose & Syntax (~ClassName)",
                    "2. Execution Order (Bottom-Up vs. Top-Down)",
                    "3. Virtual Destructors & Memory Leak Elimination",
                    "4. RAII (Resource Acquisition Is Initialization) Concept"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #065f46 0%, #10b981 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🧹 Chapter 6: Destructors & RAII Mechanics</h1>
        <p style="font-size: 1.15rem; opacity: 0.95; margin: 0;">Resource Cleanup, Virtual Destructor Tables, and Automatic Scope Reclamation</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #065f46;">1. Virtual Destructor Architecture</h2>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            When a base class pointer deletes a derived class object, declaring the base destructor <code>virtual</code> guarantees that both Derived and Base destructors execute in proper bottom-up sequence.
        </p>

        <h4 style="color: #065f46;">💻 C++ Implementation: RAII File Handler Pattern</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

// RAII: Resource Acquisition Is Initialization
class ManagedResource {
private:
    int* dataBuffer;
public:
    ManagedResource(int size) {
        dataBuffer = new int[size];
        cout &lt;&lt; "[Resource Acquired] Allocated " &lt;&lt; size &lt;&lt; " integers on heap.\n";
    }

    ~ManagedResource() {
        delete[] dataBuffer;
        cout &lt;&lt; "[Resource Released] Heap buffer automatically freed upon scope exit.\n";
    }
};

int main() {
    {
        ManagedResource res(500); // Acquired in block scope
        cout &lt;&lt; "Processing data inside inner scope...\n";
    } // Exits scope: Destructor automatically frees memory!

    cout &lt;&lt; "Back in main scope safely.\n";
    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            [Resource Acquired] Allocated 500 integers on heap.<br>
            Processing data inside inner scope...<br>
            [Resource Released] Heap buffer automatically freed upon scope exit.<br>
            Back in main scope safely.
        </div>
    </div>
</div>
"""
            }
        ]
    },

    # =========================================================================
    # PART III: THE FOUR PILLARS OF OOP (Chapters 7 - 8)
    # =========================================================================
    {
        "unit": "Part III: The Four Pillars of OOP",
        "title": "Encapsulation & Abstraction",
        "topics": [
            {
                "slug": "chapter-7-encapsulation-mastery",
                "title": "Chapter 7: Encapsulation & Data Hiding",
                "subtopics": [
                    "1. Definition and Historical Need for Encapsulation",
                    "2. Getters, Setters, and Business Data Validation",
                    "3. Complete Banking System & ATM Example",
                    "4. Encapsulation vs. Abstraction"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #4338ca 0%, #6366f1 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🛡️ Chapter 7: Encapsulation & Secure State</h1>
        <p style="font-size: 1.15rem; margin: 0;">Binding Data with Methods, State Protection, and Banking Validation</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #4338ca;">1. Encapsulation Architecture</h2>
        <p style="font-size: 1.05rem; line-height: 1.8; color: #334155;">
            <strong>Encapsulation</strong> is the wrapping up of data (variables) and functions (methods) into a single unit (class) while restricting direct external access via access specifiers.
        </p>

        <h4 style="color: #4338ca; margin-top: 20px;">💻 C++ Implementation: Banking System with Encapsulated Balance</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

class BankAccount {
private:
    string accountHolder;
    double balance; // Hidden from direct external tampering

public:
    BankAccount(string name, double initialDeposit) {
        accountHolder = name;
        balance = (initialDeposit >= 0) ? initialDeposit : 0;
    }

    // Deposit with business logic validation
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout &lt;&lt; "[Deposit Success] Deposited: $" &lt;&lt; amount &lt;&lt; " | New Balance: $" &lt;&lt; balance &lt;&lt; endl;
        } else {
            cout &lt;&lt; "[Deposit Rejected] Invalid amount.\n";
        }
    }

    // Withdraw with overdraft protection
    void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout &lt;&lt; "[Withdrawal Success] Withdrew: $" &lt;&lt; amount &lt;&lt; " | Remaining: $" &lt;&lt; balance &lt;&lt; endl;
        } else {
            cout &lt;&lt; "[Withdrawal Rejected] Insufficient funds or invalid amount.\n";
        }
    }

    // Getter
    double getBalance() const { return balance; }
};

int main() {
    BankAccount myAcc("Ravi Kumar", 1000.0);
    myAcc.deposit(500.0);
    myAcc.withdraw(2000.0); // Will be rejected safely
    myAcc.withdraw(300.0);  // Will succeed

    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            [Deposit Success] Deposited: $500 | New Balance: $1500<br>
            [Withdrawal Rejected] Insufficient funds or invalid amount.<br>
            [Withdrawal Success] Withdrew: $300 | Remaining: $1200
        </div>
    </div>
</div>
"""
            },
            {
                "slug": "chapter-8-abstraction-mastery",
                "title": "Chapter 8: Abstraction & Interface Design",
                "subtopics": [
                    "1. What is Abstraction? (Hiding Complexity, Showing Essentials)",
                    "2. Real-World Examples (Car Accelerator & TV Remote)",
                    "3. Abstract Data Types (ADT) vs. Concrete Implementation",
                    "4. Abstraction vs. Encapsulation (The Definitive Comparison)"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #4338ca 0%, #6366f1 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🎛️ Chapter 8: Abstraction & Interface Design</h1>
        <p style="font-size: 1.15rem; margin: 0;">Implementation Hiding, Abstract Data Types, and Pure Design Contracts</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #4338ca;">1. Abstraction vs. Encapsulation (Exam Matrix)</h2>
        <table style="width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 1rem;">
            <thead>
                <tr style="background: #4338ca; color: white;">
                    <th style="padding: 12px; border: 1px solid #cbd5e1;">Comparison Dimension</th>
                    <th style="padding: 12px; border: 1px solid #cbd5e1; width: 45%;">Encapsulation</th>
                    <th style="padding: 12px; border: 1px solid #cbd5e1; width: 45%;">Abstraction</th>
                </tr>
            </thead>
            <tbody>
                <tr style="background: #f8fafc;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">Core Objective</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;"><strong>Data Security</strong> (Hiding internal data)</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;"><strong>Simplicity</strong> (Hiding background complexity)</td>
                </tr>
                <tr style="background: #ffffff;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">How it is achieved</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">Using <code>private</code>, <code>protected</code> specifiers</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">Using <strong>Abstract Classes</strong> and <strong>Interfaces</strong></td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">Real-World Analogy</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">A medical capsule wrapping medicine powders inside</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">Pressing the car accelerator pedal without knowing fuel injectors</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
"""
            }
        ]
    },

    # =========================================================================
    # PART IV: CODE REUSABILITY (Chapters 9 - 10)
    # =========================================================================
    {
        "unit": "Part IV: Code Reusability",
        "title": "Inheritance & The Diamond Problem",
        "topics": [
            {
                "slug": "chapter-9-inheritance-fundamentals",
                "title": "Chapter 9: Inheritance Fundamentals & Access Modes",
                "subtopics": [
                    "1. History & Purpose of Inheritance",
                    "2. Base vs. Derived Class Terminology",
                    "3. Access Modes (public, protected, private Inheritance)",
                    "4. Constructor & Destructor Execution Order"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🧬 Chapter 9: Inheritance Fundamentals</h1>
        <p style="font-size: 1.15rem; margin: 0;">Code Reuse, Base/Derived Relationships, and Access Modes</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #7c3aed;">1. Base and Derived Construction Sequence</h2>
        <div class="mermaid" style="text-align: center; margin: 20px 0;">
graph TD
    subgraph Construction [Construction Sequence: Top-Down]
        B_C[1. Base Constructor] --> D_C[2. Derived Constructor]
    end
    subgraph Destruction [Destruction Sequence: Bottom-Up]
        D_D[1. Derived Destructor] --> B_D[2. Base Destructor]
    end
        </div>
    </div>
</div>
"""
            },
            {
                "slug": "chapter-10-types-of-inheritance",
                "title": "Chapter 10: All 5 Types of Inheritance & The Diamond Problem",
                "subtopics": [
                    "1. Single, Multilevel, Multiple, Hierarchical & Hybrid Inheritance",
                    "2. The Diamond Problem & Ambiguity Explained",
                    "3. Virtual Base Class Resolution & Memory Layout",
                    "4. Complete C++ Code Example & Output"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">💎 Chapter 10: The 5 Inheritance Types & Diamond Problem</h1>
        <p style="font-size: 1.15rem; margin: 0;">Single, Multiple, Multilevel, Hierarchical, Hybrid & Virtual Base Classes</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #7c3aed;">1. The Diamond Problem Architecture & Solution</h2>
        <div class="mermaid" style="text-align: center; margin: 20px 0;">
graph TD
    P[Grandparent: Person] --> F[Father: virtual public Person]
    P --> M[Mother: virtual public Person]
    F --> C[Child: public Father, public Mother]
    
    style P fill:#fef08a,stroke:#ca8a04,stroke-width:2px;
    style C fill:#bbf7d0,stroke:#16a34a,stroke-width:2px;
        </div>

        <h4 style="color: #7c3aed; margin-top: 20px;">💻 C++ Implementation: Diamond Resolution with Virtual Base Class</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

class Person {
public:
    int id;
    Person() : id(1001) {}
};

// virtual inheritance prevents duplicate copies of Person
class Father : virtual public Person {};
class Mother : virtual public Person {};

class Child : public Father, public Mother {
public:
    void printID() const {
        cout &lt;&lt; "Unique Person ID resolved in Child: " &lt;&lt; id &lt;&lt; " (No Ambiguity!)\n";
    }
};

int main() {
    Child c;
    c.printID();
    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            Unique Person ID resolved in Child: 1001 (No Ambiguity!)
        </div>
    </div>
</div>
"""
            }
        ]
    },

    # =========================================================================
    # PART V: POLYMORPHISM (Chapters 11 - 15)
    # =========================================================================
    {
        "unit": "Part V: Polymorphism",
        "title": "Overloading, Overriding & Virtual Functions",
        "topics": [
            {
                "slug": "chapter-11-polymorphism-overview",
                "title": "Chapter 11: Polymorphism Overview & Binding Modes",
                "subtopics": [
                    "1. Meaning and Types of Polymorphism",
                    "2. Compile-Time (Static / Early Binding) Polymorphism",
                    "3. Runtime (Dynamic / Late Binding) Polymorphism",
                    "4. Real-World Person (Father/Employee/Husband) Analogy"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🎭 Chapter 11: Polymorphism & Binding Modes</h1>
        <p style="font-size: 1.15rem; margin: 0;">Compile-Time Static Binding vs. Runtime Dynamic Dispatch</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #0284c7;">1. Classification of Polymorphism</h2>
        <div class="mermaid" style="text-align: center; margin: 20px 0;">
graph TD
    Poly["<b>Polymorphism (Many Forms)</b>"]
    Poly --> CT["<b>1. Compile-Time (Static Binding)</b><br/>Resolved during compilation"]
    Poly --> RT["<b>2. Runtime (Dynamic Binding)</b><br/>Resolved during execution via vptr/vtable"]
    
    CT --> FO["Function Overloading"]
    CT --> OO["Operator Overloading"]
    CT --> TP["Templates"]
    
    RT --> VR["Virtual Functions & Overriding"]
        </div>
    </div>
</div>
"""
            },
            {
                "slug": "chapter-12-function-overloading",
                "title": "Chapter 12: Function Overloading",
                "subtopics": [
                    "1. Rules of Function Overloading",
                    "2. Parameter Differences (Count, Types, Sequence)",
                    "3. Return Type Ambiguity Limitations",
                    "4. Complete C++ Code & Output"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🔄 Chapter 12: Function Overloading</h1>
        <p style="font-size: 1.15rem; margin: 0;">Compile-Time Function Signatures, Type Promotion & Ambiguity Prevention</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #0284c7;">1. Overloading Rules & Implementation</h2>
        <h4 style="color: #0284c7;">💻 C++ Implementation: Function Overloading</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

class AreaCalculator {
public:
    // 1. Circle
    double area(double radius) {
        return 3.14159 * radius * radius;
    }

    // 2. Rectangle
    double area(double length, double breadth) {
        return length * breadth;
    }

    // 3. Triangle
    double area(float base, float height) {
        return 0.5 * base * height;
    }
};

int main() {
    AreaCalculator calc;
    cout &lt;&lt; "Circle Area (r=5): " &lt;&lt; calc.area(5.0) &lt;&lt; endl;
    cout &lt;&lt; "Rectangle Area (10x4): " &lt;&lt; calc.area(10.0, 4.0) &lt;&lt; endl;
    cout &lt;&lt; "Triangle Area (b=6, h=8): " &lt;&lt; calc.area(6.0f, 8.0f) &lt;&lt; endl;

    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            Circle Area (r=5): 78.5397<br>
            Rectangle Area (10x4): 40<br>
            Triangle Area (b=6, h=8): 24
        </div>
    </div>
</div>
"""
            },
            {
                "slug": "chapter-13-operator-overloading",
                "title": "Chapter 13: Operator Overloading",
                "subtopics": [
                    "1. Overloadable vs. Non-Overloadable Operators (::, ., .*, ?:)",
                    "2. Unary vs. Binary Operator Overloading",
                    "3. Friend Operator Overloading for Streams (<< and >>)",
                    "4. Complex Numbers & String Concatenation Code"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">➕ Chapter 13: Operator Overloading</h1>
        <p style="font-size: 1.15rem; margin: 0;">Extending Operators to User-Defined Types and Stream Operators</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #0284c7;">1. Operators that CANNOT be Overloaded in C++</h2>
        <div style="background: #fef2f2; border: 1px solid #f87171; border-radius: 8px; padding: 15px; margin: 15px 0;">
            <strong style="color: #b91c1c;">🚫 4 Operators that CANNOT be overloaded:</strong>
            <p style="color: #7f1d1d; margin: 5px 0 0 0; font-family: monospace; font-size: 1.05rem;">
                1. <code>.</code> (Dot / Direct Member Access)<br>
                2. <code>.*</code> (Pointer to Member Operator)<br>
                3. <code>::</code> (Scope Resolution Operator)<br>
                4. <code>?:</code> (Ternary Conditional Operator)<br>
                5. <code>sizeof</code> (Size Query Operator)
            </p>
        </div>

        <h4 style="color: #0284c7; margin-top: 20px;">💻 C++ Implementation: Overloading '+' and Stream Insertion '<<'</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

class Complex {
private:
    int real, imag;

public:
    Complex(int r = 0, int i = 0) : real(r), imag(i) {}

    // Overload '+' binary operator
    Complex operator+(const Complex& other) const {
        return Complex(real + other.real, imag + other.imag);
    }

    // Overload '&lt;&lt;' stream insertion operator as friend function
    friend ostream& operator&lt;&lt;(ostream& out, const Complex& c) {
        out &lt;&lt; c.real &lt;&lt; " + " &lt;&lt; c.imag &lt;&lt; "i";
        return out;
    }
};

int main() {
    Complex c1(4, 5), c2(2, 3);
    Complex c3 = c1 + c2; // Direct '+' addition of complex objects
    cout &lt;&lt; "Sum of Complex Numbers: " &lt;&lt; c3 &lt;&lt; endl;
    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            Sum of Complex Numbers: 6 + 8i
        </div>
    </div>
</div>
"""
            },
            {
                "slug": "chapter-14-function-overriding",
                "title": "Chapter 14: Function Overriding & override Keyword",
                "subtopics": [
                    "1. Function Overriding Mechanics",
                    "2. Same Signature Rule",
                    "3. The override and final Keywords in C++11",
                    "4. Overloading vs. Overriding Comparison"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🔁 Chapter 14: Function Overriding</h1>
        <p style="font-size: 1.15rem; margin: 0;">Specializing Base Behaviors, Signature Integrity, and C++11 Keywords</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #0284c7;">1. Overloading vs. Overriding (Exam Comparison)</h2>
        <table style="width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 1rem;">
            <thead>
                <tr style="background: #0284c7; color: white;">
                    <th style="padding: 12px; border: 1px solid #cbd5e1;">Dimension</th>
                    <th style="padding: 12px; border: 1px solid #cbd5e1; width: 45%;">Function Overloading</th>
                    <th style="padding: 12px; border: 1px solid #cbd5e1; width: 45%;">Function Overriding</th>
                </tr>
            </thead>
            <tbody>
                <tr style="background: #f8fafc;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">Scope</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">Occurs within the <strong>same class</strong></td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">Occurs across <strong>Base and Derived classes</strong></td>
                </tr>
                <tr style="background: #ffffff;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">Function Signature</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;"><strong>Must be DIFFERENT</strong> (parameters vary)</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;"><strong>Must be EXACTLY IDENTICAL</strong></td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 12px; border: 1px solid #cbd5e1; font-weight: bold;">Binding Time</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">Compile-Time (Early Binding)</td>
                    <td style="padding: 12px; border: 1px solid #cbd5e1;">Runtime (Late Binding via <code>virtual</code>)</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
"""
            },
            {
                "slug": "chapter-15-virtual-functions-vtable",
                "title": "Chapter 15: Virtual Functions, vptr & vtable Architecture",
                "subtopics": [
                    "1. Why Virtual Functions were Introduced",
                    "2. The Donkey vs. Horse Analogy",
                    "3. Internal Mechanism: Virtual Table (vtable) and Virtual Pointer (vptr)",
                    "4. Performance Considerations & Rules"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">⚡ Chapter 15: Virtual Functions & V-Table Engine</h1>
        <p style="font-size: 1.15rem; opacity: 0.95; margin: 0;">Runtime Dynamic Binding, Virtual Pointers (vptr), and Virtual Method Tables (vtable)</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #0284c7;">1. How Virtual Table (vtable) & vptr Work</h2>
        <div class="mermaid" style="text-align: center; margin: 20px 0;">
graph LR
    Obj["<b>Derived Object in Memory</b><br/>[vptr] -> points to vtable"] --> VT["<b>Derived vtable (Array of Function Pointers)</b><br/>[0] -> &Derived::start()<br/>[1] -> &Base::stop()"]
        </div>

        <h4 style="color: #0284c7; margin-top: 20px;">💻 C++ Implementation: Virtual Function Dynamic Binding</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

class Car {
public:
    virtual void drive() {
        cout &lt;&lt; "[Base Car] Moving at standard speed.\n";
    }
};

class SportsCar : public Car {
public:
    void drive() override {
        cout &lt;&lt; "[SportsCar] Turbo acceleration at 250 km/h!\n";
    }
};

int main() {
    Car* ptr = new SportsCar(); // Base pointer pointing to Derived object
    ptr->drive(); // Executes SportsCar's drive() dynamically at runtime!

    delete ptr;
    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            [SportsCar] Turbo acceleration at 250 km/h!
        </div>
    </div>
</div>
"""
            }
        ]
    },

    # =========================================================================
    # PART VI: ABSTRACT PROGRAMMING (Chapters 16 - 17)
    # =========================================================================
    {
        "unit": "Part VI: Abstract Programming",
        "title": "Pure Virtual Functions & Abstract Classes",
        "topics": [
            {
                "slug": "chapter-16-17-pure-virtual-and-abstract-classes",
                "title": "Chapters 16 & 17: Pure Virtual Functions (= 0) & Abstract Interfaces",
                "subtopics": [
                    "1. Pure Virtual Function Syntax (= 0)",
                    "2. Abstract Class Properties (Cannot instantiate objects, pointers allowed)",
                    "3. Interface-Like Architecture in C++",
                    "4. Complete Payment Gateway Example (PayPal, Stripe, UPI)"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #0d9488 0%, #14b8a6 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">📐 Chapters 16 & 17: Pure Virtual Functions & Interfaces</h1>
        <p style="font-size: 1.15rem; margin: 0;">Contract Enforcements, Abstract Base Classes, and Payment Processing Architecture</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #0d9488;">1. Real-World Architecture: Payment Gateway Interface</h2>
        
        <h4 style="color: #0d9488;">💻 C++ Implementation: Abstract Interface for Payment Processing</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

// Pure Abstract Class (Interface Contract)
class PaymentGateway {
public:
    virtual void processPayment(double amount) = 0; // Pure Virtual Function
    virtual ~PaymentGateway() {}
};

class UPIPayment : public PaymentGateway {
public:
    void processPayment(double amount) override {
        cout &lt;&lt; "[UPI Engine] Payment of ₹" &lt;&lt; amount &lt;&lt; " processed instantly via UPI QR!\n";
    }
};

class CreditCardPayment : public PaymentGateway {
public:
    void processPayment(double amount) override {
        cout &lt;&lt; "[Bank Gateway] Payment of ₹" &lt;&lt; amount &lt;&lt; " authorized with 2FA OTP verification.\n";
    }
};

int main() {
    // PaymentGateway gateway; // ERROR: Abstract class cannot be instantiated!
    
    PaymentGateway* paymentMethod1 = new UPIPayment();
    PaymentGateway* paymentMethod2 = new CreditCardPayment();

    paymentMethod1->processPayment(1500.0);
    paymentMethod2->processPayment(8500.0);

    delete paymentMethod1;
    delete paymentMethod2;
    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            [UPI Engine] Payment of ₹1500 processed instantly via UPI QR!<br>
            [Bank Gateway] Payment of ₹8500 authorized with 2FA OTP verification.
        </div>
    </div>
</div>
"""
            }
        ]
    },

    # =========================================================================
    # PART VII: ADVANCED CLASS FEATURES (Chapters 18 - 20)
    # =========================================================================
    {
        "unit": "Part VII: Advanced Class Features",
        "title": "Statics, Friends & this Pointer",
        "topics": [
            {
                "slug": "chapter-18-20-statics-friends-this",
                "title": "Chapters 18, 19 & 20: Statics, Friends and the this Pointer",
                "subtopics": [
                    "1. Static Data Members & Static Member Functions",
                    "2. Friend Functions & Friend Classes (Access & Risks)",
                    "3. The this Pointer (Method Chaining & Shadow Resolution)"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #c2410c 0%, #ea580c 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🔧 Chapters 18–20: Advanced Class Mechanisms</h1>
        <p style="font-size: 1.15rem; margin: 0;">Class-Level State, Controlled Friendship, and Method Chaining via this</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #c2410c;">1. Method Chaining using the 'this' Pointer</h2>
        <h4 style="color: #c2410c;">💻 C++ Implementation: Method Chaining with return *this</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

class Builder {
private:
    int x, y;
public:
    Builder& setX(int x) {
        this->x = x; // Resolving shadowed variable
        return *this; // Returning current instance for cascading
    }

    Builder& setY(int y) {
        this->y = y;
        return *this;
    }

    void print() const {
        cout &lt;&lt; "Coordinates -> X: " &lt;&lt; x &lt;&lt; ", Y: " &lt;&lt; y &lt;&lt; endl;
    }
};

int main() {
    Builder b;
    // Method Chaining in action
    b.setX(10).setY(20).print();
    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            Coordinates -> X: 10, Y: 20
        </div>
    </div>
</div>
"""
            }
        ]
    },

    # =========================================================================
    # PART VIII: MEMORY MANAGEMENT & COPYING (Chapters 21 - 23)
    # =========================================================================
    {
        "unit": "Part VIII: Memory & Copying",
        "title": "Dynamic Memory, Deep Copy & Rule of 3/5",
        "topics": [
            {
                "slug": "chapter-21-23-memory-deep-copy-rule-of-three-five",
                "title": "Chapters 21, 22 & 23: Dynamic Memory, Shallow vs Deep Copy & Rule of 3/5",
                "subtopics": [
                    "1. Dynamic Memory (Stack vs Heap, new, delete)",
                    "2. Shallow Copy vs Deep Copy & The Double-Free Bug",
                    "3. The Rule of Three and Rule of Five in Modern C++",
                    "4. Smart Pointers (unique_ptr, shared_ptr, weak_ptr)"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #059669 0%, #10b981 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🧠 Chapters 21–23: Memory Safety & Deep Copying</h1>
        <p style="font-size: 1.15rem; margin: 0;">Pointer Ownership, Shallow vs. Deep Copy Disasters, and Rule of Three/Five</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #059669;">1. The Rule of Three / Rule of Five</h2>
        <div style="background: #f8fafc; border-left: 5px solid #059669; padding: 18px; border-radius: 8px; margin: 15px 0;">
            <strong style="color: #065f46; font-size: 1.1rem;">The Rule of Three (Classic C++):</strong>
            <p style="color: #334155; margin: 6px 0 0 0; font-size: 1rem; line-height: 1.7;">
                If a class manages dynamic heap memory and requires a custom <strong>Destructor</strong>, it almost certainly requires a custom <strong>Copy Constructor</strong> and <strong>Copy Assignment Operator</strong> (<code>operator=</code>) to prevent double-free crashes.
            </p>
        </div>

        <h4 style="color: #059669; margin-top: 20px;">💻 C++ Implementation: Deep Copy vs Shallow Copy Protection</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

class DeepArray {
private:
    int* ptr;
    int size;

public:
    DeepArray(int s) : size(s) {
        ptr = new int[size];
        for(int i = 0; i &lt; size; i++) ptr[i] = (i + 1) * 10;
        cout &lt;&lt; "[Constructor] Allocated array of size " &lt;&lt; size &lt;&lt; endl;
    }

    // Deep Copy Constructor: Allocates distinct heap buffer
    DeepArray(const DeepArray& other) : size(other.size) {
        ptr = new int[size];
        for(int i = 0; i &lt; size; i++) ptr[i] = other.ptr[i];
        cout &lt;&lt; "[Deep Copy Constructor] Cloned with independent heap buffer.\n";
    }

    void display() const {
        for(int i = 0; i &lt; size; i++) cout &lt;&lt; ptr[i] &lt;&lt; " ";
        cout &lt;&lt; endl;
    }

    ~DeepArray() {
        delete[] ptr; // Safe individual deallocation
    }
};

int main() {
    DeepArray arr1(3);
    DeepArray arr2 = arr1; // Deep Copy invoked safely!

    cout &lt;&lt; "Arr1: "; arr1.display();
    cout &lt;&lt; "Arr2: "; arr2.display();

    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            [Constructor] Allocated array of size 3<br>
            [Deep Copy Constructor] Cloned with independent heap buffer.<br>
            Arr1: 10 20 30<br>
            Arr2: 10 20 30
        </div>
    </div>
</div>
"""
            }
        ]
    },

    # =========================================================================
    # PART IX: ADVANCED C++ OOP (Chapters 24 - 25)
    # =========================================================================
    {
        "unit": "Part IX: Advanced C++ OOP",
        "title": "Exception Handling & Templates",
        "topics": [
            {
                "slug": "chapter-24-25-exceptions-and-templates",
                "title": "Chapters 24 & 25: Exception Handling & Generic Programming",
                "subtopics": [
                    "1. Exception Flow (try, throw, catch, catch-all)",
                    "2. Stack Unwinding & Custom Exceptions",
                    "3. Function Templates & Class Templates"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">⚡ Chapters 24 & 25: Exceptions & Generic Templates</h1>
        <p style="font-size: 1.15rem; margin: 0;">Stack Unwinding, Custom Error Hierarchies, and Type-Independent Blueprints</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #4f46e5;">1. Generic Stack Class Template</h2>
        <h4 style="color: #4f46e5;">💻 C++ Implementation: Generic Class Template</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

template &lt;typename T&gt;
class Stack {
private:
    T elements[10];
    int topIndex;

public:
    Stack() : topIndex(-1) {}

    void push(T val) {
        if (topIndex &lt; 9) {
            elements[++topIndex] = val;
        }
    }

    T pop() {
        if (topIndex >= 0) return elements[topIndex--];
        throw "Stack Underflow!";
    }
};

int main() {
    Stack&lt;int&gt; intStack;
    intStack.push(100);
    intStack.push(200);
    cout &lt;&lt; "Popped Int: " &lt;&lt; intStack.pop() &lt;&lt; endl;

    Stack&lt;string&gt; strStack;
    strStack.push("Hello");
    strStack.push("OOPs");
    cout &lt;&lt; "Popped String: " &lt;&lt; strStack.pop() &lt;&lt; endl;

    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            Popped Int: 200<br>
            Popped String: OOPs
        </div>
    </div>
</div>
"""
            }
        ]
    },

    # =========================================================================
    # PART X: SOFTWARE DESIGN PRINCIPLES (Chapters 26 - 27)
    # =========================================================================
    {
        "unit": "Part X: Software Design Principles",
        "title": "SOLID Principles & Design Patterns",
        "topics": [
            {
                "slug": "chapter-26-solid-principles",
                "title": "Chapter 26: The SOLID Principles of OOP",
                "subtopics": [
                    "S — Single Responsibility Principle (SRP)",
                    "O — Open/Closed Principle (OCP)",
                    "L — Liskov Substitution Principle (LSP)",
                    "I — Interface Segregation Principle (ISP)",
                    "D — Dependency Inversion Principle (DIP)"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #831843 0%, #db2777 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🏛️ Chapter 26: The SOLID Design Principles</h1>
        <p style="font-size: 1.15rem; margin: 0;">Architectural Guidelines for Scalable, Maintainable Enterprise Software</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #831843;">1. The 5 SOLID Pillars Breakdown</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin: 20px 0;">
            <div style="background: #fdf2f8; border-left: 5px solid #db2777; padding: 15px; border-radius: 8px;">
                <h4 style="color: #9d174d; margin: 0 0 6px 0;">S — Single Responsibility</h4>
                <p style="color: #374151; font-size: 0.95rem; margin: 0;">A class should have <strong>one and only one reason to change</strong> (Single focused responsibility).</p>
            </div>
            <div style="background: #fdf2f8; border-left: 5px solid #db2777; padding: 15px; border-radius: 8px;">
                <h4 style="color: #9d174d; margin: 0 0 6px 0;">O — Open / Closed Principle</h4>
                <p style="color: #374151; font-size: 0.95rem; margin: 0;">Software entities should be <strong>Open for extension, but Closed for modification</strong>.</p>
            </div>
            <div style="background: #fdf2f8; border-left: 5px solid #db2777; padding: 15px; border-radius: 8px;">
                <h4 style="color: #9d174d; margin: 0 0 6px 0;">L — Liskov Substitution</h4>
                <p style="color: #374151; font-size: 0.95rem; margin: 0;">Derived objects must be substitutable for their Base class without breaking program correctness.</p>
            </div>
            <div style="background: #fdf2f8; border-left: 5px solid #db2777; padding: 15px; border-radius: 8px;">
                <h4 style="color: #9d174d; margin: 0 0 6px 0;">I — Interface Segregation</h4>
                <p style="color: #374151; font-size: 0.95rem; margin: 0;">Clients should not be forced to depend on interfaces with methods they do not use.</p>
            </div>
            <div style="background: #fdf2f8; border-left: 5px solid #db2777; padding: 15px; border-radius: 8px;">
                <h4 style="color: #9d174d; margin: 0 0 6px 0;">D — Dependency Inversion</h4>
                <p style="color: #374151; font-size: 0.95rem; margin: 0;">Depend upon abstract interfaces, never upon concrete low-level implementations.</p>
            </div>
        </div>
    </div>
</div>
"""
            },
            {
                "slug": "chapter-27-design-patterns-basics",
                "title": "Chapter 27: Essential Design Patterns in C++",
                "subtopics": [
                    "1. Creational: Singleton & Factory Pattern",
                    "2. Structural: Adapter & Decorator Pattern",
                    "3. Behavioral: Observer & Strategy Pattern"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #831843 0%, #db2777 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🎨 Chapter 27: Classic OOP Design Patterns</h1>
        <p style="font-size: 1.15rem; margin: 0;">Singleton, Factory, Strategy, and Observer Patterns in C++</p>
    </div>

    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #831843;">1. Thread-Safe Singleton Pattern in C++</h2>
        <h4 style="color: #831843;">💻 C++ Implementation: Singleton Logger</h4>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

class Logger {
private:
    // Private Constructor prevents direct creation
    Logger() { cout &lt;&lt; "[Logger Initialized] Single instance active.\n"; }

public:
    // Delete copy constructor and assignment operator
    Logger(const Logger&) = delete;
    Logger& operator=(const Logger&) = delete;

    // Static Accessor
    static Logger& getInstance() {
        static Logger instance; // Thread-safe Meyers Singleton
        return instance;
    }

    void log(string message) {
        cout &lt;&lt; "[LOG INFO]: " &lt;&lt; message &lt;&lt; endl;
    }
};

int main() {
    Logger::getInstance().log("System booted.");
    Logger::getInstance().log("Database connected.");
    return 0;
}
        </pre>
        
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 14px 20px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px; font-size: 1rem;">
            <strong>🖥️ Terminal Output:</strong><br>
            [Logger Initialized] Single instance active.<br>
            [LOG INFO]: System booted.<br>
            [LOG INFO]: Database connected.
        </div>
    </div>
</div>
"""
            }
        ]
    },

    # =========================================================================
    # PART XI: COMPLETE C++ OOP PROJECTS (Chapter 28)
    # =========================================================================
    {
        "unit": "Part XI: Complete C++ OOP Projects",
        "title": "Real-World Projects & Full Source Code",
        "topics": [
            {
                "slug": "chapter-28-complete-oop-projects",
                "title": "Chapter 28: 6 End-to-End Real-World OOP Projects",
                "subtopics": [
                    "Project 1: Student Management System (Classes, Encapsulation, File I/O)",
                    "Project 2: Bank Management System (Polymorphism & Account Types)",
                    "Project 3: Library Management System (Object Relationships)",
                    "Project 4: Employee Payroll Management System",
                    "Project 5: Vehicle Rental System",
                    "Project 6: Hospital Patient Management System"
                ],
                "content": """
<div class="learning-path">
    <div class="board-banner" style="background: linear-gradient(135deg, #0f172a 0%, #334155 100%); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px;">
        <h1 style="font-size: 2.2rem; margin-bottom: 8px; font-weight: 800;">🚀 Chapter 28: Complete End-to-End OOP Projects</h1>
        <p style="font-size: 1.15rem; margin: 0;">Complete Production-Grade Architecture & Fully Runnable Source Code</p>
    </div>

    <!-- Project 1: Student System -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e3a8a;">Project 1: Student Record & Performance Management System</h2>
        <p style="color: #475569;">Demonstrates: <em>Classes, Encapsulation, Methods, and Arrays of Objects</em></p>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
#include &lt;vector&gt;
using namespace std;

class Student {
private:
    int id;
    string name;
    float gpa;

public:
    Student(int id, string name, float gpa) : id(id), name(name), gpa(gpa) {}

    void display() const {
        cout &lt;&lt; "ID: " &lt;&lt; id &lt;&lt; " | Name: " &lt;&lt; name &lt;&lt; " | GPA: " &lt;&lt; gpa &lt;&lt; "/4.0\n";
    }
};

int main() {
    vector&lt;Student&gt; database;
    database.push_back(Student(101, "Ravi Kumar", 3.9));
    database.push_back(Student(102, "Sneha Sharma", 3.8));

    cout &lt;&lt; "--- Student Management System Records ---\n";
    for(const auto& s : database) {
        s.display();
    }
    return 0;
}
        </pre>
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 12px 18px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px;">
            <strong>🖥️ Output:</strong><br>
            --- Student Management System Records ---<br>
            ID: 101 | Name: Ravi Kumar | GPA: 3.9/4.0<br>
            ID: 102 | Name: Sneha Sharma | GPA: 3.8/4.0
        </div>
    </div>

    <!-- Project 2: Bank System -->
    <div class="concept-section" style="background: white; border-radius: 12px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h2 style="color: #065f46;">Project 2: Polymorphic Bank Account & Interest Engine</h2>
        <p style="color: #475569;">Demonstrates: <em>Inheritance, Polymorphism, Abstract Base Class, Dynamic Binding</em></p>
        <pre style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; overflow-x: auto; font-family: Consolas, monospace; font-size: 1rem; line-height: 1.6;">
#include &lt;iostream&gt;
using namespace std;

class Account {
protected:
    string accountNo;
    double balance;

public:
    Account(string no, double bal) : accountNo(no), balance(bal) {}
    virtual void applyInterest() = 0; // Pure Virtual Method
    virtual void printSummary() const {
        cout &lt;&lt; "Acc: " &lt;&lt; accountNo &lt;&lt; " | Balance: $" &lt;&lt; balance &lt;&lt; endl;
    }
    virtual ~Account() {}
};

class SavingsAccount : public Account {
public:
    SavingsAccount(string no, double bal) : Account(no, bal) {}
    void applyInterest() override {
        balance += balance * 0.05; // 5% Interest
        cout &lt;&lt; "[Savings] 5% Interest applied. New balance: $" &lt;&lt; balance &lt;&lt; endl;
    }
};

int main() {
    Account* acc = new SavingsAccount("SAV-9901", 10000.0);
    acc->printSummary();
    acc->applyInterest();
    delete acc;
    return 0;
}
        </pre>
        <div style="background: #090d16; border-left: 5px solid #22c55e; color: #4ade80; padding: 12px 18px; border-radius: 6px; font-family: Consolas, monospace; margin-top: 10px;">
            <strong>🖥️ Output:</strong><br>
            Acc: SAV-9901 | Balance: $10000<br>
            [Savings] 5% Interest applied. New balance: $10500
        </div>
    </div>
</div>
"""
            }
        ]
    }
]
