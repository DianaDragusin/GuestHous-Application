from Functions.Functions_Gast import functions
from Domain.Gast import Gast
from File_Reader import Reader
from File_Writer import Gast_writer
from Functions.Functions_Zimmer import functions_zimmer
from Domain.Zimmer import Zimmer


class ui_Zimmer:

    def __init__(self,functions_zimmer,rooms,rooms_app):
        self.functions_zimmer= functions_zimmer
        self.rooms=rooms
        self.rooms_app= rooms_app

    def menu (self):
      return"""0. Return
1. Füge ein Zimmer hin
2 Aktualisierung des Preises eines Zimmers
3 Löschung eines Zimmers
4 Anzeige die Liste von Zimmern
        """
    
    def main(self):
        self.functions_zimmer.add_to_zimmerliste(self.rooms)

        while True:
            print (self.menu())
            x=int(input(" Choose one option "))
            if x==0:
                return 0
            if x==1 :
                nummer = int(input("Room Number: "))
                self.functions_zimmer.value_error_or_type_error(nummer)
                anzahlgaste = input("Numer of customers :")
                self.functions_zimmer.value_error_or_type_error(anzahlgaste)
                preis = input ("Cost: ")
                self.functions_zimmer.value_error_or_type_error(preis)
                farbe = input ("Color:")
                meerblick= input("Does it have a seaside view? (1-yes, 0- no) ")
                self.rooms_app.append_zimmer(nummer,anzahlgaste, preis, farbe, meerblick)
                #self.gaste.append(Gast(vorname,nachname))
                # self.functions.add_gast(Gast(vorname,nachname))
            if x==2:
                nummer =int(input("Room Number: "))
                self.functions_zimmer.nummer_error(nummer)
                newpreis = int(input("New Cost: "))
                self.functions_zimmer.nummer_error(newpreis)
                rooms=self.functions_zimmer.update_zimmer(nummer,newpreis)

                self.rooms_app.update_zimmer(rooms)
              #  self.gaste_app.update_guest

            if x==3:
                nummer = int(input("Room Number: "))
                self.functions_zimmer.nummer_error(nummer)
                rooms=self.functions_zimmer.delete_zimmer(nummer)
                self.rooms_app.delete_zimmer(rooms)
            if x== 4:

                #self.functions.add_to_gastliste(self.gaste)
                self.functions_zimmer.print_rooms()







