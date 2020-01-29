class Trie(object):
    """""
    Svaki node Trie drveta ima u sebi 45 referenci na sledece slovo (45 ovde jer ima 45 slova engleskog alfabeta + specijalnih znakova)
    Te reference su na kreaciji postavljene na None, tj nisu ucitane
    Primera radi, ako hocemo da ucitamo rec JA u strukturu.
        Prvo cemo referencu iz nextLetter niza, koja odgovara slovu J staviti da bude novi Trie() node.
        Zatim se spustimo u referencu J, pa onda u njenom skupu nextLetter, kreiramo novi cvor na mestu
        slova A, tako da vise nije None, vec novi Node.
    Upotreba polja Value je trenutno da nam daje Word count odredjene reci.
    Ovaj konkretan Trie objekat funkcionise za ASCII slova alfabeta, i za sledece znakove:

        0 1 2 3 4 5 6 7 8 9 . , [ ] ( ) _ -

    Svi ostali znakovi su trenutno nepodrzani.
    """

    def __init__(self):
        self.nextLetter = [None] * 45
        self.value = 0

    def insertWord(self, word):
        node = self
        word = word.lower()
        for c in word:
            if ord(c) in range(ord('a'), ord('z')):
                " ASCII vrednost karaktera ukoliko je u pitanju slovo "
                asciiValue = ord(c) - ord('a')
            else:
                " ASCII vrednost karaktera ukoliko je u pitanju specijalan znak 0-9 ili zagrade/crtice "
                asciiValue = self.otherAsciiCharacter(c)

            if (node.nextLetter[asciiValue] == None):
                node.nextLetter[asciiValue] = Trie()
            node = node.nextLetter[asciiValue]

        "Value nam broji ponavljanje reci"
        node.value += 1

    def otherAsciiCharacter(self, char):
        " Specijalna funkcija koja odredjenim specijalnim karakterima dodeljuje mesto u nizu polja Trie "
        switcher = {
            '1': 27,
            '2': 28,
            '3': 29,
            '4': 30,
            '5': 31,
            '6': 32,
            '7': 33,
            '8': 34,
            '9': 35,
            '0': 36,
            '.': 37,
            ',': 38,
            '(': 39,
            ')': 40,
            '[': 41,
            ']': 42,
            '/': 43,
            '_': 44,
            '-': 45,
        }
        return switcher.get(char, 0)

    def getTrieArrayIndexForChar(self, char):
        if ord(char) in range(ord('a'), ord('z')):
            return ord(char) - ord('a')
        else:
            return self.otherAsciiCharacter(char)

    def printWordCount(self, word):
        node = self
        word = word.lower()

        for char in word:
            index = self.getTrieArrayIndexForChar(char)
            if node.nextLetter[index] != None:
                node = node.nextLetter[index]
            else:
                print("Rec '" + word + "' se ne pojavljuje u fajlovima.")
                return

        print(node.value)
