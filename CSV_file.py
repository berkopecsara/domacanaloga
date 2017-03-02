class podatki:
    def __init__(self, ime_priimek, email, kraj_bivanja):
        print (ime_priimek + " " + email + " " + kraj_bivanja)
        self.ime_priimek = ime_priimek
        self.email = email
        self.kraj_bivanja= kraj_bivanja

    def izpis(self):
        print (self.ime_priimek+ ", " + self.email + ", " + self.kraj_bivanja)

podatek1 = podatki("Sara Berkopec", "berkopecsara@gmail.com", "Novo mesto")
podatek2= podatki("Jasmina Perne", "jasperne@gmail.com", "Ljubljana")
podatek3= podatki("Lilija Kuk", "lilijakuk@gmail.com", "Ljubljana")


print ("Vsi podatki: ")
vsi_podatki = [podatek1, podatek2, podatek3]
for v in vsi_podatki:
    v.izpis()

