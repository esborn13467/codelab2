### Sorting Algorithms

#### Bubble Sort
- **Description**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- **Complexity**: O(n^2)
- **Stability**: Stable
- **Code Example in Python**:
  ```python
  def bubble_sort(arr):
      n = len(arr)
      for i in range(n):
          for j in range(0, n-i-1):
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
      return arr
  ```
- **Code Example in JavaScript**:
  ```javascript
  function bubbleSort(arr) {
      let n = arr.length;
      for (let i = 0; i < n; i++) {
          for (let j = 0; j < n-i-1; j++) {
              if (arr[j] > arr[j+1]) {
                  [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
              }
          }
      }
      return arr;
  }
  ```

#### Selection Sort
- **Description**: Divides the input list into two parts: a sorted sublist and an unsorted sublist, and repeatedly selects the smallest (or largest) element from the unsorted sublist and moves it to the end of the sorted sublist.
- **Complexity**: O(n^2)
- **Stability**: Not stable
- **Code Example in Python**:
  ```python
  def selection_sort(arr):
      n = len(arr)
      for i in range(n):
          min_idx = i
          for j in range(i+1, n):
              if arr[j] < arr[min_idx]:
                  min_idx = j
          arr[i], arr[min_idx] = arr[min_idx], arr[i]
      return arr
  ```
- **Code Example in JavaScript**:
  ```javascript
  function selectionSort(arr) {
      let n = arr.length;
      for (let i = 0; i < n; i++) {
          let min_idx = i;
          for (let j = i+1; j < n; j++) {
              if (arr[j] < arr[min_idx]) {
                  min_idx = j;
              }
          }
          [arr[i], arr[min_idx]] = [arr[min_idx], arr[i]];
      }
      return arr;
  }
  ```

#### Insertion Sort
- **Description**: Builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
- **Complexity**: O(n^2)
- **Stability**: Stable
- **Code Example in Python**:
  ```python
  def insertion_sort(arr):
      for i in range(1, len(arr)):
          key = arr[i]
          j = i-1
          while j >= 0 and key < arr[j]:
              arr[j + 1] = arr[j]
              j -= 1
          arr[j + 1] = key
      return arr
  ```
- **Code Example in JavaScript**:
  ```javascript
  function insertionSort(arr) {
      for (let i = 1; i < arr.length; i++) {
          let key = arr[i];
          let j = i - 1;
          while (j >= 0 && arr[j] > key) {
              arr[j + 1] = arr[j];
              j = j - 1;
          }
          arr[j + 1] = key;
      }
      return arr;
  }
  ```

#### Merge Sort
- **Description**: A divide and conquer algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves.
- **Complexity**: O(n log n)
- **Stability**: Stable
- **Code Example in Python**:
  ```python
  def merge_sort(arr):
      if len(arr) > 1:
          mid = len(arr) // 2
          L = arr[:mid]
          R = arr[mid:]
          merge_sort(L)
          merge_sort(R)
          i = j = k = 0
          while i < len(L) and j < len(R):
              if L[i] < R[j]:
                  arr[k] = L[i]
                  i += 1
              else:
                  arr[k] = R[j]
                  j += 1
              k += 1
          while i < len(L):
              arr[k] = L[i]
              i += 1
              k += 1
          while j < len(R):
              arr[k] = R[j]
              j += 1
              k += 1
      return arr
  ```
- **Code Example in JavaScript**:
  ```javascript
  function mergeSort(arr) {
      if (arr.length <= 1) {
          return arr;
      }
      const mid = Math.floor(arr.length / 2);
      const left = mergeSort(arr.slice(0, mid));
      const right = mergeSort(arr.slice(mid));
      return merge(left, right);
  }

  function merge(left, right) {
      let result = [];
      let i = 0;
      let j = 0;
      while (i < left.length && j < right.length) {
          if (left[i] < right[j]) {
              result.push(left[i]);
              i++;
          } else {
              result.push(right[j]);
              j++;
          }
      }
      return result.concat(left.slice(i)).concat(right.slice(j));
  }
  ```

