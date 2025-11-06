(Deutsch / English)

DEUTSCH

Kurzbeschreibung

Ein einfacher Schuldenrechner mit grafischer Oberfläche (für Pythonista iOS ui-Modul). Er erlaubt, mehrere Personen anzulegen, Zahlungen mit einem oder mehreren Zahlern zu erfassen, Aufteilungen auszuwählen und die resultierenden Schulden / Forderungen zu berechnen und anzuzeigen.
Features

Personenliste erfassen (bis zu 20 Personen).
Mehrere Zahler pro Zahlung möglich (je Zahler Betrag eingeben).
Aufteilung wählen: „Auf alle“ oder eine Auswahl einzelner Personen.
Zahlung hinzufügen und Liste der Zahlungen führen.
Berechnung pro Person:
Auflistung, wem die Person Schulden hat.
Auflistung, von wem die Person Geld erhält.
Gesamtschuld, Gesamterhalt und Netto-Saldo.
Eingabevalidierung: mindestens ein Name, positive Beträge, mindestens eine Zahlung vor Berechnung.
Friendly GUI mit Buttons, Labels und Ergebnis-Textfeld.
Installation

Erforderlich: Pythonista (iOS) oder eine Umgebung, die das ui-Modul von Pythonista bereitstellt.
Vorgehen:
Pythonista öffnen.
Datei Schuldenrechner.py in Pythonista importieren oder neu anlegen.
Skript ausführen.
Benutzung (Kurz)

Namen eingeben (z. B. Person1, Person2, Person3) und auf „Personen bestätigen“ klicken.
„Zahler wählen“ -> gewünschte Zahler auswählen -> „Beträge eingeben“ -> Beträge für jeden Zahler eintragen -> OK.
„Aufteilung wählen“ -> „Auf alle“ oder bestimmte Personen auswählen -> OK.
„Zahlung hinzufügen“.
Nach Erfassung aller Zahlungen: „Berechnen“ klicken, um Übersicht zu sehen.
Beispiel

Personen: Person1, Person2, Person3
Zahlung 1: Person1 zahlt 30€; Aufteilung: Auf alle
Ergebnis: Person2 und Person3 schuldenPerson1 je 10€, Person1 Netto +20€
Zahlung 2: Person2 und Person3 zahlen jeweils 15€; Aufteilung: Person1, Person2, Person3
Hinweis: siehe bekannte Einschränkungen zur Behandlung mehrerer Zahler.
GUI-Elemente (kurz)

Textfeld für Namen
Buttons: Personen bestätigen, Zahler wählen, Aufteilung wählen, Zahlung hinzufügen, Berechnen
Labels zeigen aktuell ausgewählte Zahler/Aufteilung
Ergebnis-TextView zeigt detaillierte Auflistung und Zahlungsverlauf
Bekannte Einschränkungen & Hinweise

Mehrere Zahler pro Zahlung: die Berechnung teilt den Gesamtbetrag durch die Anzahl der Empfänger und weist für jeden Zahler denselben Rückzahlbetrag pro Empfänger zu. Die individuellen Beträge der Zahler werden nicht proportional berücksichtigt — das kann zu falschen Salden führen, wenn Zahler unterschiedliche Beträge beigetragen haben. (Bug / Verbesserungspunkt.)
Platzhalter für zusätzliche manuelle Rückzahlungen (additional_receives) ist implementiert, aber standardmäßig leer.
Keine dauerhafte Speicherung: Zahlungen/Personen werden nicht in einer Datei gespeichert.
Locale / Währungsformat: einfache €-Formatierung, keine Lokalisierung.
Limit: maximal 20 Personen (eingebaut).
Die App läuft nur in Umgebungen mit dem Pythonista ui-Modul. Auf Desktop-Python (ohne ui) nicht lauffähig ohne Anpassung.
Validierungen: negative oder nicht-numerische Beträge werden abgefangen und melden Fehler.

ENGLISH

Short description

A simple debt calculator with a graphical interface (built for Pythonista's ui module on iOS). It lets you add multiple people, record payments with one or multiple payers, select how payments are split, and compute resulting debts / credits.
Features

Enter a list of people (up to 20).
Multiple payers per payment (enter amount per payer).
Choose split: "Everyone" or select specific people.
Add payments and keep a payments list.
Per-person results:
Who they owe money to.
Who owes them money.
Total owed, total received and net balance.
Input validation: at least one name, positive numeric amounts, at least one payment before calculation.
Simple, user-friendly GUI (buttons, labels, result text view).
Installation

Requirements: Pythonista (iOS) or an environment providing Pythonista's ui module.
Steps:
Open Pythonista.
Import or create Schuldenrechner.py.
Run the script.
Usage (brief)

Enter names (e.g. Person1, Person2, Person3) and click "Personen bestätigen" (Confirm people).
Click "Zahler wählen" (Choose payer) -> select payer(s) -> click "Beträge eingeben" (Enter amounts) -> input amounts -> OK.
Click "Aufteilung wählen" (Choose split) -> select "Auf alle" (Everyone) or particular people -> OK.
Click "Zahlung hinzufügen" (Add payment).
After all payments are entered click "Berechnen" (Calculate) to get the overview.
Example

People: Person1, Person2, Person3
Payment 1: Person1 pays €30, split among everyone
Result: Person2 and Person3 owe Luckas €10 each; Person1 net +€20
Payment 2: Person2 and Person3 each pay €15, split among Person1, Person2, Person3
Note: see known limitations about multi-payer handling.
GUI elements (brief)

Text field for names
Buttons: Confirm people, Choose payer, Choose split, Add payment, Calculate
Labels show selected payer/split
Result TextView lists detailed per-person debts and payment history
Known limitations & notes

Multiple payers per payment: the code divides the total amount by the number of recipients and assigns the same repayment per recipient for each payer. Individual payer amounts are not handled proportionally — this can produce incorrect totals when payers contributed different amounts. (Bug / improvement item.)
The additional_receives placeholder is present but empty by default.
No persistence: payments/people are not saved to disk.
Locale/currency formatting: simple € formatting without localization.
Limit: maximum 20 people.
Runs only in environments with the Pythonista ui module. Not runnable on standard desktop Python without changes.
Validation: negative or non-numeric amounts produce error messages.
