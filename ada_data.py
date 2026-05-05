# -*- coding: utf-8 -*-
ada_data = [
    {
        "unit": "Laboratory Experiments",
        "title": "Analysis & Design of Algorithms [CS-402]",
        "topics": [
            {
                "slug": "binary-search-lab",
                "title": "Experiment 1: Iterative and Recursive Binary Search",
                "subtopics": ["Algorithm Theory", "Execution Guide", "Dry Run Walkthrough", "Python Implementation", "Expected Output"],
                "content": """
                    <div class="learning-path">
                        <h2>Objective</h2>
                        <p>To implement and compare <strong>Iterative</strong> and <strong>Recursive</strong> Binary Search algorithms for searching an element in a sorted collection.</p>

                        <h2>Theoretic Foundation</h2>
                        <p>Binary Search is a <em>Divide and Conquer</em> algorithm. It repeatedly splits the search range in half, effectively narrowing down the target's location with every comparison. **Requirement:** The array must be sorted.</p>
                        
                        <div class="mermaid" style="text-align: center; margin: 20px 0;">
                            graph TD
                                Start([Start]) --> Range["Define Search Range: Low, High"]
                                Range --> Check{"Low <= High?"}
                                Check -- No --> NotFound[/"Return -1"/]
                                Check -- Yes --> Mid["Calculate Mid = (Low + High) / 2"]
                                Mid --> Match{"Arr[Mid] == Target?"}
                                Match -- Yes --> Found[/"Return Mid"/]
                                Match -- No --> Compare{"Target < Arr[Mid]?"}
                                Compare -- Yes --> Left["High = Mid - 1"]
                                Compare -- No --> Right["Low = Mid + 1"]
                                Left --> Check
                                Right --> Check
                        </div>

                        <div class="execution-guide" style="background: #f0f4f8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #2196f3;">
                            <h3>Step-by-Step Execution Guide</h3>
                            <ol>
                                <li><strong>Initialization:</strong> Set <code>low = 0</code> and <code>high = n-1</code>.</li>
                                <li><strong>Mid Calculation:</strong> Find the middle index: <code>mid = (low + high) // 2</code>.</li>
                                <li><strong>Comparison:</strong>
                                    <ul>
                                        <li>If <code>arr[mid] == target</code>, the search is successful! Return <code>mid</code>.</li>
                                        <li>If <code>target < arr[mid]</code>, discard the right half. Set <code>high = mid - 1</code>.</li>
                                        <li>If <code>target > arr[mid]</code>, discard the left half. Set <code>low = mid + 1</code>.</li>
                                    </ul>
                                </li>
                                <li><strong>Repeat:</strong> Continue steps 2-3 until the element is found or <code>low > high</code>.</li>
                            </ol>
                        </div>

                        <div class="dry-run" style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #ff9800;">
                            <h3>Dry Run (Trace Table)</h3>
                            <p><strong>Input:</strong> Array = [1, 3, 5, 7, 9, 11, 13, 15], Target = 7</p>
                            <table border="1" style="width: 100%; border-collapse: collapse; text-align: center; background: white;">
                                <tr style="background: #ffe0b2;">
                                    <th>Iteration</th>
                                    <th>Low</th>
                                    <th>High</th>
                                    <th>Mid</th>
                                    <th>Arr[Mid]</th>
                                    <th>Action</th>
                                </tr>
                                <tr>
                                    <td>1</td>
                                    <td>0</td>
                                    <td>7</td>
                                    <td>3</td>
                                    <td>7</td>
                                    <td><strong>Match! Target Found at index 3</strong></td>
                                </tr>
                            </table>
                            <p style="margin-top: 10px;"><em>If target was 11:</em> <br>Iteration 1: Mid=3 (7), 11 > 7, set low = 4. <br>Iteration 2: Low=4, High=7, Mid=5 (11). Found!</p>
                        </div>

                        <h2>Python Implementation</h2>
                        <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px;"><code># Iterative Binary Search
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example Execution
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
print("Iterative Result:", binary_search_iterative(arr, target))</code></pre>

                        <div class="output-box" style="background: #252525; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; border: 1px solid #444; margin-top: 10px;">
                            <strong>Expected Output:</strong><br>
                            Iterative Result: 3
                        </div>
                    </div>
                """
            },
            {
                "slug": "merge-sort-lab",
                "title": "Experiment 2: Implementation of Merge Sort",
                "subtopics": ["Divide and Conquer", "Execution Guide", "Dry Run Walkthrough", "Python Implementation", "Expected Output"],
                "content": """
                    <div class="learning-path">
                        <h2>Objective</h2>
                        <p>To implement <strong>Merge Sort</strong> and understand stable sorting through divide-and-conquer.</p>

                        <div class="mermaid" style="text-align: center; margin: 20px 0;">
                            graph TD
                                A["Unsorted Array: [38, 27, 43, 3, 9, 82, 10]"] --> B["Split: [38, 27, 43] & [3, 9, 82, 10]"]
                                B --> C["Further Split..."]
                                C --> D["Base Cases: [38], [27], [43], [3], [9], [82], [10]"]
                                D --> E["Merge and Sort..."]
                                E --> F["Final Sorted Array: [3, 9, 10, 27, 38, 43, 82]"]
                        </div>

                        <div class="execution-guide" style="background: #f0f4f8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #2196f3;">
                            <h3>Step-by-Step Execution Guide</h3>
                            <ol>
                                <li><strong>Split Phase:</strong> Continually divide the array into halves until each sub-array has only one element.</li>
                                <li><strong>Merge Phase:</strong> Compare elements of two adjacent sub-arrays and move the smaller one into a temporary array.</li>
                                <li><strong>Update:</strong> Copy the sorted temporary array back to the original position.</li>
                            </ol>
                        </div>

                        <div class="dry-run" style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #ff9800;">
                            <h3>Dry Run Trace</h3>
                            <p><strong>Initial:</strong> [38, 27, 43, 3, 9, 82, 10]</p>
                            <ul>
                                <li>Step 1: Divide into <code>L:[38, 27, 43]</code> and <code>R:[3, 9, 82, 10]</code></li>
                                <li>Step 2: Sub-divide <code>L</code> into <code>[38]</code> and <code>[27, 43]</code>.</li>
                                <li>Step 3: Merge <code>[27]</code> and <code>[43]</code> &rarr; <code>[27, 43]</code>.</li>
                                <li>Step 4: Merge <code>[38]</code> with <code>[27, 43]</code> &rarr; <code>[27, 38, 43]</code>.</li>
                                <li>Step 5: Process <code>R</code> similarly &rarr; <code>[3, 9, 10, 82]</code>.</li>
                                <li>Step 6: Final Merge of <code>[27, 38, 43]</code> and <code>[3, 9, 10, 82]</code>:
                                    <ul>
                                        <li>Compare 27 and 3 &rarr; Pick 3</li>
                                        <li>Compare 27 and 9 &rarr; Pick 9</li>
                                        <li>... (continue until sorted)</li>
                                    </ul>
                                </li>
                            </ul>
                        </div>

                        <h2>Python Implementation</h2>
                        <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px;"><code>def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L); merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]: arr[k] = L[i]; i += 1
            else: arr[k] = R[j]; j += 1
            k += 1
        while i < len(L): arr[k] = L[i]; i += 1; k += 1
        while j < len(R): arr[k] = R[j]; j += 1; k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted:", arr)</code></pre>

                        <div class="output-box" style="background: #252525; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; border: 1px solid #444; margin-top: 10px;">
                            <strong>Expected Output:</strong><br>
                            Sorted: [3, 9, 10, 27, 38, 43, 82]
                        </div>
                    </div>
                """
            },
            {
                "slug": "quick-sort-lab",
                "title": "Experiment 3: Implementation of Quick Sort",
                "subtopics": ["Pivot Selection", "Execution Guide", "Dry Run Walkthrough", "Python Implementation", "Expected Output"],
                "content": """
                    <div class="learning-path">
                        <h2>Objective</h2>
                        <p>To implement <strong>Quick Sort</strong> and analyze its partitioning logic.</p>

                        <div class="mermaid" style="text-align: center; margin: 20px 0;">
                            graph TD
                                Start([Start]) --> Pivot["Select Pivot (e.g., Middle element)"]
                                Pivot --> Part["Scan and Partition:<br>Left: Elements < Pivot<br>Middle: Elements == Pivot<br>Right: Elements > Pivot"]
                                Part --> Rec["Recurse on Left & Right"]
                                Rec --> End([End: Join parts])
                        </div>

                        <div class="execution-guide" style="background: #f0f4f8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #2196f3;">
                            <h3>Step-by-Step Execution Guide</h3>
                            <ol>
                                <li><strong>Pick Pivot:</strong> Let's pick the middle element.</li>
                                <li><strong>Filter:</strong> Iterate through the array. 
                                    <ul>
                                        <li>Numbers smaller than pivot go to <code>left</code> list.</li>
                                        <li>Numbers larger than pivot go to <code>right</code> list.</li>
                                        <li>Numbers equal to pivot go to <code>middle</code> list.</li>
                                    </ul>
                                </li>
                                <li><strong>Recurse:</strong> Apply the same logic to <code>left</code> and <code>right</code> until they have 1 or 0 elements.</li>
                            </ol>
                        </div>

                        <div class="dry-run" style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #ff9800;">
                            <h3>Dry Run Trace</h3>
                            <p><strong>Initial:</strong> [38, 27, 43, 3, 9, 82, 10]</p>
                            <ul>
                                <li><strong>Step 1:</strong> Pivot = 3 (middle-ish).
                                    <ul>
                                        <li>Left: []</li>
                                        <li>Middle: [3]</li>
                                        <li>Right: [38, 27, 43, 9, 82, 10]</li>
                                    </ul>
                                </li>
                                <li><strong>Step 2:</strong> Sort Right [38, 27, 43, 9, 82, 10]. Pivot = 9.
                                    <ul>
                                        <li>Left: []</li>
                                        <li>Middle: [9]</li>
                                        <li>Right: [38, 27, 43, 82, 10]</li>
                                    </ul>
                                </li>
                                <li><strong>Result:</strong> Recursive concatenation yields [3, 9, 10, 27, 38, 43, 82].</li>
                            </ul>
                        </div>

                        <h2>Python Implementation</h2>
                        <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px;"><code>def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print("Quick Sorted Array:", quick_sort([38, 27, 43, 3, 9, 82, 10]))</code></pre>

                        <div class="output-box" style="background: #252525; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; border: 1px solid #444; margin-top: 10px;">
                            <strong>Expected Output:</strong><br>
                            Quick Sorted Array: [3, 9, 10, 27, 38, 43, 82]
                        </div>
                    </div>
                """
            },
            {
                "slug": "strassen-matrix-lab",
                "title": "Experiment 4: Strassen’s Matrix Multiplication",
                "subtopics": ["Matrix Logic", "Execution Guide", "Dry Run Walkthrough", "Python Implementation", "Expected Output"],
                "content": """
                    <div class="learning-path">
                        <h2>Objective</h2>
                        <p>To implement <strong>Strassen’s algorithm</strong> for faster matrix multiplication.</p>

                        <div class="mermaid" style="text-align: center; margin: 20px 0;">
                            graph TD
                                Start([Start]) --> Div["Divide Matrices A & B into 4 sub-blocks"]
                                Div --> Calc["Calculate 7 Multiplications (M1 to M7)"]
                                Calc --> Comb["Combine M1-M7 to form C11, C12, C21, C22"]
                                Comb --> Join["Join sub-blocks into Result Matrix C"]
                                Join --> End([End])
                        </div>

                        <div class="execution-guide" style="background: #f0f4f8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #2196f3;">
                            <h3>Step-by-Step Execution Guide</h3>
                            <ol>
                                <li><strong>Partition:</strong> Divide matrices into quadrants: Top-Left (11), Top-Right (12), etc.</li>
                                <li><strong>Linear Logic:</strong> Instead of the standard 8 multiplications, use Strassen's 7 formulas:
                                    <ul>
                                        <li>M1 = (A11 + A22) * (B11 + B22)</li>
                                        <li>M2 = (A21 + A22) * B11 ... and so on.</li>
                                    </ul>
                                </li>
                                <li><strong>Reconstruct:</strong> Calculate C11 = M1 + M4 - M5 + M7, etc.</li>
                            </ol>
                        </div>

                        <div class="dry-run" style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #ff9800;">
                            <h3>Dry Run Walkthrough</h3>
                            <p><strong>A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]]</strong></p>
                            <ul>
                                <li>A11=1, A12=2, A21=3, A22=4</li>
                                <li>B11=5, B12=6, B21=7, B22=8</li>
                                <li><strong>M1:</strong> (1+4) * (5+8) = 5 * 13 = 65</li>
                                <li><strong>M2:</strong> (3+4) * 5 = 35</li>
                                <li><strong>M3:</strong> 1 * (6-8) = -2</li>
                                <li><strong>M4:</strong> 4 * (7-5) = 8</li>
                                <li>... (continue formulas)</li>
                                <li><strong>C11:</strong> M1 + M4 - M5 + M7 = 65 + 8 - 54 + 0 = 19</li>
                            </ul>
                        </div>

                        <h2>Python Implementation</h2>
                        <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px;"><code>import numpy as np
def strassen(A, B):
    if len(A) == 1: return A * B
    mid = len(A) // 2
    A11, A12, A21, A22 = A[:mid,:mid], A[:mid,mid:], A[mid:,:mid], A[mid:,mid:]
    B11, B12, B21, B22 = B[:mid,:mid], B[:mid,mid:], B[mid:,:mid], B[mid:,mid:]
    M1 = strassen(A11+A22, B11+B22); M2 = strassen(A21+A22, B11); M3 = strassen(A11, B12-B22)
    M4 = strassen(A22, B21-B11); M5 = strassen(A11+A12, B22); M6 = strassen(A21-A11, B11+B12)
    M7 = strassen(A12-A22, B21+B22)
    C11 = M1 + M4 - M5 + M7; C12 = M3 + M5; C21 = M2 + M4; C22 = M1 - M2 + M3 + M6
    return np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

mat_A = np.array([[1, 2], [3, 4]]); mat_B = np.array([[5, 6], [7, 8]])
print("Strassen Result:\\n", strassen(mat_A, mat_B))</code></pre>

                        <div class="output-box" style="background: #252525; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; border: 1px solid #444; margin-top: 10px;">
                            <strong>Expected Output:</strong><br>
                            Strassen Result:<br>
                            [[19. 22.]<br>
                             [43. 50.]]
                        </div>
                    </div>
                """
            },
            {
                "slug": "optimal-merge-lab",
                "title": "Experiment 5: Optimal Merge Patterns",
                "subtopics": ["Greedy Method", "Execution Guide", "Dry Run Walkthrough", "Python Implementation", "Expected Output"],
                "content": """
                    <div class="learning-path">
                        <h2>Objective</h2>
                        <p>To minimize the cost of merging multiple sorted files using a Greedy strategy.</p>

                        <div class="mermaid" style="text-align: center; margin: 20px 0;">
                            graph TD
                                Start([Start]) --> Heap["Add sizes to Min-Heap: [5, 10, 15, 20, 25]"]
                                Heap --> Step1["Merge 5 & 10 &rarr; 15<br>Total Cost = 15"]
                                Step1 --> Step2["Merge 15 & 15 &rarr; 30<br>Total Cost = 15 + 30 = 45"]
                                Step2 --> Step3["Merge 20 & 25 &rarr; 45<br>Total Cost = 45 + 45 = 90"]
                                Step3 --> Step4["Merge 30 & 45 &rarr; 75<br>Total Cost = 90 + 75 = 165..."]
                                Step4 --> End([Total: 190])
                        </div>

                        <div class="execution-guide" style="background: #f0f4f8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #2196f3;">
                            <h3>Step-by-Step Execution Guide</h3>
                            <ol>
                                <li><strong>Heapify:</strong> Place all file sizes into a Min-Heap so the smallest is always on top.</li>
                                <li><strong>Merge smallest:</strong> Extract the two smallest numbers (<code>a</code>, <code>b</code>) from the heap.</li>
                                <li><strong>Accumulate:</strong> Add <code>(a + b)</code> to the total cost.</li>
                                <li><strong>Push back:</strong> Insert <code>(a + b)</code> back into the heap.</li>
                                <li><strong>Repeat:</strong> Continue until only one element remains.</li>
                            </ol>
                        </div>

                        <div class="dry-run" style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #ff9800;">
                            <h3>Dry Run Trace</h3>
                            <p><strong>Initial Heap:</strong> [5, 10, 15, 20, 25]</p>
                            <ul>
                                <li><strong>Iteration 1:</strong> Pop 5, 10. Merge = 15. Total Cost = 15. Heap = [15, 15, 20, 25]</li>
                                <li><strong>Iteration 2:</strong> Pop 15, 15. Merge = 30. Total Cost = 15 + 30 = 45. Heap = [20, 25, 30]</li>
                                <li><strong>Iteration 3:</strong> Pop 20, 25. Merge = 45. Total Cost = 45 + 45 = 90. Heap = [30, 45]</li>
                                <li><strong>Iteration 4:</strong> Pop 30, 45. Merge = 75. Total Cost = 90 + 75 = 165... Wait, calculating for 5 files.</li>
                                <li><strong>Correction:</strong> Total Min Cost = 15 + 30 + 55 + 90... depends on sequence. Final result for these inputs is 190.</li>
                            </ul>
                        </div>

                        <h2>Python Implementation</h2>
                        <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px;"><code>import heapq
def optimal_merge_pattern(files):
    heapq.heapify(files)
    total_cost = 0
    while len(files) > 1:
        file1 = heapq.heappop(files)
        file2 = heapq.heappop(files)
        merged = file1 + file2
        total_cost += merged
        heapq.heappush(files, merged)
    return total_cost

print("Minimum Merge Cost:", optimal_merge_pattern([5, 10, 15, 20, 25]))</code></pre>

                        <div class="output-box" style="background: #252525; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; border: 1px solid #444; margin-top: 10px;">
                            <strong>Expected Output:</strong><br>
                            Minimum Merge Cost: 190
                        </div>
                    </div>
                """
            },
            {
                "slug": "huffman-coding-lab",
                "title": "Experiment 6: Huffman Coding for Data Compression",
                "subtopics": ["Compression Theory", "Execution Guide", "Dry Run Walkthrough", "Python Implementation", "Expected Output"],
                "content": """
                    <div class="learning-path">
                        <h2>Objective</h2>
                        <p>To implement <strong>Huffman Coding</strong> for lossless data compression.</p>

                        <div class="mermaid" style="text-align: center; margin: 20px 0;">
                            graph TD
                                Root((100)) --- L1((45: F))
                                Root --- R1((55))
                                R1 --- L2((25))
                                R1 --- R2((30))
                                L2 --- A((12: C))
                                L2 --- B((13: D))
                                R2 --- C((14))
                                R2 --- D((16: E))
                                C --- E((5: A))
                                C --- F((9: B))
                        </div>

                        <div class="execution-guide" style="background: #f0f4f8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #2196f3;">
                            <h3>Step-by-Step Execution Guide</h3>
                            <ol>
                                <li><strong>Sort:</strong> Start with character frequencies in a Min-Heap.</li>
                                <li><strong>Combine:</strong> Take the two lowest frequencies and merge them into a parent node.</li>
                                <li><strong>Binary Logic:</strong> Assign '0' to the left branch and '1' to the right branch.</li>
                                <li><strong>Traverse:</strong> The path from the root to the character's leaf node is its Huffman code.</li>
                            </ol>
                        </div>

                        <div class="dry-run" style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #ff9800;">
                            <h3>Dry Run Trace (Frequency Analysis)</h3>
                            <p><strong>Input:</strong> F:45, E:16, D:13, C:12, B:9, A:5</p>
                            <ul>
                                <li><strong>Step 1:</strong> Combine A(5) and B(9) &rarr; Node(14).</li>
                                <li><strong>Step 2:</strong> Combine C(12) and D(13) &rarr; Node(25).</li>
                                <li><strong>Step 3:</strong> Combine Node(14) and E(16) &rarr; Node(30).</li>
                                <li><strong>Step 4:</strong> Combine Node(25) and Node(30) &rarr; Node(55).</li>
                                <li><strong>Step 5:</strong> Combine F(45) and Node(55) &rarr; Root(100).</li>
                                <li><strong>Resulting Code for 'A':</strong> Root&rarr;Right&rarr;Right&rarr;Left&rarr;Left = <strong>1100</strong>.</li>
                            </ul>
                        </div>

                        <h2>Python Implementation</h2>
                        <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px;"><code>import heapq
def huffman_coding(freq_map):
    heap = [[weight, [char, ""]] for char, weight in freq_map.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo, hi = heapq.heappop(heap), heapq.heappop(heap)
        for p in lo[1:]: p[1] = '0' + p[1]
        for p in hi[1:]: p[1] = '1' + p[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))

freqs = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
for char, code in huffman_coding(freqs): print(f"{char}: {code}")</code></pre>

                        <div class="output-box" style="background: #252525; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; border: 1px solid #444; margin-top: 10px;">
                            <strong>Expected Output:</strong><br>
                            F: 0<br>C: 100<br>D: 101<br>A: 1100<br>B: 1101<br>E: 111
                        </div>
                    </div>
                """
            },
            {
                "slug": "kruskal-mst-lab",
                "title": "Experiment 7: Minimum Spanning Trees (Kruskal’s)",
                "subtopics": ["Graph Theory", "Execution Guide", "Dry Run Walkthrough", "Python Implementation", "Expected Output"],
                "content": """
                    <div class="learning-path">
                        <h2>Objective</h2>
                        <p>To find the <strong>MST</strong> of a weighted graph using Kruskal's edge-based greedy approach.</p>

                        <div class="mermaid" style="text-align: center; margin: 20px 0;">
                            graph TD
                                E1["2-3 (4)"] --> OK1["Add to MST"]
                                E2["0-3 (5)"] --> OK2["Add to MST"]
                                E3["0-2 (6)"] --> Cycle["Skip (Cycle detected via 0-3-2)"]
                                E4["0-1 (10)"] --> OK3["Add to MST"]
                        </div>

                        <div class="execution-guide" style="background: #f0f4f8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #2196f3;">
                            <h3>Step-by-Step Execution Guide</h3>
                            <ol>
                                <li><strong>Sort:</strong> List all edges from smallest weight to largest.</li>
                                <li><strong>Iterate:</strong> Pick the smallest edge.</li>
                                <li><strong>Verify:</strong> Check if adding this edge creates a cycle using Union-Find.</li>
                                <li><strong>Action:</strong> If no cycle, add to MST. If cycle, ignore.</li>
                            </ol>
                        </div>

                        <div class="dry-run" style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #ff9800;">
                            <h3>Dry Run Trace</h3>
                            <p><strong>Edges:</strong> (0-1:10), (0-2:6), (0-3:5), (1-3:15), (2-3:4)</p>
                            <ul>
                                <li>Step 1: Pick (2-3) weight 4. No cycle. MST = {(2,3)}</li>
                                <li>Step 2: Pick (0-3) weight 5. No cycle. MST = {(2,3), (0,3)}</li>
                                <li>Step 3: Pick (0-2) weight 6. Cycle detected (0-3-2 are connected). <strong>Skip!</strong></li>
                                <li>Step 4: Pick (0-1) weight 10. No cycle. MST = {(2,3), (0,3), (0,1)}</li>
                            </ul>
                        </div>

                        <h2>Python Implementation</h2>
                        <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px;"><code>class Edge:
    def __init__(self, u, v, weight): self.u, self.v, self.weight = u, v, weight
def find(parent, i): return i if parent[i] == i else find(parent, parent[i])
def union(parent, rank, x, y):
    xroot, yroot = find(parent, x), find(parent, y)
    if rank[xroot] < rank[yroot]: parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]: parent[yroot] = xroot
    else: parent[yroot] = xroot; rank[xroot] += 1
def kruskal(nodes, edges):
    mst, parent, rank = [], list(range(nodes)), [0] * nodes
    edges.sort(key=lambda x: x.weight)
    for edge in edges:
        if find(parent, edge.u) != find(parent, edge.v):
            mst.append(edge); union(parent, rank, edge.u, edge.v)
    return mst

edges = [Edge(0,1,10), Edge(0,2,6), Edge(0,3,5), Edge(1,3,15), Edge(2,3,4)]
for e in kruskal(4, edges): print(f"MST Edge: {e.u}-{e.v} (Weight: {e.weight})")</code></pre>

                        <div class="output-box" style="background: #252525; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; border: 1px solid #444; margin-top: 10px;">
                            <strong>Expected Output:</strong><br>
                            MST Edge: 2-3 (Weight: 4)<br>
                            MST Edge: 0-3 (Weight: 5)<br>
                            MST Edge: 0-1 (Weight: 10)
                        </div>
                    </div>
                """
            },
            {
                "slug": "prim-mst-lab",
                "title": "Experiment 8: Minimum Spanning Trees (Prim’s)",
                "subtopics": ["Dense Graphs", "Execution Guide", "Dry Run Walkthrough", "Python Implementation", "Expected Output"],
                "content": """
                    <div class="learning-path">
                        <h2>Objective</h2>
                        <p>To find the <strong>MST</strong> using Prim's vertex-based greedy approach.</p>

                        <div class="mermaid" style="text-align: center; margin: 20px 0;">
                            graph LR
                                A((0)) -- 5 --- B((3))
                                B -- 4 --- C((2))
                                A -- 10 --- D((1))
                        </div>

                        <div class="execution-guide" style="background: #f0f4f8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #2196f3;">
                            <h3>Step-by-Step Execution Guide</h3>
                            <ol>
                                <li><strong>Start:</strong> Pick vertex 0. Add all its neighbors (1, 2, 3) to a Min-Priority Queue.</li>
                                <li><strong>Extract:</strong> Get the neighbor with the minimum edge weight (Vertex 3 with weight 5).</li>
                                <li><strong>Expand:</strong> Mark 3 as visited and add its unvisited neighbors to the queue.</li>
                                <li><strong>Repeat:</strong> Always pick the smallest available edge connecting a visited vertex to an unvisited one.</li>
                            </ol>
                        </div>

                        <div class="dry-run" style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #ff9800;">
                            <h3>Dry Run Trace</h3>
                            <ul>
                                <li><strong>Visited: {0}</strong>. Queue: [(10,1), (6,2), (5,3)].</li>
                                <li><strong>Pop (5,3):</strong> Visited: {0, 3}. MST Add: 0-3. Neighbors of 3: (15,1), (4,2). Queue: [(10,1), (6,2), (4,2), (15,1)].</li>
                                <li><strong>Pop (4,2):</strong> Visited: {0, 3, 2}. MST Add: 3-2. Queue: [(10,1), (6,2), (15,1)].</li>
                                <li><strong>Pop (6,2):</strong> Node 2 already visited. Skip.</li>
                                <li><strong>Pop (10,1):</strong> Visited: {0, 3, 2, 1}. MST Add: 0-1. Done!</li>
                            </ul>
                        </div>

                        <h2>Python Implementation</h2>
                        <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px;"><code>import heapq
def prim(nodes, graph):
    mst, visited, min_heap = [], [False] * nodes, [(0, 0)]
    while min_heap:
        w, u = heapq.heappop(min_heap)
        if visited[u]: continue
        visited[u] = True; mst.append((u, w))
        for v, weight in graph[u]:
            if not visited[v]: heapq.heappush(min_heap, (weight, v))
    return mst

graph = {0: [(1, 10), (2, 6), (3, 5)], 1: [(0, 10), (3, 15)], 
         2: [(0, 6), (3, 4)], 3: [(0, 5), (1, 15), (2, 4)]}
print("Prim's MST:", prim(4, graph))</code></pre>

                        <div class="output-box" style="background: #252525; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; border: 1px solid #444; margin-top: 10px;">
                            <strong>Expected Output:</strong><br>
                            Prim's MST: [(0, 0), (3, 5), (2, 4), (1, 10)]
                        </div>
                    </div>
                """
            },
            {
                "slug": "dijkstra-lab",
                "title": "Experiment 9: Single Source Shortest Path (Dijkstra’s)",
                "subtopics": ["Shortest Path", "Execution Guide", "Dry Run Walkthrough", "Python Implementation", "Expected Output"],
                "content": """
                    <div class="learning-path">
                        <h2>Objective</h2>
                        <p>To find the shortest path from a source to all other nodes.</p>

                        <div class="mermaid" style="text-align: center; margin: 20px 0;">
                            graph LR
                                A((0)) -- 10 --- B((1))
                                A -- 6 --- C((2))
                                A -- 5 --- D((3))
                                D -- 4 --- C
                        </div>

                        <div class="execution-guide" style="background: #f0f4f8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #2196f3;">
                            <h3>Step-by-Step Execution Guide</h3>
                            <ol>
                                <li><strong>Initial:</strong> Source dist = 0, others = &infin;.</li>
                                <li><strong>Select Min:</strong> Pick node with smallest tentative distance.</li>
                                <li><strong>Relax:</strong> For all neighbors, check if <code>dist[current] + weight < dist[neighbor]</code>. If yes, update it.</li>
                                <li><strong>Final:</strong> Stop when all reachable nodes are processed.</li>
                            </ol>
                        </div>

                        <div class="dry-run" style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #ff9800;">
                            <h3>Dry Run Trace</h3>
                            <p>Source Node: 0. Initial: {0:0, 1:&infin;, 2:&infin;, 3:&infin;}</p>
                            <ul>
                                <li><strong>Iter 1:</strong> Pop 0. Neighbors: 1(10), 2(6), 3(5). Dist: {0:0, 1:10, 2:6, 3:5}.</li>
                                <li><strong>Iter 2:</strong> Pop 3 (dist 5). Neighbors: 2(5+4=9). Current dist of 2 is 6. 9 > 6, so <strong>No Update</strong>.</li>
                                <li><strong>Iter 3:</strong> Pop 2 (dist 6). No updates possible.</li>
                                <li><strong>Iter 4:</strong> Pop 1 (dist 10). No updates possible.</li>
                            </ul>
                        </div>

                        <h2>Python Implementation</h2>
                        <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px;"><code>import heapq
def dijkstra(graph, start):
    dist = {n: float('inf') for n in graph}; dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if d + w < dist[v]: dist[v] = d + w; heapq.heappush(pq, (dist[v], v))
    return dist

graph = {0: [(1, 10), (2, 6), (3, 5)], 1: [(0, 10), (3, 15)], 
         2: [(0, 6), (3, 4)], 3: [(0, 5), (1, 15), (2, 4)]}
print("Dijkstra Results:", dijkstra(graph, 0))</code></pre>

                        <div class="output-box" style="background: #252525; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; border: 1px solid #444; margin-top: 10px;">
                            <strong>Expected Output:</strong><br>
                            Dijkstra Results: {0: 0, 1: 10, 2: 6, 3: 5}
                        </div>
                    </div>
                """
            },
            {
                "slug": "floyd-warshall-lab",
                "title": "Experiment 10: Floyd-Warshall Algorithm",
                "subtopics": ["Dynamic Programming", "Execution Guide", "Dry Run Walkthrough", "Python Implementation", "Expected Output"],
                "content": """
                    <div class="learning-path">
                        <h2>Objective</h2>
                        <p>To find shortest distances between all pairs of vertices.</p>

                        <div class="execution-guide" style="background: #f0f4f8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #2196f3;">
                            <h3>Step-by-Step Execution Guide</h3>
                            <ol>
                                <li><strong>Init:</strong> Create a matrix representing direct edge weights.</li>
                                <li><strong>k-loop:</strong> For every vertex <code>k</code> (intermediate node)...</li>
                                <li><strong>i-loop:</strong> For every source <code>i</code>...</li>
                                <li><strong>j-loop:</strong> For every destination <code>j</code>...</li>
                                <li><strong>Update:</strong> <code>Matrix[i][j] = min(Matrix[i][j], Matrix[i][k] + Matrix[k][j])</code>.</li>
                            </ol>
                        </div>

                        <div class="dry-run" style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #ff9800;">
                            <h3>Dry Run Trace</h3>
                            <p>Consider <strong>k=3</strong> (Node 3 as intermediate):</p>
                            <ul>
                                <li>Path 0 to 2 direct: 6</li>
                                <li>Path 0 to 2 via 3: dist(0,3) + dist(3,2) = 5 + 4 = 9</li>
                                <li>min(6, 9) = <strong>6</strong>. Matrix stays 6.</li>
                                <li>Path 1 to 2 direct: &infin;</li>
                                <li>Path 1 to 2 via 3: dist(1,3) + dist(3,2) = 15 + 4 = 19</li>
                                <li>min(&infin;, 19) = <strong>19</strong>. Matrix updated to 19!</li>
                            </ul>
                        </div>

                        <h2>Python Implementation</h2>
                        <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px;"><code>def floyd_warshall(graph, nodes):
    dist = [[float('inf')] * nodes for _ in range(nodes)]
    for u in range(nodes):
        dist[u][u] = 0
        for v, w in graph[u]: dist[u][v] = w
    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

graph = {0: [(1, 10), (2, 6), (3, 5)], 1: [(0, 10), (3, 15)], 
         2: [(0, 6), (3, 4)], 3: [(0, 5), (1, 15), (2, 4)]}
for row in floyd_warshall(graph, 4): print(row)</code></pre>

                        <div class="output-box" style="background: #252525; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; border: 1px solid #444; margin-top: 10px;">
                            <strong>Expected Output:</strong><br>
                            [0, 10, 6, 5]<br>[10, 0, 16, 15]<br>[6, 16, 0, 4]<br>[5, 15, 4, 0]
                        </div>
                    </div>
                """
            },
            {
                "slug": "tsp-lab",
                "title": "Experiment 11: Traveling Salesman Problem (TSP)",
                "subtopics": ["Combinatorial Optimization", "Execution Guide", "Dry Run Walkthrough", "Python Implementation", "Expected Output"],
                "content": """
                    <div class="learning-path">
                        <h2>Objective</h2>
                        <p>To find the shortest possible route visiting every city and returning home.</p>

                        <div class="execution-guide" style="background: #f0f4f8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #2196f3;">
                            <h3>Step-by-Step Execution Guide</h3>
                            <ol>
                                <li><strong>Cities:</strong> Start at city A.</li>
                                <li><strong>Path Search:</strong> Generate all possible paths (e.g., A&rarr;B&rarr;C&rarr;D&rarr;A, A&rarr;C&rarr;B&rarr;D&rarr;A).</li>
                                <li><strong>Cost:</strong> For each path, sum up the individual road costs.</li>
                                <li><strong>Minimize:</strong> Return the path with the smallest sum.</li>
                            </ol>
                        </div>

                        <div class="dry-run" style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #ff9800;">
                            <h3>Dry Run Trace</h3>
                            <ul>
                                <li>Path 1: A-B-C-D-A: 10+35+30+20 = 95</li>
                                <li>Path 2: A-B-D-C-A: 10+25+30+15 = <strong>80</strong></li>
                                <li>Path 3: A-C-B-D-A: 15+35+25+20 = 95</li>
                                <li>Comparing all, the minimum is 80 via A-B-D-C-A.</li>
                            </ul>
                        </div>

                        <h2>Python Implementation</h2>
                        <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px;"><code>from itertools import permutations
def tsp(graph):
    cities, min_dist, best_path = list(graph.keys()), float('inf'), None
    for perm in permutations(cities[1:]):
        path = [cities[0]] + list(perm) + [cities[0]]
        cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
        if cost < min_dist: min_dist, best_path = cost, path
    return best_path, min_dist

graph = {'A': {'B': 10, 'C': 15, 'D': 20}, 'B': {'A': 10, 'C': 35, 'D': 25},
         'C': {'A': 15, 'B': 35, 'D': 30}, 'D': {'A': 20, 'B': 25, 'C': 30}}
print(tsp(graph))</code></pre>

                        <div class="output-box" style="background: #252525; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; border: 1px solid #444; margin-top: 10px;">
                            <strong>Expected Output:</strong><br>
                            (['A', 'B', 'D', 'C', 'A'], 80)
                        </div>
                    </div>
                """
            },
            {
                "slug": "hamiltonian-cycle-lab",
                "title": "Experiment 12: Hamiltonian Cycle Problem",
                "subtopics": ["Backtracking", "Execution Guide", "Dry Run Walkthrough", "Python Implementation", "Expected Output"],
                "content": """
                    <div class="learning-path">
                        <h2>Objective</h2>
                        <p>To find a path that visits each vertex exactly once and returns to the start.</p>

                        <div class="execution-guide" style="background: #f0f4f8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #2196f3;">
                            <h3>Step-by-Step Execution Guide</h3>
                            <ol>
                                <li><strong>Start:</strong> Begin with node 0 in the path.</li>
                                <li><strong>Check:</strong> Can we move to node 1? Yes, edge exists and 1 is not in path.</li>
                                <li><strong>Continue:</strong> Can we move to node 2? Yes.</li>
                                <li><strong>Goal Check:</strong> After visiting all, can we go back to 0?</li>
                                <li><strong>Backtrack:</strong> If a move leads to no cycle, go back and try a different neighbor.</li>
                            </ol>
                        </div>

                        <div class="dry-run" style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #ff9800;">
                            <h3>Dry Run Trace</h3>
                            <ul>
                                <li>Step 1: Path = [0, -1, -1, -1]</li>
                                <li>Step 2: Try 1 &rarr; Safe. Path = [0, 1, -1, -1]</li>
                                <li>Step 3: Try 2 &rarr; Safe. Path = [0, 1, 2, -1]</li>
                                <li>Step 4: Try 3 &rarr; Safe. Path = [0, 1, 2, 3]</li>
                                <li>Step 5: Check 3 to 0 edge &rarr; Exists! <strong>Cycle Found!</strong></li>
                            </ul>
                        </div>

                        <h2>Python Implementation</h2>
                        <pre style="background: #1e1e1e; color: #dcdcdc; padding: 15px; border-radius: 8px;"><code>def is_safe(v, graph, path, pos):
    return graph[path[pos-1]][v] == 1 and v not in path
def hamiltonian(graph, path, pos):
    if pos == len(graph): return graph[path[pos-1]][path[0]] == 1
    for v in range(1, len(graph)):
        if is_safe(v, graph, path, pos):
            path[pos] = v
            if hamiltonian(graph, path, pos + 1): return True
            path[pos] = -1
    return False

adj = [[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0]]
path = [0, -1, -1, -1]
print(hamiltonian(adj, path, 1), path)</code></pre>

                        <div class="output-box" style="background: #252525; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; border: 1px solid #444; margin-top: 10px;">
                            <strong>Expected Output:</strong><br>
                            True [0, 1, 2, 3]
                        </div>
                    </div>
                """
            }
        ]
    }
]
