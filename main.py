# CODE PYTHON POUR JEU MONOPOLY YDAYS #

import random

mon_dict = {"position": "card",
            0: "GO",
            1: "TRINITY WINCHESTER",
            2: "COMMUNITY CHEST",
            3: "KING ALFRED'S STATUE",
            4: "INCOME TAX",
            5: "RIVER ITCHEN",
            6: "CITY MUSEUM",
            7: "CHANCE",
            8: "WESTGATE MUSEUM",
            9: "MILITARY MUSEUMS",
            10: "PRISON VISITING/IN JAIL",
            11: "THE BUTTERCROSS",
            12: "ADAM KNIBB ARCHITECTS",
            13: "HAT FAIR",
            14: "THEATRE ROYAL WINCHESTER",
            15: "WINCHESTER TRAIN STATION",
            16: "JEWRY STREET",
            17: "COMMUNITY CHEST",
            18: "HIGH STREET",
            19: "PARCHMENT JEWELLERS",
            20: "FREE PARKING",
            21: "CHESIL RECTORY RESTAURANT",
            22: "CHANCE",
            23: "HAMPSHIRE CHRONICLES",
            24: "WINCHESTER DISTILLERY",
            25: "WINCHESTER TAXI",
            26: "HOSPITAL OF ST.CROSS",
            27: "WINCHESTER SCIENCE CENTRE",
            28: "BLUE APPLE THEATRE",
            29: "MARWELL ZOO",
            30: "GO TO JAIL",
            31: "WINCHESTER DISCOVERY CENTRE",
            32: "8 COLLEGE STREET",
            33: "COMMUNITY CHEST",
            34: "THE UNIVERSITY OF WINCHESTER",
            35: "STAGECOACH KINGS CITY",
            36: "CHANCE",
            37: "THE GREAT HALL",
            38: "LUXURY TAX",
            39: "WINCHESTER CATHEDRAL"}

if __name__ == '__main__':

    walletAmount = 1500                                     # set the initial wallet amount at 1500 dollars
    playersPosition = 0                                     # set the initial player's position at 0
    for i in [0, 1, 2, 3, 4, 6, 7, 8, 9]:
        print("You are at the " + str(playersPosition)+" position.")
        dice1 = random.randint(1, 6)                            # throw the first dice
        dice2 = random.randint(1, 6)                            # throw the second dice
        total_dices = dice1 + dice2                             # total

        print("You must advance " + str(total_dices) + " spaces.")

        playersPosition = playersPosition + total_dices
        print("You are now at the " + str(playersPosition) + " position. You are currently at "
              + mon_dict[playersPosition])
