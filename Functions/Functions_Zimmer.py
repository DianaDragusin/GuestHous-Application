from Domain.Zimmer import Zimmer

class functions_zimmer:
    def __init__(self):
        self.zimmerliste = []
    def add_to_zimmerliste(self, rooms):
        """
        Fugt die Zimmer in der zimmerliste und sichert sich dass die daten nicht zwei mal in der liste erscheinen

        :param rooms:
        :return:
        """
        for room in self.zimmerliste:
            self.zimmerliste.remove(room)
        for room in rooms:
           self.zimmerliste.append(room)
    def value_error_or_type_error(self,value):
        if isinstance(int(value),int)== False:
            raise TypeError("You must enter an int value")
        if int(value)<= 0:
            raise ValueError("The value must be bigger than 0")
    def get_zimmerliste(self):
        return self.zimmerliste
    def add_zimmer(self, zimmer):
        """
        Fugt ein Zimmer in der liste
        :param zimmer:
        :return:
        """
        self.zimmerliste.append(zimmer)
    def print_rooms(self):
        """
        Schreibt alle zimmer auf
        :return:
        """
        for room in self.zimmerliste:
            print (room)
    def update_zimmer(self,nummer,newpreis):
        """
        Andert der preis einer zimmer
        :param nummer:
        :param newpreis:
        :return:
        """
        for room in self.zimmerliste:
            if room.nummer== nummer :
                room.preis = newpreis

        return self.zimmerliste
    def delete_zimmer(self,nummer):
        """
        Loscht einen Zimmer
        :param nummer:
        :return:
        """
        to_delete = list(filter(lambda zimmer: zimmer.nummer== nummer, self.zimmerliste))
        for room in to_delete:
            self.zimmerliste.remove(room)
        return self.zimmerliste


