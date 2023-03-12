from Domain.Gast import Gast

class functions:
    def __init__(self):
        self.gastliste = []
    def add_to_gastliste(self,gaste):
        """
        Fugt in gastliste alle gaste,und stellt sicher dass sich die gaste nicht verdoppeln
        :param gaste:
        :return:
        """
        for gast in self.gastliste:
            self.gastliste.remove(gast)
        for gast in gaste:
           self.gastliste.append(gast)
    def test_append(self,vorname,nachname):
        """
        Pruft ob ein Gast schon in der gastliste ist(er soll nicht noch einmal hinzugefugt sein)
        :param vorname:
        :param nachname:
        :return:
        """

        for gast in self.gastliste:
            if gast.vorname== vorname and gast.nachname== nachname:
                return 0
        return 1

    def get_gaste(self):
        """
        gibt die gastliste zuruck
        :return:
        """
        return self.gastliste
    def add_gast(self, gast):
        """
        fugt einen gast zur gastliste
        :param gast: der Form Gast()
        :return:
        """
        self.gastliste.append(gast)
    def print_gaste(self):
       """
       schreibt alle gaste
       :return:
       """
       for gast in self.gastliste:
            print (gast)
    def update_gast(self, vorname, nachname,newnachname):
        """
        Endert den nachname eines Gastes
        :param vorname:
        :param nachname:
        :param newnachname:
        :return:
        """
        for gast in self.gastliste:
            if gast.vorname== vorname and gast.nachname== nachname:
                self.gastliste.remove(gast)
                self.gastliste.append(Gast(vorname,newnachname))
        return self.gastliste
    def delete_gast(self,vorname,nachname):
        """
        Loscht einen Gast
        :param vorname:
        :param nachname:
        :return:
        """
        to_delete = list(filter(lambda gast: gast.vorname== vorname and gast.nachname== nachname, self.gastliste))
        for gast in to_delete:
            self.gastliste.remove(gast)
        return self.gastliste


