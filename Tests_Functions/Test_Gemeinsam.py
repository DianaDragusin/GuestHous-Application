from Domain.Reservierungen import Reservierungen
from Domain.Gast import Gast
from Domain.Zimmer import Zimmer
from datetime import date
from Functions.Functions_Gemeinsam import functions_gemeinsam

class test_Gemeinsam:
    def __init__(self, functions_gemeinsam):
        self.functions_gemeinsam = functions_gemeinsam
    def test_add_to_reservierungsliste(self):
        reservierungen= []
        Reservierung1= Reservierungen(Gast("ana","maria"),1,date(2021,11,1),date(2021,11,5))
        Reservierung2 = Reservierungen(Gast("ana", "maria"), 1, date(2021, 11, 6), date(2021, 11, 8))
        reservierungen.append(Reservierung1)
        reservierungen.append(Reservierung2)
        self.functions_gemeinsam.add_to_reservierungenliste(reservierungen)
        assert reservierungen[0] == self.functions_gemeinsam.reservierungenliste[0]
        assert reservierungen[1]== self.functions_gemeinsam.reservierungenliste[1]
        self.functions_gemeinsam.reservierungenliste= []
    def test_add_reservierung(self):
        Reservierung1 = Reservierungen(Gast("ana", "maria"), 1, date(2021, 11, 1), date(2021, 11, 5))
        self.functions_gemeinsam.add_reservierung(Reservierung1)
        assert Reservierung1 == self.functions_gemeinsam.reservierungenliste[0]
        self.functions_gemeinsam.reservierungenliste = []
    def test_get_rooms(self):
        room1= Zimmer(1,5,22,"blau",1)
        room2 = Zimmer(2, 2, 22, "grun", 1)
        self.functions_gemeinsam.zimmerliste.append(room1)
        self.functions_gemeinsam.zimmerliste.append(room2)
        assert room1== self.functions_gemeinsam.get_rooms(3)[0]
        self.functions_gemeinsam.zimmerliste= []
    def test_get_freind(self):
        gas1= Gast("ana", "mariuca")
        self.functions_gemeinsam.gasteliste.append(gas1)
        assert self.functions_gemeinsam.get_friend(gas1)
        self.functions_gemeinsam.gasteliste= []
    def test_add_to_zimmerliste(self):
        room1 = Zimmer(1, 5, 22, "blau", 1)
        room2 = Zimmer(1, 2, 22, "grun", 1)
        rooms= []
        rooms.append(room1)
        rooms.append(room2)
        self.functions_gemeinsam.add_to_zimmerliste(rooms)
        assert room1== self.functions_gemeinsam.zimmerliste[0]
        assert room2 == self.functions_gemeinsam.zimmerliste[1]
        self.functions_gemeinsam.zimmerliste= []
    def test_is_room_ok(self):
        reservierungen = []
        room1 = Zimmer(1, 5, 22, "blau", 1)
        self.functions_gemeinsam.zimmerliste.append(room1)
        room2 = Zimmer(2, 2, 22, "grun", 1)
        Reservierung1 = Reservierungen(Gast("ana", "maria"), room1, date(2021, 11, 1), date(2021, 11, 5))
        Reservierung2 = Reservierungen(Gast("ana", "maria"), room1, date(2021, 11, 6), date(2021, 11, 8))
        reservierungen.append(Reservierung1)
        reservierungen.append(Reservierung2)
        self.functions_gemeinsam.add_to_reservierungenliste(reservierungen)
        assert self.functions_gemeinsam.is_room_ok(room2)
        self.functions_gemeinsam.zimmerliste=[]
        self.functions_gemeinsam.reservierungenliste=[]
    def test_compare_two_dates(self):
        datato1= date(2021, 11,3)
        datato2= date(2021, 11, 5)
        data1= date(2021, 11, 6)
        data2= date(2021, 11, 8)
        assert self.functions_gemeinsam.compare_two_dates(datato1,datato2,data1,data2)
    def test_compare_all_dates(self):
        datato1 = date(2021, 11, 3)
        datato2 = date(2021, 11, 5)
        data1 = date(2021, 11, 6)
        data2 = date(2021, 11, 8)
        anfang=[]
        ende=[]
        anfang.append(datato1)
        ende.append(datato2)
        assert self.functions_gemeinsam.compare_all_dates(anfang,ende,data1,data2)
    def test_is_it_available(self):
        reservierungen = []
        room1 = Zimmer(1, 5, 22, "blau", 1)
        room2 = Zimmer(2, 5, 22, "blau", 1)
        rooms=[]
        rooms.append(room1)
        self.functions_gemeinsam.zimmerliste.append(room1)
        Reservierung1 = Reservierungen(Gast("ana", "maria"), room1, date(2021, 11, 1), date(2021, 11, 5))
        Reservierung2 = Reservierungen(Gast("ana", "maria"), room1, date(2021, 11, 6), date(2021, 11, 8))
        datato1 = date(2021, 11, 9)
        datato2 = date(2021, 11, 10)
        reservierungen.append(Reservierung1)
        reservierungen.append(Reservierung2)
        self.functions_gemeinsam.add_to_reservierungenliste(reservierungen)
        assert self.functions_gemeinsam.is_it_available(rooms,datato1,datato2)[0] == room1

    def main (self,test_gemeinsam):
        test_gemeinsam.test_add_to_reservierungsliste()
        test_gemeinsam.test_get_rooms()
        test_gemeinsam.test_add_reservierung()
        test_gemeinsam.test_get_freind()
        test_gemeinsam.test_is_room_ok()
        test_gemeinsam.test_compare_two_dates()
        test_gemeinsam.test_compare_two_dates()
        test_gemeinsam.test_is_it_available()
        test_gemeinsam.test_add_to_zimmerliste()