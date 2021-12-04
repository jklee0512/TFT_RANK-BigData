import csv
import json
import pprint

import pandas as pd


def combination_change(csv_data):
    for i in range(1, 79999):
        num = 0
        str = csv_data['combination'][i]
        val = str.find("DarkStar")

        if str.find("Void") != -1:
            if int(str[str.find("Void") + 7]) >= 3:
                num += 4
        if str.find("MechPilot") != -1:
            if int(str[str.find("MechPilot") + 12]) >= 3:
                num += 4
        if str.find("Rebel") != -1:
            if int(str[str.find("Rebel") + 8]) >= 9:
                num += 8
            elif int(str[str.find("Rebel") + 8]) >= 6:
                num += 4
            elif int(str[str.find("Rebel") + 8]) >= 3:
                num += 1
        if str.find("Valkyrie") != -1:
            if int(str[str.find("Valkyrie") + 11]) >= 2:
                num += 4
        if str.find("StarGuardian") != -1:
            if int(str[str.find("StarGuardian") + 15]) >= 6:
                num += 4
            elif int(str[str.find("StarGuardian") + 15]) >= 3:
                num += 1
        if str.find("Cybernetic") != -1:
            if int(str[str.find("Cybernetic") + 13]) >= 6:
                num += 4
            elif int(str[str.find("Cybernetic") + 13]) >= 3:
                num += 1
        if str.find("Chrono") != -1:
            if int(str[str.find("Chrono") + 9]) >= 6:
                num += 4
            elif int(str[str.find("Chrono") + 9]) >= 4:
                num += 2
            elif int(str[str.find("Chrono") + 9]) >= 4:
                num += 1
        if str.find("DarkStar") != -1:
            if int(str[str.find("DarkStar") + 11]) >= 9:
                num += 8
            elif int(str[str.find("DarkStar") + 11]) >= 6:
                num += 4
            elif int(str[str.find("DarkStar") + 11]) >= 3:
                num += 1
        if str.find("SpacePirate") != -1:
            if int(str[str.find("SpacePirate") + 14]) >= 4:
                num += 4
            elif int(str[str.find("SpacePirate") + 14]) >= 2:
                num += 1
        if str.find("Celestial") != -1:
            if int(str[str.find("Celestial") + 12]) >= 6:
                num += 4
            elif int(str[str.find("Celestial") + 12]) >= 4:
                num += 2
            elif int(str[str.find("Celestial") + 12]) >= 2:
                num += 1
        if str.find("Blademaster") != -1:
            if int(str[str.find("Blademaster") + 14]) >= 9:
                num += 8
            elif int(str[str.find("Blademaster") + 14]) >= 6:
                num += 4
            elif int(str[str.find("Blademaster") + 14]) >= 3:
                num += 1
        if str.find("ManaReaver") != -1:
            if int(str[str.find("ManaReaver") + 13]) >= 2:
                num += 4
        if str.find("Sorcerer") != -1:
            if int(str[str.find("Sorcerer") + 11]) >= 8:
                num += 8
            elif int(str[str.find("Sorcerer") + 11]) >= 6:
                num += 4
            elif int(str[str.find("Sorcerer") + 11]) >= 4:
                num += 2
            elif int(str[str.find("Sorcerer") + 11]) >= 2:
                num += 1
        if str.find("Protector") != -1:
            if int(str[str.find("Protector") + 12]) >= 4:
                num += 4
            elif int(str[str.find("Protector") + 12]) >= 2:
                num += 1
        if str.find("Vanguard") != -1:
            if int(str[str.find("Vanguard") + 11]) >= 4:
                num += 8
            elif int(str[str.find("Vanguard") + 11]) >= 4:
                num += 4
            elif int(str[str.find("Vanguard") + 11]) >= 2:
                num += 1
        if str.find("Mystic") != -1:
            if int(str[str.find("Mystic") + 9]) >= 4:
                num += 4
            elif int(str[str.find("Mystic") + 9]) >= 2:
                num += 1
        if str.find("Brawler") != -1:
            if int(str[str.find("Brawler") + 10]) >= 4:
                num += 4
            elif int(str[str.find("Brawler") + 10]) >= 2:
                num += 1
        if str.find("Mercenary") != -1:
            num += 4
        if str.find("Starship") != -1:
            num += 4
        if str.find("Infiltrator") != -1:
            if int(str[str.find("Infiltrator") + 14]) >= 6:
                num += 8
            elif int(str[str.find("Infiltrator") + 14]) >= 4:
                num += 4
            elif int(str[str.find("Infiltrator") + 14]) >= 2:
                num += 1
        if str.find("Sniper") != -1:
            if int(str[str.find("Sniper") + 9]) >= 2:
                num += 4
        if str.find("Blaster") != -1:
            if int(str[str.find("Blaster") + 10]) >= 4:
                num += 4
            elif int(str[str.find("Blaster") + 10]) >= 2:
                num += 1
        if str.find("Demolitionist") != -1:
            if int(str[str.find("Demolitionist") + 16]) >= 2:
                num += 4
        print(csv_data['combination'][i])
        print(num)


if __name__ == '__main__':
    names = ['gameId', 'gameDuration', 'level', 'lastRound', 'Ranked', 'ingameDuration', 'combination', 'champion']
    csv_data = pd.read_csv("TFT_MatchData.csv", names=names, low_memory=False)
    csv_data.drop('gameId', axis=1, inplace=True)
    csv_data.drop('gameDuration', axis=1, inplace=True)
    csv_data.drop('ingameDuration', axis=1, inplace=True)
    csv_data.to_json("test.json", orient="records")
    val = csv_data['combination'][1].find("DarkStar")
    print(type(csv_data['champion'][1]))
