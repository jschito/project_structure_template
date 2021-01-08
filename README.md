# Mein Projekt

## Kurzbeschreibung
In diesem Beispiel werden die Werte eines JSON-Files geladen und in ein CSV geschrieben. All dies hängt davon ab, ob man als Argument das Szenario "A", "B" oder "C" eingibt. 

## Zur Ordnerstruktur
Die vorgeschlagene Ordnerstruktur muss nicht zwingend eingehalten werden. Es lohnt sich aber, bestimmte Dokumenttypen voneinander zu trennen. In unserem Vorschlag sind dies:
- res: resources; hier speicherst du deine Daten ab (z.B. json, xml, xls, tiff, etc.), auf die du mit deinen Scripts zugreifst. 
- src: sources; hier speicherst du deine Scripts ab (z.B. R, sql oder py). Dieser Ordner kann in PyCharm speziell markiert werden. 
- doc: documents; hier speicherst du die Dokumentationen zu deinem Projekt ab, z.B. Berichte, Metadaten oder externe Dokumente. 
- output: output; wir schlagen vor, für die Outputs einen speziellen Ordner zu generieren, damit die Ausgabedaten von den Eingangsdaten getrennt sind. 

## Datensätze
Der unter *res* gespeicherte Datensatz *scenario.json* ist ein Testdatensatz im JSON-Dateiformat. Darauf wird in constants.py zugegriffen. 