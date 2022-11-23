class BaseClass():
    #Die Attribute der Klasse sind im Aufruf des Konstruktors angegeben
    def __init__(self, attribut1, attribut2, attribut3):
        self.attribut1 = attribut1
        self.attribut2 = attribut2
        self.attribut3 = attribut3
    #Mithilfe von self sprechen wir die Instanz der Klasse die wir erstellen an

    #Die Methoden einer Klasse sind wie Funktionen zu definieren
    def methode1(self):
        return self.attribut1

    def methode2(self, parameter):
        return f"Geil sogar dieses mal mit einem Parameter:{parameter}"

#Ein Beispiel einer Instanz
#Beim Aufrufen des beispiels müssen wir die 3 Attribute in BaseClass(Attribut1, Attribut2, Attribut3) angeben
#der BaseClass Aufruf spricht die __init__ funktion der Klasse an

beispiel = BaseClass("Erstes Attribut", "Zweites Attribut", "Drittes Attribut")

#Hier printen wir einmal die Attribute
print(beispiel.attribut1, "\n",beispiel.attribut2, "\n",beispiel.attribut3)

#Hier führen wir die Methode 1 aus
print(beispiel.methode1())

#Hier führen wir die Methode 2 aus, welche einen parameter benötigt
print(beispiel.methode2("Krasser parameter yo"))

