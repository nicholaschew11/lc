from collections import defaultdict

class WordDictionary:

    def __init__(self):
        self.map = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.map[len(word)].append(word)
        

    def search(self, word: str) -> bool:
        if not word:
            return False
        if '.' not in word:
            return word in self.map[len(word)]
        for candidate in self.map[len(word)]:
            for i, c in enumerate(word):
                if candidate[i] != word[i] and c != '.':
                    break
            else:
                return True
        return False
                
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)