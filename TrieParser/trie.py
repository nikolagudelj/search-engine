__author__ = "Nikola"

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
        self.nextLetter = [None] * 26
        self.pages = []

    def insertWord(self, word, pageNum):
        node = self
        word = word.lower()
        for c in word:
            index = node.getArrayPosition(c, 1)

            if node.nextLetter[index] is None:
                node.nextLetter[index] = Trie()
            node = node.nextLetter[index]

        """" 
            Svaki node ima Array u kom se cuva broj ponavljanja te reci u svakom fajlu.
            Svaki fajl ima svoj redni broj, i na tom rednom broju u okviru arraya se belezi broj ponavljanja.
            Npr ako fajl HtmlTest1.html ima redni broj 6, u Array[5] ce se nalaziti broj ponavljanja reci "x".
        """
        while node.pages.__len__() <= pageNum:
            node.pages.append(0)
        node.pages[pageNum] += 1

    def getArrayPosition(self, char, flag):
        " Specijalna funkcija koja odredjenim specijalnim karakterima dodeljuje mesto u nizu polja Trie "
        if ord(char) in range(ord('a'), ord('z') + 1):
            return ord(char) - ord('a')
        else:
            index = 26
            list_length = self.nextLetter.__len__()

            while index < list_length:
                if self.nextLetter[index].value == char:
                    return index
                index += 1

            """ 
                Flag nam sluzi da kazemo funkciji da li zelimo da kreiramo novi index, ili samo da proverimo da li "
                zadati indeks postoji. 
                flag == 0    ->  samo gledamo da li postoji 
                flag == 1    ->  dodajemo dati indeks ako ne postoji
            """
            if flag == 0:
                return -1
            self.nextLetter.append(Trie())
            self.nextLetter[index].value = char

            #print("Trazili ste slovo " + char + " , ono je na indeksu " + str(index))
            return index

    " Returns the custom ASCII value for the given character"
    def getTrieArrayIndexForChar(self, char):
        return self.getArrayPosition(char, 0)

    " Vraca niz intedzera, gde je svaki clan niza broj ponavljanja reci <word> na stranici ciji je to indeks"
    def findContainingPages(self, word):
        node = self
        for char in word:
            index = node.getTrieArrayIndexForChar(char)
            if index == -1:
                return {}
            if node.nextLetter[index] is None:
                return {}
            else:
                node = node.nextLetter[index]

        return node.pages

    " Vraca ukupan broj pojavljivanja reci <word> u svim stranicama "
    def getTotalWordCount(self, word):
        node = self

        for char in word:
            index = node.getArrayPosition(char, 0)
            if index == -1:
                return 0
            if node.nextLetter[index] is not None:
                node = node.nextLetter[index]
            else:
                return 0
        word_count = 0
        for pageCount in node.pages:
            word_count += pageCount

        return word_count

    " Vraca ukupan broj ponavljanja reci <word> u stranici oznacenoj brojem <pageNum>"
    def getWordCountForPage(self, word, pageNum):
        node = self

        for char in word:
            index = node.getArrayPosition(char, 0)
            if index == -1:
                return 0
            if node.nextLetter[index] is not None:
                node = node.nextLetter[index]
            else:
                return 0

        if node.pages.__len__() < pageNum + 1:
            return 0
        return node.pages[pageNum]