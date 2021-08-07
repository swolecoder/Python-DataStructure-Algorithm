# A class to store a Trie node
class TrieNode:
    def __init__(self):
 
        # `count` and `key` is only set for leaf nodes
        # `key` stores the string, and `count` stores its frequency so far
        self.key = None
        self.count = 0
 
        # each node stores a dictionary to its child nodes
        self.character = {}
 

# Iterative function to insert a string into a Trie
def insert(head, str):
 
    # start from the root node
    curr = head
 
    for c in str:
        # go to the next node and create a new node if the path doesn't exist
        curr = curr.character.setdefault(c, TrieNode())
 
    # store key and its count in leaf nodes
    curr.key = str
    curr.count += 1



dict = [
        "code", "coder", "coding", "codable", "codec", "codecs", "coded",
        "codeless", "codec", "codecs", "codependence", "codex", "codify",
        "codependents", "codes", "code", "coder", "codesign", "codec",
        "codeveloper", "codrive", "codec", "codecs", "codiscovered"
    ]

root = TrieNode()
for word in dict:
    insert(root, word)
print(root)

print("hello")