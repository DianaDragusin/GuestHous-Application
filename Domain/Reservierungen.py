from datetime import date
"""
class Zeitraum:
    def __init__(self,Jahr,Monat,Tag):
        self.jahr= Jahr
        self.monat = Monat
        self.tag = Tag"""

class Reservierungen :
    def __init__(self,Gaste,Zimmer, Anfang_Zeitraum, Ende_Zeitraum):
        self.__gaste = Gaste
        self.__zimmer = Zimmer
        self.__anfang_zeitraum = Anfang_Zeitraum
        self.__ende_zeitraum= Ende_Zeitraum


    @property
    def gaste(self):
        return self.__gaste

    @gaste.setter
    def gaste(self, values):
        l = len(values)
        for i in range(l):
            self.__gaste[i] = values[i]

    @property
    def zimmer(self):
        return self.__zimmer

    @zimmer.setter
    def zimmer(self, value):
        self.__zimmer = value

    @property
    def anfang_zeitraum(self):
        return self.__anfang_zeitraum

    @anfang_zeitraum.setter
    def anfang_zeitraum(self, value):
        self.__anfang_zeitraum = value

    @property
    def ende_zeitraum(self):
        return self.__ende_zeitraum

    @ende_zeitraum.setter
    def ende_zeitraum(self, value):
        self.__ende_zeitraum = value

    def __str__(self):
        return f'Reservierung({ self.__gaste }, {self.__zimmer},{self.__anfang_zeitraum}, {self.__ende_zeitraum})'
    def __repr__(self):
        return f'Reservierung({ self.__gaste }, {self.__zimmer},{self.__anfang_zeitraum}, {self.__ende_zeitraum})'




