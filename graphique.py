
from tkinter import *
# Création d’une fenêtre
fntre=Tk()
fntre.geometry("700x650")

# Colonne de gauche
pos20 = Label(fntre, text="FREE PARKING", bg='white')
pos19 = Label(fntre, text="PARCHMENT\nJEWELLERS", bg='orange')
pos18 = Label(fntre, text="HIGH STREET", bg='orange')
pos17 = Label(fntre, text="COMMUNITY CHEST", bg='cyan')
pos16 = Label(fntre, text="JEWRY STREET", bg='orange')
pos15 = Label(fntre, text="WINCHESTER TRAIN\n STATION", bg='grey')
pos14 = Label(fntre, text="THEATRE ROYAL\nWINCHESTER", bg='pink')
pos13 = Label(fntre, text="HAT FAIR", bg='pink')
pos12 = Label(fntre, text="ADAM KNIBB\nARCHITECTS", bg='white')
pos11 = Label(fntre, text="THE BUTTERCROSS", bg='pink')
pos10 = Label(fntre, text="PRISON", bg='white')

# Ligne du haut
pos21 = Label(fntre, text="CHESIL RECTORY\n RETAURANT", bg='red')
pos22 = Label(fntre, text="CHANCE", bg='white')
pos23 = Label(fntre, text="HAMPSHIRE\n CHRONICLES", bg='red')
pos24 = Label(fntre, text="WINCHESTER\n DISTILLERY", bg='red')
pos25 = Label(fntre, text="WINCHESTER\nTAXI", bg='grey')
pos26 = Label(fntre, text="HOSPITAL OF\nST CROSS", bg='yellow')
pos27 = Label(fntre, text="WINCHESTER SCIENCE\n CENTER", bg='yellow')
pos28 = Label(fntre, text="BLUE APPLE\n THEATRE", bg='white')
pos29 = Label(fntre, text="MARWELL\nZOO", bg='yellow')
pos30 = Label(fntre, text="GO TO\nPRISON", bg='white')

# Colonne de droite
pos31 = Label(fntre, text="WINCHESTER DISCOVERY\nCENTER", bg='green')
pos32 = Label(fntre, text="8COLLEGE\nSTREET", bg='green')
pos33 = Label(fntre, text="COM\n CHEST", bg='cyan')
pos34 = Label(fntre, text="UNIVERSITY OF WINCHESTER", bg='green')
pos35 = Label(fntre, text="STAGECOACH\n KINGS CITY", bg='grey')
pos36 = Label(fntre, text="CHANCE", bg='white')
pos37 = Label(fntre, text="THE GREAT\n HALL", bg='blue')
pos38 = Label(fntre, text="LUXURY\n TAX", bg='white')
pos39 = Label(fntre, text="WINCHESTER\nCATHEDRAL", bg='blue')

# Ligne du bas
pos9 = Label(fntre, text="MILITARY\nMUSEUM", bg='blue')
pos8 = Label(fntre, text="WESTGATE\n MUSEUM", bg='blue')
pos7 = Label(fntre, text="CHANCE", bg='white')
pos6 = Label(fntre, text="CITY MUSEUM", bg='blue')
pos5 = Label(fntre, text="RIVER ITCHEN", bg='grey')
pos4 = Label(fntre, text="INCOME\nTAX", bg='white')
pos3 = Label(fntre, text="KING ALFRED'S\n STATUE", bg='brown')
pos2 = Label(fntre, text="COM CHEST", bg='cyan')
pos1 = Label(fntre, text="TRINITY\nWINCHESTER", bg='brown')
pos0 = Label(fntre, text="GOOOO", bg='white')

# Colonne de gauche
pos20.grid(row=0, column=0)
pos19.grid(row=1, column=0)
pos18.grid(row=2, column=0)
pos17.grid(row=3, column=0)
pos16.grid(row=4, column=0)
pos15.grid(row=5, column=0)
pos14.grid(row=6, column=0)
pos13.grid(row=7, column=0)
pos12.grid(row=8, column=0)
pos11.grid(row=9, column=0)
pos10.grid(row=10, column=0)

# Ligne du haut
pos21.grid(row=0, column=1)
pos22.grid(row=0, column=2)
pos23.grid(row=0, column=3)
pos24.grid(row=0, column=4)
pos25.grid(row=0, column=5)
pos26.grid(row=0, column=6)
pos27.grid(row=0, column=7)
pos28.grid(row=0, column=8)
pos29.grid(row=0, column=9)
pos30.grid(row=0, column=10)

# Colonne de droite
pos31.grid(row=1, column=10)
pos32.grid(row=2, column=10)
pos33.grid(row=3, column=10)
pos34.grid(row=4, column=10)
pos35.grid(row=5, column=10)
pos36.grid(row=6, column=10)
pos37.grid(row=7, column=10)
pos38.grid(row=8, column=10)
pos39.grid(row=9, column=10)

# Ligne du bas
pos9.grid(row=10, column=1)
pos8.grid(row=10, column=2)
pos7.grid(row=10, column=3)
pos6.grid(row=10, column=4)
pos5.grid(row=10, column=5)
pos4.grid(row=10, column=6)
pos3.grid(row=10, column=7)
pos2.grid(row=10, column=8)
pos1.grid(row=10, column=9)
pos0.grid(row=10, column=10)


fntre.mainloop()