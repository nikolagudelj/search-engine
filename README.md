<h1>
<b>Search engine za .html fajlove</b>
</h1>

<h4>
Program za pretragu 'reči u '.html' fajlovima u okviru određenog direktorijuma.<br>
</h4>
<h3>
<b>Pokretanje</b></h3>
<p>
Klasa <i>ConsoleUI</i> sadrži u sebi sve komponente neophodne za efikasno pokretanje programa. 
  Poziv metode <i>ConsoleUI.start()</i> startuje program. 
Neophodno je uneti korektnu putanju do direktorijuma. <br>
</p>
<h3>Učitavanje</h3>
<p>
Nakon unosa, poziva se metoda <i>HtmlLoader.getHtmlFiles()</i>, koja prolazi rekurzivno kroz ceo dati direktorijum, i u zasebnu listu odvaja putanje do svakog pojedinačnog <i>.html</i> fajla. Kada su svi fajlovi učitani, poziva se metoda <i>Parser.parse()</i>, koja parsira svaki fajl iz liste, i njegove reči ubacuje u strukturu <b>Trie</b>. 
Nakon punjenja Trie strukture, formira se objekat <b>Graph</b>, koji se koristi za prikaz međusobnih veza između <i>.html</i> stranica. 
</p>

<h3>Trie struktura</h3>
<p>
Trie struktura je drvolika predstava reči u fajlovima, gde svaki čvor odgovara određenom karakteru.<br>
Konkretna implementacija se bazira na ideji da svaki čvor u sebi sadrži 26 referenci na sledeće slovo, gde je svaka od datih 26 referenci vezana za jedno slovo engleskog alfabeta, s obzirom na to da se ona najčešće nalaze u stranicama.
<br>
Po potrebi, ukoliko je pročitani karakter različit od slova alfabeta, traži se ili se dodaje odgovarajući karakter 
  na indeksima <b>26+</b> u listi referenci.
</p>

<h3>Graph struktura</h3>
<p>
Graf struktura je sačinjena od čvorova koji reprezentuju .html stranice i veza koje reprezentuju likove između tih stranica.
Radi efikasnosti, implementacija grafa je bazirana na Python rečnicima. Graf u sebi sadrži 2 rečnika; jedan modeluje izlazne, a drugi
ulazne ivice čvorova grafa.
Svaki ključ rečnika koji modeluje izlazne ivice predstavlja čvor od kojeg ivica polazi, dok se na mestu
vrednosti nalazi novi rečnik čiji ključ predstavlja odredišni čvor ivice, a vrednost je objekat koji modeluje tu ivicu.
<br>Analogno važi i za rečnik koji modeluje ulazne ivice.
</p>

<h3>Set struktura</h3>
<p>
Set struktura sa svojim operacijama unije, preseka i komplementa služi za određivanje rezultujućeg skupa .html stranica koje odgovaraju
prosleđenom upitu. Radi efikasnosti, implementacija skupa je bazirana na Python rečnicima. Dodavanje elementa u skup je zapravo dodavanje novog ključa u rečnik koji reprezentuje taj skup. Na taj način efikasno možemo dodati nove elemente bez pojava duplikata.
</p>

<h3>Pretraga</h3>
<p>
Nakon učitavanja, korisnik unosi query za pretragu reči u celom skupu učitanih dokumenata. 
Postoji mogućnost odabira između Osnovne i Kompleksne pretrage.<br> 
  Osnovna pretraga se sastoji od maksimalno jedne operacije. Imena operacija su <b> and, or, not </b><br>
  Primera radi:
  <br>&nbsp <code>python and java</code><br>
  &nbsp <code>not python </code><br>
  &nbsp <code>python java sql clojure </code>.<br>
  &nbsp <i>Ukoliko korisnik ne koristi operatore, dozvoljen je bilo koji broj reči u queriju osnovne pretrage. </i>
