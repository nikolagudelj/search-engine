# Search engine (University course project 2020)

## Python application for word search in HTML documents inside a directory.

## How to run
#### Run ```ConsoleUI```, and enter the path to directory you wish to search through.

## Technicalities
#### After you enter the path to directory, ```HtmlLoader.getHtmlFiles()``` is called. It iterates recursively through the directory, while storing absolute paths to all ```.html``` files. When this iteration is completed, ```Parser.parse()``` is called. It parses every ```.html``` file which was found. During parsing, every word from each file is put into a ```Trie``` structure. After forming the ```Trie```, a ```Graph``` object is created, to model relationships between different ```.html``` files.

* Trie structure:
  * Tree-like structure, which keeps track of all words which appear in ```.html``` files.
  * This implementation is based on the idea that every node contains 26 children, where each child is a reference to an ```ASCII``` character. If a ```non-ASCII``` character is found, a new child is appended to the children's list.

## Search
After all the ```.html``` files have been read and parsed into data structures, the user can perform search queries. A query can be ```Basic``` or ```Complex```.
* <a href="https://github.com/nikolagudelj/search-engine/blob/master/BasicQuery/BasicParser.py">Basic query</a>
  * Contains a maximum of 1 operation. 
  * Operations are: ```and```, ```or```, ```not```.
  * Examples: 
    * *python and java*
      * This will return a list of all ```.html``` files which contain words *python* and *java*
    * *not python*
      * This will return a list of all ```.html``` files which do **not** contain the word *python*
    * *python java kotlin sql*
      * When querying without operators, we can use any number of words, and the default operator is ```or```
* <a href="https://github.com/nikolagudelj/search-engine/blob/master/ComplexQuery/ComplexParser.py">Complex query</a>
  * Supports complex logical expressions for more elaborate queries.
  * Allowed operators are ```!```, ```()```, ```||```, ```&&```
  * Examples:
    * *!python && java*
    * *java || (python && !(sql || kotlin))*
  * Complex queries are parsed and evaluated by a custom parser implemented using [ply](https://www.dabeaz.com/ply/)


When the application finds all the ```.html``` files which fit the query, they are ranked using a custom ```PageRank``` algorithm. This algorithm works on the principles of Google's initial PageRank algorithm, thus taking into account the number of external links to that page and number of word appearances.





