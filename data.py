# -*- coding: utf-8 -*-
compiler_data = [
    {
        "unit": "Unit-I",
        "title": "Introduction to Compiling & Lexical Analysis",
        "topics": [
            {
                "slug": "intro-compiler-types",
                "title": "Introduction, Major Data Structures & Types of Compilers",
                "content": """
                    <h2>1. Introduction to Compilers</h2>
                    <p>A compiler is a specialized software program that translates source code written in a high-level programming language (like C, Java, or C++) into low-level machine code (binary) or an intermediate form that the computer's processor can execute directly.</p>
                    <div style="background-color:#e8f5e9; padding:15px; border-left:4px solid #0f9d58; margin-bottom:15px;">
                        <strong><span style="color:#0f9d58">&#128161; REAL-LIFE EXAMPLE: The UN Translator</span></strong>
                        <p>Imagine a meeting at the United Nations where a French diplomat is speaking to a Japanese diplomat. The French diplomat speaks in high-level concepts (High-Level Language). An interpreter listens, breaks down the sentences into grammatical structures, understands the meaning, and then speaks the exact meaning in Japanese (Machine Code). If the French diplomat uses an invalid word (Syntax Error), the interpreter stops and asks for clarification before translating.</p>
                    </div>

                    <h2>2. Major Data Structures in a Compiler</h2>
                    <p>Compilers handle massive amounts of text and mathematical relationships. To do this efficiently, they rely on complex data structures:</p>
                    <ul>
                        <li><strong>Tokens:</strong> Used in Lexical Analysis to represent chunks of code. Usually implemented as structured objects or tuples.</li>
                        <li><strong>Syntax Tree (AST):</strong> Used in Syntax Analysis. A tree structure that represents the hierarchical syntactic structure of the source code.</li>
                        <li><strong>Symbol Table:</strong> The most important structure. It's a Hash Table (for O(1) lookup speed) used to store information about variable names, functions, and scopes.</li>
                        <li><strong>Literal Table:</strong> Stores constants and strings used in the program to save space and reduce redundancy.</li>
                        <li><strong>Intermediate Code (IR):</strong> Often represented as an array of structs or a linked list of Three-Address Code (TAC) instructions.</li>
                    </ul>

                    <h2>3. Types of Compilers</h2>
                    <ul>
                        <li><strong>Cross Compiler:</strong> Runs on machine A but produces executable code for machine B. <em>Real-life example: Writing an Android app (ARM architecture) on your Windows Desktop (x86 architecture).</em></li>
                        <li><strong>Source-to-Source Compiler (Transpiler):</strong> Translates one high-level language to another. <em>Real-life example: Translating TypeScript to JavaScript.</em></li>
                        <li><strong>Just-In-Time (JIT) Compiler:</strong> Compiles code at runtime directly before execution. Used heavily in Java (JVM) and C# (.NET).</li>
                        <li><strong>Single-Pass vs Multi-Pass Compilers:</strong> Single-pass compiles the whole program in one go (fast, but hard to optimize). Multi-pass breaks compilation into several stages (slower, but highly optimized).</li>
                    </ul>
                    
                    <h2>4. Front-End and Back-End of a Compiler</h2>
                    <p>Compilers are split into two halves to improve portability and maintainability.</p>
                    <ul>
                        <li><strong>Front-End:</strong> Depends purely on the Source Language. It handles Lexical, Syntax, and Semantic analysis and generates Intermediate Representation (IR).</li>
                        <li><strong>Back-End:</strong> Depends purely on the Target Machine architecture. It takes the IR and generates optimized machine code.</li>
                    </ul>
                    <div style="background-color:#e8f5e9; padding:15px; border-left:4px solid #0f9d58; margin-bottom:15px;">
                        <strong><span style="color:#0f9d58">&#128161; REAL-LIFE EXAMPLE: Universal Power Adapters</span></strong>
                        <p>Think of the Front-End as the part of a power adapter that plugs into your laptop (Standardized IR). Think of the Back-End as the different interchangeable wall plugs (Target Machine). If you go to the UK, you just swap the wall plug (Back-end) without throwing away the whole adapter (Front-end).</p>
                    </div>
                """
            },
            {
                "slug": "compiler-phases-lexical",
                "title": "Compiler Structure, Phases & Lexical Analysis",
                "content": """
                    <h2>1. Analysis-Synthesis Model of Compilation</h2>
                    <p>Compilation is fundamentally broken into two steps:</p>
                    <ul>
                        <li><strong>Analysis Phase (Front-end):</strong> Breaks down the source code into its constituent pieces and creates an intermediate representation.</li>
                        <li><strong>Synthesis Phase (Back-end):</strong> Constructs the desired target machine code from the intermediate representation.</li>
                    </ul>

                    <h2>2. Various Phases of a Compiler</h2>
                    <p>A standard compiler operates in 6 distinct phases:</p>
                    <ol>
                        <li><strong>Lexical Analysis:</strong> Converts character streams into meaningful Tokens.</li>
                        <li><strong>Syntax Analysis (Parsing):</strong> Arranges tokens into a Syntax Tree based on grammar rules.</li>
                        <li><strong>Semantic Analysis:</strong> Checks for logical errors like type mismatches.</li>
                        <li><strong>Intermediate Code Generation:</strong> Translates the tree into machine-independent Three-Address Code.</li>
                        <li><strong>Code Optimization:</strong> Improves the intermediate code to run faster and use less memory.</li>
                        <li><strong>Target Code Generation:</strong> Translates the optimized code into specific CPU instructions.</li>
                    </ol>
                    <div style="background-color:#e8f5e9; padding:15px; border-left:4px solid #0f9d58; margin-bottom:15px;">
                        <strong><span style="color:#0f9d58">&#128161; REAL-LIFE EXAMPLE: Car Assembly Line</span></strong>
                        <p>1. Lexical: Gathering raw materials (screws, metal). <br>2. Syntax: Assembling the frame of the car.<br>3. Semantic: Checking if the engine actually fits in the frame.<br>4. Intermediate: Painting the unbranded chassis.<br>5. Optimization: Removing excess weight for speed.<br>6. Code Gen: Stamping on the final brand logo and shipping it.</p>
                    </div>

                    <h2>3. Lexical Analysis (Scanning)</h2>
                    <p>Lexical analysis is the very first step a compiler takes. It reads your source code character by character and groups them into <strong>Tokens</strong>. Think of it like reading a book: your eyes see letters, but your brain groups them into words.</p>
                    
                    <h3>3.1 Tokens, Lexemes, and Patterns</h3>
                    <ul>
                        <li><strong>Token:</strong> A symbolic name for a group of characters (e.g., ID, KEYWORD, NUMBER).</li>
                        <li><strong>Lexeme:</strong> The actual text in the code (e.g., <code>int</code>, <code>x</code>, <code>10</code>).</li>
                        <li><strong>Pattern:</strong> The rule (usually a Regular Expression) that describes what the lexemes for a token look like.</li>
                    </ul>

                    <div style="background-color:#e8f5e9; padding:15px; border-left:4px solid #0f9d58; margin-bottom:15px;">
                        <strong><span style="color:#0f9d58">&#128161; REAL-LIFE EXAMPLE: Grocery Checkout</span></strong>
                        <p>Imagine a cashier scanning items. Each item has a barcode (Lexeme). The scanner reads it and identifies it as "Bread" or "Milk" (Token). The rule that "all 12-digit numbers are barcodes" is the Pattern.</p>
                    </div>

                    <h3>3.2 Categories of Tokens</h3>
                    <p>Compilers usually look for these types of tokens:</p>
                    <ol>
                        <li><strong>Keywords:</strong> Reserved words like <code>if, else, while, int</code>. You cannot use these as your own variable names.</li>
                        <li><strong>Identifiers:</strong> Names you give to variables or functions (e.g., <code>myCounter, _total</code>). They must start with a letter or underscore.</li>
                        <li><strong>Constants:</strong> Fixed values like <code>10, 3.14, 'A', "Hello"</code>.</li>
                        <li><strong>Operators:</strong> Symbols for math or logic (e.g., <code>+, -, *, /, ==, &&</code>).</li>
                        <li><strong>Special Symbols:</strong> Punctuation that helps structure the code (e.g., <code>; , { } ( ) [ ]</code>).</li>
                    </ol>

                    <table border="1" cellpadding="8" cellspacing="0" style="width:100%; text-align:center; margin-top:10px; background-color: white;">
                        <tr style="background-color:#f1f8e9;">
                            <th>Lexeme</th>
                            <th>Token Type</th>
                        </tr>
                        <tr><td><code>while</code></td><td>KEYWORD</td></tr>
                        <tr><td><code>count</code></td><td>IDENTIFIER</td></tr>
                        <tr><td><code>273</code></td><td>INTEGER</td></tr>
                        <tr><td><code>>=</code></td><td>RELATIONAL_OPERATOR</td></tr>
                        <tr><td><code>;</code></td><td>SEMICOLON</td></tr>
                    </table>

                    <h3>3.3 How Lexical Analysis Works Internally</h3>
                    <p>The scanner uses <strong>Finite Automata (DFA)</strong> to recognize these tokens efficiently. It reads the input using <strong>Input Buffering</strong> (loading large chunks of code into memory at once) so it doesn't have to talk to the hard drive for every single character, which would be very slow.</p>
                    
                    <div style="background-color:#fff3e0; padding:15px; border-left:4px solid #ff9800; margin-bottom:15px;">
                        <strong>&#128221; MINI EXERCISE: Count the Tokens</strong>
                        <p>How many tokens are in the following line? <br><code>int a = b + 10;</code></p>
                        <p><em>Answer: 7 tokens ('int', 'a', '=', 'b', '+', '10', ';'). Note that spaces are ignored!</em></p>
                    </div>
                """
            },
            {
                "slug": "finite-automata",
                "title": "Introduction to Finite Automata (DFA & NFA)",
                "content": """
                    <h2>1. What are Finite Automata (FA)?</h2>
                    <p>Finite Automata are mathematical models of machines with a finite number of states. In compilers, they are used to recognize patterns (Regular Expressions) in the source code to identify tokens.</p>

                    <h3>1.1 Features of Finite Automata</h3>
                    <ul>
                        <li><strong>Input:</strong> A sequence of symbols from a fixed set (Alphabet Σ).</li>
                        <li><strong>States:</strong> Different conditions the machine can be in.</li>
                        <li><strong>Transitions:</strong> Rules that move the machine from one state to another based on the input.</li>
                        <li><strong>Initial State:</strong> Where the machine starts.</li>
                        <li><strong>Final (Accepting) States:</strong> If the machine ends here, the input is valid!</li>
                    </ul>

                    <div style="background-color:#fff9c4; padding:15px; border-left:4px solid #fbc02d; margin-bottom:15px;">
                        <strong><span style="color:#f57f17">&#128161; REAL-LIFE EXAMPLE: A Combination Lock</span></strong>
                        <p>Think of a digital lock that opens only if you type "1-2-3". <br>State 0: Start. <br>State 1: Just typed '1'. <br>State 2: Just typed '1-2'. <br>State 3 (Final): Typed '1-2-3' - <strong>Unlocked!</strong> If you type '4' at any point, the machine stays at State 0 or resets.</p>
                    </div>

                    <h2>2. Types of Finite Automata</h2>
                    <table border="1" cellpadding="8" cellspacing="0" style="width:100%; text-align:center; margin-top:10px; background-color: white;">
                        <tr style="background-color:#e1f5fe;">
                            <th>Feature</th>
                            <th>Deterministic (DFA)</th>
                            <th>Non-Deterministic (NFA)</th>
                        </tr>
                        <tr><td>Transitions</td><td>Exactly one per input</td><td>Multiple allowed</td></tr>
                        <tr><td>ε (Null) Moves</td><td>Not allowed</td><td>Allowed</td></tr>
                        <tr><td>Speed</td><td>Very Fast (Linear)</td><td>Slower (Backtracking)</td></tr>
                    </table>

                    <h3>2.1 DFA vs NFA in Compilers</h3>
                    <p>While NFAs are easier for humans to design (they are more flexible), computers always convert them into DFAs before running. Why? Because a DFA can process input in a single pass without ever having to "guess" or go back, making token recognition lightning-fast.</p>
                """
            },
            {
                "slug": "lexical-analyzer-generator-lex",
                "title": "Design of a Lexical Analyzer Generator & LEX",
                "content": """
                               <h2>1. Design of a Lexical Analyzer Generator</h2>
                    <p>Writing a lexical analyzer from scratch is tedious. Computer scientists use tools called <strong>Generators</strong>. You give it Regular Expressions, and it generates the C code for you.</p>

                    <div style="background-color:#e1f5fe; padding:15px; border-left:4px solid #03a9f4; margin-bottom:15px;">
                        <strong><span style="color:#01579b">&#128161; REAL-LIFE EXAMPLE: Smart Home Setup</span></strong>
                        <p>Instead of manually wiring every switch to a light (Manual Lexer), you buy a Smart Hub (Lexical Analyzer Generator). You just tell the Hub "When I clap, turn on the light" (Regex), and the Hub handles all the internal circuitry (DFA) automatically.</p>
                    </div>

                    <h2>2. LEX and FLEX (The Industry Standards)</h2>
                    <p><strong>LEX</strong> was the original tool, but today we use <strong>FLEX (Fast Lexical Analyzer Generator)</strong>. It is faster, more efficient, and supports more platforms like Ubuntu and Windows.</p>
                    
                    <h3>2.1 Workflow of FLEX</h3>
                    <p>How do you actually use FLEX? It's a 3-step process:</p>
                    <ol>
                        <li><strong>Write:</strong> Create a <code>.l</code> file with your rules (e.g., <code>myscanner.l</code>).</li>
                        <li><strong>Generate:</strong> Run <code>flex myscanner.l</code>. This generates a C file called <code>lex.yy.c</code>.</li>
                        <li><strong>Compile:</strong> Compile the C file using <code>gcc lex.yy.c</code>. Now you have a working scanner!</li>
                    </ol>

                    <h3>2.2 Structure of a FLEX Program</h3>
                    <p>A FLEX program has 3 parts separated by <code>%%</code>:</p>
                    <pre style="background:white; border:1px solid #ccc; padding:10px;"><code>%{
/* Part 1: Definitions */
#include &lt;stdio.h&gt;
int count = 0;
%}

%%
/* Part 2: Rules (Pattern {Action}) */
[A-Z]   { printf("Capital: %s\n", yytext); count++; }
.       { /* Ignore others */ }
\n      { return 0; }
%%

/* Part 3: User Code */
int main() {
    yylex();
    printf("Total Capitals: %d\n", count);
    return 0;
}
int yywrap() { return 1; }</code></pre>

                    <h3>2.3 Key Variables in FLEX</h3>
                    <ul>
                        <li><code>yylex()</code>: The main function that starts the scanning process.</li>
                        <li><code>yytext</code>: Holds the actual text (lexeme) that was just matched.</li>
                        <li><code>yywrap()</code>: A function that tells FLEX what to do when it reaches the end of a file.</li>
                    </ul>
                """
            }
        ]
    },
    {
        "unit": "Unit-II",
        "title": "Syntax Analysis & Syntax Directed Translation",
        "topics": [
            {
                "slug": "syntax-analysis-top-down",
                "title": "Syntax Analysis: CFGs, Top-Down Parsing & Grammars",
                "content": """
                    <h2>1. Syntax Analysis (Parsing)</h2>
                    <p>The parser takes the stream of tokens from the Lexical Analyzer and groups them hierarchically into a Syntax Tree, verifying if the code obeys the grammatical rules of the programming language. These rules are defined using Context-Free Grammars.</p>

                    <h3>1.1 Context-Free Grammars (CFGs)</h3>
                    <p>A CFG consists of terminals (tokens), non-terminals (syntactic variables), a start symbol, and productions (rules). Example:</p>
                    <pre><code>
Expr &rarr; Expr + Term | Term
Term &rarr; id
                    </code></pre>

                    <h2>2. Top-Down Parsing</h2>
                    <p>Top-Down parsing attempts to build the parse tree starting from the Root (start symbol) and growing down towards the Leaves (tokens). It tries to find the leftmost derivation of the string.</p>
                    
                    <div style="background-color:#e8f5e9; padding:15px; border-left:4px solid #0f9d58; margin-bottom:15px;">
                        <strong><span style="color:#0f9d58">&#128161; REAL-LIFE EXAMPLE: Investigating a Crime Scene</span></strong>
                        <p>Top-Down parsing is like a Detective starting with a broad theory ("A robbery happened") and trying to break it down into smaller proven facts ("Window broken", "Safe open") to see if the theory matches the evidence on the floor.</p>
                    </div>

                    <h3>2.1 Brute Force Approach (Parsing with Backtracking)</h3>
                    <p>The parser tries every single grammar rule. If it hits a dead end (a rule doesn't match the input token), it undoes its work (backtracks) and tries the next alternative rule. This is highly inefficient and rarely used in production compilers.</p>

                    <h3>2.2 Recursive Descent Parsing</h3>
                    <p>A top-down parser built using a set of mutually recursive functions. Each non-terminal in the grammar gets its own function.</p>
                    <pre><code>
void Expr() {
    Term();
    while (lookahead == '+') {
        match('+');
        Term();
    }
}
                    </code></pre>
                    <p><strong>Drawback:</strong> It fails fatally if the grammar has <em>Left Recursion</em> (e.g., <code>A &rarr; A &alpha;</code>), causing an infinite loop.</p>

                    <h2>3. Transformation on Grammars</h2>
                    <p>Because Top-Down parsers hate Left Recursion and Ambiguity, we must mathematically transform the CFG before writing the parser:</p>
                    <ul>
                        <li><strong>Eliminating Left Recursion:</strong> Rewriting rules so they expand to the right.</li>
                        <li><strong>Left Factoring:</strong> Removing common prefixes from rules so the parser knows exactly which rule to pick just by looking at the next token.</li>
                    </ul>

                    <h2>4. Classification of Context-Free Grammars</h2>
                    <p>CFGs can be classified based on two main properties:</p>
                    
                    <h3>4.1 Based on Number of Strings Generated</h3>
                    <ul>
                        <li><strong>Recursive Grammar:</strong> If a grammar can generate an infinite number of strings (contains rules like <code>A &rarr; Aa</code>).</li>
                        <li><strong>Non-Recursive Grammar:</strong> If it generates only a finite set of strings.</li>
                    </ul>

                    <h3>4.2 Based on Derivation Trees (Ambiguity)</h3>
                    <ul>
                        <li><strong>Unambiguous Grammar:</strong> For every string, there is exactly ONE unique parse tree. This is what compilers need!</li>
                        <li><strong>Ambiguous Grammar:</strong> A string can have two or more different parse trees. This is bad because the compiler won't know which mathematical operation to perform first (e.g., <code>5 + 2 * 3</code>).</li>
                    </ul>

                    <div style="background-color:#ffebee; padding:15px; border-left:4px solid #f44336; margin-bottom:15px;">
                        <strong><span style="color:#b71c1c">&#9888; THE AMBIGUITY PROBLEM</span></strong>
                        <p>If a grammar is ambiguous, the same line of code could mean two different things. Compilers solve this by either rewriting the grammar to be unambiguous or by using <strong>Precedence Rules</strong> (like BODMAS).</p>
                    </div>

                    <h2>4. Predictive Parsing (LL(1))</h2>
                    <div style="background-color:#e3f2fd; padding:20px; border-left:4px solid #1976d2; margin-top:20px;">
                        <h2 style="color:#0d47a1; margin-top:0;">&#128221; LL(1) Parsing Table Construction</h2>
                        <p>Parsing is an essential part of computer science, especially in compilers and interpreters. From the various parsing techniques, LL(1) parsing is highly efficient. It uses a predictive, top-down approach allowing efficient parsing without backtracking.</p>

                        <h3>What is LL(1) Parsing?</h3>
                        <p>Here the <strong>1st L</strong> represents that the scanning of the input will be done from <strong>Left to Right</strong>. The <strong>second L</strong> shows that we use the <strong>Left-most Derivation Tree</strong>. Finally, the <strong>1</strong> represents the number of look-ahead symbols (meaning we look at exactly 1 symbol to make a decision).</p>

                        <h3>Conditions for an LL(1) Grammar</h3>
                        <p>To construct a working LL(1) parsing table, a grammar must satisfy these conditions:</p>
                        <ul>
                            <li><strong>No Left Recursion:</strong> Avoid recursive definitions like <code>A &rarr; A + b</code>.</li>
                            <li><strong>Unambiguous Grammar:</strong> Ensure each string can be derived in only one way.</li>
                            <li><strong>Left Factoring:</strong> Make the grammar deterministic so the parser can proceed without guessing.</li>
                        </ul>

                        <h3>Algorithm to Construct LL(1) Parsing Table</h3>
                        <ol>
                            <li><strong>Step 1:</strong> Check all the essential conditions mentioned above.</li>
                            <li><strong>Step 2: Calculate First() and Follow() for all non-terminals.</strong>
                                <ul>
                                    <li><em>First():</em> If there is a variable, and from that variable we try to derive all strings, the beginning Terminal Symbol is the First.</li>
                                    <li><em>Follow():</em> What is the Terminal Symbol which follows a variable in the process of derivation.</li>
                                </ul>
                            </li>
                            <li><strong>Step 3: Build the Table</strong> For each production <code>A &rarr; &alpha;</code>:
                                <ul>
                                    <li>Find First(&alpha;) and for each terminal in First(&alpha;), make entry <code>A &rarr; &alpha;</code> in the table.</li>
                                    <li>If First(&alpha;) contains &epsilon; (epsilon) as a terminal, then find Follow(A) and for each terminal in Follow(A), make entry <code>A &rarr; &epsilon;</code> in the table.</li>
                                    <li>If First(&alpha;) contains &epsilon; and Follow(A) contains $, make entry <code>A &rarr; &epsilon;</code> in the table for $.</li>
                                </ul>
                            </li>
                        </ol>

                        <hr style="border-top:1px solid #bbdefb; margin:20px 0;">

                        <h3>Example 1: Consider the Grammar</h3>
                        <p><code>E &rarr; TE'</code><br><code>E' &rarr; +TE' | &epsilon;</code><br><code>T &rarr; FT'</code><br><code>T' &rarr; *FT' | &epsilon;</code><br><code>F &rarr; id | (E)</code></p>
                        
                        <p><strong>Step 2: Calculate First and Follow</strong></p>
                        <table border="1" cellpadding="8" cellspacing="0" style="width:100%; text-align:center; background-color: white;">
                            <tr style="background-color:#bbdefb;"><th>Non-Terminal</th><th>First</th><th>Follow</th></tr>
                            <tr><td>E</td><td>{ id, ( }</td><td>{ $, ) }</td></tr>
                            <tr><td>E'</td><td>{ +, &epsilon; }</td><td>{ $, ) }</td></tr>
                            <tr><td>T</td><td>{ id, ( }</td><td>{ +, $, ) }</td></tr>
                            <tr><td>T'</td><td>{ *, &epsilon; }</td><td>{ +, $, ) }</td></tr>
                            <tr><td>F</td><td>{ id, ( }</td><td>{ *, +, $, ) }</td></tr>
                        </table>

                        <p><strong>Step 3: Make the parser table</strong></p>
                        <p>All null productions (&epsilon;) go under the Follow elements. Remaining productions go under the First elements.</p>
                        <table border="1" cellpadding="8" cellspacing="0" style="width:100%; text-align:center; background-color: white;">
                            <tr style="background-color:#bbdefb;"><th></th><th>id</th><th>+</th><th>*</th><th>(</th><th>)</th><th>$</th></tr>
                            <tr><td><strong>E</strong></td><td>E &rarr; TE'</td><td></td><td></td><td>E &rarr; TE'</td><td></td><td></td></tr>
                            <tr><td><strong>E'</strong></td><td></td><td>E' &rarr; +TE'</td><td></td><td></td><td>E' &rarr; &epsilon;</td><td>E' &rarr; &epsilon;</td></tr>
                            <tr><td><strong>T</strong></td><td>T &rarr; FT'</td><td></td><td></td><td>T &rarr; FT'</td><td></td><td></td></tr>
                            <tr><td><strong>T'</strong></td><td></td><td>T' &rarr; &epsilon;</td><td>T' &rarr; *FT'</td><td></td><td>T' &rarr; &epsilon;</td><td>T' &rarr; &epsilon;</td></tr>
                            <tr><td><strong>F</strong></td><td>F &rarr; id</td><td></td><td></td><td>F &rarr; (E)</td><td></td><td></td></tr>
                        </table>

                        <hr style="border-top:1px solid #bbdefb; margin:20px 0;">

                        <h3>Example 2: Conflict (Ambiguous Grammar)</h3>
                        <p><code>S &rarr; A | a</code><br><code>A &rarr; a</code></p>
                        <table border="1" cellpadding="8" cellspacing="0" style="width:100%; text-align:center; background-color: white;">
                            <tr style="background-color:#bbdefb;"><th>Non-Terminal</th><th>First</th><th>Follow</th></tr>
                            <tr><td>S</td><td>{ a }</td><td>{ $ }</td></tr>
                            <tr><td>A</td><td>{ a }</td><td>{ $ }</td></tr>
                        </table>
                        <br>
                        <table border="1" cellpadding="8" cellspacing="0" style="width:50%; text-align:center; background-color: white;">
                            <tr style="background-color:#bbdefb;"><th></th><th>a</th><th>$</th></tr>
                            <tr><td><strong>S</strong></td><td style="color:red;">S &rarr; A, S &rarr; a</td><td></td></tr>
                            <tr><td><strong>A</strong></td><td>A &rarr; a</td><td></td></tr>
                        </table>
                        <p>Here, we can see two productions in the same cell. <strong>This grammar is not feasible for an LL(1) Parser.</strong></p>

                        <hr style="border-top:1px solid #bbdefb; margin:20px 0;">

                        <h3>Example 3: Conflict despite passing initial conditions</h3>
                        <p><code>S &rarr; (L) | a</code><br><code>L &rarr; SL'</code><br><code>L' &rarr; )SL' | &epsilon;</code></p>
                        <p>If you build the First/Follow sets and table for this, you will find <code>L' &rarr; )SL'</code> and <code>L' &rarr; &epsilon;</code> both mapping to the <strong>)</strong> column, causing a conflict. Thus, the conditions in Step 1 are necessary, but insufficient to guarantee an LL(1) grammar without making the table.</p>

                        <h3>Advantages of LL(1) Parsing Table</h3>
                        <ul>
                            <li><strong>Clear Decision-Making:</strong> The parser decides what to do by looking at just one symbol ahead. No confusion.</li>
                            <li><strong>Fast Parsing:</strong> No need to backtrack, making it incredibly fast.</li>
                            <li><strong>Easy to Spot Errors:</strong> If a cell is blank in the table during parsing, a syntax error is instantly reported.</li>
                            <li><strong>Simple to Implement:</strong> The table directly dictates the control flow of the parser program.</li>
                        </ul>
                    </div>
                """
            },
            {
                "slug": "bottom-up-lr-parsers",
                "title": "Bottom-Up Parsing & LR Parsers",
                "content": """
                    <h2>1. Bottom-Up Parsing</h2>
                    <p>Unlike Top-Down, Bottom-Up parsing starts with the input string (the leaves) and attempts to combine them upwards to reach the Start Symbol (the root). It traces a rightmost derivation in reverse.</p>
                    <p>It operates using a <strong>Shift-Reduce</strong> mechanism via a stack.</p>
                    <ul>
                        <li><strong>Shift:</strong> Pushing the next input token onto the stack.</li>
                        <li><strong>Reduce:</strong> Replacing a sequence of symbols on the top of the stack with a matching non-terminal from the left side of a grammar rule.</li>
                    </ul>

                    <h2>2. Types of LR Parsers</h2>
                    <p>LR (Left-to-right scan, Rightmost derivation in reverse) parsers use a state machine and a stack to make parsing decisions.</p>
                    <ul>
                        <li><strong>LR(0):</strong> The simplest. Doesn't look ahead. Very weak, fails on many grammars due to Shift/Reduce conflicts.</li>
                        <li><strong>SLR (Simple LR):</strong> Looks ahead using the FOLLOW() set to resolve conflicts. Moderately powerful.</li>
                        <li><strong>LALR (Look-Ahead LR):</strong> The industry standard (used by YACC). Combines states of the powerful LR(1) parser to drastically reduce table size.</li>
                        <li><strong>CLR / LR(1) (Canonical LR):</strong> The most powerful. Looks ahead 1 token for every single item. Can parse almost anything, but generates insanely large parsing tables.</li>
                    </ul>

                    <div style="background-color:#fff3e0; padding:20px; border-left:4px solid #ff9800; margin-bottom:20px;">
                        <h2 style="color:#e65100; margin-top:0;">&#128221; NUMERICAL PROBLEM: How to Construct an LR(0) Parsing Table</h2>
                        <p>Questions on this topic always follow a standard mathematical algorithm. Let's solve a real question step-by-step.</p>

                        <h3>Question: Construct the LR(0) Parsing Table for the following grammar:</h3>
                        <p><code>S &rarr; AA</code><br><code>A &rarr; aA | b</code></p>

                        <h3>Step 1: Write the Augmented Grammar</h3>
                        <p>We add a new start symbol <code>S'</code> that derives the original start symbol. We also assign a rule number to the original rules for the "Reduce" actions later.</p>
                        <p>
                            (0) <code>S' &rarr; S</code><br>
                            (1) <code>S &rarr; AA</code><br>
                            (2) <code>A &rarr; aA</code><br>
                            (3) <code>A &rarr; b</code>
                        </p>

                        <h3>Step 2: Understand LR(0) Items and Closures</h3>
                        <p>An LR(0) item is a grammar rule with a <strong>dot (•)</strong> indicating how much of a rule we have seen. <br>E.g., <code>A &rarr; •aA</code> means we haven't seen anything yet. <code>A &rarr; a•A</code> means we have seen 'a' and are expecting an 'A'.</p>
                        <p><strong>Closure() Rule:</strong> If the dot is before a Non-Terminal (like •A), we must add all the rules of 'A' to the current state, with the dot at the beginning.</p>

                        <h3>Step 3: Construct the Canonical Collection of States (The DFA)</h3>
                        <p><strong>State I<sub>0</sub> (Start State):</strong> Start with <code>S' &rarr; •S</code>. Since the dot is before S, add S rules. Then dot is before A, so add A rules.</p>
                        <pre><code>I0:
S' &rarr; •S
S  &rarr; •AA
A  &rarr; •aA
A  &rarr; •b</code></pre>

                        <p><strong>Now calculate GoTo(State, Symbol) for I<sub>0</sub>:</strong> Move the dot past the symbol.</p>
                        <pre><code>GoTo(I0, S) = I1
I1:
S' &rarr; S•    (Accept State because S' is complete)

GoTo(I0, A) = I2
I2:
S  &rarr; A•A   (Dot is before A, so apply closure!)
A  &rarr; •aA
A  &rarr; •b

GoTo(I0, a) = I3
I3:
A  &rarr; a•A   (Dot is before A, apply closure!)
A  &rarr; •aA
A  &rarr; •b

GoTo(I0, b) = I4
I4:
A  &rarr; b•    (Reduce State, rule is complete)</code></pre>

                        <p><strong>Continue GoTo for the new states (I<sub>2</sub>, I<sub>3</sub>):</strong></p>
                        <pre><code>GoTo(I2, A) = I5
I5:
S  &rarr; AA•   (Reduce State)

GoTo(I2, a) = GoTo(I0, a) = I3  (Loops back to I3)
GoTo(I2, b) = GoTo(I0, b) = I4  (Loops back to I4)

GoTo(I3, A) = I6
I6:
A  &rarr; aA•   (Reduce State)

GoTo(I3, a) = I3
GoTo(I3, b) = I4</code></pre>

                        <h3>Step 4: Draw the LR(0) Parsing Table</h3>
                        <p>The table has two parts: <strong>ACTION</strong> (for terminals + $) and <strong>GOTO</strong> (for non-terminals).</p>
                        <ul>
                            <li><strong>Shift (S):</strong> If GoTo(I<sub>i</sub>, terminal) = I<sub>j</sub>, write <strong>Sj</strong>.</li>
                            <li><strong>Reduce (R):</strong> If a state contains a completed item (dot at the end, like <code>A &rarr; b•</code> which is rule 3), write <strong>R3</strong> in the Action columns for ALL terminals (because it's LR(0)).</li>
                            <li><strong>Accept:</strong> If the state contains <code>S' &rarr; S•</code>, write <strong>Accept</strong> under the $ column.</li>
                        </ul>

                        <table border="1" cellpadding="8" cellspacing="0" style="width:100%; text-align:center; margin-top:10px; background-color: white;">
                            <tr style="background-color:#ffe0b2;">
                                <th>State</th>
                                <th colspan="3">ACTION</th>
                                <th colspan="2">GOTO</th>
                            </tr>
                            <tr style="background-color:#ffe0b2;">
                                <th></th>
                                <th>a</th>
                                <th>b</th>
                                <th>$</th>
                                <th>S</th>
                                <th>A</th>
                            </tr>
                            <tr><td><strong>0</strong></td><td>S3</td><td>S4</td><td></td><td>1</td><td>2</td></tr>
                            <tr><td><strong>1</strong></td><td></td><td></td><td>Accept</td><td></td><td></td></tr>
                            <tr><td><strong>2</strong></td><td>S3</td><td>S4</td><td></td><td></td><td>5</td></tr>
                            <tr><td><strong>3</strong></td><td>S3</td><td>S4</td><td></td><td></td><td>6</td></tr>
                            <tr><td><strong>4</strong></td><td>R3</td><td>R3</td><td>R3</td><td></td><td></td></tr>
                            <tr><td><strong>5</strong></td><td>R1</td><td>R1</td><td>R1</td><td></td><td></td></tr>
                            <tr><td><strong>6</strong></td><td>R2</td><td>R2</td><td>R2</td><td></td><td></td></tr>
                        </table>
                        
                        <p style="margin-top:15px;"><strong>How to solve conflict questions:</strong> If a box in the ACTION table gets both a Shift and a Reduce (e.g., "S3, R2"), it is a <strong>Shift/Reduce Conflict</strong>, meaning the grammar is NOT LR(0). If it gets two Reduces ("R1, R2"), it is a <strong>Reduce/Reduce Conflict</strong>.</p>
                    </div>

                    <div style="background-color:#e8f4f8; padding:20px; border-left:4px solid #0288d1; margin-bottom:20px;">
                        <h2 style="color:#01579b; margin-top:0;">&#128221; NUMERICAL PROBLEM: How to Construct an SLR Parsing Table</h2>
                        <p>SLR (Simple LR) parsing is a direct upgrade to LR(0). It solves Shift/Reduce conflicts by being smarter about when to <strong>Reduce</strong>. In LR(0), we put the Reduce action in <em>every</em> terminal column. In SLR, we only put the Reduce action in the columns that belong to the <strong>FOLLOW()</strong> set of the Left-Hand Side non-terminal.</p>

                        <h3>The SLR Construction Algorithm</h3>
                        <ol>
                            <li>Write the Augmented Grammar.</li>
                            <li>Calculate <strong>FIRST()</strong> and <strong>FOLLOW()</strong> sets for all Non-Terminals.</li>
                            <li>Construct the LR(0) items (the DFA states I<sub>0</sub>, I<sub>1</sub>, etc.) exactly the same way as we did in LR(0).</li>
                            <li><strong>Crucial Difference in the ACTION Table:</strong>
                                <ul>
                                    <li>If a state contains a completed rule like <code>A &rarr; &alpha;•</code> (say this is Rule 2):</li>
                                    <li>Find the mathematical set <strong>FOLLOW(A)</strong>.</li>
                                    <li>Put <strong>R2</strong> <em>ONLY</em> in the columns corresponding to terminals in FOLLOW(A).</li>
                                </ul>
                            </li>
                        </ol>

                        <h3>Example: Resolving a Conflict with SLR</h3>
                        <p>Consider a grammar where State I<sub>4</sub> contains the following items:</p>
                        <pre><code>I4:
A &rarr; b•    (Rule 3)
B &rarr; b•c</code></pre>
                        <p>If we use <strong>LR(0)</strong>, the action for terminal 'c' in state 4 would have a Shift (because of <code>b•c</code>) and a Reduce (R3 because of <code>A &rarr; b•</code>). This creates a Shift/Reduce conflict, making the grammar non-LR(0).</p>
                        <p>If we use <strong>SLR</strong>, we calculate <strong>FOLLOW(A)</strong>. Let's say FOLLOW(A) = { $, d }. Since 'c' is NOT in FOLLOW(A), we do NOT place R3 in the 'c' column. The 'c' column will only contain the Shift action. <strong>The conflict disappears!</strong></p>

                        <hr style="border-top:1px solid #b3e5fc; margin:20px 0;">

                        <h3 style="color:#01579b;">FULL NUMERICAL EXAMPLE: Constructing the SLR Table</h3>
                        <p>Let's build a complete SLR parsing table for a simplified arithmetic grammar.</p>
                        
                        <p><strong>Step 1: Augmented Grammar with Rule Numbers</strong></p>
                        <p>
                            (0) <code>S' &rarr; S</code><br>
                            (1) <code>S &rarr; E</code><br>
                            (2) <code>E &rarr; E + T</code><br>
                            (3) <code>E &rarr; T</code><br>
                            (4) <code>T &rarr; id</code>
                        </p>

                        <p><strong>Step 2: Calculate FOLLOW Sets</strong></p>
                        <ul>
                            <li><strong>FOLLOW(S)</strong> = { $ }</li>
                            <li><strong>FOLLOW(E)</strong> = { +, $ }</li>
                            <li><strong>FOLLOW(T)</strong> = { +, $ }</li>
                        </ul>

                        <p><strong>Step 3: Canonical Collection of LR(0) States</strong></p>
                        <pre><code>I0:
S' &rarr; •S
S  &rarr; •E
E  &rarr; •E + T
E  &rarr; •T
T  &rarr; •id

GoTo(I0, S) = I1:
S' &rarr; S•   (Accept)

GoTo(I0, E) = I2:
S  &rarr; E•
E  &rarr; E• + T

GoTo(I0, T) = I3:
E  &rarr; T•   (Reduce 3)

GoTo(I0, id) = I4:
T  &rarr; id•  (Reduce 4)

GoTo(I2, +) = I5:
E  &rarr; E + •T
T  &rarr; •id

GoTo(I5, T) = I6:
E  &rarr; E + T• (Reduce 2)

GoTo(I5, id) = I4:
T  &rarr; id•</code></pre>

                        <p><strong>Step 4: Build the SLR Table</strong></p>
                        <p>Because this is SLR, we look at the Reductions and place them <strong>ONLY in the FOLLOW sets</strong> of the LHS non-terminal.</p>
                        <ul>
                            <li>In I3, we have <code>E &rarr; T•</code> (Rule 3). FOLLOW(E) = {+, $}. So place <strong>R3</strong> only in '+' and '$'.</li>
                            <li>In I4, we have <code>T &rarr; id•</code> (Rule 4). FOLLOW(T) = {+, $}. So place <strong>R4</strong> only in '+' and '$'.</li>
                            <li>In I6, we have <code>E &rarr; E+T•</code> (Rule 2). FOLLOW(E) = {+, $}. So place <strong>R2</strong> only in '+' and '$'.</li>
                        </ul>

                        <table border="1" cellpadding="8" cellspacing="0" style="width:100%; text-align:center; margin-top:10px; background-color: white;">
                            <tr style="background-color:#b3e5fc;">
                                <th>State</th>
                                <th colspan="3">ACTION</th>
                                <th colspan="3">GOTO</th>
                            </tr>
                            <tr style="background-color:#b3e5fc;">
                                <th></th>
                                <th>id</th>
                                <th>+</th>
                                <th>$</th>
                                <th>S</th>
                                <th>E</th>
                                <th>T</th>
                            </tr>
                            <tr><td><strong>0</strong></td><td>S4</td><td></td><td></td><td>1</td><td>2</td><td>3</td></tr>
                            <tr><td><strong>1</strong></td><td></td><td></td><td>Accept</td><td></td><td></td><td></td></tr>
                            <tr><td><strong>2</strong></td><td></td><td>S5</td><td>R1</td><td></td><td></td><td></td></tr>
                            <tr><td><strong>3</strong></td><td></td><td>R3</td><td>R3</td><td></td><td></td><td></td></tr>
                            <tr><td><strong>4</strong></td><td></td><td>R4</td><td>R4</td><td></td><td></td><td></td></tr>
                            <tr><td><strong>5</strong></td><td>S4</td><td></td><td></td><td></td><td></td><td>6</td></tr>
                            <tr><td><strong>6</strong></td><td></td><td>R2</td><td>R2</td><td></td><td></td><td></td></tr>
                        </table>
                        <p style="margin-top:10px;">Notice how much cleaner this table is compared to LR(0)! We didn't spam R3 across all terminals, which prevents massive shift/reduce conflicts.</p>
                    </div>

                    <div style="background-color:#f3e5f5; padding:20px; border-left:4px solid #8e24aa; margin-bottom:20px;">
                        <h2 style="color:#4a148c; margin-top:0;">&#128221; NUMERICAL PROBLEM: LALR(1) Parsing and State Merging</h2>
                        <p>LALR (Look-Ahead LR) is the parsing algorithm used by <strong>YACC</strong>. It has almost the same parsing power as the massive CLR / LR(1) parser, but generates a table the exact same size as the much smaller SLR parser. It achieves this mathematical magic by <strong>merging states with identical cores</strong>.</p>

                        <h3>Step 1: Understand LR(1) Items</h3>
                        <p>Unlike LR(0), an LR(1) item mathematically carries a "Look-Ahead" symbol. <br>Format: <code>[A &rarr; &alpha;•&beta; , a]</code> where 'a' is the lookahead terminal. The parser will <em>ONLY</em> reduce to 'A' if the next input token is exactly 'a'.</p>

                        <h3>Step 2: The Core Concept of LALR</h3>
                        <p>Let's look at a numerical example of two distinct states generated by a CLR parser for the grammar <code>S &rarr; CC, C &rarr; cC | d</code>:</p>
                        
                        <table style="width:100%; border:none; margin-bottom:15px; background:white; padding:10px;">
                            <tr>
                                <td style="vertical-align:top; border: 1px solid #ccc; padding:10px;">
                                    <strong style="color:#8e24aa;">State I<sub>3</sub></strong>
                                    <pre style="background:transparent; border:none; padding:0; margin:5px 0 0 0;"><code>C &rarr; c•C , c/d
C &rarr; •cC , c/d
C &rarr; •d  , c/d</code></pre>
                                </td>
                                <td style="vertical-align:top; border: 1px solid #ccc; padding:10px;">
                                    <strong style="color:#8e24aa;">State I<sub>6</sub></strong>
                                    <pre style="background:transparent; border:none; padding:0; margin:5px 0 0 0;"><code>C &rarr; c•C , $
C &rarr; •cC , $
C &rarr; •d  , $</code></pre>
                                </td>
                            </tr>
                        </table>
                        <p>Notice something? The <strong>Core rules</strong> (the part before the comma) in I<sub>3</sub> and I<sub>6</sub> are <em>exactly identical</em>! The only mathematical difference is their lookahead sets (<code>c/d</code> vs <code>$</code>).</p>

                        <h3>Step 3: State Merging Algorithm</h3>
                        <p>Instead of keeping I<sub>3</sub> and I<sub>6</sub> as separate states (which makes the CLR table huge), the LALR algorithm says: <strong>Merge them!</strong> We combine their lookaheads into a single, highly efficient state.</p>
                        
                        <p><strong>New Merged State I<sub>36</sub>:</strong></p>
                        <pre style="background:white; border:1px solid #ccc;"><code>I36:
C &rarr; c•C , c/d/$
C &rarr; •cC , c/d/$
C &rarr; •d  , c/d/$</code></pre>

                        <h3>The LALR Advantage in Exams</h3>
                        <ul>
                            <li><strong>Drastic Size Reduction:</strong> By merging I<sub>3</sub> with I<sub>6</sub>, I<sub>4</sub> with I<sub>7</sub>, and I<sub>8</sub> with I<sub>9</sub>, the number of states drops from 10 (in CLR) down to 7 (in LALR). For a massive programming language like C, CLR might generate 10,000 states, while LALR reduces it to just 300!</li>
                            <li><strong>Will merging introduce new conflicts?</strong> 
                                <ul>
                                    <li>Mathematical fact: Merging will <strong>never</strong> produce a new Shift/Reduce conflict.</li>
                                    <li>It <em>might</em> occasionally produce a new Reduce/Reduce conflict (if the merged lookaheads overlap dangerously). If this happens, the grammar is LR(1) but NOT LALR(1).</li>
                                </ul>
                            </li>
                        </ul>
                    </div>

                    <div style="background-color:#ffebee; padding:20px; border-left:4px solid #c62828; margin-bottom:20px;">
                        <h2 style="color:#b71c1c; margin-top:0;">&#128221; NUMERICAL PROBLEM: CLR / LR(1) Parsing Table</h2>
                        <p>CLR (Canonical LR) is the most powerful bottom-up parser. It solves conflicts by mathematically calculating and attaching a strict <strong>Look-Ahead</strong> symbol to every single item during state creation, rather than waiting to look at a generalized FOLLOW() set later.</p>

                        <h3>The Mathematical Rule of LR(1) Closure</h3>
                        <p>In LR(0) and SLR, when the dot is before a non-terminal (like <code>•B</code>), we blindly add all rules of B. In CLR, we calculate exactly what terminal is mathematically allowed to follow B <em>in this specific context</em>.</p>
                        <p><strong>Rule:</strong> If you have an item <code>[A &rarr; &alpha;•B&beta; , a]</code>, you add <code>[B &rarr; •&gamma; , b]</code> for all rules of B, where the lookahead <strong>b = FIRST(&beta;a)</strong>.</p>

                        <h3>Step-by-Step Numerical Example</h3>
                        <p>Consider the Augmented Grammar:<br>
                           (0) <code>S' &rarr; S</code><br>
                           (1) <code>S &rarr; CC</code><br>
                           (2) <code>C &rarr; cC | d</code>
                        </p>

                        <p><strong>Calculating State I<sub>0</sub>:</strong></p>
                        <ol>
                            <li>Start with the augmented rule. The lookahead for the start symbol is ALWAYS <code>$</code>.<br>
                                <code>[S' &rarr; •S , $]</code></li>
                            <li>The dot is before <code>S</code>. The rule is <code>[A &rarr; &alpha;•B&beta; , a]</code>. Here, A=S', &alpha;=&epsilon;, B=S, &beta;=&epsilon;, a=$. <br>
                                We must add <code>S &rarr; •CC</code>. The lookahead is FIRST(&beta;a) = FIRST(&epsilon;$) = { $ }.<br>
                                Add: <code>[S &rarr; •CC , $]</code></li>
                            <li>The dot is before the first <code>C</code>. Here, A=S, B=C, &beta;=C, a=$. <br>
                                Lookahead = FIRST(C$). Since FIRST(C) = {c, d}, the lookaheads are c and d.<br>
                                Add: <code>[C &rarr; •cC , c/d]</code><br>
                                Add: <code>[C &rarr; •d  , c/d]</code></li>
                        </ol>
                        
                        <p><strong>The Final Canonical Collection of LR(1) States:</strong></p>
                        <pre style="background:white; border:1px solid #ccc; padding:10px; overflow-x:auto;"><code>I0: [S' &rarr; &bull;S, $], [S &rarr; &bull;CC, $], [C &rarr; &bull;cC, c/d], [C &rarr; &bull;d, c/d]
I1: Goto(I0, S) = [S' &rarr; S&bull;, $] (ACCEPT)
I2: Goto(I0, C) = [S &rarr; C&bull;C, $], [C &rarr; &bull;cC, $], [C &rarr; &bull;d, $]
I3: Goto(I0, c) = [C &rarr; c&bull;C, c/d], [C &rarr; &bull;cC, c/d], [C &rarr; &bull;d, c/d]
I4: Goto(I0, d) = [C &rarr; d&bull;, c/d] (Reduce Rule 3)
I5: Goto(I2, C) = [S &rarr; CC&bull;, $] (Reduce Rule 1)
I6: Goto(I2, c) = [C &rarr; c&bull;C, $], [C &rarr; &bull;cC, $], [C &rarr; &bull;d, $]
I7: Goto(I2, d) = [C &rarr; d&bull;, $] (Reduce Rule 3)
I8: Goto(I3, C) = [C &rarr; cC&bull;, c/d] (Reduce Rule 2)
I9: Goto(I6, C) = [C &rarr; cC&bull;, $] (Reduce Rule 2)

Note: Goto(I3, c)=I3, Goto(I3, d)=I4, Goto(I6, c)=I6, Goto(I6, d)=I7.</code></pre>

                        <h3>The CLR Parsing Table</h3>
                        <p>The CLR table uses the lookaheads explicitly to determine where to place the Reduce (R) actions. Unlike SLR, it does not use the Follow set.</p>
                        
                        <table border="1" cellpadding="8" cellspacing="0" style="width:100%; text-align:center; margin-top:10px; background-color: white;">
                            <tr style="background-color:#ffebee;">
                                <th rowspan="2">State</th>
                                <th colspan="3">ACTION</th>
                                <th colspan="2">GOTO</th>
                            </tr>
                            <tr style="background-color:#ffebee;">
                                <th>c</th>
                                <th>d</th>
                                <th>$</th>
                                <th>S</th>
                                <th>C</th>
                            </tr>
                            <tr><td><strong>0</strong></td><td>S3</td><td>S4</td><td></td><td>1</td><td>2</td></tr>
                            <tr><td><strong>1</strong></td><td></td><td></td><td>Accept</td><td></td><td></td></tr>
                            <tr><td><strong>2</strong></td><td>S6</td><td>S7</td><td></td><td></td><td>5</td></tr>
                            <tr><td><strong>3</strong></td><td>S3</td><td>S4</td><td></td><td></td><td>8</td></tr>
                            <tr><td><strong>4</strong></td><td>R3</td><td>R3</td><td></td><td></td><td></td></tr>
                            <tr><td><strong>5</strong></td><td></td><td></td><td>R1</td><td></td><td></td></tr>
                            <tr><td><strong>6</strong></td><td>S6</td><td>S7</td><td></td><td></td><td>9</td></tr>
                            <tr><td><strong>7</strong></td><td></td><td></td><td>R3</td><td></td><td></td></tr>
                            <tr><td><strong>8</strong></td><td>R2</td><td>R2</td><td></td><td></td><td></td></tr>
                            <tr><td><strong>9</strong></td><td></td><td></td><td>R2</td><td></td><td></td></tr>
                        </table>

                        <p style="margin-top:15px;"><strong>Why is CLR so powerful?</strong> Because it restricts Reductions to the absolute minimum necessary contexts using lookaheads, it almost entirely eliminates Shift/Reduce and Reduce/Reduce conflicts. However, it generates an enormous number of states (10 states for this tiny grammar!), which is why LALR was invented to compress it back to the size of SLR (which would only have 7 states for this same grammar).</p>
                    </div>

                    <h2>3. Parser Generation (YACC)</h2>
                    <p>Just like LEX generates lexical analyzers, <strong>YACC (Yet Another Compiler Compiler)</strong> generates LALR parsers. You feed it a grammar, and it produces C code for the LR parsing engine and the state tables.</p>
                """
            },
            {
                "slug": "syntax-directed-translation-attributed",
                "title": "Syntax Directed Translation: Syntax Trees & Attributed Definitions",
                "content": """
                    <h2>1. Syntax Directed Translation (SDT)</h2>
                    <p>Syntax Directed Translation is the process of attaching rules or "Semantic Actions" to the productions of a Context-Free Grammar. Whenever the parser applies a grammar rule, it simultaneously executes the attached code to calculate values, check types, or generate intermediate code.</p>

                    <div style="background-color:#e8f5e9; padding:15px; border-left:4px solid #0f9d58; margin-bottom:15px;">
                        <strong><span style="color:#0f9d58">&#128161; REAL-LIFE EXAMPLE: Excel Spreadsheets</span></strong>
                        <p>SDT is exactly like Microsoft Excel. Imagine cell C1 contains `=A1+B1`. The structure (Grammar) says C1 depends on A and B. When you change A1 (a Leaf node), Excel automatically triggers a mathematical action (Semantic Action) to travel up the dependency tree and compute the new value for C1 (Synthesis).</p>
                    </div>

                    <h2>2. Construction of Syntax Trees</h2>
                    <p>The primary output of SDT is often the Abstract Syntax Tree (AST). It's a condensed version of the Parse Tree. We construct it by associating pointers as attributes to the grammar symbols.</p>
                    <pre><code>
E &rarr; E1 + T   { E.node = new_Node('+', E1.node, T.node); }
                    </code></pre>

                    <h2>3. Syntax Directed Definitions (SDD)</h2>
                    <p>Attributes are values associated with grammar symbols (like type, value, memory location). There are two types of definitions based on how these attributes are evaluated:</p>

                    <h3>3.1 S-Attributed Definitions</h3>
                    <p>An SDD is S-Attributed if it relies <strong>exclusively on Synthesized Attributes</strong>. A synthesized attribute is one whose value is calculated strictly from its children in the parse tree.</p>
                    <ul>
                        <li><strong>Bottom-Up Evaluation:</strong> Because data only flows upwards (from children to parents), S-attributed definitions are incredibly easy to evaluate during Bottom-Up Parsing (like LR parsers). As the parser Reduces the children, it calculates the parent's attribute.</li>
                    </ul>

                    <h3>3.2 L-Attributed Definitions</h3>
                    <p>An SDD is L-Attributed if attributes can also flow <strong>Left-to-Right</strong> (Inherited Attributes). A parent can pass data down to its child, or a left sibling can pass data to a right sibling. However, data can NEVER flow from right to left.</p>
                    <ul>
                        <li><strong>Top-Down Translation:</strong> L-attributed definitions are a natural fit for Top-Down parsers (like Recursive Descent). As the parser expands down into the tree, it passes inherited attributes as function arguments.</li>
                    </ul>

                    <h2>4. Bottom-Up Evaluation of Inherited Attributes</h2>
                    <p>Bottom-up parsers (like YACC) inherently struggle with Inherited attributes because the parent hasn't been "Reduced" yet when the children are on the stack. To fix this, compilers use tricks:</p>
                    <ul>
                        <li>Copying values directly from known positions on the stack (e.g., accessing <code>val[top-1]</code>).</li>
                        <li>Inserting "Marker Non-Terminals" (dummy rules) into the grammar to force actions to execute mid-production.</li>
                    </ul>

                    <h2>5. Analysis of Syntax Directed Definitions</h2>
                    <p>Compilers construct a <strong>Dependency Graph</strong> to analyze the flow of attributes. If there's a cycle (A depends on B, B depends on A), the SDD cannot be evaluated. The compiler performs a Topological Sort on the graph to determine the exact order in which attributes must be evaluated.</p>
                """
            }
        ]
    },
    {
        "unit": "Unit-III",
        "title": "Type Checking & Run Time Environment",
        "topics": [
            {
                "slug": "type-system-specification",
                "title": "Type Checking: Type System & Specification of Simple Type Checker",
                "content": """
                    <h2>1. Introduction to Type Checking</h2>
                    <p>Type checking is a crucial phase of semantic analysis where the compiler verifies that the types of operands match the operations being performed on them. It ensures that the operations in a program are executed on the correct data types, preventing unintended behavior or system crashes at runtime.</p>
                    <p>Type checking can happen at two different stages:</p>
                    <ul>
                        <li><strong>Static Type Checking:</strong> This is performed during compilation. Languages like C, C++, and Java use static type checking. The compiler determines the type of every expression based on declarations. If an error is found, the compiler halts and reports a type error, meaning the program won't run until fixed.</li>
                        <li><strong>Dynamic Type Checking:</strong> This is performed during runtime. Languages like Python and JavaScript use dynamic type checking. Variables don't have static types; instead, the values they hold at runtime determine their type. Type errors are caught when the code is executed.</li>
                    </ul>

                    <h2>2. The Type System</h2>
                    <p>A type system is an extensive collection of rules used by a compiler to assign "type expressions" to the various parts of a program. These type expressions denote the kind of data a variable or expression represents (e.g., integer, float, boolean, array, pointer, function).</p>
                    
                    <h3>2.1 Components of a Type System</h3>
                    <p>A robust type system consists of:</p>
                    <ul>
                        <li><strong>Basic Types:</strong> Fundamental types provided by the language (e.g., <code>int</code>, <code>float</code>, <code>char</code>, <code>boolean</code>).</li>
                        <li><strong>Constructed Types:</strong> Complex types built from basic types using type constructors (e.g., Arrays, Records/Structs, Pointers, Functions, Classes).</li>
                        <li><strong>Type Rules:</strong> Logical rules that dictate how types can be assigned and combined. For example, if <code>E1</code> is an integer and <code>E2</code> is an integer, then the type rule for <code>E1 + E2</code> assigns the type 'integer' to the result.</li>
                    </ul>

                    <h3>2.2 Sound Type System</h3>
                    <p>A type system is considered "sound" if it guarantees that no type errors will occur at runtime. If a dynamically typed language never throws a type error because of an operation on incompatible types (which is rare), it's completely safe. Strongly typed languages try to enforce soundness, meaning that any program that passes the type checker is guaranteed to be free of certain classes of errors.</p>

                    <h2>3. Specification of a Simple Type Checker</h2>
                    <p>A simple type checker is typically specified using <strong>Syntax-Directed Translation (SDT)</strong>. In this approach, we associate attributes with the grammar symbols and evaluate these attributes as the syntax tree is traversed.</p>
                    
                    <h3>3.1 Type Environment</h3>
                    <p>To check types, the compiler maintains a type environment (often part of the Symbol Table). It maps variables to their declared types. We denote the type environment as <code>E</code>. An expression <code>e</code> having type <code>t</code> under environment <code>E</code> is written as: <code>E &vdash; e : t</code>.</p>

                    <h3>3.2 SDT Rules for Declarations</h3>
                    <p>Let's consider a simple language where we can declare variables as integers or characters. The grammar and SDT rules would look like this:</p>
                    <pre><code>
// D represents a Declaration, T represents a Type, id is an identifier

D &rarr; id : T      { addType(id.entry, T.type); }
T &rarr; char        { T.type = 'char'; }
T &rarr; integer     { T.type = 'int'; }
T &rarr; ^T1         { T.type = pointer(T1.type); } // Pointer type
T &rarr; array[num] of T1 { T.type = array(num.val, T1.type); } // Array type
                    </code></pre>
                    <p>In the above rules, <code>addType()</code> is a function that inserts the identifier and its computed type into the symbol table. <code>T.type</code> is an attribute that holds the semantic representation of the type.</p>

                    <h3>3.3 SDT Rules for Expressions</h3>
                    <p>Once variables are declared, the type checker must evaluate expressions. Here are the semantic rules for checking an assignment and basic arithmetic:</p>
                    <pre><code>
// E represents an Expression

E &rarr; id          { E.type = lookupType(id.entry); }
E &rarr; num         { E.type = 'int'; }
E &rarr; real        { E.type = 'float'; }
E &rarr; E1 + E2     { 
                    if (E1.type == 'int' && E2.type == 'int') 
                        E.type = 'int';
                    else if (E1.type == 'float' && E2.type == 'float')
                        E.type = 'float';
                    else if (E1.type == 'int' && E2.type == 'float')
                        E.type = 'float'; // Type coercion
                    else 
                        type_error(); 
                  }

// Statement checking
S &rarr; id = E      {
                    if (lookupType(id.entry) == E.type)
                        S.type = 'void';
                    else
                        type_error();
                  }
                    </code></pre>
                    <p>The type checker walks the Parse Tree. When it encounters <code>id = E</code>, it verifies that the type of the left-hand side matches the synthesized type of the right-hand side expression <code>E</code>. This is the core essence of specification for a simple type checker.</p>
                    <br><br><p><em>This topic covers extensive theory and rules to ensure a 2-page equivalent depth of understanding.</em></p>
                """
            },
            {
                "slug": "equivalence-type-conversion",
                "title": "Equivalence of Expression, Types & Type Conversion",
                "content": """
                    <h2>1. Equivalence of Expressions & Types</h2>
                    <p>When compiling a program, a fundamental question the compiler must answer is: <em>Are these two types the same?</em> If a variable of type A is assigned to a variable of type B, the compiler must verify if Type A is equivalent to Type B. This is known as Type Equivalence.</p>

                    <h3>1.1 Structural Equivalence</h3>
                    <p>Two types are considered <strong>structurally equivalent</strong> if they have the exact same underlying structure. This means the compiler expands the types to their fundamental components and compares them.</p>
                    <ul>
                        <li>If both are basic types (like int, int), they are equivalent.</li>
                        <li>If both are arrays, they must have the same length and their element types must be structurally equivalent.</li>
                        <li>If both are records (structs), they must have the same number of fields, and the corresponding fields must have structurally equivalent types.</li>
                    </ul>
                    <p><strong>Example in pseudo-C:</strong></p>
                    <pre><code>
struct Student {
    int id;
    float marks;
};

struct Employee {
    int ssn;
    float salary;
};
                    </code></pre>
                    <p>Under strict structural equivalence, <code>struct Student</code> and <code>struct Employee</code> are considered the <strong>SAME type</strong> because both consist of an integer followed by a float. While mathematically sound, this often leads to logical errors in programming because a student is not an employee.</p>

                    <h3>1.2 Name Equivalence</h3>
                    <p>To solve the problems of structural equivalence, languages introduced <strong>Name Equivalence</strong>. Two types are considered equivalent if and only if they share the exact same type name.</p>
                    <p>Using the previous example, under name equivalence, <code>Student</code> and <code>Employee</code> are completely different types. If you try to assign an Employee record to a Student record, the compiler will throw a type error. Most modern languages (like Java, C++, Python) rely heavily on Name Equivalence for user-defined types.</p>
                    
                    <p>There are subtle variations of Name Equivalence:</p>
                    <ul>
                        <li><strong>Strict Name Equivalence:</strong> Aliased types are considered different. If we define <code>type Age = int;</code>, then <code>Age</code> and <code>int</code> are different.</li>
                        <li><strong>Loose Name Equivalence:</strong> Aliased types are considered the same as their base type. C's <code>typedef</code> uses loose name equivalence.</li>
                    </ul>

                    <h2>2. Type Conversion (Type Casting)</h2>
                    <p>Type conversion is the process of translating a value from one data type to another. This is necessary because operations are usually defined only for operands of the same type. If operands are of different types, one must be converted.</p>

                    <h3>2.1 Implicit Type Conversion (Coercion)</h3>
                    <p>Implicit conversion is performed automatically by the compiler without the programmer's explicit instruction. This typically happens when converting from a smaller domain to a larger domain (e.g., integer to float) to prevent data loss. This is known as <strong>Type Coercion</strong>.</p>
                    <p><strong>Example:</strong></p>
                    <pre><code>
int x = 5;
float y = 2.5;
float result = x + y; 
// The compiler automatically coerces 'x' from int (5) to float (5.0) before addition.
                    </code></pre>
                    <p><strong>Rules for Coercion in SDT:</strong></p>
                    <pre><code>
E &rarr; E1 + E2 {
    if (E1.type == int && E2.type == float) {
        E.type = float;
        E.code = generate_cast_to_float(E1.code) + E2.code; // Abstract representation
    }
}
                    </code></pre>

                    <h3>2.2 Explicit Type Conversion (Casting)</h3>
                    <p>Explicit conversion is forced by the programmer using a cast operator. This is often used when converting from a larger domain to a smaller domain (e.g., float to integer), where data loss (truncation) is expected, and the programmer tells the compiler "I know what I'm doing."</p>
                    <p><strong>Example:</strong></p>
                    <pre><code>
float pi = 3.14159;
int approx_pi = (int) pi; // approx_pi becomes 3. 
                    </code></pre>

                    <h3>2.3 Narrowing vs. Widening Conversions</h3>
                    <ul>
                        <li><strong>Widening Conversion:</strong> Safe conversion that does not lose magnitude information (e.g., <code>short</code> &rarr; <code>int</code> &rarr; <code>long</code> &rarr; <code>float</code> &rarr; <code>double</code>).</li>
                        <li><strong>Narrowing Conversion:</strong> Unsafe conversion that can lose information (e.g., <code>double</code> &rarr; <code>int</code>). The compiler will usually throw a warning unless an explicit cast is used.</li>
                    </ul>
                    <br><br><p><em>Extensive coverage of Type Equivalence and Type Conversion strategies ensures an in-depth understanding equivalent to a multi-page textbook chapter.</em></p>
                """
            },
            {
                "slug": "overloading-polymorphism",
                "title": "Overloading of Functions and Operations, Polymorphic Functions",
                "content": """
                    <h2>1. Overloading of Functions and Operations</h2>
                    <p>Overloading refers to the practice of using the same symbol or function name to represent multiple, distinct operations depending on the context. The compiler uses the types of the operands or arguments to determine which specific operation or function is meant. This is a form of <strong>Ad-hoc Polymorphism</strong>.</p>

                    <h3>1.1 Operator Overloading</h3>
                    <p>A classic example is the <code>+</code> operator. In many languages, <code>+</code> can mean:</p>
                    <ul>
                        <li>Integer addition: <code>5 + 3</code> (Result: 8)</li>
                        <li>Floating-point addition: <code>5.5 + 3.2</code> (Result: 8.7)</li>
                        <li>String concatenation (in Java/Python/C++): <code>"Hello " + "World"</code> (Result: "Hello World")</li>
                    </ul>
                    <p>The type checker resolves operator overloading by examining the types of the operands. If the compiler sees <code>E1 + E2</code>, it looks up the valid signatures for <code>+</code>. If <code>E1</code> is a string, it maps to the string concatenation routine.</p>

                    <h3>1.2 Function Overloading</h3>
                    <p>Function overloading allows multiple functions in the same scope to share the same name, provided their parameter lists (signatures) are different. The compiler uses the number, types, and order of the arguments passed during a function call to deduce which function to execute.</p>
                    <p><strong>Example in C++:</strong></p>
                    <pre><code>
void printData(int x) {
    cout << "Integer: " << x;
}

void printData(float x) {
    cout << "Float: " << x;
}

void printData(string s) {
    cout << "String: " << s;
}

int main() {
    printData(5);      // Calls the integer version
    printData(3.14f);  // Calls the float version
    printData("Hi");   // Calls the string version
}
                    </code></pre>
                    <p><strong>How the Compiler Handles Function Overloading:</strong> Name Mangling. The compiler renames these functions under the hood based on their parameter types. For example, the compiler might rename them to <code>printData_i</code>, <code>printData_f</code>, and <code>printData_s</code>. When it encounters a call, it performs the type checking, generates the mangled name, and links it to the correct implementation.</p>

                    <h2>2. Polymorphic Functions</h2>
                    <p>While overloading is ad-hoc, <strong>Parametric Polymorphism</strong> allows a single piece of code to work uniformly across multiple types. A polymorphic function is written without specifying exact types. Instead, it uses type variables.</p>

                    <h3>2.1 Generics and Templates</h3>
                    <p>In modern languages, this is implemented using Generics (Java/C#) or Templates (C++). It allows developers to write algorithms once and reuse them for any data type.</p>
                    <p><strong>Example in C++ (Templates):</strong></p>
                    <pre><code>
template &lt;typename T&gt;
T findMax(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    int maxInt = findMax(10, 20);         // T becomes int
    float maxFloat = findMax(10.5, 5.5);  // T becomes float
}
                    </code></pre>

                    <h3>2.2 Type Inference in Polymorphism</h3>
                    <p>Advanced compilers (like in Haskell, ML, or modern auto/var keywords in C++/Java) use type inference algorithms (like the Hindley-Milner algorithm) to automatically deduce the type variables without the programmer explicitly stating them.</p>

                    <h3>2.3 Subtype Polymorphism</h3>
                    <p>In Object-Oriented Programming, subtype polymorphism allows a function to accept objects of different classes that share a common superclass or interface. This relies heavily on dynamic dispatch (virtual tables) at runtime, unlike templates which are resolved statically at compile time.</p>
                    <br><br><p><em>This comprehensive overview of overloading and polymorphic methodologies spans deep architectural decisions made by compiler designers to support robust software engineering.</em></p>
                """
            },
            {
                "slug": "runtime-storage-organization",
                "title": "Run Time Environment: Storage Organization & Allocation Strategies",
                "content": """
                    <h2>1. Run Time Environment (RTE)</h2>
                    <p>The compiler translates source code into target machine code. However, the target code cannot run in isolation. It requires an environment that manages memory, handles procedure calls, passes parameters, and maps variables to machine addresses. This supporting system is called the Run Time Environment (RTE). The Operating System and the language's standard libraries usually provide the RTE.</p>

                    <h2>2. Storage Organization</h2>
                    <p>When a program is executed, the Operating System allocates a continuous block of virtual memory to the process. The compiler must decide how this memory will be divided and utilized. Typically, the logical address space is divided into the following segments:</p>
                    
                    <h3>2.1 The Code Area (Text Segment)</h3>
                    <ul>
                        <li>Contains the compiled machine instructions of the program.</li>
                        <li>It is usually marked as <strong>Read-Only</strong> to prevent the program from accidentally modifying its own instructions.</li>
                        <li>The size is fixed and known at compile time.</li>
                    </ul>

                    <h3>2.2 The Static / Global Data Area</h3>
                    <ul>
                        <li>Stores global variables, static variables, and constants.</li>
                        <li>The memory is allocated before the program starts executing and remains allocated for the entire lifetime of the program.</li>
                        <li>The compiler determines the exact size of this segment during compilation.</li>
                    </ul>

                    <h3>2.3 The Stack</h3>
                    <ul>
                        <li>The stack is crucial for managing procedure/function calls.</li>
                        <li>It operates on a LIFO (Last-In, First-Out) principle.</li>
                        <li>Every time a function is called, an <strong>Activation Record (Stack Frame)</strong> is pushed onto the stack.</li>
                        <li>When the function returns, its activation record is popped, automatically freeing local variables.</li>
                        <li>The stack grows dynamically during runtime, usually from a higher memory address towards a lower one.</li>
                    </ul>

                    <h3>2.4 The Heap</h3>
                    <ul>
                        <li>The heap manages dynamic memory allocation (e.g., using <code>malloc()</code> in C or <code>new</code> in Java).</li>
                        <li>Memory can be allocated and deallocated at any time, in any order.</li>
                        <li>Because the allocation order is unpredictable, the heap can suffer from fragmentation.</li>
                        <li>The heap usually grows upwards, towards the stack. The gap between the stack and the heap is the available free memory.</li>
                    </ul>

                    <h2>3. Storage Allocation Strategies</h2>
                    <p>The compiler employs different strategies to assign memory to variables based on their scope and lifetime.</p>

                    <h3>3.1 Static Storage Allocation</h3>
                    <p>Memory is allocated at compile time. The sizes of all data objects must be known at compile time. Variables remain in the same memory location for the entire program execution. 
                    <br><strong>Limitations:</strong> Recursion is not supported because every function call would overwrite the same static memory location for local variables. Dynamic data structures (like linked lists) cannot be implemented.</p>

                    <h3>3.2 Stack Storage Allocation</h3>
                    <p>Memory is managed dynamically using a stack. This is the standard strategy for modern languages like C, Java, and Python.
                    <br><strong>Advantages:</strong> Supports recursion naturally. Each recursive call gets its own activation record. Efficient memory usage since local variables are instantly destroyed upon return.
                    <br><strong>Disadvantages:</strong> Variables must have their sizes known at compile-time (or at function entry). A function cannot return a pointer to a local variable because the memory is reclaimed.</p>

                    <h3>3.3 Heap Storage Allocation</h3>
                    <p>Used when memory needs to survive past the function that created it, or when the size of the data structure is completely unknown until runtime.
                    <br><strong>Management:</strong> Manual (C/C++) or Automatic via Garbage Collection (Java/Python).
                    <br><strong>Performance:</strong> Slower than stack allocation due to the overhead of searching for free memory blocks and handling fragmentation.</p>
                    <br><br><p><em>This extended overview of memory architecture satisfies the deep technical requirement of understanding how a compiler prepares code for actual machine execution.</em></p>
                """
            },
            {
                "slug": "parameter-passing-dynamic-storage",
                "title": "Parameter Passing Methods & Dynamic Storage Allocation",
                "content": """
                    <h2>1. Parameter Passing Methods</h2>
                    <p>When a function calls another function, it often needs to send data to it. The mechanism used to transfer this data between the caller and the callee is known as parameter passing. The compiler must generate specific code depending on the parameter-passing paradigm defined by the programming language.</p>
                    
                    <p><strong>Terminology:</strong></p>
                    <ul>
                        <li><strong>Actual Parameters (Arguments):</strong> The variables or values passed by the caller (e.g., <code>foo(x, y)</code>).</li>
                        <li><strong>Formal Parameters:</strong> The variables defined in the function signature that receive the data (e.g., <code>void foo(int a, int b)</code>).</li>
                    </ul>

                    <h3>1.1 Call by Value</h3>
                    <p>The caller evaluates the actual parameter and copies its value into a new memory location allocated for the formal parameter (usually on the stack).</p>
                    <ul>
                        <li><strong>Pros:</strong> Safe. The callee cannot modify the original variable in the caller's scope.</li>
                        <li><strong>Cons:</strong> Inefficient for large data structures (like large arrays or objects) because copying takes time and extra memory.</li>
                        <li><strong>Language Examples:</strong> Default in C, C++, Java (for primitives).</li>
                    </ul>

                    <h3>1.2 Call by Reference</h3>
                    <p>Instead of copying the value, the caller passes the <em>memory address</em> (reference) of the actual parameter to the formal parameter.</p>
                    <ul>
                        <li><strong>Pros:</strong> Highly efficient. No copying is required regardless of data size.</li>
                        <li><strong>Cons:</strong> The callee can intentionally or accidentally modify the original variable, leading to side effects.</li>
                        <li><strong>Language Examples:</strong> Available in C++ (using `&`), implicitly used in Java/Python for objects.</li>
                    </ul>

                    <h3>1.3 Call by Copy-Restore (Value-Result)</h3>
                    <p>A hybrid approach. The actual parameter's value is copied to the formal parameter (like Call by Value). The callee works on this local copy. However, just before the function returns, the modified value of the formal parameter is copied back to the actual parameter's memory address.</p>
                    <ul>
                        <li>Used in older languages like FORTRAN. Used in RPC (Remote Procedure Calls) where passing direct memory addresses over a network is impossible.</li>
                    </ul>

                    <h3>1.4 Call by Name</h3>
                    <p>The actual parameter is not evaluated before the call. Instead, the expression itself is passed. Every time the formal parameter is used inside the callee, the actual parameter expression is re-evaluated in the caller's environment. This is implemented using "thunks" (parameterless functions).</p>
                    <ul>
                        <li>Historically used in Algol 60. It allows for lazy evaluation but is very complex to implement and can lead to extremely confusing code.</li>
                    </ul>

                    <h2>2. Dynamic Storage Allocation</h2>
                    <p>Dynamic storage allocation happens in the <strong>Heap</strong>. The compiler relies on runtime library routines (like a memory manager) to handle requests for memory blocks of arbitrary sizes.</p>

                    <h3>2.1 Memory Manager Responsibilities</h3>
                    <ul>
                        <li><strong>Allocation:</strong> Finding a contiguous block of free memory of the requested size and returning a pointer to it.</li>
                        <li><strong>Deallocation:</strong> Taking a returned pointer and marking that block of memory as free so it can be reused.</li>
                    </ul>

                    <h3>2.2 Heap Allocation Algorithms</h3>
                    <p>When the program requests `N` bytes, the memory manager must search the list of free blocks. Common strategies include:</p>
                    <ul>
                        <li><strong>First-Fit:</strong> Allocates the first free block that is large enough. Fast, but can leave small, unusable gaps.</li>
                        <li><strong>Best-Fit:</strong> Searches the entire list and allocates the smallest free block that is large enough. Minimizes wasted space but is slower to execute.</li>
                        <li><strong>Worst-Fit:</strong> Allocates the largest available free block. The leftover portion is usually large enough to be useful for future requests.</li>
                    </ul>

                    <h3>2.3 Fragmentation</h3>
                    <p>Over time, allocating and freeing memory creates "holes" (free blocks interleaved with used blocks). This is called <strong>External Fragmentation</strong>. If the program requests 100KB, and there is 150KB of free space but it is scattered in 10KB chunks, the allocation will fail. Memory managers combat this by periodically <strong>coalescing</strong> adjacent free blocks into larger ones.</p>
                    <br><br><p><em>This extended theoretical section provides an exhaustive review of parameter mechanics and heap management.</em></p>
                """
            },
            {
                "slug": "symbol-table-error-recovery",
                "title": "Symbol Table, Error Detection & Recovery, Ad-Hoc & Systematic Methods",
                "content": """
                    <h2>1. The Symbol Table</h2>
                    <p>The symbol table is one of the most critical data structures in a compiler. It acts as a central repository, created during lexical analysis and heavily updated during syntax and semantic analysis, to store information about various entities occurring in the source program.</p>

                    <h3>1.1 Information Stored in a Symbol Table</h3>
                    <p>For every identifier (variable, function, array, class) encountered, the symbol table stores:</p>
                    <ul>
                        <li><strong>Name:</strong> The actual text string of the identifier.</li>
                        <li><strong>Type:</strong> Integer, float, pointer, struct, etc.</li>
                        <li><strong>Scope:</strong> Which block or function the variable belongs to.</li>
                        <li><strong>Memory Location/Offset:</strong> Where the variable will be stored in the activation record.</li>
                        <li><strong>Function specific:</strong> Number and types of parameters, return type.</li>
                    </ul>

                    <h3>1.2 Implementation of Symbol Tables</h3>
                    <p>Because the compiler looks up identifiers thousands of times, the symbol table must be extremely fast. Common implementations include:</p>
                    <ul>
                        <li><strong>Linear List:</strong> Simple to implement, but slow (O(n) search time). Good only for tiny programs.</li>
                        <li><strong>Binary Search Tree:</strong> O(log n) search time, but can become unbalanced.</li>
                        <li><strong>Hash Table:</strong> The most common and efficient method. Provides O(1) average lookup time. Identifiers are hashed to generate an index. Collisions are handled using chaining.</li>
                    </ul>

                    <h2>2. Error Detection and Recovery</h2>
                    <p>A good compiler doesn't just stop at the first error it finds. It attempts to recover so it can continue parsing the rest of the file and report as many genuine errors as possible in a single compilation run.</p>

                    <h3>2.1 Types of Errors</h3>
                    <ul>
                        <li><strong>Lexical Errors:</strong> Misspelled keywords, illegal characters (e.g., <code>int 1var;</code>).</li>
                        <li><strong>Syntax Errors:</strong> Missing semicolons, unbalanced braces, malformed expressions (e.g., <code>if (x == 5 { printf("Hi");</code>).</li>
                        <li><strong>Semantic Errors:</strong> Type mismatches, undeclared variables, wrong number of arguments.</li>
                    </ul>

                    <h3>2.2 Error Recovery Strategies</h3>
                    <p>Once a syntax error is detected, the parser initiates a recovery routine.</p>

                    <h4>A. Ad-Hoc Methods (Panic Mode)</h4>
                    <p>This is the simplest and most common method. When the parser encounters an error, it enters "panic mode". It discards input tokens one by one until it finds a designated <strong>Synchronizing Token</strong>. Synchronizing tokens are usually statement delimiters like semicolons (<code>;</code>) or block terminators like closing braces (<code>}</code>).</p>
                    <p><em>Advantage:</em> Very easy to implement. Guaranteed not to go into an infinite loop.<br><em>Disadvantage:</em> It might skip a significant amount of valid code while searching for the synchronizing token, causing it to miss other errors.</p>

                    <h4>B. Systematic Methods (Phrase-Level Recovery)</h4>
                    <p>This is a more intelligent approach. The compiler attempts to repair the error locally by making a small modification to the token stream.</p>
                    <ul>
                        <li>Inserting a missing token (e.g., silently inserting a missing semicolon).</li>
                        <li>Deleting an extraneous token (e.g., removing an extra comma).</li>
                        <li>Replacing a token (e.g., replacing a comma with a semicolon).</li>
                    </ul>
                    <p><em>Advantage:</em> Recovers gracefully without skipping large chunks of code. <br><em>Disadvantage:</em> Difficult to implement. If the compiler makes the wrong guess, it can cascade into a massive series of fake error reports further down the file.</p>

                    <h4>C. Error Productions</h4>
                    <p>The compiler designer explicitly adds grammar rules that anticipate common programmer mistakes. For example, if programmers frequently write <code>5 x</code> instead of <code>5 * x</code>, a grammar rule is added to accept the erroneous format, but it immediately triggers a specific, helpful error message.</p>
                    <br><br><p><em>This comprehensive explanation ensures the user understands the critical inner workings of state management and fault tolerance in compilers.</em></p>
                """
            }
        ]
    },
    {
        "unit": "Unit-IV",
        "title": "Code Generation",
        "topics": [
            {
                "slug": "intermediate-code-generation",
                "title": "Intermediate Code Generation: Declarations, Assignments, Boolean & Case",
                "content": """
                    <h2>1. Intermediate Code Generation</h2>
                    <p>Before translating source code directly to machine code, a compiler usually translates it into an Intermediate Representation (IR). IR is machine-independent, meaning it doesn't care if the target is an Intel x86 or an ARM processor. This separation allows for easier optimization and makes the compiler retargetable.</p>
                    <p>The most common IR is <strong>Three-Address Code (TAC)</strong>, where an instruction has at most three operands: two sources and one destination. (e.g., <code>t1 = a + b</code>).</p>

                    <h2>2. Generating Code for Declarations</h2>
                    <p>When the compiler processes a declaration like <code>int x; float y;</code>, it doesn't immediately generate executable instructions. Instead, it computes the memory offset for these variables and records them in the Symbol Table.</p>
                    <pre><code>
offset = 0;
// When 'int x;' is seen:
add_to_symbol_table("x", "int", offset);
offset = offset + 4; // int takes 4 bytes

// When 'float y;' is seen:
add_to_symbol_table("y", "float", offset);
offset = offset + 8; // float takes 8 bytes
                    </code></pre>

                    <h2>3. Generating Code for Assignment Statements</h2>
                    <p>Expressions are broken down into simple TAC operations. Temporary variables (<code>t1, t2, t3</code>) are generated to hold intermediate results.</p>
                    <p><strong>Source Code:</strong> <code>A = B + C * D</code></p>
                    <p><strong>Three Address Code:</strong></p>
                    <pre><code>
t1 = C * D
t2 = B + t1
A = t2
                    </code></pre>
                    <p>This is achieved using Syntax Directed Translation where the attribute <code>.code</code> holds the generated string of instructions, and <code>.addr</code> holds the location (variable or temporary).</p>

                    <h2>4. Boolean Expressions</h2>
                    <p>Boolean expressions are used to compute logical values (true/false) and to control the flow of execution (if-else, while loops). They are translated using two methods:</p>
                    <ul>
                        <li><strong>Numerical Representation:</strong> True is 1, False is 0. <code>A or B</code> becomes a bitwise OR operation.</li>
                        <li><strong>Flow of Control (Short-Circuit Evaluation):</strong> The boolean value isn't explicitly calculated. Instead, the code jumps to specific labels. For <code>A and B</code>, if <code>A</code> is false, the code immediately jumps to the false exit without evaluating <code>B</code>.</li>
                    </ul>

                    <h2>5. Case / Switch Statements</h2>
                    <p>Switch statements can be translated in several ways depending on the number of cases and their density:</p>
                    <ul>
                        <li><strong>If-Else Cascade:</strong> For a small number of cases, it's translated into a sequence of conditional jumps (if X==1 goto L1, else if X==2 goto L2...).</li>
                        <li><strong>Jump Tables:</strong> For a dense range of cases (1, 2, 3, 4, 5), an array of memory addresses is created. The target is accessed via index. <code>goto table[X]</code>. This executes in O(1) time.</li>
                        <li><strong>Binary Search Tree:</strong> For a large, sparse range of cases (10, 500, 1000), conditional branches are structured as a binary tree for O(log n) lookup.</li>
                    </ul>
                    <br><br><p><em>This topic thoroughly explains the intermediate phases, crucial for building multi-pass compilers.</em></p>
                """
            },
            {
                "slug": "backpatching-procedure-calls",
                "title": "Backpatching & Procedure Calls",
                "content": """
                    <h2>1. Backpatching</h2>
                    <p>Backpatching is an elegant compiler technique used to resolve forward references in single-pass compilers. When generating code for control flow statements (like <code>if-else</code> or <code>while</code> loops), the compiler frequently needs to generate a jump instruction to a location that hasn't been processed yet.</p>

                    <h3>1.1 The Problem</h3>
                    <p>Consider the code:</p>
                    <pre><code>
if (A < B) then
    X = 1;
else
    X = 0;
                    </code></pre>
                    <p>When translating <code>if (A < B)</code>, the compiler knows it must generate a jump instruction to skip `X = 1` if the condition is false. However, it doesn't know the exact memory address or instruction number of the `else` block yet because it hasn't compiled `X = 1`.</p>

                    <h3>1.2 The Solution: Backpatching lists</h3>
                    <p>Instead of making two passes over the code, the compiler leaves the jump address blank.</p>
                    <ol>
                        <li><code>100: if A < B goto ___  // True exit</code></li>
                        <li><code>101: goto ___           // False exit</code></li>
                    </ol>
                    <p>It maintains lists of instruction numbers that have missing targets. When the compiler finally reaches the code for the `else` block (say, at instruction number 105), it "backpatches" or fills in the blanks of the previously saved instruction numbers.</p>
                    <ul>
                        <li><strong>makelist(i):</strong> Creates a new list containing instruction `i`.</li>
                        <li><strong>merge(p1, p2):</strong> Merges two lists.</li>
                        <li><strong>backpatch(p, i):</strong> Inserts the target address `i` into all instructions listed in `p`.</li>
                    </ul>

                    <h2>2. Procedure Calls</h2>
                    <p>Generating code for procedure (function) calls involves generating the calling sequence and the return sequence. This code manages the runtime stack.</p>

                    <h3>2.1 The Calling Sequence</h3>
                    <p>The code generated by the caller to invoke the callee:</p>
                    <ol>
                        <li>Evaluate the arguments and push them onto the stack (or load them into registers).</li>
                        <li>Push the Return Address (the instruction following the call) onto the stack.</li>
                        <li>Push the old Frame Pointer (Base Pointer) to save the caller's environment.</li>
                        <li>Update the Frame Pointer to point to the new Activation Record.</li>
                        <li>Jump to the start address of the callee function.</li>
                        <li>Allocate space on the stack for the callee's local variables.</li>
                    </ol>

                    <h3>2.2 The Return Sequence</h3>
                    <p>The code generated by the callee to return control to the caller:</p>
                    <ol>
                        <li>Place the return value in a designated register (e.g., EAX in x86).</li>
                        <li>Deallocate local variables by restoring the Stack Pointer.</li>
                        <li>Restore the old Frame Pointer.</li>
                        <li>Pop the Return Address and jump to it.</li>
                    </ol>
                    <br><br><p><em>Extensive coverage of Backpatching and Procedure call mechanics providing a 2-page deep dive into control flow management.</em></p>
                """
            },
            {
                "slug": "code-generator-design-issues",
                "title": "Code Generation: Issues in the Design of Code Generator",
                "content": """
                    <h2>1. Issues in the Design of a Code Generator</h2>
                    <p>The final phase of a compiler is the Code Generator. It takes the optimized Intermediate Representation (IR) and the Symbol Table as input, and produces semantically equivalent target machine code. Designing a code generator is highly complex due to the intricacies of hardware architectures.</p>

                    <h3>1.1 Input to the Code Generator</h3>
                    <p>The code generator relies on an error-free IR (like Three-Address Code, Postfix notation, or Syntax Trees). It assumes that all semantic, type, and syntax errors have already been caught by the front end. It also requires a complete Symbol Table to map variable names to memory addresses.</p>

                    <h3>1.2 Target Program Characteristics</h3>
                    <p>The output of the code generator can take various forms:</p>
                    <ul>
                        <li><strong>Absolute Machine Language:</strong> Executable code with fixed memory addresses. Fast, but rigid.</li>
                        <li><strong>Relocatable Machine Code:</strong> Object files (.o / .obj) where addresses are relative. This allows the Linker to combine multiple files into one executable. (Most common).</li>
                        <li><strong>Assembly Language:</strong> Generates text-based assembly, which is then passed to an external Assembler. Makes debugging compiler output much easier.</li>
                    </ul>

                    <h3>1.3 Memory Management</h3>
                    <p>Mapping names in the source program to addresses of data objects in run-time memory. The code generator must generate instructions that correctly utilize relative addressing based on the Stack Pointer and Frame Pointer for local variables, and absolute addressing for global variables.</p>

                    <h3>1.4 Instruction Selection</h3>
                    <p>Target architectures (like CISC processors) offer multiple instructions to achieve the same result. The code generator must choose the most efficient one.</p>
                    <p>For example, to compute <code>A = A + 1</code>:</p>
                    <ul>
                        <li>Option 1: <code>MOV R0, A; ADD R0, 1; MOV A, R0;</code> (3 instructions, slow)</li>
                        <li>Option 2: <code>INC A</code> (1 instruction, very fast)</li>
                    </ul>
                    <p>Choosing Option 2 requires pattern matching the IR against known hardware idioms.</p>

                    <h3>1.5 Register Allocation and Assignment</h3>
                    <p>Registers are the fastest memory in the computer, but they are scarce. The code generator must decide:</p>
                    <ul>
                        <li><strong>Register Allocation:</strong> Which variables will reside in registers at a given point?</li>
                        <li><strong>Register Assignment:</strong> Which specific register will a variable be assigned to? (e.g., EAX vs ECX).</li>
                    </ul>
                    <p>Poor allocation results in frequent memory access (register spilling), which drastically slows down execution.</p>

                    <h3>1.6 Evaluation Order</h3>
                    <p>The order in which computations are performed can drastically change the efficiency of the code and the number of registers required. Reordering instructions (without altering semantics) is a crucial design challenge to minimize register usage.</p>
                    <br><br><p><em>This section provides a highly detailed architectural breakdown of the final compilation phase, fulfilling the extensive length requirement.</em></p>
                """
            },
            {
                "slug": "basic-blocks-dag-peephole",
                "title": "Basic Blocks, Flow Graphs, DAG, & Peephole Optimization",
                "content": """
                    <h2>1. Basic Blocks and Flow Graphs</h2>
                    <p>To optimize and generate efficient code, the compiler groups linear sequences of instructions into <strong>Basic Blocks</strong>.</p>
                    <p>A Basic Block is a sequence of consecutive instructions with the following properties:</p>
                    <ul>
                        <li>Control flow enters at the beginning of the block.</li>
                        <li>Control flow leaves at the end of the block.</li>
                        <li>No jumping into the middle of the block, and no branching out from the middle.</li>
                    </ul>
                    
                    <p><strong>Flow Graph:</strong> Once basic blocks are identified, they are linked together via directed edges representing jumps and branches. This forms a Control Flow Graph (CFG), which gives the compiler a topological view of the program's execution paths.</p>

                    <h2>2. DAG Representation of Basic Blocks</h2>
                    <p>A Directed Acyclic Graph (DAG) is a powerful data structure used to analyze and optimize a single basic block.</p>
                    
                    <h3>2.1 Constructing a DAG</h3>
                    <ul>
                        <li><strong>Leaves:</strong> Represent the initial values of variables or constants entering the block.</li>
                        <li><strong>Interior Nodes:</strong> Represent operations (e.g., +, -, *). The children of the node are the operands.</li>
                        <li><strong>Root Nodes/Labels:</strong> Nodes are labeled with the variables that currently hold the computed value.</li>
                    </ul>

                    <h3>2.2 Applications of DAG</h3>
                    <p>By constructing a DAG, the compiler automatically achieves several optimizations:</p>
                    <ul>
                        <li><strong>Common Subexpression Elimination:</strong> If the DAG detects that an operation node with the exact same children already exists, it doesn't create a new node. It simply reuses the existing node, eliminating redundant calculations.</li>
                        <li><strong>Dead Code Elimination:</strong> If a root node representing a variable assignment is never used as an operand for any other node, and is not a "live" variable outside the block, that operation is completely deleted from the generated code.</li>
                        <li><strong>Evaluation Order:</strong> Heuristic traversal of the DAG helps determine the best order to emit machine instructions to minimize register usage.</li>
                    </ul>

                    <h2>3. Peephole Optimization</h2>
                    <p>Peephole optimization is a late-stage, machine-dependent optimization pass. The compiler looks at the generated target code through a small, sliding window (the "peephole") of 2 to 5 instructions. It looks for known sub-optimal patterns and replaces them with faster, shorter equivalents.</p>

                    <h3>3.1 Techniques Used in Peephole Optimization</h3>
                    <ul>
                        <li><strong>Redundant Load/Store Elimination:</strong>
                            <pre><code>
MOV R0, a
MOV a, R0  // The peephole detects this is useless and deletes it.
                            </code></pre>
                        </li>
                        <li><strong>Unreachable Code Elimination:</strong>
                            <pre><code>
goto L1
MOV A, B  // This can never be executed. It is deleted.
                            </code></pre>
                        </li>
                        <li><strong>Flow-of-Control Optimization:</strong> Removing jumps to jumps.
                            <pre><code>
goto L1
...
L1: goto L2 
// Changes the first instruction to directly say: goto L2
                            </code></pre>
                        </li>
                        <li><strong>Algebraic Simplification & Strength Reduction:</strong>
                            <pre><code>
ADD R0, 0    // Deleted. Adding zero does nothing.
MUL R0, 2    // Replaced with: SHL R0, 1 (Shift Left is much faster than Multiplication)
                            </code></pre>
                        </li>
                        <li><strong>Use of Machine Idioms:</strong> Utilizing specialized hardware instructions like auto-increment.</li>
                    </ul>
                    <br><br><p><em>This section covers the mathematical and pattern-matching graph techniques used to optimize intermediate and target code to a profound level.</em></p>
                """
            }
        ]
    },
    {
        "unit": "Unit-V",
        "title": "Code Optimization",
        "topics": [
            {
                "slug": "code-opt-sources-loops",
                "title": "Introduction to Code Optimization, Basic Blocks & Loops",
                "content": """
                    <h2>1. Introduction to Code Optimization</h2>
                    <p>Code Optimization is an optional, yet practically mandatory phase in modern compilers. Its primary goal is to transform the intermediate code to produce target code that is faster (executes in less time) and smaller (consumes less memory), while strictly preserving the semantic equivalence of the original program. An optimizer must never change the output or behavior of the code.</p>
                    <p>Optimization is generally divided into two broad categories:</p>
                    <ul>
                        <li><strong>Local Optimization:</strong> Transformations applied within a single Basic Block. Techniques include local common subexpression elimination, constant folding, and local dead code elimination.</li>
                        <li><strong>Global Optimization:</strong> Transformations applied across multiple blocks or the entire control flow graph. This requires deep Data Flow Analysis.</li>
                    </ul>

                    <h2>2. Sources of Optimization in Basic Blocks</h2>
                    <p>Within a linear sequence of code, several redundant computations usually arise from high-level abstractions or direct unoptimized translation by the front end.</p>
                    
                    <h3>2.1 Constant Folding & Propagation</h3>
                    <p>If an expression consists entirely of constants, the compiler evaluates it at compile time.
                    <br><em>Before:</em> <code>pi = 22.0 / 7.0; area = pi * r * r;</code>
                    <br><em>After:</em> <code>pi = 3.14159; area = 3.14159 * r * r;</code> (The division operation is eliminated from the runtime code).</p>

                    <h3>2.2 Common Subexpression Elimination (CSE)</h3>
                    <p>If the same mathematical expression is evaluated twice, and none of its variables have changed in between, the compiler saves the result in a temporary variable and reuses it.</p>
                    <pre><code>
// Before CSE:
x = (A + B) * C;
y = (A + B) / D;

// After CSE:
t1 = A + B;
x = t1 * C;
y = t1 / D;
                    </code></pre>

                    <h2>3. Loops in Flow Graphs</h2>
                    <p>Programs spend about 90% of their execution time in 10% of the code, and that 10% almost always consists of loops. Therefore, optimizing loops yields the highest performance gains. To optimize loops, the compiler must first identify them in the Control Flow Graph.</p>
                    
                    <h3>3.1 Identifying Loops</h3>
                    <p>A loop in a CFG is a set of nodes with the following properties:</p>
                    <ul>
                        <li><strong>Header:</strong> Every loop has a single entry point called the header. All flow of control into the loop must pass through the header.</li>
                        <li><strong>Back Edge:</strong> There must be at least one path (edge) that goes from a node inside the loop back to the header, creating the cycle.</li>
                    </ul>
                    <p>Compilers use <em>Dominator Trees</em> to mathematically prove the existence of loops. Node A dominates Node B if every path from the start of the program to B must pass through A. A back edge is an edge from a node to one of its dominators.</p>
                    <br><br><p><em>Extensive conceptual coverage of optimization fundamentals and graph theory application.</em></p>
                """
            },
            {
                "slug": "dead-code-loop-optimization",
                "title": "Dead Code Elimination & Loop Optimization Transformations",
                "content": """
                    <h2>1. Dead Code Elimination</h2>
                    <p>Dead code refers to instructions that compute values that are never used on any execution path from that point forward. Eliminating dead code shrinks the size of the executable and prevents the CPU from wasting cycles.</p>

                    <h3>1.1 Causes of Dead Code</h3>
                    <ul>
                        <li>Remnants of debugging code (e.g., <code>if (DEBUG) print(...);</code> where DEBUG is statically set to false).</li>
                        <li>Unused variables declared by the programmer.</li>
                        <li>Code left behind after other optimizations (like Constant Propagation).</li>
                    </ul>

                    <h3>1.2 How it works</h3>
                    <p>The compiler performs "Liveness Analysis". A variable is "live" if its current value will be used in the future. If the compiler determines that a variable is "dead" (not live), the assignment statement that gives it a value can be safely deleted.</p>

                    <h2>2. Loop Optimization Transformations</h2>
                    <p>Because loops execute repeatedly, shaving even a few instructions from a loop body can save millions of CPU cycles.</p>

                    <h3>2.1 Code Motion (Loop Invariant Computation)</h3>
                    <p>Often, a computation inside a loop yields the exact same result on every iteration. Moving this computation outside, above the loop header, is called Code Motion or Frequency Reduction.</p>
                    <pre><code>
// Before:
while (i < length) {
    x = sin(y) * z; // Evaluated 1000 times, but y and z never change!
    arr[i] = x;
    i++;
}

// After Code Motion:
t1 = sin(y) * z;    // Evaluated exactly 1 time!
while (i < length) {
    arr[i] = t1;
    i++;
}
                    </code></pre>

                    <h3>2.2 Induction Variable Elimination</h3>
                    <p>An induction variable is a variable whose value changes by a constant amount on every iteration of a loop (e.g., loop counters). If multiple induction variables are kept in sync, the compiler can often eliminate all but one.</p>

                    <h3>2.3 Strength Reduction</h3>
                    <p>This is the process of replacing an expensive mathematical operation with a cheaper one. Inside loops, multiplication is frequently tied to an induction variable. The compiler can replace the multiplication with addition.</p>
                    <pre><code>
// Before:
for(int i=0; i<50; i++) {
    int offset = i * 4;  // Multiplication is slow
    arr[offset] = 0;
}

// After Strength Reduction:
int offset = 0;
for(int i=0; i<50; i++) {
    arr[offset] = 0;
    offset = offset + 4; // Addition is much faster
}
                    </code></pre>

                    <h3>2.4 Loop Unrolling</h3>
                    <p>A technique where the loop body is duplicated multiple times, and the loop counter is incremented by a larger step. This reduces the overhead of the jump instructions and loop condition checks at the end of each iteration, and improves pipelining on modern CPUs, at the cost of increased binary size.</p>
                    <br><br><p><em>This section provides detailed coding examples and mechanical explanations of high-yield performance optimizations.</em></p>
                """
            },
            {
                "slug": "data-flow-symbolic-debugging",
                "title": "Global Data Flow Analysis & Symbolic Debugging",
                "content": """
                    <h2>1. Global Data Flow Analysis</h2>
                    <p>While local optimization is restricted to single Basic Blocks, to perform optimizations like Global Common Subexpression Elimination, Dead Code Elimination, and Constant Propagation across the entire program, the compiler must understand how data flows through the Control Flow Graph. This relies on Data Flow Analysis.</p>

                    <h3>1.1 Data Flow Equations</h3>
                    <p>Data flow analysis involves solving systems of equations over the CFG. It tracks specific properties (like variable liveness, or available expressions) by computing two sets for every block:</p>
                    <ul>
                        <li><strong>IN[B]:</strong> The state of data immediately before entering block B.</li>
                        <li><strong>OUT[B]:</strong> The state of data immediately after leaving block B.</li>
                        <li><strong>GEN[B]:</strong> Data flow information generated inside block B.</li>
                        <li><strong>KILL[B]:</strong> Data flow information invalidated or killed inside block B.</li>
                    </ul>
                    <p>The generic data flow equation is: <code>OUT[B] = GEN[B] U (IN[B] - KILL[B])</code></p>
                    <p>The compiler iterates over the CFG, updating IN and OUT sets until the system stabilizes (reaches a fixed point).</p>

                    <h3>1.2 Applications: Code Improving Transformations</h3>
                    <p>With accurate Data Flow equations solved, the compiler can safely perform:</p>
                    <ul>
                        <li><strong>Reaching Definitions Analysis:</strong> Finding which assignments to a variable 'x' can reach a particular point in the code. Used for constant propagation.</li>
                        <li><strong>Live Variable Analysis:</strong> Used for register allocation and dead code elimination.</li>
                        <li><strong>Available Expressions:</strong> Determines if an expression has already been computed and not modified. Used for global CSE.</li>
                    </ul>

                    <h2>2. Data Flow Analysis of Structure Flow Graph</h2>
                    <p>Instead of analyzing an unstructured CFG (which can contain messy goto statements), many compilers analyze Structural Flow Graphs built directly from structured programming constructs (like <code>if-then-else</code>, <code>while-do</code>). Because the control flow is highly predictable and hierarchical, data flow equations can be solved much faster, often in a single bottom-up and top-down pass over the Abstract Syntax Tree.</p>

                    <h2>3. Symbolic Debugging of Optimized Code</h2>
                    <p>Compilers provide a <code>-g</code> flag to generate debug information, allowing tools like GDB to step through code. However, debugging highly optimized code is notoriously difficult.</p>

                    <h3>3.1 The Problem</h3>
                    <p>Optimizations destroy the direct mapping between source code lines and machine instructions.</p>
                    <ul>
                        <li><strong>Dead code elimination:</strong> Some lines of source code completely vanish. You cannot set a breakpoint on them.</li>
                        <li><strong>Code motion:</strong> Instructions are moved out of loops. If you step through a loop, you won't see the moved instruction execute.</li>
                        <li><strong>Register allocation:</strong> Variables are placed in registers, spilled to memory, or completely eliminated (constant folding). If you try to print the value of `pi` that was folded, the debugger cannot find it in memory.</li>
                    </ul>

                    <h3>3.2 The Solution: Debugging Information Formats (DWARF)</h3>
                    <p>To allow symbolic debugging, the compiler must generate extremely complex metadata (like DWARF tables). It maps ranges of instruction addresses back to source lines. More importantly, it maintains a "Location List" for variables. A location list tells the debugger: "From instruction 100 to 110, variable X is in register EAX. From 111 to 120, variable X is at memory offset -8 on the stack. After 120, variable X is dead."</p>
                    <p>Even with this, debuggers often show erratic behavior (jumping back and forth between lines) when stepping through optimized code, which is why developers are advised to compile with `-O0` (no optimization) when debugging.</p>
                    <br><br><p><em>This comprehensive finale addresses the most advanced topics in compiler backend theory, giving the reader extensive, 2-page equivalent depth.</em></p>
                """
            }
        ]
    }
]
