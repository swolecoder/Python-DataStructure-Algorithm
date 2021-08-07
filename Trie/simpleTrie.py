

class Trie:
    def __init__(self):
        self.root = {}
    

    def insert(self,word):

        root = self.root

        for w in word:

            if w not in root:
                # do stuff
                root[w] = {}
            root = root[w]
        root["#"] = True
            
    
    def find(self,word):
        root = self.root

        for w in word:
            if w not in root:
                return None
            
            root = root[w]
        
        # now find if its the end
        for k,v in root.items():
            if k != "#":
                return False
            return True

tr = Trie()
tr.insert("here")
# tr.insert("hear")
# tr.insert("he")
# tr.insert("hello")
# tr.insert("how ")
# tr.insert("her")
a = tr.find("he")
print("A",a)