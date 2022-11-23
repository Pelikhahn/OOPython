#Die selbe BaseClass wie in classes.py zu finden ist
#Hier wurde sie nicht importiert, damit man bei Betrachten des Kurses nicht zwischen 2 Dateien springen muss um
#die BaseClass anschauen zu können

class BaseClass():
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def methode1(self):
        return self.a1

    def methode2(self, parameter):
        return f"Geil sogar dieses mal mit einem Parameter:{parameter}"

class KlasseMitVererbung(BaseClass):
    #hier ist der Konstruktor der KlasseMitVererbung welcher zu den Attributen a1, a2 und a3 das neue Attribut a4 bekommt
    #damit KlasseMitVererbung von BaseClass erben kann, muss KlasseMitVererbung die selben Attribute wie BaseClass haben
    def __init__(self, a1, a2, a3, a4):
        #Super spricht die hierarchisch drüber stehende Klasse an: BaseClass (Die Klasse die in den Klammern steht)
        #a1, a2 und a3 werden in dem Konstruktor von BaseClass zugewiesen
        super().__init__(a1, a2, a3)
        #sobald der super().__init__ call fertig ist, wird a4 zugewiesen
        self.a4 = a4
    #wir überschreiben "methode2" aus BaseClass um eine neue Funktionalität abzubilden, "methode1" wird aus BaseClass übernommen
    def methode2(self, parameter: float):
        ergebnis = parameter * parameter
        ergebnis = int(ergebnis)
        return f"{ergebnis}. methode2 in KlasseMitVererbung macht etwas anderes als methode2 bei BaseClass"


class ChildClass(KlasseMitVererbung):
    #ChildClass erbt von "KlasseMitVererbung", welche von "BaseClass" erbt. Hierarchisch gesehen also:
    #ChildClass <- KlasseMitVererbung <- BaseClass. BaseClass hat zu den Attributen a1, a2, a3 und a4 noch das neue
    #Attribut a5.
    def __init__(self, a1, a2, a3, a4, a5):
        #Super spricht hier KlasseMitVererbung an um a1-a4 zuzuweisen, KlasseMitVererbung weißt a1-a3 über den super-call
        #auf BaseClass zu und weißt dann a4 zu. Sobald a4 zugewiesen wurde, weisen wir im Konstruktor von ChildClass a5 zu.
        super().__init__(a1, a2, a3, a4)
        self.a5 = a5

    #ChildClass hat jetzt die überschriebene methode "methode2" von KlasseMitVererbung(NICHT VON BASE CLASS!)
    #und überschreibt die methode1, welche in BaseClass und KlasseMitVererbung identisch sind
    def methode1(self):
        return "Dieses mal überschreiben wir methode1 und nicht methode2"



beispiel = ChildClass(1, 2, 3, 4, 5)

#Hier einmal ein Beispiel um zu zeigen, dass ChildClass die überschrieben methode2 von KlasseMitVererbung hat und nicht
#die methode2 aus BaseClass.
print(beispiel.methode2(8.30662386292))

