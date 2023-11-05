class Node:
    def __init__(self, freq_, symbol_, left_=None, right_=None):
        self.freq = freq_
        self.symbol = symbol_
        self.left = left_
        self.right = right_
        self.huff = ""

def print_nodes(node, val=""):
    new_val = val + str(node.huff)
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")

def huffman_encoding(word):
    # Calculate the frequency of characters in the given word
    freq = {}
    for char in word:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    chars = list(freq.keys())
    frequencies = list(freq.values())

    nodes = [Node(frequencies[x], chars[x]) for x in range(len(chars))]

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes[0]
        right = nodes[1]
        left.huff = 0
        right.huff = 1
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)

    print("Huffman Encoding:")
    print_nodes(nodes[0])

if __name__ == "__main__":
    word = input("Enter a word: ")
    huffman_encoding(word)

"""
Characters: [a, b, c, d, e, f]
Frequency: [5, 9, 12, 13, 16, 45]

Step 1: Frequency Analysis
a: 5
b: 9
c: 12
d: 13
e: 16
f: 45

Step 2: Priority Queue
(a, 5) (b, 9) (c, 12) (d, 13) (e, 16) (f, 45)

Step 3: Building the Huffman Tree
1. Take the two nodes with the lowest frequencies: (a, 5) and (b, 9)
   Create a new node with frequency 14 and set the two nodes as its children.
   New Node: (null, 14)

2. Updated Priority Queue:
(c, 12) (d, 13) (e, 16) (f, 45) (null, 14)

3. Take the two nodes with the lowest frequencies: (c, 12) and (d, 13)
   Create a new node with frequency 25 and set the two nodes as its children.
   New Node: (null, 25)

4. Updated Priority Queue:
(e, 16) (f, 45) (null, 14) (null, 25)

5. Take the two nodes with the lowest frequencies: (e, 16) and (null, 14)
   Create a new node with frequency 30 and set the two nodes as its children.
   New Node: (null, 30)

6. Updated Priority Queue:
(f, 45) (null, 25) (null, 30)

7. Take the two nodes with the lowest frequencies: (null, 25) and (null, 30)
   Create a new node with frequency 55 and set the two nodes as its children.
   New Node: (null, 55)

8. Updated Priority Queue:
(f, 45) (null, 55)

9. Take the two nodes with the lowest frequencies: (f, 45) and (null, 55)
   Create a new node with frequency 100 and set the two nodes as its children.
   New Node: (null, 100)

10. Updated Priority Queue:
(null, 100)

Step 4: Huffman Tree
         (null, 100)
         /          \
        (null, 55)    f
       /           \
    (null, 25)     (null, 30)
     /       \
 (null, 14)  e
             /   \
          (a, 5) (b, 9)

Step 5: Assigning Codes
f: 1
e: 001
a: 0000
b: 0001
c: 010
d: 011

Step 6: Encoding
Input: cbedaf
Encoded Output: 0100001011001

Step 7: Decoding
Encoded Input: 0100001011001
Decoded Output: cbedaf

"""