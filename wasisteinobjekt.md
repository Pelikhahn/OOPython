#Was ist ein Objekt
Ein Objekt ist die Instanz einer Klasse.<br>
````python
class Beispiel():
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

objekt = Beispiel(1, 2)
````

Die Variable objekt repräsentiert hier ein objekt, Objekte haben immer eine objekt-referenz

````python
print(objekt)
print(objekt.a2)
````

Der call print(objekt) gibt nur die Speicheradresse, also die Objekt-Referenz, des Objekts an.
Der call darunter gibt das Attribut "a2" des Objektes aus.