#### Quick Sort
- **Description**: A divide and conquer algorithm that selects a 'pivot' element, partitions the array around the pivot, and then recursively sorts the partitions.
- **Complexity**: Average case O(n log n), worst case O(n^2)
- **Stability**: Not stable
- **Code Example in Python**:
  ```python
  def quick_sort(arr):
      if len(arr) <= 1:
          return arr
      pivot = arr[len(arr) // 2]
      left = [x for x in arr if x < pivot]
      middle = [x for x in arr if x == pivot]
      right = [x for x in arr if x > pivot]
      return quick_sort(left) + middle + quick_sort(right)
  ```
- **Code Example in JavaScript**:
  ```javascript
  function quickSort(arr) {
      if (arr.length <= 1) {
          return arr;
      }
      const pivot = arr[Math.floor(arr.length / 2)];
      const left = arr.filter(x => x < pivot);
      const middle = arr.filter(x => x === pivot);
      const right = arr.filter(x => x > pivot);
      return quickSort(left).concat(middle).concat(quickSort(right));
  }
  ```

#### Heap Sort
- **Description**: Converts the array into a heap data structure, then repeatedly extracts the maximum element and rebuilds the heap.
- **Complexity**: O(n log n)
- **Stability**: Not stable
- **Code Example in Python**:
  ```python
  def heapify(arr, n, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
      if l < n and arr[i] < arr[l]:
          largest = l
      if r < n and arr[largest] < arr[r]:
          largest = r
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)

  def heap_sort(arr):
      n = len(arr)
      for i in range(n // 2 - 1, -1, -1):
          heapify(arr, n, i)
      for i in range(n-1, 0, -1):
          arr[i], arr[0] = arr[0], arr[i]
          heapify(arr, i, 0)
      return arr
  ```
- **Code Example in JavaScript**:
  ```javascript
  function heapify(arr, n, i) {
      let largest = i;
      let left = 2 * i + 1;
      let right = 2 * i + 2;
      if (left < n && arr[left] > arr[largest]) {
          largest = left;
      }
      if (right < n && arr[right] > arr[largest]) {
          largest = right;
      }
      if (largest != i) {
          [arr[i], arr[largest]] = [arr[largest], arr[i]];
          heapify(arr, n, largest);
      }
  }

  function heapSort(arr) {
      let n = arr.length;
      for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
          heapify(arr, n, i);
      }
      for (let i = n - 1; i > 0; i--) {
          [arr[0], arr[i]] = [arr[i], arr[0]];
          heapify(arr, i, 0);
      }
      return arr;
  }
  ```

### Algorithm Techniques: Memoization

- **Definition**: Memoization is an optimization technique used to speed up programs by storing the results of expensive function calls and reusing those results when the same inputs occur again.
- **Applications**: Commonly used in dynamic programming, such as in solving problems like Fibonacci sequence, knapsack problem, and shortest path algorithms.

####

 Python Example:
```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

#### JavaScript Example:
```javascript
function fibMemo(n, memo = {}) {
    if (n in memo) {
        return memo[n];
    }
    if (n <= 2) {
        return 1;
    }
    memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo);
    return memo[n];
}
```

### Tree, Tree Traversal, Application, Red-Black Trees

#### Trees

- **Binary Tree**: A tree structure in which each node has at most two children.
- **Binary Search Tree (BST)**: A binary tree in which for each node, the value of all the nodes in the left subtree is less than the node's value, and the value of all the nodes in the right subtree is greater.
- **AVL Tree**: A self-balancing binary search tree where the difference between heights of left and right subtrees cannot be more than one.
- **Red-Black Tree**: A self-balancing binary search tree with an additional bit for color (red or black) to ensure balance during insertions and deletions.

#### Tree Traversal

- **Inorder Traversal (LNR)**: Visit left subtree, node, right subtree.
- **Preorder Traversal (NLR)**: Visit node, left subtree, right subtree.
- **Postorder Traversal (LRN)**: Visit left subtree, right subtree, node.
- **Level Order Traversal**: Visit nodes level by level from top to bottom.

#### Applications of Trees

- **Binary Search Trees (BSTs)**: Efficient searching, insertion, and deletion.
- **Heaps**: Implement priority queues.
- **Tries**: Implement dictionary and prefix-based searching.
- **Segment Trees**: Range queries and updates.

#### Red-Black Trees

- **Properties**:
    1. Each node is either red or black.
    2. The root is black.
    3. All leaves (NIL nodes) are black.
    4. If a node is red, then both its children are black.
    5. Every path from a node to its descendant NIL nodes has the same number of black nodes.

- **Operations**:
    - **Insertion**: Insert as in a binary search tree, then fix violations of red-black properties.
    - **Deletion**: Remove as in a binary search tree, then fix violations of red-black properties.

#### Python Example of Red-Black Tree Node:
```python
class Node:
    def __init__(self, data, color="red"):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
