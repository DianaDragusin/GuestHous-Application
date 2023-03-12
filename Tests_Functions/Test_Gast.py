from Functions.Functions_Gast import functions
from Domain.Gast import Gast
class Test_gast:
    def __init__(self, functions):
        self.functions = functions

    def test_add_to_gastliste(self):
        gastliste= []
        gast1= Gast("ana", "maria")
        gastliste.append(gast1)
        self.functions.add_to_gastliste(gastliste)
        gastliste2= self.functions.gastliste
        assert gast1 == gastliste2[len(gastliste)-1]
        self.functions.gastliste = []
    def test_add_gast(self):
        gast1 = Gast("ana", "maria")
        self.functions.add_gast(gast1)
        gasteliste= self.functions.gastliste
        assert gast1== gasteliste[len(gasteliste)-1]
        self.functions.gastliste = []

    def test_update_gast(self):
        gast1 = Gast("ana", "maria")
        self.functions.add_gast(gast1)
        self.functions.update_gast("ana", "maria", "mircescu")
        gast2= Gast("ana", "mircescu")
        assert gast2== self.functions.gastliste[0]
        self.functions.gastliste=[]
    def test_delete_gast(self):
        gast1 = Gast("ana", "maria")
        gast2 = Gast("ana", "mircescu")
        self.functions.add_gast(gast1)
        self.functions.add_gast(gast2)
        self.functions.delete_gast("ana", "maria")
        assert gast2== self.functions.gastliste[0]
        self.functions.gastliste = []

    def main (self,test_gast):
        test_gast.test_add_to_gastliste()
        test_gast.test_add_gast()
        test_gast.test_update_gast()
        test_gast.test_delete_gast()





