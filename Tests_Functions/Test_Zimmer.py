from Domain.Zimmer import Zimmer
from Functions.Functions_Zimmer import functions_zimmer

class test_Zimmer:
    def __init__(self, functions_zimmer):
        self.functions_zimmer = functions_zimmer
    def test_add_to_zimmerliste(self):
        zimmerliste= []
        zimmer1= Zimmer(1,2,22,"blau",0)
        zimmer2 = Zimmer(2, 5, 22, "blau", 0)
        zimmerliste.append(zimmer1)
        zimmerliste.append(zimmer2)
        self.functions_zimmer.add_to_zimmerliste(zimmerliste)
        assert zimmer1 == self.functions_zimmer.zimmerliste[0]
        assert zimmer2 == self.functions_zimmer.zimmerliste[1]
        self.functions_zimmer.zimmerliste= []
    def test_add_zimmer(self):
        zimmer1 = Zimmer(1, 2, 22, "blau", 0)
        self.functions_zimmer.add_zimmer(zimmer1)
        assert zimmer1== self.functions_zimmer.zimmerliste[0]
        self.functions_zimmer.zimmerliste = []
    def test_update_zimmer(self):
        zimmer1 = Zimmer(1, 2, 22, "blau", 0)
        self.functions_zimmer.zimmerliste.append(zimmer1)
        self.functions_zimmer.update_zimmer(1,44)
        zimmer1 = Zimmer(1, 2, 44, "blau", 0)
        assert zimmer1 == self.functions_zimmer.zimmerliste[0]
        self.functions_zimmer.zimmerliste = []
    def test_delete_zimmer(self):
        zimmer1 = Zimmer(1, 2, 22, "blau", 0)
        zimmer2 = Zimmer(2, 5, 22, "blau", 0)
        self.functions_zimmer.zimmerliste.append(zimmer1)
        self.functions_zimmer.zimmerliste.append(zimmer2)
        self.functions_zimmer.delete_zimmer(1)
        assert zimmer2 == self.functions_zimmer.zimmerliste[0]
        self.functions_zimmer.zimmerliste = []

    def main(self,test_zimmer):
        test_zimmer.test_add_to_zimmerliste()
        test_zimmer.test_add_zimmer()
        test_zimmer.test_update_zimmer()
        test_zimmer.test_delete_zimmer()




