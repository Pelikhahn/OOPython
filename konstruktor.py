#DISCLAIMER! DIESE DATEI HAT BEABSICHTIGE SYNTAX FEHLER FÜR LERNEFFEKTE; SIE IST NICHT AUSFÜHRBAR!

#Konstruktoren haben gewissen Vorgaben die erfüllt sein müssen. Diese sind in classes.py zu ermitteln.
#Hier einmal ein paar Fehlerquellen die beim Schreiben von Konstruktoren entstehen können:

class A():
    #a2 hat den Standardwert 50, jedoch haben wir danach noch ein Attribut. Attribute mit DefaultWerten müssen die
    #letzten Parameter der __init__ Funktion sein(Generelle Python Regel zu Funktionen!)
    def __init__(self, a1, a2=50, a3):
        self.a1= a1
        self.a2= a2
        self.a3= a3

class B(A):
    #Die Klasse B, welche von A erbt hat weniger Attribute als A, daher kann Sie nicht instanziert werden
    def __init__(self, a1, a2):
        super().__init__(a1, a2)


