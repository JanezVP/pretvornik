# -*- coding: UTF-8 -*-
print ("Pozdravljen uporabnik. Jaz sem pretvornik enot.")

odgovor = "da"

while True:
    if odgovor == "da":
        kilometer = float (raw_input("Vnesite kilometer: "))
        milja = 0.62 * kilometer
        print milja
    elif odgovor == "ne":
        break

    odgovor = raw_input ("Bi radi se enkrat uporabili pretvornik? Vpišite Da ali Ne: ")
    print ("hvala")
