class TrieNode:

    def __init__(self):
        self.hash = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.hash:
                curr.hash[char] = TrieNode()
            curr = curr.hash[char]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.hash.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.hash:
                        return False
                    curr = curr.hash[c]
            return curr.end

        return dfs(0, self.root)
