class Gast:

    def __init__(self,  Vorname, Nachname):

        self.__vorname = Vorname
        self.__nachname = Nachname


    @property
    def nachname (self):
        return self.__nachname
    @nachname.setter
    def nachname (self,value):
        self.__nachname= value

    @property
    def vorname(self):
        return self.__vorname

    @vorname.setter
    def vorname(self, value):
        self.__vorname = value
    def __str__(self):
        return (f'Gast({self.vorname},{self.nachname})')
    def __repr__(self):
        return (f'Gast({self.vorname},{self.nachname})')
    def __eq__(self, other):
        if self.__vorname == other.__vorname and self.__nachname== other.__nachname:
            return 1
        else:
            return 0

"""@property
    def reservierungen(self):
        return self.__reservierungen

    @reservierungen.setter
    def reservierungen(self, values):
        l= len(values)
        for i in range (l):
            self.__reservierungen[i]= values[i]"""
