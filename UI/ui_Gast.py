from Functions.Functions_Gast import functions
from Domain.Gast import Gast
from File_Reader import Reader
from File_Writer import Gast_writer

class ui_Gast:

    def __init__(self,functions,gaste,gaste_app):
        self.functions= functions
        self.gaste=gaste
        self.gaste_app= gaste_app

    def menu (self):
      return"""0. Return
1. Add Guest
2. Update Last Name of a Guest
3. Delete Guest
4. Show a list of the guests
        """
    def main(self):
        self.functions.add_to_gastliste(self.gaste)

        while True :
            print (self.menu())
            x=int(input(" Choose one option "))
            if x== 0:
                return 0
            if x==1 :
                vorname = input("First Name: ")
                nachname = input("Last Name :")
                self.functions.add_gast(Gast(vorname,nachname))
                if(self.functions.test_append(vorname,nachname)==1):
                     self.gaste_app.append_guest(vorname, nachname)
                #self.gaste.append(Gast(vorname,nachname))
               # self.functions.add_gast(Gast(vorname,nachname))
            if x==2:
                vorname = input("First Name: ")
                nachname = input("Last Name :")
                newnachname = input("New Last Name :")
                clients=self.functions.update_gast(vorname,nachname,newnachname)
                self.gaste_app.update_guest(clients)
              #  self.gaste_app.update_guest

            if x==3:
                vorname = input("First Name: ")
                nachname = input("Last Name :")
                clients=self.functions.delete_gast(vorname, nachname)
                self.gaste_app.delete_guest(clients)
            if x== 4:

                #self.functions.add_to_gastliste(self.gaste)
                self.functions.print_gaste()







