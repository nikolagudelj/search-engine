<h1>
<b>Search engine za .html fajlove</b>

Program za pretragu 'reči u '.html' fajlovima u okviru određenog direktorijuma. 
</h1>

<h5>
<b>Pokretanje</b><br>
Klasa *ConsoleUI* sadrži u sebi sve komponente neophodne za efikasno pokretanje programa. 
Poziv metode *ConsoleUI.start()* startuje program. 
Neophodno je uneti korektnu putanju do direktorijuma. 
<b>Učitavanje</b><br>
  
Nakon unosa, poziva se metoda *HtmlLoader.getHtmlFiles()*, koja prolazi rekurzivno kroz ceo dati direktorijum, i u zasebnu listu odvaja putanje do svakog pojedinačnog *.html* fajla. Kada su svi fajlovi učitani, poziva se metoda *Parser.parse()*, koja parsira svaki fajl iz liste, i njegove reči ubacuje u strukturu <b>Trie</b>. 
Nakon punjenja Trie strukture, formira se objekat <b>Graph</b>, koji se koristi za prikaz međusobnih veza između *.html* stranica. 
</h5>

<h6>
Nakon učitavanja, korisnik unosi query za pretragu reči u celom skupu učitanih dokumenata. 
Korisnik ima mogućnost da bira između Osnovne i Kompleksne pretrage. 
Osnovna pretraga se sastoji od maksimalno jedne operacije. Primera radi:
  <br><code> python and java</code><br>
  <code> not python </code><br>
  <code> python java sql clojure </code>.<br>
  <i> Ukoliko korisnik ne koristi operatore, dozvoljen je bilo koji broj reči u queriju osnovne pretrage. </i>
</h6>