```

#### JavaScript Example of Red-Black Tree Node:
```javascript
class Node {
    constructor(data, color = "red") {
        this.data = data;
        this.color = color;
        this.left = null;
        this.right = null;
        this.parent = null;
    }
}
```

### Git and Version Control

#### Basics

- **Repository (repo)**: A storage location for software packages.
- **Commit**: Saving changes to the repository.
- **Branch**: A separate line of development.

#### Common Commands

- **git init**: Initialize a new repository.
- **git clone**: Create a copy of an existing repository.
- **git add**: Add files to the staging area.
- **git commit**: Record changes to the repository.
- **git status**: Show the working tree status.
- **git log**: Show commit logs.
- **git branch**: List, create, or delete branches.
- **git checkout**: Switch branches or restore working tree files.
- **git merge**: Merge branches.
- **git pull**: Fetch and integrate changes from a remote repository.
- **git push**: Update the remote repository with local commits.

#### Branching and Merging

- **Feature Branch Workflow**: Develop features on separate branches.
- **Git Flow**: A branching model for Git, using feature, develop, release, and hotfix branches.
- **Merge Conflicts**: Occur when changes from different branches conflict; resolved manually.

#### Best Practices

- Commit often with meaningful messages.
- Use branches for feature development.
- Regularly sync with the main branch to avoid conflicts.
- Review code before merging to ensure quality and consistency.
### Detailed Summary of Graph Concepts for Exam Revision

**Graphs:**
- A graph \( G = (V, E) \) consists of a set of vertices \( V \) and edges \( E \).
- **Directed Graph (Digraph):** Edges have a specific direction \( e = \langle n1, n2 \rangle \) and can have self-loops.
- **Undirected Graph:** Edges have no direction \( e = \{n1, n2\} \) and do not have self-loops or parallel edges.

**Graph Terminology:**
- **Indegree(v):** Number of edges entering vertex \( v \).
- **Outdegree(v):** Number of edges leaving vertex \( v \).
- **Path:** Sequence of vertices where each adjacent pair is connected by an edge.
- **Cycle:** A path where the start and end vertices are the same.
- **Simple Path:** A path with all distinct vertices.
- **Simple Cycle:** A cycle with all distinct vertices except the start and end.

**Graph Representations and Operations:**
- **Vertex and Edge Operations:** Create, insert, and manipulate vertices and edges.
- **Traversal Techniques:**
  - **Breadth-First Search (BFS):** Visits vertices in order of increasing distance from the start vertex.
  - **Depth-First Search (DFS):** Visits vertices by exploring as far as possible before backtracking.

**Directed Acyclic Graphs (DAGs) and Topological Sort:**
- **DAG:** A directed graph with no cycles.
- **Topological Sorting:** Ordering of vertices such that for every directed edge \( \langle u, v \rangle \), vertex \( u \) comes before \( v \).

**Critical Paths:**
- **Definition:** The longest path from the start to the stop vertex in a DAG, determining the earliest completion time.
- **Critical Path Problem:** Find the longest path in terms of edge costs.

**Shortest Path Problems:**
- **Problem Definition:** Find the path with the minimum total cost from a start vertex \( a \) to an end vertex \( b \).
- **Assumptions:** Edges can have negative costs, but no negative cost cycles.
- **Shortest Path Spanning Tree:** Tree rooted at the start vertex containing the shortest paths to all other vertices.

**Triangle Inequality:**
- **Statement:** For vertices \( u, v, \) and \( w \), \( d(u, w) \leq d(u, v) + d(v, w) \).
- **Implication:** Ensures that the shortest path between any two vertices adheres to this inequality.

These topics cover the foundational concepts of graphs, their properties, and various algorithms and problems associated with graph theory, essential for your exam revision.
