from Domain.Zimmer import Zimmer
from Domain.Gast import Gast
from Domain.Reservierungen import Reservierungen
from Functions.Functions_Zimmer import functions_zimmer
from Functions.Functions_Gast import functions
from datetime import date

class functions_gemeinsam:
    def __init__(self):
        self.reservierungenliste = []
        self.gasteliste=[]
        self.zimmerliste=[]



    def add_to_reservierungenliste(self, reservierungen):
        """
        Fugt die gelesene reservierungen in den reservierungsliste
        :param reservierungen:
        :return:
        """
        for reservierung in self.reservierungenliste:
            self.reservierungenliste.remove(reservierung)

        for reservierung in reservierungen:
           self.reservierungenliste.append(reservierung)
    def add_to_gasteliste(self, gaste):
        """
        Fugt die gelesene Gaste in der gasteliste
        :param gaste:
        :return:
        """
        for gast in self.gasteliste:
            self.gasteliste.remove(gast)
        for gast in gaste:
           self.gasteliste.append(gast)
    def add_gast_to_gastliste(self,gast):
        """
        Fugt einen Gast in der gasteliste
        :param gast:
        :return:
        """
        self.gasteliste.append(gast)
    def add_to_zimmerliste(self, rooms):
        """
        Fugt die gelesene zimmer aus der Datei in der zimmerliste
        :param rooms:
        :return:
        """
        for zimmer in self.zimmerliste:
            self.zimmerliste.remove(zimmer)
        for room in rooms:
           self.zimmerliste.append(room)
    def get_rooms(self,nr_people):
        """
        Bringt alle Zimmer die die gleiche Anzahl von Platze wie nr_people haben zuruck
        :param nr_people:
        :return:
        """
        zimmer_for_client= list(filter(lambda zimmer: zimmer.anzahlgaste>=nr_people,self.zimmerliste))
        return zimmer_for_client
    def dates(self,an1,luna1,zi1,an2,luna2,zi2):
        """
        Diese Funktion bestimmt ob der Zeitraum valid fur die Reservierung ist
        :param an1:
        :param luna1:
        :param zi1:
        :param an2:
        :param luna2:
        :param zi2:
        :return:
        """
        if an1-an2 >0 :
            raise ValueError("You can't time travel")
        else:
            if luna1-luna2 >0 :
                raise ValueError("You can't time travel")
            else:
                if zi1-zi2 >0:
                    raise ValueError("You can't time travel")



    def value_error_or_type_error(self,value):
        """
        Checkt ob den Wert ein Int und ob es grosser als Null ist
        :param value:
        :return:
        """
        if isinstance(int(value),int)== False:
            raise TypeError("You must enter an int value")
        if int(value)<= 0:
            raise ValueError("The value must be bigger than 0")
    def get_friend(self,friend):
        """
        Checkt ob der Freund von dem client in der gasteliste schon ist
        :param friend:
        :return:
        """
        for gast in self.gasteliste:
            if gast.vorname== friend.vorname and gast.nachname== friend.nachname:
                return 1
        return 0

    def is_room_ok(self,room):
        """
        checkt ob room noch keine Reservierungen hat
        :param room:
        :return:
        """
        ok=0

        for reservierung in self.reservierungenliste:
            if reservierung.zimmer == room :
                ok = ok+1
        if ok==0 :
            return 1
        else:
            return 0
    def compare_all_dates(self,anfang,ende,anfang_zeitraum,ende_zeitraum):
        """
        Checkt alle reservierungen von einem zimmer und sucht ob es einen zimmer gibt fur die, die zeitraume nicht uberschneiden
        :param anfang:
        :param ende:
        :param anfang_zeitraum:
        :param ende_zeitraum:
        :return:
        """
        notok=0
        for i in range (len(anfang) ):
            if self.compare_two_dates(anfang_zeitraum,ende_zeitraum,anfang[i],ende[i])==0:
                notok= notok+1
        if notok == 0 :
            return 1
        else:
            return 0
    def is_it_available(self,rooms,anfang_zeitraum,ende_zeitraum):
        """
        bringt die zimmern zuruck die frei fur die gewehlte Periode sind
        :param rooms:
        :param anfang_zeitraum:
        :param ende_zeitraum:
        :return:
        """
        available_rooms= []
        for room in rooms:
            if self.is_room_ok(room)==1:
                available_rooms.append(room)

        if len(available_rooms)!=0 :
            return available_rooms
        if len(available_rooms)==0:
            for room in rooms:
                anfang = []
                ende = []
                for reservierung in self.reservierungenliste:
                    if reservierung.zimmer == room:
                        anfang.append(reservierung.anfang_zeitraum)
                        ende.append(reservierung.ende_zeitraum)
                if self.compare_all_dates(anfang, ende, anfang_zeitraum, ende_zeitraum) == 1:
                    available_rooms.append(room)

        if len(available_rooms) == 0:
            return 0
        else :
            return available_rooms

    def compare_two_dates(self, anfang_zeitraum, ende_zeitraum,anfang_zeitraum_res,ende_zeitraum_res):
        """
        Untersucht ob sich 2 Perioden uberschneiden
        :param anfang_zeitraum:
        :param ende_zeitraum:
        :param anfang_zeitraum_res:
        :param ende_zeitraum_res:
        :return:
        """
        if anfang_zeitraum>= ende_zeitraum_res:
            return 1
        if anfang_zeitraum< anfang_zeitraum_res and ende_zeitraum<= anfang_zeitraum_res:
            return 1
        return 0





    def add_reservierung(self, reservierung):
        """
        Fugt eine Reservierung in der Reservierungsliste
        :param reservierung:
        :return:
        """
        self.reservierungenliste.append(reservierung)




    def aktuelle_reservierungen(self):
        """
        Gibt die Reservierungen die aktuell sind
        :return:
        """
        gasten=[]
        for reservierung in self.reservierungenliste:
            if reservierung.ende_zeitraum >= date.today() :
                for gast in reservierung.gaste:
                    gasten.append(gast)
        return gasten
    def filter_preis_meerblick(self,preis,meerblick):
        """
        Filtert die Zimmern die preise unter einem bestimmten preis haben und die meerblick haben konnen oder nicht
        :param preis:
        :param meerblick:
        :return:
        """
       
        rooms= list(filter(lambda room: room.preis <= preis and room.meerblick== meerblick,self.zimmerliste))
        """for reservierung in self.reservierungenliste:
            if reservierung.zimmer.preis <= preis and reservierung.zimmer.meerblick== meerblick:
                rooms.append(reservierung.zimmer)"""
        return rooms
    def today_free(self):
        """
        Gibt die Zimmer die heute frei sind zuruck
        :return:
        """
        notrooms=[]
        rooms=[]
        all_rooms=[]
        for room in self.zimmerliste:
            for reservierung in self.reservierungenliste:
                if reservierung.zimmer== room:
                    if reservierung.anfang_zeitraum <= date.today() and reservierung.ende_zeitraum >date.today():
                        notrooms.append(room)
        for room in self.zimmerliste:
            if room not in notrooms:
                rooms.append(room)

        return rooms