<br><br>
Kompleksna pretraga se sastoji od proizvoljnog broja operacija i reči. Pritom je neophodno ispoštovati osnovna matematička/logička pravila ispisa. Između svake 2 reči je neophodan operand. Zagrade moraju biti <i>matching</i>.
  <br>Dozvoljeni kompleksni operatori su: <b> ! ( ) || &&</b>.
<br>Primer kompleksnog querija:<br>
  &nbsp <code>!python || java</code> 
  <br>
  &nbsp <code>java || (python && !(sql || clojure))</code>


</p>

<p>
Nakon unetog querija, pozivaju se odgovarajuće klase za logičku proveru korektnosti unosa. Klase za proveru su 
  <i>BasicQueryChecker</i> i <i>ComplexQueryChecker</i>.
  Obe klase koriste eksternu biblioteku <b>PYL</b> (Python-Lex-Yacc) kako bi definisale gramatička pravila kojima uneti query mora da se "pokori". Ukoliko dođe to nepoštovanja gramatičke norme, <i>Checkeri</i> bacaju <code>SyntaxError</code>, i aplikacija traži ponovni unos querija.
  <br><a href="https://www.dabeaz.com/ply/"> Link za zvanicnu stranicu PYL parsera </a><br>
<br>
Nakon pretrage skupa svih stranica, dobijamo rezultujući set stranica, koje ispunjavaju uslove pretrage. Pre nego što ih ispišemo u terminalu, pozivamo metodu za <i>rangiranje</i> datih stranica, tako da najrelevantnije stranice, sa najvećim rezultatom operacije <code>rank</code> budu istaknute na vrhu pretrage, dok su one slabije rangirane pri dnu.
</p>
<br>
<p>
  Python interpreter Version 3.8<br>
  pip Version 19.2.3<br>
  setuptools Version 41.2.0
</p>


<h2><u>Pregled algoritama</u></h2>
<h3>Ubacivanje u Trie</h3>
<p>
Nakon što parser učita određeni fajl, u polju 'parser.words' se nalazi niz svih reči na koje 
je parser naišao u okviru datog fajla.<br>
Da bismo popunili Trie strukturu, pokrećemo for-loop, koji svaku reč ponaosob
ubacuje u Trie. Kao što se u sledećem isečku pseudokoda može videti:<br>

<code>
node = self <br><br>
for character in word:
<br> &nbsp if not node.next[charIndex].exists: <br>
&nbsp &nbsp node.next[charIndex] = new Trie() <br>
&nbsp node = node.next[charIndex]
</code><br><br>
Dakle, za svaki karakter u okviru reči proveravamo da li postoji čvor koji ga predstavlja.
Ako ne postoji, kreiramo ga, ako postoji, samo skočimo na njega. Loop traje dok ne dođemo do poslednjeg 
slova u reči. <br>
Kada smo u finalnom čvoru, dolazi na red inkrement broja pojavljivanja te reči u 
stranici koja se trenutno učitava.
</p>
<h3>Brojanje pojavljivanja po stranici</h3>
<p>
U okviru Trie strukture implementirano je polje <i>pages</i>, koje je nista drugo
do običan niz intedžerskih vrednosti. Ono po čemu je specifično, je to da se tokom
učitavanja stranica pomoću Parsera, svaka stranica obeleži nekim brojem K.
Pritom K = (0, N), gde je N ukupan broj učitanih stranica. <br>
Parovi <i>page : pageID </i> se čuvaju u odvojenom dictionariju, da možemo u svakom momentu da im pristupimo <br>
Kada dođemo do poslednjeg čvora, gledamo u prosleđeni argument <i>pageNum</i> (K),
koji predstavlja identifikacioni broj (ID) stranice koja se učitava u tom momentu.
U nizu vrednosti <i>pages</i>, na indeksu <i>pageNum</i>, inkrementiramo vrednost za 1.
Podrazumevano je da je startna vrednost datog niza ekvivalentna C-komandi <br>
<code>pages = calloc(N * sizeof(int))</code><br><br>
Da demonstriram ovu primenu, recimo da u prosleđenom folderu imamo 3 <i>.html</i>
fajla. I recimo da se u svakom od njih samo pojavljuje reč <i>python</i>, 2, 3 i 4 puta respektivno.<br>
U Trie strukturi, kada siđemo niz čvorove putanjom <i>p-y-t-h-o-n</i>, posmatramo <i>pages</i>
u čvoru <b>N</b>. Njegov <i>pages</i> bi izgledao ovako: <br>
<code>
node.pages = [2   3   4]
</code><br><br>
Ukoliko dodamo četvrtu stranicu, sa 10 ponavljanja reči <i>python</i>, imali bismo<br>
<code>
node.pages = [2   3   4   10]
</code><br>

