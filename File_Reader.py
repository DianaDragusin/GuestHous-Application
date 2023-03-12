from Domain.Zimmer  import Zimmer
from Domain.Gast import Gast
from Domain.Reservierungen import Reservierungen
from datetime import date
class Reader:
    def Gast(self):
        """
        Liest alle Gaste von der Datei und fugt sie in einer liste von Gaste
        :return:
        """
        f=open ("Gast_File", "r")
        name = f.readline()
        list_gast= []
        while name:
            ready_name= name.split(" ")
            vorname = ready_name[0]
            nachname= ready_name[1].strip()
            list_gast.append(Gast(vorname,nachname))
            name = f.readline()
        f.close()
        return list_gast
    def Zimmer (self):
        """
        Liest alle Zimmer von der Datei und fugt sie in einer Liste
        :return:
        """
        f = open("Zimmer_File", "r")
        zimmer = f.readline()
        list_zimmer = []
        while zimmer:
            zimmer_attribute = zimmer.split(" ")
            nummer = int(zimmer_attribute[0])
            anzahlgaste= int(zimmer_attribute[1])
            preis = int(zimmer_attribute[2])
            farbe = zimmer_attribute[3]
            meerblick= int(zimmer_attribute[4])


            list_zimmer.append(Zimmer(nummer, anzahlgaste,preis, farbe, meerblick))
            zimmer = f.readline()
        f.close()
        return list_zimmer
    def Reservierungen(self):
        """
        Liest alle Reservierungen von einer Datei und fugt sie in einer Liste
        :return:
        """
        f = open("Reservierungen_File", "r")
        reservierung = f.readline()
        list_reservierungen = []
        while reservierung:
            reservierung_teile = reservierung.split(";")
            reservierung_gaste= reservierung_teile[0].split()
            reservierung_zimmer= reservierung_teile[1].split()
            nummer = int(reservierung_zimmer[0])
            anzahlgaste = int(reservierung_zimmer[1])
            preis = int(reservierung_zimmer[2])
            farbe = reservierung_zimmer[3]
            meerblick =int(reservierung_zimmer[4])
            room= Zimmer(nummer,anzahlgaste,preis,farbe,meerblick)
            reservierung_date= reservierung_teile[2].split()
            anfang= date(int(reservierung_date[0]),int(reservierung_date[1] ),int(reservierung_date[2]))
            ende= date(int(reservierung_date[3]),int(reservierung_date[4]),int(reservierung_date[5]))
            gaste_liste=[]
            j=0
            while j<= len(reservierung_gaste)-1:

                vorname = reservierung_gaste[j]
                nachname = reservierung_gaste[j + 1]
                gast = Gast(vorname, nachname)
                gaste_liste.append(gast)
                j = j + 2

            list_reservierungen.append(Reservierungen(gaste_liste,room,anfang,ende))
            reservierung = f.readline()
        f.close()
        return list_reservierungen

