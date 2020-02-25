<h1>
<b>Search engine za .html fajlove</b>
</h1>

<h4>
Program za pretragu 'reči u '.html' fajlovima u okviru određenog direktorijuma.<br>
<h4>
  
<h3>
<b>Pokretanje</b></h3>
<p>
Klasa *ConsoleUI* sadrži u sebi sve komponente neophodne za efikasno pokretanje programa. 
Poziv metode *ConsoleUI.start()* startuje program. 
Neophodno je uneti korektnu putanju do direktorijuma. <br><br>
</p>
<h3><b>Učitavanje</b></h3>
 
<p>
Nakon unosa, poziva se metoda <i>HtmlLoader.getHtmlFiles()</i>, koja prolazi rekurzivno kroz ceo dati direktorijum, i u zasebnu listu odvaja putanje do svakog pojedinačnog <i>.html</i> fajla. Kada su svi fajlovi učitani, poziva se metoda <i?Parser.parse()</i>, koja parsira svaki fajl iz liste, i njegove reči ubacuje u strukturu <b>Trie</b>. 
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
  Python interpreter Version 3.8
  pip Version 19.2.3
  setuptools Version 41.2.0
</p>