Ova logika se primenjuje za sve ostale reči analogno.<br>
Ako želimo da vidimo koliko puta se reč <i>python</i> pojavljuje u stranici 
<i>index.html</i>, proces je sledeći.<br>
1. Siđemo do čvora <b>N</b> u reči <i>python</i>.<br>
2. Pogledamo u dictionary, koja je ID vrednost stranice <i>index.html</i><br>
3. Datu ID vrednost (nazovimo je K), tražimo u <i>pages</i> strukturi čvora.
4. <code>pythonOccurences = node.pages[K]</code>
</p>

<h3>Parsiranje query izraza</h3>
<p>
U okviru programa se koristi eksterna biblioteka <i>PLY</i>, odnosno <b>Python-Yacc-Lex</b>, koja 
je ništa drugo do implementacija ovih klasičnih C-ovskih alata u Pythonu. Iskorišćena je kao 
sredstvo da se uneti query podvrgne logičkom testiranju po specificiranoj <i>BNF gramatici</i>, kako 
bi klase koje računaju rezultate querija, mogle da rade sa unapred korektnim izrazima, bez potrebe za 
dodatnim proverama. <br>
Implementacija je krajnje jednostavna, uprkos relativno lošoj čitljivosti ove biblioteke. Definisan je lekser,
koji proverava da li je uneti karakter u queriju korektan. Ukoliko se učita nedozvoljeni karakter, program 
baca <code>Lexic error</code>, i obaveštava korisnika. <br>
Ukoliko je unos korektan, query se prosleđuje <i>Yacc</i> parseru, koji prolazi kroz string, i klasičnom
Yacc/Bison metodom Finite-Automata, proverava da li je query logički korektan u odnosu na zadata pravila
unosa.<br>
Osnovna pretraga je relativno jednostavna, dozvoljava <b>jedan</b> operator i <b>dve</b> reči, ili
<b>nijedan</b> operator i <b>neograničeni</b> broj reči, koje su u tom slučaju odvojene implicitnim <i>or</i>
operatorom. <br>
Kompleksni query zahteva dublju matematičku analizu, zbog prisustva zagrada i kompleksnije matematičke 
računice kod računanja rezultata. Primer korektnog izraza je:<br>
<code>
&nbsp !python || (java && (sql || !rust))
</code><br>
Parser učitava ovaj string, i proverava da li je logički korektan, prateći rekurzivnu formu definisanu 
u pravilima gramatike. Konkretan isečak ove gramatike glasi: <br>
<code>
QUERY : <br> 
OPERATOR <br> 
&nbsp | UNARY LEFT_PAREN QUERY RIGHT_PAREN <br> 
&nbsp | QUERY BINARY_OP QUERY <br> 
</code><br>
Ovom rekurzivnom definicijom, pokrivene su sve moguće kombinacije unosa. <br>
Ukoliko parser naiđe na grešku u unosu, baca <code>Syntax Error</code>.
</p>

