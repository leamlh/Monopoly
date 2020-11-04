
from tkinter import *
# Page creation
page=Tk()
page.geometry("700x650")

# Left column
pos20 = Label(page, text="FREE PARKING", bg='white')
pos19 = Label(page, text="PARCHMENT\nJEWELLERS", bg='orange')
pos18 = Label(page, text="HIGH STREET", bg='orange')
pos17 = Label(page, text="COMMUNITY CHEST", bg='cyan')
pos16 = Label(page, text="JEWRY STREET", bg='orange')
pos15 = Label(page, text="WINCHESTER TRAIN\n STATION", bg='grey')
pos14 = Label(page, text="THEATRE ROYAL\nWINCHESTER", bg='pink')
pos13 = Label(page, text="HAT FAIR", bg='pink')
pos12 = Label(page, text="ADAM KNIBB\nARCHITECTS", bg='white')
pos11 = Label(page, text="THE BUTTERCROSS", bg='pink')
pos10 = Label(page, text="PRISON", bg='white')

# Up row
pos21 = Label(page, text="CHESIL RECTORY\n RETAURANT", bg='red')
pos22 = Label(page, text="CHANCE", bg='white')
pos23 = Label(page, text="HAMPSHIRE\n CHRONICLES", bg='red')
pos24 = Label(page, text="WINCHESTER\n DISTILLERY", bg='red')
pos25 = Label(page, text="WINCHESTER\nTAXI", bg='grey')
pos26 = Label(page, text="HOSPITAL OF\nST CROSS", bg='yellow')
pos27 = Label(page, text="WINCHESTER SCIENCE\n CENTER", bg='yellow')
pos28 = Label(page, text="BLUE APPLE\n THEATRE", bg='white')
pos29 = Label(page, text="MARWELL\nZOO", bg='yellow')
pos30 = Label(page, text="GO TO\nPRISON", bg='white')

# Right column
pos31 = Label(page, text="WINCHESTER DISCOVERY\nCENTER", bg='green')
pos32 = Label(page, text="8COLLEGE\nSTREET", bg='green')
pos33 = Label(page, text="COM\n CHEST", bg='cyan')
pos34 = Label(page, text="UNIVERSITY OF WINCHESTER", bg='green')
pos35 = Label(page, text="STAGECOACH\n KINGS CITY", bg='grey')
pos36 = Label(page, text="CHANCE", bg='white')
pos37 = Label(page, text="THE GREAT\n HALL", bg='blue')
pos38 = Label(page, text="LUXURY\n TAX", bg='white')
pos39 = Label(page, text="WINCHESTER\nCATHEDRAL", bg='blue')

# Down row
pos9 = Label(page, text="MILITARY\nMUSEUM", bg='blue')
pos8 = Label(page, text="WESTGATE\n MUSEUM", bg='blue')
pos7 = Label(page, text="CHANCE", bg='white')
pos6 = Label(page, text="CITY MUSEUM", bg='blue')
pos5 = Label(page, text="RIVER ITCHEN", bg='grey')
pos4 = Label(page, text="INCOME\nTAX", bg='white')
pos3 = Label(page, text="KING ALFRED'S\n STATUE", bg='brown')
pos2 = Label(page, text="COM CHEST", bg='cyan')
pos1 = Label(page, text="TRINITY\nWINCHESTER", bg='brown')
pos0 = Label(page, text="GOOOO", bg='white')

# Left column
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

# Up row
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

# Right column
pos31.grid(row=1, column=10)
pos32.grid(row=2, column=10)
pos33.grid(row=3, column=10)
pos34.grid(row=4, column=10)
pos35.grid(row=5, column=10)
pos36.grid(row=6, column=10)
pos37.grid(row=7, column=10)
pos38.grid(row=8, column=10)
pos39.grid(row=9, column=10)

# Down row
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

page.mainloop()