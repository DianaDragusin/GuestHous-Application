from File_Reader import Reader
from File_Writer import Gast_writer, Zimmer_writer,Reservierung_writer
from UI.ui_Gast import ui_Gast
from UI.ui_Zimmer import ui_Zimmer
from UI.ui_Gemeinsam import ui_Gemeinsam
from Functions.Functions_Gast import  functions
from Functions.Functions_Zimmer import functions_zimmer
from Functions.Functions_Gemeinsam import functions_gemeinsam
from Tests_Functions.Test_Gast import Test_gast
from  Tests_Functions.Test_Zimmer import test_Zimmer
from Tests_Functions.Test_Gemeinsam import test_Gemeinsam

class Starters:
    def menu(self):
            return """0. Return
        1. Gast Teil
        2. Zimmer Teil
        3. Gemeinsam Teil
                """
    def main(self,uiGast,uiZimmer,uiGemeinsam,testgast,testzimmer,testgemeinsam):
        while True:
            print(self.menu())
            x = int(input(" Choose one option "))
            if x == 0:
                return 0
            if x == 1:
                testgast.main(testgast)
                uiGast.main()
            if x == 2:
                testzimmer.main(testzimmer)
                uiZimmer.main()
            if x == 3:
                testgemeinsam.main(testgemeinsam)
                uiGemeinsam.main()
class Console_App:



    @staticmethod
    def start():
        file_reservierung_r=Reader().Reservierungen()
        file_reservierung_w=Reservierung_writer()
        file_gast_r= Reader().Gast()
        file_gast_w= Gast_writer()
        file_zimmer_r= Reader().Zimmer()
        file_zimmer_w= Zimmer_writer()
        methods_gemeinsam=functions_gemeinsam()
        methods_Zimmer= functions_zimmer()
        methods_Gast= functions()
        uiGemeinsam= ui_Gemeinsam(methods_Gast,methods_Zimmer,methods_gemeinsam,file_gast_r,file_zimmer_r,file_reservierung_r,file_gast_w,file_reservierung_w)
        uiGast= ui_Gast(methods_Gast,file_gast_r,file_gast_w)
        uiZimmer= ui_Zimmer(methods_Zimmer,file_zimmer_r,file_zimmer_w)
        testgast= Test_gast(methods_Gast)
        testzimmer= test_Zimmer(methods_Zimmer)
        testgemeinsam= test_Gemeinsam(methods_gemeinsam)


        return uiGast,uiZimmer,uiGemeinsam,testgast,testzimmer,testgemeinsam



def mainul ():
   uiGast,uiZimmer,uiGemeinsam,testgast,testzimmer,testgemeinsam=Console_App.start()
   join=Starters()
   join.main(uiGast,uiZimmer,uiGemeinsam,testgast,testzimmer,testgemeinsam)

mainul()