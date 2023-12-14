# Advent of Code 2023

Hier meine unbeholfenen Lösungen für den diesjährigen [AoC](https://adventofcode.com/2023/).
Proudly erstellt mit viel Frustrationstoleranz und dem [Python Grundlagenkurs](https://open.sap.com/courses/python1) von Stephan & [Christian](https://drumm.sh).

## Notes to day 7
Unfinished business. Vielleicht hole ich das am WE noch nach

## Notes to day 8
Ich war so stolz auf meine Lösung (day8.21.py). Leider wohl etwas rechenintensiv, dass mein MBP M1 auch nach 2h keine Lösung gebracht hat. Ohne Christian wäre das hier ein grauer Stern. Der Punkt geht also eigentlich an ihn.
Anmerkung zur Anmerkung: Wenn man die Dauer der Berechnung auf Basis der 6 Schritte hochrechnet, dauert die Rechenzeit 8,8 Jahre :-o  

## Notes to day 9
In der ursprünglichen Lösung habe ich die While Schleife mit der Bedingung abgebrochen, dass die Summe aller Ableitungen = 0 sei. Leider gibt es eine Zeile, bei der die Summe der Ableitungen 0 ist, obwohl nicht alle Werte 0 sind z.B. [-14, 7, 7]. Hat mich gut 90 min gekostet, das zu finden. Oh mann...

## Notes to day 10
Teil 1 ist sicherlich das haesslichste Stück Code meiner bisherigen AOC. Aber funktioniert.
Teil 2 habe ich nach wilder Recherche den flood-fill Algorithmus entdeckt und angewendet. Hat mir ein paar schöne Visualisierungs-Snippets gebracht. Leider hat die Aufgabenstellung für dieses Vorgehen ein besonderes Schmankerl: Das Tier kann sich zwischen den Rohren durchquetschen. Damit ist das wohl ein #fail... :-( 
Schade eigentlich.

## Notes to day 11
Gut angefangen heute, Teil 1 ging verhältnismäßig gradlinig und schnell (im Rahmen der begrenzten Möglichkditen). Teil 2 war leider totales Desaster. Habe tolle arrays gebaut und das ging auch richtig gut. Leider war das Ergebnis aber konstant um 10 niedriger als das Beispiel und die vorgehende Lösung. Habe dann 2h gebraucht, um festzustellen, dass der Ansatz der Manhattan Distance nicht mit meinen Werten in der Matrix funktioniert (oder ich habe es einfach nicht zum Funktionieren gebracht). Was für ein Scheiß!

## Notes to day 14
Eigentlich ganz prima gelaufen. Musste den ersten Teil 2 Mal bauen, der erste Ansatz mit numpy arrays war zu kompliziert (für meinen Kopf). Also neu und einfacher gestrickt. Habe auch eine funktionierende Lösung für Teil 2 gebaut, bin dann aber leider an der Milliarde Cycles gescheitert - bzw. an den rund 78h Laufzeit. Leider hat sich meine Funktion auch nicht eingependelt, so dass ich die Schätzmethodik nicht anwenden konnte. Nun gut, in Summe bin ich happy, ein Teilstern für Teil 2 wäre schön gewesen :-)
