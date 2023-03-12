class Zimmer :
    def __init__(self,Nummer,AnzahlGäste,Preis,Farbe,Meerblick):
        self.__nummer= Nummer
        self.__anzahlgaste = AnzahlGäste
        self.__preis= Preis
        self.__farbe= Farbe
        self.__meerblick= Meerblick

    @property
    def nummer(self):
        return self.__nummer
    @nummer.setter
    def nummer(self,value):
        self.__nummer=value

    @property
    def anzahlgaste(self):
        return self.__anzahlgaste

    @anzahlgaste.setter
    def anzahlgaste(self, value):
        self.__anzahlgaste = value

    @property
    def preis(self):
        return self.__preis

    @preis.setter
    def preis(self, value):
        self.__preis = value

    @property
    def farbe(self):
        return self.__farbe

    @farbe.setter
    def farbe(self, value):
        self.__farbe = value

    @property
    def meerblick(self):
        return self.__meerblick

    @meerblick.setter
    def meerblick(self, value):
        self.__meerblick = value


    def __str__(self):
        return (f'Zimmer({self.nummer}, {self.anzahlgaste}, {self.preis}, {self.farbe}, {self.meerblick})')

    def __eq__(self, other):
        if self.nummer== other.nummer and self.anzahlgaste== other.anzahlgaste and self.preis== other.preis and self.farbe==other.farbe and  self.meerblick==other.meerblick:
            return True
        else:
            return False
    def __repr__(self):
        return (f'Zimmer({self.nummer}, {self.anzahlgaste}, {self.preis}, {self.farbe}, {self.meerblick})')