from Projekat.parser import Parser
from Projekat.trie import Trie
import os
import time

trie = Trie()
parser = Parser()

path = "C:\\Users\\Gudli\\Desktop\\OISISI Drugi projekat\\python-2.7.7-docs-html"

module_counter = 0

start = time.time()
"""
    OS.Walk() prolazi kroz ceo zadati direktorijum i belezi imena fajlova, kao i path do njih. 
    Zatim pomocu for petlje, uzimamo svaki .html fajl koji smo pronasli i parsiramo ga. 
    Nakon sto isparsiramo svaki, u okviru polja parser.words ce se nalaziti Array Stringova koji predstavljaju 
    reci. Taj Array onda prosledimo strukturi Trie, koja svaku rec ponaosob ubacuje u strukturu.
    Loop se ponavlja za svaki .html fajl dok ne popunimo drvo u potpunosti.
"""
for root, dirs, files in os.walk(path, topdown = False):
    for filename in files:
        if r".html" in filename:
            "Ova linija uzima filename, i spaja ga sa root directorijem, tako da dobijemo Absolute Path"
            parser.parse(os.path.join(root, filename))
            for word in parser.words:
                word = word.lower()
                trie.insertWord(word)
                #if word == "module":
                #    module_counter += 1

end = time.time()

print("Counter module occurences: " + str(module_counter) + "\nRecognized module occurences: ", end = "")
trie.printWordCount("module")
print("Time elapsed: " + str(end-start))