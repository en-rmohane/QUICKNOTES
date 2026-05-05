c_programming_data = [
    {
        "unit": "Unit-I",
        "title": "Mastering the Fundamentals",
        "topics": [
            {
                "slug": "computer-evolution-basics",
                "title": "Chapter 1: The World of Computers",
                "subtopics": [
                    "The Journey of Computing",
                    "What makes a Computer?",
                    "Hardware vs Software vs Firmware",
                    "Modern Computing Paradigms",
                    "The Language of Machines",
                    "How Programs are Built",
                    "Logic Design with Algorithms"
                ],
                "content": """
                    <div class="learning-path">
                        <h2>1. The Evolution of Computing</h2>
                        <p>The story of computers began with <strong>Charles Babbage</strong>, the visionary who designed the 'Analytical Engine'. While early machines were purely mechanical, they paved the way for the digital revolution we see today.</p>
                        
                        <div class="timeline-container" style="margin: 20px 0;">
                            <div class="gen-box" style="background: #f1f8ff; border-radius: 8px; padding: 15px; margin-bottom: 10px; border-left: 5px solid #0366d6;">
                                <strong>The Vacuum Tube Era (1940-1956):</strong> Massive machines like ENIAC that filled rooms. They were fast for their time but produced immense heat and required machine-level binary coding.
                            </div>
                            <div class="gen-box" style="background: #fff5f5; border-radius: 8px; padding: 15px; margin-bottom: 10px; border-left: 5px solid #d73a49;">
                                <strong>The Transistor Revolution (1956-1964):</strong> Transistors made computers smaller and more reliable. This era introduced Assembly language and early business languages like COBOL.
                            </div>
                            <div class="gen-box" style="background: #f0fff4; border-radius: 8px; padding: 15px; margin-bottom: 10px; border-left: 5px solid #28a745;">
                                <strong>Integrated Circuits (1964-1971):</strong> Thousands of components were packed onto silicon chips (ICs). Computers finally became 'desktop-sized', and operating systems like UNIX were born.
                            </div>
                            <div class="gen-box" style="background: #fffaf0; border-radius: 8px; padding: 15px; margin-bottom: 10px; border-left: 5px solid #f9c513;">
                                <strong>The Microprocessor Age (1971-Present):</strong> The 'Computer on a Chip'. This led to the birth of the Personal Computer (PC), the Internet, and high-level languages like C.
                            </div>
                            <div class="gen-box" style="background: #f5f0ff; border-radius: 8px; padding: 15px; margin-bottom: 10px; border-left: 5px solid #6f42c1;">
                                <strong>AI & Quantum Future (Present-Beyond):</strong> Focusing on Artificial Intelligence, robotics, and natural language processing. Systems are now learning to 'think' rather than just follow instructions.
                            </div>
                        </div>

                        <h2>2. Defining the Digital Brain</h2>
                        <p>At its core, a computer is a system that follows a simple <strong>Input-Process-Output (IPO)</strong> cycle:</p>
                        <ul class="custom-list">
                            <li><strong>Ingestion:</strong> Collecting raw data through input devices.</li>
                            <li><strong>Persistence:</strong> Keeping data safe in memory or permanent storage.</li>
                            <li><strong>Computation:</strong> Transforming raw data into meaningful information using logic.</li>
                            <li><strong>Delivery:</strong> Presenting the results via screens, printers, or speakers.</li>
                        </ul>

                        <div class="mermaid" style="text-align: center;">
                            graph LR
                                USER((User)) -->|Input| IN[Input Unit]
                                IN --> CPU[The CPU]
                                MU[(Storage/Memory)] <--> CPU
                                CPU -->|Output| OUT[Output Unit]
                                OUT --> USER
                                subgraph Internal [Computer Core]
                                    MU
                                    CPU
                                end
                        </div>

                        <h2>3. The Architecture: Hardware & Software</h2>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                            <div style="background: #eef2f3; padding: 15px; border-radius: 8px;">
                                <h3>The Body (Hardware)</h3>
                                <p>The physical parts you can touch: Motherboards, Processors, RAM, and storage drives.</p>
                            </div>
                            <div style="background: #eef2f3; padding: 15px; border-radius: 8px;">
                                <h3>The Soul (Software)</h3>
                                <p>The instructions that guide the body. Includes System Software (OS) and Application Software (Apps).</p>
                            </div>
                        </div>
                        <p style="margin-top:10px;"><strong>Pro Tip:</strong> There's also <em>Firmware</em>—software that is permanently 'baked' into the hardware, like the program in your washing machine or microwave.</p>

                        <h2>4. Modern Computing Environments</h2>
                        <p>We no longer just use standalone PCs. Today's world is connected:</p>
                        <ul>
                            <li><strong>Cloud Computing:</strong> Renting computer power and storage over the internet (like Google Drive).</li>
                            <li><strong>Distributed Systems:</strong> Multiple computers working together as one giant system (the Internet itself).</li>
                            <li><strong>Client-Server:</strong> Your browser (client) requesting data from a website (server).</li>
                        </ul>

                        <h2>5. Programming: The Art of Communication</h2>
                        <p>To talk to a computer, we use 'Translators':</p>
                        <ul>
                            <li><strong>Compilers:</strong> Translate the whole program at once. Fast execution but slower startup.</li>
                            <li><strong>Interpreters:</strong> Translate line-by-line. Great for debugging but slower for big tasks.</li>
                        </ul>

                        <h2>6. The 8-Step Blueprint for Building Software</h2>
                        <p>Professional developers don't just start coding. They follow a cycle:</p>
                        <ol>
                            <li><strong>Define:</strong> What problem are we solving?</li>
                            <li><strong>Analyze:</strong> What inputs do we need?</li>
                            <li><strong>Plan:</strong> Design the algorithm.</li>
                            <li><strong>Visualize:</strong> Draw the flowchart.</li>
                            <li><strong>Draft:</strong> Write pseudo-code.</li>
                            <li><strong>Build:</strong> Write the actual code (C, Java, etc.).</li>
                            <li><strong>Test:</strong> Fix errors (Bugs).</li>
                            <li><strong>Finalize:</strong> Document the project for others.</li>
                        </ol>

                        <hr>

                        <h2>7. Algorithm Masterclass</h2>
                        <p>Let's look at how we solve real-world problems using logic.</p>

                        <h3>Logic 1: The Prime Number Challenge</h3>
                        <p>A prime number is only divisible by 1 and itself. Here is how a computer checks it:</p>
                        <div class="mermaid">
                            graph TD
                                Start([Start]) --> Read[/Get Number n/]
                                Read --> Init[Set i=2, isPrime=true]
                                Init --> Loop{i < n?}
                                Loop -- Yes --> Check{n % i == 0?}
                                Check -- Yes --> Fail[isPrime=false]
                                Check -- No --> Next[i = i + 1]
                                Next --> Loop
                                Fail --> Result
                                Loop -- No --> Result{isPrime == true?}
                                Result -- Yes --> P[/Display Prime/]
                                Result -- No --> NP[/Display Not Prime/]
                                P --> Stop([End])
                                NP --> Stop
                        </div>

                        <h3>Logic 2: Fibonacci Sequence</h3>
                        <p>Generating the famous sequence: 0, 1, 1, 2, 3, 5, 8...</p>
                        <pre style="background: #2d3436; color: white; padding: 15px; border-radius: 8px;">
1. Start
2. Let A = 0, B = 1
3. Show A and B
4. Loop 'Count' times:
   Next = A + B
   Show Next
   A = B
   B = Next
5. End</pre>
                        <hr>

                        <div class="interview-prep" style="background: #fff3e0; padding: 20px; border-radius: 10px; border-left: 6px solid #ff9800; margin-top: 30px;">
                            <h2 style="color: #e65100; margin-top: 0;">🎯 Interview Prep: Chapter 1</h2>
                            
                            <div class="question-box" style="margin-bottom: 15px;">
                                <strong style="display: block; color: #bf360c;">Q1: What is the primary difference between a Compiler and an Interpreter?</strong>
                                <p style="margin: 5px 0;"><em>Answer:</em> A Compiler translates the entire source code into machine code at once (creating an executable file), which makes it faster for repeated runs. An Interpreter translates and executes the code line-by-line, which is slower but makes debugging much easier.</p>
                            </div>

                            <div class="question-box" style="margin-bottom: 15px;">
                                <strong style="display: block; color: #bf360c;">Q2: Why is the Fourth Generation considered a 'landmark' in computer history?</strong>
                                <p style="margin: 5px 0;"><em>Answer:</em> It introduced the <strong>Microprocessor</strong> (LSI/VLSI technology). This allowed the entire CPU to fit on a single chip, leading to the birth of the Personal Computer (PC) and making computers accessible to everyone, not just large organizations.</p>
                            </div>

                            <div class="question-box" style="margin-bottom: 15px;">
                                <strong style="display: block; color: #bf360c;">Q3: What is 'Firmware' and how is it different from Software?</strong>
                                <p style="margin: 5px 0;"><em>Answer:</em> Firmware is a specific type of software that is permanently stored in a hardware device (like a BIOS or the program in a remote control). Unlike regular software (like MS Word) which can be easily installed/removed, firmware is fixed and essential for the hardware's basic operation.</p>
                            </div>

                            <div class="question-box" style="margin-bottom: 15px;">
                                <strong style="display: block; color: #bf360c;">Q4: Define an 'Efficient Algorithm'.</strong>
                                <p style="margin: 5px 0;"><em>Answer:</em> An algorithm is considered efficient if it solves the problem correctly using the <strong>minimum amount of memory</strong> (Space Complexity) and the <strong>least amount of processor time</strong> (Time Complexity).</p>
                            </div>
                        </div>
                    </div>
                """
            },
            {
                "slug": "fundamental-concepts-in-c",
                "title": "Chapter 2: Deep Dive into Fundamental Concepts in C",
                "subtopics": [
                    "The Genesis and Evolution of C",
                    "Understanding C as a Middle-Level Language",
                    "Detailed Structure of a C Program",
                    "Composition: The Building Blocks of C",
                    "Character Set & Symbols in Detail",
                    "Constants: Types and Usage",
                    "Variables: Rules and Declarations",
                    "Reserved Keywords (The 32 Pillars)",
                    "Introduction to C Statements",
                    "The stdio.h Library and Header Files",
                    "Single Character I/O (getchar & putchar)",
                    "String Level I/O (gets & puts)",
                    "Mastering Formatted Input (scanf)",
                    "Mastering Formatted Output (printf)",
                    "Escape Sequences & Backslash Codes",
                    "The Execution Sequence (Compile to Run)",
                    "Working with Turbo C (Shortcuts & Help)",
                    "C in the Unix Environment (vi & cc)",
                    "Visual C++ 6.0 (Projects & Workspaces)",
                    "Advanced: Command Line Arguments",
                    "Debugging with Step-by-Step Tracing"
                ],
                "content": """
                    <div class="learning-path">
                        <h2>1. The Birth and Legacy of C</h2>
                        <p>It is truly remarkable that even after more than forty years, the C language remains the foundational choice for programmers across the globe. For any individual aspiring to become a serious software professional, starting their educational journey with C is highly recommended. C has a unique pedagogical power; it transforms a novice into a disciplined engineer who understands the internal workings of a computer. While other languages like BASIC, COBOL, and FORTRAN once dominated, they eventually faded after the arrival of C, which provided a more robust and flexible framework for both system and application development.</p>
                        
                        <h2>2. Why C is Termed a 'Middle-Level' Language</h2>
                        <p>One of the most common questions in technical interviews is about the classification of C. To understand this, we must look at the spectrum of programming languages:</p>
                        <div class="info-card" style="background: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 5px solid #2196f3; margin: 15px 0;">
                            <strong>A. High-Level Languages:</strong> Examples include Pascal, FORTRAN, and Java. These use English-like syntax and are designed for developer productivity. However, they are distant from the hardware and cannot easily manipulate memory addresses or registers directly.
                            <br><br>
                            <strong>B. Low-Level Languages:</strong> Assembly language is the primary example. It allows for direct hardware control and is extremely fast, but it is incredibly difficult to write, read, and maintain.
                        </div>
                        <p><strong>The Bridge:</strong> C sits perfectly in the middle. It provides the structured approach and readability of high-level languages while retaining the 'raw power' of low-level languages to access memory and hardware. This dual capability makes it the 'Middle-Level' bridge of the computing world.</p>

                        <h2>3. The History and Development of C</h2>
                        <p>The story of C begins in the late 1960s at the prestigious <strong>AT&T Bell Labs</strong>. At that time, a team was working on developing a more efficient operating system. <strong>Ken Thompson</strong> developed the 'B' language, which was a condensed version of BCPL (Basic Combined Programming Language). While 'B' was useful, it had limitations. <strong>Dennis Ritchie</strong> took the core concepts of 'B' and added crucial features like data types, complex operators, and structured functions. By <strong>1972</strong>, this refined language was unveiled as 'C'. It was immediately used to rewrite the UNIX operating system, marking the first time an OS was written in a high-level language rather than Assembly.</p>

                        <h2>4. The Architectural Blueprint of a C Program</h2>
                        <p>Every C program follows a specific hierarchical structure. Think of it as a house with designated rooms for different tasks:</p>
                        <div class="mermaid" style="text-align: center; margin: 20px 0;">
                            graph TD
                                A[Preprocessor Section - Header Includes] --> B[Global Variable Declarations]
                                B --> C["main() Function { Start of Execution }"]
                                subgraph Inside_Main [Main Logic Block]
                                    D[Local Variable Declarations]
                                    E[Executable Code & Logic]
                                end
                                C --> D
                                E --> F[Sub-Functions & Modular Logic]
                        </div>
                        <ul>
                            <li><strong>Preprocessor Directives:</strong> Lines starting with <code>#</code> (like <code>#include &lt;stdio.h&gt;</code>) tell the compiler to gather necessary tools before starting the build.</li>
                            <li><strong>Global Section:</strong> Defining data that needs to be accessed by multiple parts of the program.</li>
                            <li><strong>The main() Function:</strong> The heart of every program. The OS looks for 'main' to start running your instructions.</li>
                        </ul>

                        <h2>5. Composition: The Logic of Building Code</h2>
                        <p>Building a program is a step-by-step assembly process. We use the most basic elements to create complex systems:</p>
                        <p style="background: #f1f1f1; padding: 15px; border-radius: 5px; text-align: center; font-weight: bold;">
                            Character Set &rarr; Tokens (Words) &rarr; Statements (Sentences) &rarr; Program (Story)
                        </p>

                        <h3>The C Character Set</h3>
                        <p>The compiler recognizes a specific set of symbols:</p>
                        <ul>
                            <li><strong>Letters:</strong> Both Upper Case (A-Z) and Lower Case (a-z).</li>
                            <li><strong>Numbers:</strong> Digits from 0 to 9.</li>
                            <li><strong>Special Symbols:</strong> <code>+ - * / % ^ & | ! = ( ) [ ] { } < > , . ; : ' " _ #</code></li>
                        </ul>

                        <h2>6. Tokens in C: Constants, Variables & Keywords</h2>
                        <p>Once the compiler reads the characters, it groups them into 'Tokens' or words.</p>
                        
                        <h3>A. Constants (Invariable Data)</h3>
                        <p>Data values that remain fixed throughout the life of the program:</p>
                        <ul>
                            <li><strong>Integers:</strong> Whole numbers without decimals (e.g., 42, -500).</li>
                            <li><strong>Reals (Floats):</strong> Numbers with decimal points (e.g., 98.6, -0.005).</li>
                            <li><strong>Characters:</strong> Single symbols in single quotes (e.g., 'X', '7', '$').</li>
                            <li><strong>Strings:</strong> Sequences of text in double quotes (e.g., "Deep Learning", "C-Language").</li>
                        </ul>

                        <h3>B. Variables (Container Logic)</h3>
                        <p>A variable is a symbolic name for a memory location. You can change the value stored inside this location as the program runs.
                        <br><strong>Naming Protocol:</strong>
                        1. Must begin with a letter or an underscore (_).
                        2. Cannot contain spaces or special symbols.
                        3. Cannot be a Reserved Keyword.
                        4. It is best practice to use descriptive names (e.g., <code>student_age</code> instead of just <code>a</code>).</p>

                        <h3>C. The 32 Reserved Keywords</h3>
                        <p>C has 32 special words that are strictly reserved for the compiler's own logic. You cannot use these as variable names. They are: <code>auto, break, case, char, const, continue, default, do, double, else, enum, extern, float, for, goto, if, int, long, register, return, short, signed, sizeof, static, struct, switch, typedef, union, unsigned, void, volatile, while</code>.</p>

                        <h2>7. Standard Input and Output (I/O)</h2>
                        <p>Programs are useless if they cannot communicate with the user. C provides a set of standard functions in the <code>stdio.h</code> (Standard Input Output) header file.</p>

                        <h3>Single Character Operations</h3>
                        <p>Sometimes you only need to process one character at a time:</p>
                        <ul>
                            <li><code>getchar()</code>: Pauses the program and waits for the user to press a key.</li>
                            <li><code>putchar(ch)</code>: Displays the character stored in 'ch' onto the screen.</li>
                        </ul>

                        <h3>String Operations (Text Blocks)</h3>
                        <ul>
                            <li><code>gets(str)</code>: Accepts an entire line of text, including spaces, until the user hits 'Enter'.</li>
                            <li><code>puts(str)</code>: Displays a line of text and automatically adds a new line at the end.</li>
                        </ul>

                        <h2>8. Masterclass: scanf() and printf()</h2>
                        <p>These are the most powerful I/O functions because they are 'formatted'. They use <strong>Format Specifiers</strong> to handle different types of data.</p>
                        
                        <table style="width:100%; border-collapse: collapse; margin: 15px 0; background: white;">
                            <tr style="background: #2c3e50; color: white;">
                                <th style="padding: 10px; border: 1px solid #ddd;">Type</th>
                                <th style="padding: 10px; border: 1px solid #ddd;">Specifier</th>
                                <th style="padding: 10px; border: 1px solid #ddd;">Example Use</th>
                            </tr>
                            <tr><td style="padding: 10px; border: 1px solid #ddd;">Integer</td><td style="padding: 10px; border: 1px solid #ddd;">%d</td><td style="padding: 10px; border: 1px solid #ddd;">scanf("%d", &age);</td></tr>
                            <tr><td style="padding: 10px; border: 1px solid #ddd;">Float</td><td style="padding: 10px; border: 1px solid #ddd;">%f</td><td style="padding: 10px; border: 1px solid #ddd;">printf("Val: %f", pi);</td></tr>
                            <tr><td style="padding: 10px; border: 1px solid #ddd;">Character</td><td style="padding: 10px; border: 1px solid #ddd;">%c</td><td style="padding: 10px; border: 1px solid #ddd;">ch = getchar();</td></tr>
                            <tr><td style="padding: 10px; border: 1px solid #ddd;">String</td><td style="padding: 10px; border: 1px solid #ddd;">%s</td><td style="padding: 10px; border: 1px solid #ddd;">scanf("%s", name);</td></tr>
                        </table>

                        <div style="background: #fdf2f2; border: 1px solid #f5c6cb; padding: 15px; border-radius: 8px; margin: 15px 0;">
                            <strong>Crucial Concept: The '&' Operator</strong>
                            <br>In <code>scanf()</code>, you must use the <code>&</code> (Address Of) operator for numeric variables so the computer knows exactly which memory slot to fill. However, for <strong>Strings</strong>, the name of the string is already a memory address, so no <code>&</code> is needed!
                        </div>

                        <h2>9. Advanced Output Styling</h2>
                        <p>You can control the appearance of your output using field width and precision:</p>
                        <ul>
                            <li><strong>Width:</strong> <code>%10d</code> tells the computer to use 10 spaces to print the number (padding with spaces on the left).</li>
                            <li><strong>Leading Zeros:</strong> <code>%05d</code> prints <code>00025</code> instead of just <code>25</code>.</li>
                            <li><strong>Decimal Control:</strong> <code>%.3f</code> ensures only three digits appear after the decimal point.</li>
                        </ul>

                        <h2>10. Execution: How the Computer Processes Your Code</h2>
                        <p>The journey from a text file to a running program involves three critical steps:</p>
                        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin: 20px 0;">
                            <div style="background: #e1f5fe; padding: 10px; border-radius: 5px; border-top: 5px solid #03a9f4; text-align: center;">
                                <strong>Compile</strong><br>Translates .c to .obj (Object Code)
                            </div>
                            <div style="background: #f3e5f5; padding: 10px; border-radius: 5px; border-top: 5px solid #9c27b0; text-align: center;">
                                <strong>Link</strong><br>Joins .obj with Libraries to create .exe
                            </div>
                            <div style="background: #e8f5e9; padding: 10px; border-radius: 5px; border-top: 5px solid #4caf50; text-align: center;">
                                <strong>Run</strong><br>CPU executes the .exe instructions
                            </div>
                        </div>

                        <h2>11. Platform Specific Execution</h2>
                        <h3>A. Turbo C (DOS Path)</h3>
                        <p>Commonly used in legacy systems and academics. 
                        <br><strong>Shortcuts:</strong> <code>Alt+F9</code> (Compile), <code>Ctrl+F9</code> (Run), <code>Alt+F5</code> (Output Screen). 
                        <br><strong>Help:</strong> Highlight a word and press <code>Ctrl+F1</code>. 
                        <br><strong>Tracing:</strong> Press <code>F7</code> to watch the program execute line-by-line.</p>

                        <h3>B. Unix/Linux (The Developer's Home)</h3>
                        <p>C is at home here. Open the terminal and type:
                        <br><code>$ vi sum.c</code> (To create/edit)
                        <br><code>$ cc sum.c</code> (To compile)
                        <br><code>$ ./a.out</code> (To execute)
                        <br><strong>Note:</strong> If using <code>math.h</code>, compile with <code>cc sum.c -lm</code>.</p>

                        <h3>C. Visual Studio (The Professional IDE)</h3>
                        <p>Modern environment using 'Workspaces' and 'Projects'. Every program must be part of a project. Use the <strong>Build -> Execute</strong> menu to run. For programs needing inputs at start, use <strong>Project Settings -> Debug -> Program Arguments</strong>.</p>

                        <hr>

                        <div class="interview-prep" style="background: #fcfcfc; border: 1px solid #ddd; padding: 25px; border-radius: 12px; margin-top: 40px;">
                            <h2 style="color: #333; margin-top: 0; display: flex; align-items: center;">
                                <span style="font-size: 30px; margin-right: 10px;">🛡️</span> Career-Ready: Interview Intel
                            </h2>
                            
                            <div style="margin-bottom: 20px;">
                                <strong style="color: #d32f2f;">Q: What is a 'Garbage Value' in C?</strong>
                                <p><em>Ans:</em> When you declare a variable but do not initialize it (give it a value), it contains whatever data was left behind by a previous program in that memory location. This unpredictable data is called a garbage value.</p>
                            </div>

                            <div style="margin-bottom: 20px;">
                                <strong style="color: #d32f2f;">Q: Can you explain the difference between printf() and sprintf()?</strong>
                                <p><em>Ans:</em> <code>printf()</code> sends formatted text to the standard output device (the screen). <code>sprintf()</code> is used to format a string and save it into a character array (buffer) in memory, rather than displaying it.</p>
                            </div>

                            <div style="margin-bottom: 20px;">
                                <strong style="color: #d32f2f;">Q: What happens if you forget the '#' in #include?</strong>
                                <p><em>Ans:</em> The <code>#</code> is a Preprocessor Directive signal. Without it, the compiler treats the line as a normal statement and throws an error because <code>include</code> is not a valid C command or keyword.</p>
                            </div>

                            <div>
                                <strong style="color: #d32f2f;">Q: Why is 'main' special? Can we have multiple 'main' functions?</strong>
                                <p><em>Ans:</em> No, you can only have ONE <code>main</code> function per program. It serves as the unique entry point. If multiple <code>main</code> functions exist, the compiler will be unable to decide where to start execution.</p>
                            </div>
                        </div>
                    </div>
                """
            }
        ]
    }
]
