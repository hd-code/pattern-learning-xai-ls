---
title: "Lernen von Pattern-Sprachen mit XAI"
subtitle: "Handbuch zur Anwendung"
author: Hannes Dröse
date: 6.7.2021
lang: de
documentclass: article
classoption:
  - 10pt
  - a4paper
  - oneside
  - titlepage
geometry:
  - top=20mm
  - bottom=20mm
  - left=20mm
  - right=20mm
---

# Einführung

Bei diesem Projekt handelt es sich um eine Projektarbeit für das Modul "Lernende Systeme" an der FH Erfurt. Ziel ist es gewesen, den Algorithmus von Lange und Wiehagen zum Lernen von Pattern aus eingegebenen Zeichenketten in einer ansprechenden Anwendung umzusetzen. Dabei soll die Anwendung "sprechen" und transparent darlegen, was sie lernt und wie. Im Ergebnis ist eine interaktive Anwendung mit grafischer Nutzeroberfläche entstanden.

Das Projekt wird mittels einer `ZIP`-Datei bereitgestellt. Diese gilt es an einer beliebigen Stelle im System zu entpacken. Das entpackte Verzeichnis enthält das gesamte Projekt. Im folgenden wird dieses Verzeichnis stets als "Projektordner" bezeichnet.

# Installation und Verwendung

Grundsätzlich gibt es drei verschiedene Wege, die Anwendung zu starten. Die Komplexität steigt mit jeder der Optionen an.

## Option 1 – vorkompilierte Version starten {#opt1}

Dieses Projekt liefert lauffähige, compilierte Anwendungen für Windows und Mac mit. Das heißt, das Programm kann auf den erwähnten Plattformen direkt gestartet werden ohne eine weitere Installation.

Im Projektordner gibt es ein Verzeichnis namens `dist`, welches die lauffähigen Programme enthält.

**Windows:** Mit einem Doppelklick auf die Datei `pattern-learning-xai.exe` wird die Anwendung gestartet.

**Mac:** Mit einem Doppelklick auf die Datei `pattern-learning-xai.app` kann die Anwendung gestartet werden. Alternativ kann auch im Terminal die Datei `pattern-learning-xai` aufgerufen werden. Dies startet das Programm ebenfalls.

*Hinweis:* Sollte es bei der Ausführung der Programme zu Problemen kommen, bitte eine der beiden alternativen Optionen bemühen.

## Option 2 – Abhängigkeiten selbst installieren {#opt2}

Der Source-Code der Anwendung ist im Projektordner im Verzeichnis `src` zu finden. Der Code ist in Python geschrieben und kann entsprechend mittels dem Python-Interpreter ausgeführt werden. Dazu muss Python auf dem System installiert und lauffähig sein. Außerdem müssen externe Abhängigkeiten des Projektes vorher installiert werden.

### Vorraussetzungen {#install-python}

Es wird **Python** *Version 3.9 oder später* zur Ausführung der Skripte benötigt. Informationen zur Installation von Python sind der offiziellen Webseite unter <https://www.python.org> zu entnehmen.

Wichtig ist, dass Python korrekt installiert und der sog. `PYTHONPATH` Teil der Umgebungsvariable `PATH` (unter Windows und Mac) ist. Dies wird normalerweise automatisch während der Installation eingerichtet. Sollte das nicht richtig konfiguriert sein, werden bei der Installation der externen Abhängigkeiten von Python selbst Warnungen und Hinweise zum Beheben des Problems ausgegeben.

*Hinweis:* Um Befehle mit dem Python-Interpreter auf der Kommandozeile auszuführen, ist normalerweise der Befehl `python <args>` gedacht. Auf manchen Systemen muss aber `python3 <args>` geschrieben werden, damit die richtige Python-Version angesprochen wird. Die Befehle sind ansonsten komplett identisch.

### Abhängigkeiten installieren

Zusammen mit Python kommt das Tool `pip`, welches zum Installieren externer Abhängigkeiten verwendet werden kann.

Die einzige benötigte Abhängigkeit ist `PySimpleGui`. Das ist eine Bibliothek, die das Erstellen von GUIs stark vereinfacht. Zur Installation bitte folgenden Befehl in der Kommandozeile ausführen:

```sh
python -m pip install PySimpleGui
```

*Hinweis:* `pip` installiert Bibliotheken immer global für das gesamte System. Wenn das nicht gewünscht ist, lieber [Option 3](#opt3) bevorzugen.

### Anwendung starten

Nun können die Skripte in `src` ausgeführt werden. Dazu muss die Kommandozeile im Projektordner geöffnet werden. Anschließend muss folgender Befehl ausgeführt werden:

```sh
python src
```

Das sollte die Anwendung starten.

## Option 3 – `pipenv`, der cleanste Weg {#opt3}

`pipenv` ist ein Tool, mit dem die Abhängigkeiten eines Projektes in einer isolierten Umgebung verwaltet werden können. Dadurch sind deterministische Installationen möglich. Außerdem gibt es keine Konflikte, wenn zwei Python-Projekte die gleiche Bibliothek in unterschiedlichen Versionen benötigen.

### Vorraussetzungen

Auch für diese Option wird eine funktionierende Python-Installation benötigt. Siehe [Option 2 – Vorraussetzungen](#install-python).

### Installation von `pipenv`

`pipenv` ist ein normales Modul, welches mittels `pip` installiert werden kann. Dazu muss in der Kommandozeile folgender Befehl ausgeführt werden:

```sh
python -m pip install pipenv
```

### Installation der Abhängigkeiten

Im Projektordner befinden sich zwei Dateien `Pipfile` und `Pipfile.lock`. Mit diesen kann `pipenv` alle benötigten Abhängigkeiten installieren. Dazu muss die Kommandozeile im Projektordner geöffnet werden und dieser Befehl ausgeführt werden:

```sh
pipenv install
```

`pipenv` erzeugt nun eine isolierte Umgebung für diesen Ordner.

### Anwendung starten

Um die Anwendung zu starten, müssen die Skripte mit Hilfe von `pipenv` aufgerufen werden. Dazu bitte in der Kommandozeile im Projektordner den folgenden Befehl ausführen:

```sh
pipenv run python src
```

Das sollte die Anwendung starten.

# Automatische Tests

Im Projektordner gibt es ein Verzeichnis namens `test`. Dieses enthält automatisierte Tests für die Logik-Komponenten der Anwendung.

Die Tests können nur mittels Python-Interpreter ausgeführt werden. Das heißt, dass [Option 2](#opt2) oder [Option 3](#opt3) für die Installation verwendet werden muss.

Die Tests können ausgeführt werden, wenn der Projektordner in der Kommandozeile geöffnet und der folgende Befehl ausgeführt wird:

```sh
python test --verbose
```

oder mit `pipenv`:

```sh
pipenv run python test --verbose
```

Das Flag `--verbose` kann auch weggelassen werden. Dann werden nur fehlgeschlagene Tests auf der Konsole ausgegeben.
