
class Gast_writer:
    def append_guest(self,vorname,nachname):
        f = open("Gast_File", "a")
        f.write (vorname + " " + nachname)
        f.write("\n")
        f.close()
    def update_guest(self,guests):
        f = open("Gast_File", "a")
        f.seek(0)
        f.truncate()
        for guest in guests:
            f.write (guest.vorname+ " " + guest.nachname)
            f.write("\n")
        f.close
    def delete_guest(self,guests):
        f = open("Gast_File", "a")
        f.seek(0)
        f.truncate()
        for guest in guests:
            f.write (guest.vorname+ " " + guest.nachname)
            f.write("\n")
        f.close

class Zimmer_writer:
    def append_zimmer(self,nummer,anzahlgaste, preis, farbe, meerblick):
        f = open("Zimmer_File", "a")
        f.write("\n")
        f.write (str(nummer) + " " + str(anzahlgaste)+ " " +str(preis) + " " + farbe+ " " + str(meerblick))
        f.close()
    def update_zimmer(self, rooms):
        f = open("Zimmer_File", "a")
        f.seek(0)
        f.truncate()
        for room in rooms:
            f.write (str(room.nummer)+ " " + str(room.anzahlgaste )+ " " + str(room.preis )+ " " + room.farbe + " " + str(room.meerblick) )
            f.write("\n")
        f.close
    def delete_zimmer(self,rooms):
        f = open("Zimmer_File", "a")
        f.seek(0)
        f.truncate()
        for room in rooms:
            f.write(str(room.nummer)+ " " + str(room.anzahlgaste )+ " " + str(room.preis )+ " " + room.farbe + " " + str(room.meerblick))
            f.write("\n")
        f.close
class Reservierung_writer:
    def append_reservierung(self,gaste,zimmer,anfang,ende):
        f = open("Reservierungen_File", "a")
        for gast in gaste:
            f.write(gast.vorname + " " + gast.nachname+" ")
        f.write (";"+str(zimmer.nummer )+ " " + str(zimmer.anzahlgaste)+ " " + str(zimmer.preis)+ " " + zimmer.farbe+ " " + str(zimmer.meerblick)+";" )
        f.write(str(anfang.year) + " "+ str(anfang.month) + " "+ str(anfang.day)+ " ")
        f.write(str(ende.year) + " " + str(ende.month )+ " " + str(ende.day))
        f.write("\n")
        f.close()







