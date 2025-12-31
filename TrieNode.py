
#208. Implement Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

def run_operations(ops, args):
    res = []
    trie = None
    for op, arg in zip(ops, args):
        if op == "Trie":
            trie = Trie()
            res.append(None)          # constructor -> null
        elif op == "insert":
            trie.insert(arg[0])
            res.append(None)          # insert -> null
        elif op == "search":
            res.append(trie.search(arg[0]))
        elif op == "startsWith":
            res.append(trie.startsWith(arg[0]))
    return res

def main():
    ops = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    args = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

    output = run_operations(ops, args)
    print(output)   # [None, None, True, False, True, None, True]


if __name__ == "__main__":
    main()
