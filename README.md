# Advent of Code 2023

Hier meine unbeholfenen Lösungen für den diesjährigen [AoC](https://adventofcode.com/2023/).
Proudly erstellt mit viel Frustrationstoleranz und dem [Python Grundlagenkurs](https://open.sap.com/courses/python1) von [Stephan](https://github.com/stjaco62) & [Christian](https://drumm.sh).

## Notes to day 7
Unfinished business. Nachgeholt am 20.12., weil ich das heutige Puzzle nicht verstehe. Habe zum ersten Mal eine Liste mit einer Funktion sortiert. Danach Multisort angewendet. Wäre im Nachgang wahrscheinlich in einem Schwung gegangen. Egal. Kleiner Kniff: Habe den internen Sortiervorgang der Karten nach ihrem Kartenwert gemacht (sonst ist A ja kleiner als K). Damit ich 13 Karten handlen kann, habe ich die Werte als hex abgespeichert. Teil 2 ging fast ausschließlich mit kosmetischen Änderungen. :-)

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

## Notes to day 15
Gelernt, mit enumerate von Listen umzugehen. Sehr schön. Benutze ich ab jetzt öfters.

## Notes to day 18
Eigentlich ganz smooth gelaufen: die Baggerbewegungen ablaufen und am Ende das ganze mit Flood Fill füllen. Leider kommt der Floodfill an die maximale Anzahl an rekursionen bei der Größe der Matrix. Musste völlig ehrlos ChatGPT zu Hilfe nehmen, um den Floodfill iterativ aufzubauen. Shame shame... 
Habe mich dann noch an den zweiten Teil gemacht. Allerdings habe ich die Rechnung ohne meinen Speicher gemacht. Erzeugt immer Dead Kernel. Komisch, die Matrix ist lediglich 10787185 x 16142015 groß... Egal. Habe heute ne Menge gelernt.  

## Notes to day 19
Not my puzzle today. Tierisch aufwändig über eine Menge Dictionaries gebaut. Das Beispielpuzzle funktioniert und liefert das richtige Ergebis. Das richtige Puzzle enthält aber mehrere Werte für einen Materialtyp, so dass ich den Materialtyp nicht als Schlüssel für das Dictionary verwenden kann. Was für ein Ärger. Habe dann ChatGPT verwendet, um mein Dictionary auf Tuples umzubauen. Jetzt bekomme ich ein anderes Ergebnis raus, diesmal zu hoch... wenn du ein totes Pferd reitest, steig ab. Für Documentationszwecke habe ich die zweite Lösung als day19.2 hochgeladen, auch wenn es sich um Teil 1 handelt. Habe noch eine dritte Version erstellt, diesmal mit eval. Tut super, führt aber leider weiterhin nicht zum richtigen Puzzle Ergebnis.

## Note to day 20
Not my piece of cake. Punching over my weight. Ich habe nichtmal ein Gefühl dafür, was hier zu tun ist. Habe stattdessen Tag 7 nachgeholt :-)

## Note to day 21
Ich hatte ja schon befürchtet, die AOC hätte sich jetzt vollständig aus meinem Niveau verabschiedet. Teil 1 ging aber heute. Happy.

## Note to day 22
Ist mir zu wild. 3D Arrays bilden schaffe ich heute nicht. Habe daher nochmal die offenen Sterne vorn angefangen. Teil 3.2 sollte schnell gehen - gings natürlich erstmal nicht...
