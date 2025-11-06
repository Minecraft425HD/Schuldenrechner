import ui
import re

class SchuldenrechnerUI(ui.View):
    def __init__(self):
        self.personen = []  # Liste der Personen
        self.zahlungen = []  # Liste der Zahlungen: [(Zahler: {Person: Betrag}, Aufteilung_Personen)]
        self.zahler_auswahl = []  # Temporäre Liste für ausgewählte Zahler
        self.aufteilung_auswahl = []  # Temporäre Liste für ausgewählte Aufteilung
        self.zahler_nav_view = None  # Referenz auf NavigationView für Zahler
        self.aufteilung_nav_view = None  # Referenz auf NavigationView für Aufteilung
        self.zahler_table_view = None  # Referenz auf TableView für Zahler
        self.aufteilung_table_view = None  # Referenz auf TableView für Aufteilung
        self.betrag_nav_view = None  # Referenz auf NavigationView für Betragseingabe
        self.setup_ui()
   
    def setup_ui(self):
        self.name = 'Schuldenrechner'
        self.background_color = '#f0f0f0'  # Helles Grau für modernen Look
       
        # Eingabefeld für Personenliste
        self.personen_field = ui.TextView(frame=(20, 20, 340, 60))
        self.personen_field.font = ('Helvetica', 16)
        self.personen_field.placeholder = 'Namen (z.B. Luckas, Lisa, Ronja)'
        self.personen_field.background_color = 'white'
        self.personen_field.border_width = 1
        self.personen_field.border_color = '#cccccc'
        self.add_subview(self.personen_field)
       
        # Button zum Bestätigen der Personen
        self.personen_button = ui.Button(title='Personen bestätigen', frame=(20, 90, 340, 40))
        self.personen_button.background_color = '#007aff'
        self.personen_button.tint_color = 'white'
        self.personen_button.font = ('Helvetica-Bold', 16)
        self.personen_button.corner_radius = 8
        self.personen_button.action = self.personen_bestaetigen
        self.add_subview(self.personen_button)
       
        # Button für Zahlerauswahl
        self.zahler_button = ui.Button(title='Zahler wählen', frame=(20, 150, 165, 40))
        self.zahler_button.background_color = '#007aff'
        self.zahler_button.tint_color = 'white'
        self.zahler_button.font = ('Helvetica', 14)
        self.zahler_button.corner_radius = 8
        self.zahler_button.action = self.zahler_oeffnen
        self.zahler_button.enabled = False
        self.add_subview(self.zahler_button)
       
        # Label für ausgewählte Zahler
        self.zahler_label = ui.Label(frame=(195, 150, 165, 40))
        self.zahler_label.text = 'Keine ausgewählt'
        self.zahler_label.font = ('Helvetica', 12)
        self.zahler_label.text_color = '#333333'
        self.add_subview(self.zahler_label)
       
        # Button für Aufteilungsauswahl
        self.aufteilung_button = ui.Button(title='Aufteilung wählen', frame=(20, 200, 165, 40))
        self.aufteilung_button.background_color = '#007aff'
        self.aufteilung_button.tint_color = 'white'
        self.aufteilung_button.font = ('Helvetica', 14)
        self.aufteilung_button.corner_radius = 8
        self.aufteilung_button.action = self.aufteilung_oeffnen
        self.aufteilung_button.enabled = False
        self.add_subview(self.aufteilung_button)
       
        # Label für ausgewählte Aufteilung
        self.aufteilung_label = ui.Label(frame=(195, 200, 165, 40))
        self.aufteilung_label.text = 'Keine ausgewählt'
        self.aufteilung_label.font = ('Helvetica', 12)
        self.aufteilung_label.text_color = '#333333'
        self.add_subview(self.aufteilung_label)
       
        # Button zum Hinzufügen der Zahlung
        self.add_button = ui.Button(title='Zahlung hinzufügen', frame=(20, 250, 340, 40))
        self.add_button.background_color = '#007aff'
        self.add_button.tint_color = 'white'
        self.add_button.font = ('Helvetica-Bold', 16)
        self.add_button.corner_radius = 8
        self.add_button.action = self.add_zahlung
        self.add_button.enabled = False
        self.add_subview(self.add_button)
       
        # Button zum Berechnen
        self.calc_button = ui.Button(title='Berechnen', frame=(20, 300, 340, 40))
        self.calc_button.background_color = '#34c759'
        self.calc_button.tint_color = 'white'
        self.calc_button.font = ('Helvetica-Bold', 16)
        self.calc_button.corner_radius = 8
        self.calc_button.action = self.berechnen
        self.calc_button.enabled = False
        self.add_subview(self.calc_button)
       
        # TextView für Ergebnisse
        self.result_view = ui.TextView(frame=(20, 350, 340, 300))
        self.result_view.editable = False
        self.result_view.font = ('Helvetica', 14)
        self.result_view.background_color = 'white'
        self.result_view.border_width = 1
        self.result_view.border_color = '#cccccc'
        self.result_view.text = 'Geben Sie eine Liste von Namen ein (z.B. Luckas, Lisa, Ronja).'
        self.add_subview(self.result_view)
   
    def personen_bestaetigen(self, sender):
        text = self.personen_field.text.strip()
        if not text:
            self.result_view.text = "Fehler: Bitte geben Sie mindestens einen Namen ein!"
            return
        namen = [name.strip() for name in re.split(r',|\s+', text) if name.strip()]
        if not namen:
            self.result_view.text = "Fehler: Keine gültigen Namen eingegeben!"
            return
        if len(namen) > 20:
            self.result_view.text = "Fehler: Maximal 20 Personen erlaubt!"
            return
       
        self.personen = namen
        self.zahler_button.enabled = True
        self.aufteilung_button.enabled = True
        self.add_button.enabled = True
        self.calc_button.enabled = True
        self.result_view.text = f"{len(namen)} Personen hinzugefügt: {', '.join(namen)}"
   
    def zahler_oeffnen(self, sender):
        self.zahler_table_view = ui.TableView(frame=(0, 0, 300, 400))
        self.zahler_table_view.name = 'Zahler wählen'
        self.zahler_table_view.allows_multiple_selection = True
        self.zahler_table_view.data_source = ui.ListDataSource(self.personen)
        self.zahler_table_view.data_source.delete_enabled = False
       
        selected = [self.personen.index(p) for p in self.zahler_auswahl if p in self.personen]
        self.zahler_table_view.selected_rows = [(0, i) for i in selected]
       
        self.zahler_nav_view = ui.NavigationView(self.zahler_table_view)
        self.zahler_nav_view.right_button_items = [ui.ButtonItem(title='Beträge eingeben', action=self.zahler_betrag_eingeben)]
        self.zahler_nav_view.present('sheet', hide_title_bar=False)
   
    def zahler_betrag_eingeben(self, sender):
        if not self.zahler_table_view:
            return
        selected_indices = [i for s, i in self.zahler_table_view.selected_rows]
        if not selected_indices:
            self.result_view.text = "Fehler: Bitte wählen Sie mindestens einen Zahler aus!"
            self.zahler_nav_view.close()
            return
        self.zahler_auswahl = [self.personen[i] for i in selected_indices]
        self.zahler_label.text = ', '.join(self.zahler_auswahl) if self.zahler_auswahl else 'Keine ausgewählt'
       
        betrag_table = ui.TableView(frame=(0, 0, 300, 400))
        betrag_table.name = 'Beträge eingeben'
        betrag_table.data_source = ui.ListDataSource(self.zahler_auswahl)
        betrag_table.data_source.delete_enabled = False
       
        betrag_fields = {}
        for i, person in enumerate(self.zahler_auswahl):
            field = ui.TextField(frame=(150, i * 44, 100, 32))
            field.placeholder = f'Betrag {person}'
            field.keyboard_type = ui.KEYBOARD_DECIMAL_PAD
            betrag_table.add_subview(field)
            betrag_fields[person] = field
       
        self.betrag_nav_view = ui.NavigationView(betrag_table)
        self.betrag_nav_view.right_button_items = [ui.ButtonItem(title='OK', action=lambda s: self.zahler_betrag_bestaetigen(s, betrag_fields))]
        self.betrag_nav_view.present('sheet', hide_title_bar=False)
        self.zahler_nav_view.close()
        self.zahler_table_view = None
        self.zahler_nav_view = None
   
    def zahler_betrag_bestaetigen(self, sender, betrag_fields):
        if not self.betrag_nav_view:
            return
        zahler_betraege = {}
        for person, field in betrag_fields.items():
            try:
                betrag = float(field.text.strip())
                if betrag <= 0:
                    self.result_view.text = f"Fehler: Betrag für {person} muss positiv sein!"
                    self.betrag_nav_view.close()
                    return
                zahler_betraege[person] = betrag
            except ValueError:
                self.result_view.text = f"Fehler: Ungültiger Betrag für {person}!"
                self.betrag_nav_view.close()
                return
        self.zahler_auswahl = zahler_betraege
        self.betrag_nav_view.close()
        self.betrag_nav_view = None
   
    def aufteilung_oeffnen(self, sender):
        self.aufteilung_table_view = ui.TableView(frame=(0, 0, 300, 400))
        self.aufteilung_table_view.name = 'Aufteilung wählen'
        self.aufteilung_table_view.allows_multiple_selection = True
        items = ['Auf alle'] + self.personen
        self.aufteilung_table_view.data_source = ui.ListDataSource(items)
        self.aufteilung_table_view.data_source.delete_enabled = False
       
        selected = [items.index(p) for p in self.aufteilung_auswahl if p in items]
        self.aufteilung_table_view.selected_rows = [(0, i) for i in selected]
       
        self.aufteilung_nav_view = ui.NavigationView(self.aufteilung_table_view)
        self.aufteilung_nav_view.right_button_items = [ui.ButtonItem(title='OK', action=self.aufteilung_bestaetigen)]
        self.aufteilung_nav_view.present('sheet', hide_title_bar=False)
   
    def aufteilung_bestaetigen(self, sender):
        if not self.aufteilung_table_view or not self.aufteilung_nav_view:
            return
        selected_indices = [i for s, i in self.aufteilung_table_view.selected_rows]
        items = ['Auf alle'] + self.personen
        selected_items = [items[i] for i in selected_indices]
       
        if 'Auf alle' in selected_items:
            self.aufteilung_auswahl = self.personen[:]
        else:
            self.aufteilung_auswahl = [item for item in selected_items if item in self.personen]
       
        self.aufteilung_label.text = ', '.join(self.aufteilung_auswahl) if self.aufteilung_auswahl else 'Keine ausgewählt'
        self.aufteilung_nav_view.close()
        self.aufteilung_table_view = None
        self.aufteilung_nav_view = None
   
    def add_zahlung(self, sender):
        if not self.personen:
            self.result_view.text = "Fehler: Bitte erst Personen bestätigen!"
            return
        if not isinstance(self.zahler_auswahl, dict) or not self.zahler_auswahl:
            self.result_view.text = "Fehler: Bitte wählen Sie mindestens einen Zahler mit Betrag aus!"
            return
        if not self.aufteilung_auswahl:
            self.result_view.text = "Fehler: Bitte wählen Sie mindestens eine Person für die Aufteilung!"
            return
       
        self.zahlungen.append((self.zahler_auswahl, self.aufteilung_auswahl[:]))
        self.result_view.text = f"Zahlung hinzugefügt: {', '.join(f'{p}: {b:.2f} €' for p, b in self.zahler_auswahl.items())} (auf {', '.join(self.aufteilung_auswahl)}).\n{len(self.zahlungen)} Zahlungen erfasst."
        self.zahler_auswahl = []
        self.aufteilung_auswahl = []
        self.zahler_label.text = 'Keine ausgewählt'
        self.aufteilung_label.text = 'Keine ausgewählt'
   
    def berechnen(self, sender):
        if not self.zahlungen:
            self.result_view.text = "Fehler: Mindestens eine Zahlung erforderlich!"
            return
       
        # Initialisiere Schulden- und Erhalt-Listen
        owes = {person: {} for person in self.personen}  # Wer schuldet wem
        receives = {person: {} for person in self.personen}  # Von wem erhält wer
       
        # Spezifische zusätzliche Rückzahlungen aus deinem Beispiel (manuell hinzufügen)
        additional_receives = {}
       
       
        # Standard-Rückzahlungen basierend auf Zahlungen
        for zahler_betraege, aufteilung in self.zahlungen:
            gesamt_betrag = sum(zahler_betraege.values())
            if aufteilung:
                anteil_pro_person = gesamt_betrag / len(aufteilung)
                for zahler, betrag in zahler_betraege.items():
                    zahlende_personen = [p for p in aufteilung if p != zahler]
                    if zahlende_personen:
                        ruckzahlung_pro_person = anteil_pro_person
                        for person in zahlende_personen:
                            owes[person][zahler] = owes[person].get(zahler, 0) + ruckzahlung_pro_person
                            receives[zahler][person] = receives[zahler].get(person, 0) + ruckzahlung_pro_person
       
        # Füge zusätzliche Rückzahlungen hinzu
        for receiver, payments in additional_receives.items():
            for payer, amount in payments.items():
                receives[receiver][payer] = receives[receiver].get(payer, 0) + amount
                owes[payer][receiver] = owes[payer].get(receiver, 0) + amount
       
        # Ergebnistext generieren
        result_text = ""
        for person in self.personen:
            owes_total = sum(owes[person].values())
            receives_total = sum(receives[person].values())
            net_balance = receives_total - owes_total
           
            result_text += f"{person}\n"
            result_text += "•  Schuldet:\n"
            for owed_to, amount in owes[person].items():
                result_text += f"    •  {owed_to}: €{amount:.2f}\n"
            result_text += f"    •  Gesamtschuld: €{owes_total:.2f}\n"
            result_text += "•  Erhält:\n"
            for received_from, amount in receives[person].items():
                result_text += f"    •  Von {received_from}: €{amount:.2f}\n"
            result_text += f"    •  Gesamterhalt: €{receives_total:.2f}\n"
            result_text += f"•  Netto-Saldo: €{receives_total:.2f} - €{owes_total:.2f} = €{net_balance:.2f} "
            result_text += f"({person} {'wird geschuldet' if net_balance >= 0 else 'schuldet'} €{abs(net_balance):.2f})\n\n"
       
        # Auflistung der vorgenommenen Zahlungen
        result_text += "Vorgenommene Zahlungen:\n"
        for i, (zahler_betraege, aufteilung) in enumerate(self.zahlungen, 1):
            zahler_details = ', '.join(f"{p}: €{b:.2f}" for p, b in zahler_betraege.items())
            result_text += f"•  Zahlung {i}: {zahler_details} (Aufteilung an {', '.join(aufteilung)})\n"
       
        self.result_view.text = result_text.strip()

# UI starten
view = SchuldenrechnerUI()
view.present('sheet')
