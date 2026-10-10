# Am Wasser · Fassung 2

Lernwebseite für die Fischerprüfung in Hessen. Kurze Lehrbuchtexte, Skizzen, Wort-Hilfen und 563 Fragen aus dem bereitgestellten Katalog.

## Gesicherte Grundlage

Fassung 1 bleibt unter https://mhapunkt.github.io/am-wasser/ erhalten.

Fester Ausgangsstand: https://github.com/mhapunkt/am-wasser/tree/v1.0-grundlage
Commit: `63abace0b51c9fe858a0a19d784935ae8d654484`.

## Neu in Fassung 2

- Einzelantworten mit Zeitpunkt, gewählter Antwort, Ergebnis und Übungsart.
- Ermutigende Hinweise ab zwei falschen Antworten hintereinander oder drei falschen unter den letzten fünf Versuchen. Spätere Verbesserungen werden ebenfalls erkannt.
- Gezieltes Wiederholen schwieriger Fragen.
- Historie abgeschlossener und vorzeitig beendeter Lernrunden und Prüfungssimulationen.
- Prüfungssimulation: 60 zufällig gewählte Fragen, 12 je Gebiet, 120 Minuten. Bestanden mit mindestens 45 richtigen insgesamt und mindestens 9 in jedem Gebiet.
- Antworten während der Prüfung änderbar, Fragen überspringbar. Lösungen erst nach Abgabe. Zeitablauf führt zur Auswertung. Bei geschlossener Seite erfolgt diese beim nächsten Öffnen mit dem ursprünglichen Endzeitpunkt.
- Laufende Prüfungen bleiben beim Neuladen erhalten; die Zeit läuft weiter.
- JSON-Sicherung und Wiederherstellung einschließlich Historie. Import ersetzt nach Bestätigung den aktuellen Stand.

Die Simulation ist kein amtlicher Prüfungsbogen und keine staatliche Prüfung. Sie prüft den schriftlichen Fragebogenteil; praktische Unterweisung und Zulassung sind nicht Bestandteil dieser App. Die Uhr ist eine Browserfunktion, kein manipulationssicherer Prüfungsserver.

## Quellen und Datenstand

Regeln: §§ 23–24 Hessische Fischereiverordnung, amtlich veröffentlicht am 28.04.2023, GVBl. S. 318 ff.; geprüft am 10.10.2026.
https://starweb.hessen.de/cache/GVBL/2023/00015.pdf
https://landwirtschaft.hessen.de/wasser/fischerei

Fragen: bereitgestelltes PDF, Bund Oktober 2023 / Hessen April 2024. Der Katalog bleibt bewusst unverändert zur gesicherten Grundlage. Keine Behauptung, dass damit spätere Katalogänderungen abgedeckt sind.

## Speicherung

Alle Lernstände bleiben im lokalen Browser-Speicher. Kein Konto, kein Server für Antworten und keine Synchronisierung zwischen Geräten. Fassung 2 nutzt einen eigenen Speicherschlüssel. Beim ersten Öffnen kann sie Zähler aus Fassung 1 auf derselben Domain übernehmen; historische Zeitpunkte werden dabei nicht erfunden. Die erste Fassung wird nicht verändert.

Auf gemeinsam benutzten Geräten teilen Nutzer desselben Browserprofils den Lernstand. Für unterschiedliche Kinder getrennte Browserprofile verwenden. Regelmäßig „Verlauf sichern“ nutzen: Beim Löschen des Browser-Speichers gehen ungesicherte Daten verloren.

## Entwicklung

`src/page.html` enthält Darstellung und Logik. Die JSON-Dateien enthalten Fragen, Lektionen und zusätzliche Erklärungen.

```sh
python3 build.py
node test.cjs
python3 -m http.server 8765 --bind 127.0.0.1
```

Ohne Installation direkt `index.html` öffnen. GitHub Pages liefert die Datei aus `main` im Stammverzeichnis aus.

Die Tests prüfen Themenverteilung, Bestehensgrenzen, Zeitlimit, Wiederaufnahme, Antwortänderungen, doppelte Einträge, Lernhinweise, Import und getrennte Speicherung der ersten Fassung.
