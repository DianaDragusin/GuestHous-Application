from Functions.Functions_Gast import functions
from Domain.Zimmer import Zimmer
from Domain.Gast import Gast
from Domain.Reservierungen import Reservierungen
from File_Reader import Reader
from File_Writer import Gast_writer
from datetime import date
class ui_Gemeinsam:

    def __init__(self,functions_gast,functions_zimmer,functions_gemeinsam,gaste,rooms,reservierungen,gaste_app,reservierungen_app):
        self.functions_gast= functions_gast
        self.functions_zimmer= functions_zimmer
        self.functions_gemeinsam= functions_gemeinsam
        self.gaste= gaste
        self.rooms= rooms
        self.reservierungen=reservierungen
        self.gaste_app= gaste_app
        self.reservierungen_app= reservierungen_app

    def menu (self):    #funtion de pisat
      return"""0. Return
1. Mach eine Reservierung
2 Anzeige die Liste von Gästen, die aktuelle Reservierungen haben
3 Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien (z. B. ein Zimmer billiger
als 100 Euro, mit Meerblick)
4 Anzeige alle Zimmer, die heute frei sind
        """

    def main(self):

        self.functions_gemeinsam.add_to_reservierungenliste(self.reservierungen)
        self.functions_gemeinsam.add_to_zimmerliste(self.rooms)
        self.functions_gemeinsam.add_to_gasteliste(self.gaste)

        while True :

            print (self.menu())
            x=int(input(" Choose one option "))
            if x== 0:
                return 0
            if x==1 :

                gaste_der_reservierung = []
                print ("Clients name:")
                vorname = input("First Name: ")
                nachname = input("Last Name :")
                gaste_der_reservierung.append(Gast(vorname,nachname))
                if not self.functions_gemeinsam.get_friend(Gast(vorname, nachname)):
                    print("We have added you to our database")
                    self.functions_gemeinsam.add_gast_to_gastliste(Gast(vorname, nachname))
                    self.gaste_app.append_guest(vorname, nachname)
                family=int(input( ("How many people are you staying with?")))
                self.functions_gemeinsam.value_error_or_type_error(family)
                rooms=self.functions_gemeinsam.get_rooms(family)


                print ("Who are you staying with ?")
                for member in range(family-1):
                    vorname_friend = input("First Name:")
                    nachname_friend = input("Last Name :")
                    if not self.functions_gemeinsam.get_friend(Gast(vorname_friend,nachname_friend)):

                        print(f'{vorname_friend} {nachname_friend} is not in our database!' )
                        self.gaste_app.append_guest(vorname_friend, nachname_friend)
                        print(f'We have added {vorname_friend} {nachname_friend} to  our database ')
                    gaste_der_reservierung.append(Gast(vorname_friend,nachname_friend))
                    self.functions_gemeinsam.add_gast_to_gastliste(Gast(vorname, nachname))

                print("When would you like to stay with us?")
                year_f = int(input((f'From: year: ')))
                month_f = int(input(("month: ")))
                day_f = int(input(("day: ")))
                year_t = int(input((f'To: year: ')))
                month_t = int(input(("month: ")))
                day_t = int(input(("day: ")))
                date_from= date(year_f,month_f,day_f)
                date_to = date(year_t, month_t, day_t)
                self.functions_gemeinsam.dates(year_f,month_f,day_f,year_t,month_t,day_t)
                good_room=rooms[0]
                rooms=self.functions_gemeinsam.is_it_available(rooms,date_from,date_to)

                if len(rooms)>0:
                    ans2 =int(input("Would you like to have seaside view? yes- 1 no - 0 : "))
                    ok=0
                    for room in rooms:
                        if room.meerblick == ans2:
                            ok=1
                            print("We have found the perfect room for you.")
                            break
                    if ok==0:
                        print("We hope this room is also good")
                    good_room = room
                    self.reservierungen_app.append_reservierung(gaste_der_reservierung,good_room,date_from,date_to)
                    self.functions_gemeinsam.add_reservierung(Reservierungen(gaste_der_reservierung,good_room,date_from,date_to))
                    print (f'Mr/Mrs {vorname} {nachname} your room is room number {good_room.nummer}.Welcome to Grand Hotel!')
                else :
                    print("There are no available rooms for this period")


            if x==2:
                print(date.today())
                aktuelle_gasten=  self.functions_gemeinsam.aktuelle_reservierungen()
                print("Die Gaste die aktuelle Reservierungen haben sind folgende: ")
                for gast in aktuelle_gasten:
                    print(gast)
            if x==3:
              preis= int(input("The highest price for a room is  :") )
              self.functions_gemeinsam.value_error_or_type_error(preis)
              meerblick= int(input("Do you want seaside view ? yes=1/no=0  :"))
              rooms= self.functions_gemeinsam.filter_preis_meerblick(preis,meerblick)
              if len(rooms)>0:
                print("These are our rooms")
                for room in rooms:
                    print(room)
              else:
                  print("Sorry we don't have this kind of rooms")
            if x== 4:
                print("Today's date is" + str(date.today()))
                rooms= self.functions_gemeinsam.today_free()
                print("These are today's free rooms: ")
                for room in rooms:
                    print(room)