<h3>Računanje kompleksnog izraza </h3>
<p>
Pretpostavimo da je parser prihvatio uneti korisnički query, i da sada preostaje da se izračuna rezultat
datog izraza. Recimo da je u pitanju izraz <code>!python || java</code>. <br>
Procedura je sledeća: <br>
1. Pretvorimo uneti string iz <i>infiksne</i> u <i>Obrnutu poljsku (postfiksnu)</i> notaciju. <br>
&nbsp <code> !python || java  =>  python ! java || </code><br>
2. Parsiramo string po individualnim rečima/operatorima, i formiramo <i>array</i> koji u svakom polju
sadrži po jedan token querija. <br>
&nbsp <code> query = [python ! || java]</code> <br>
3. Prosledimo niz u poljskoj notaciji klasi <code>PolishNotation</code>, koja jednostavnom for-petljom
iterira kroz niz, i redukuje ga kada god naiđe na operaciju (binarnu/unarnu). <br>
4. Nakon <b>N</b> iteracija, niz će biti redukovan na jedan član, koji je u stvari naš rezultujući set. <br>
5. Vratimo rezultujući set u pozivajuću funkciju, kako bi se stranice tog skupa/seta rangirale i prikazale korisniku.<br>
</p>

<h3>Rangirana pretraga</h3>
<p>
Rangiranje rezultujućeg skupa .html stranica se bazina na modifikovanom PageRank algoritmu koji nagrađuje stranice koje u sebi sadrže tražene reči.
To je iterativni algoritam gde se u svakoj iteraciji rang stranice izračunava po sledećoj formuli: <br>
<br> &nbsp <code> rank(A) = (1 - d) + d * (Σ(rank(Bi) / L(Bi)) * (1 + log(brA/ubrA + 1, 2))) </code><br><br>
A - stranica za koju računamo rank <br>
d - faktor prigušenja <br>
Bi - stranice koje sadrže link ka stranici A <br>
L(Bi) - ukupan broj stranica na koje stranica Bi linkuje <br>
brA - broj traženih reči na stranici A <br>
ubrA - ukupan broj reči na stranici A <br> <br>

Smisao izraza <code>1 + log(brA/ubrA + 1, 2)</code> jeste da podigne rank stranice koja sadrži tražene reči. Rezultat ovog izraza biće
broj iz intervala [1, 2] (1 u slučaju da stranica ne sadrži tražene reči - rank ostaje nepromenjen; 2 u slučaju da sve reči na datoj
stranici odgovaraju prosleđenom upitu).
</p>

<h3>Prikaz i paginacija rezultata</h3>
<p>
Nakon određivanja rankova svih stranica iz rezultujućeg skupa, vrši se sortiranje po ranku. Za sortiranje se koristi rekurzivni algoritam QuickSort. Pseudokod: <br>
<br>
<code>
QuickSort(Niz, Levi, Desni)<br>
&nbsp If Levi < Desni Then<br>
&nbsp &nbsp Pivot = Particija(Niz, Levi, Desni)<br>
&nbsp &nbsp QuickSort(Niz, Levi, Pivot - 1)<br>
&nbsp &nbsp QuickSort(Niz, Pivot + 1, Desni)<br>
<br>
Particija(Niz, Levi, Desni)<br>
&nbsp Pivot = Niz(Desni)<br>
&nbsp i = Levi - 1<br>
&nbsp for j in (Levi, Desni)<br>
&nbsp &nbsp if Niz(j) <= Pivot<br>
&nbsp &nbsp &nbsp i++<br>
&nbsp &nbsp &nbsp Zameni(Niz(i), Niz(j))<br>
&nbsp i++<br>
&nbsp &nbsp Zameni(Niz(i), Niz(Desni))<br>
&nbsp return i<br>
</code>
</p>
<p>
Paginacija rezultata se moze predstaviti sledećim algoritmom:<br>
<img src="https://i.imgur.com/FsSCC7O.png" alt="algoritam">
</p>
