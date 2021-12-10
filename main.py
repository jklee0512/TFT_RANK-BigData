import csv
import json
import pprint
import pandas as pd

def combination_data_change(csv_data):
    list = []
    for i in range(0, len(csv_data)):
        num = 0
        str = csv_data['combination'][i]
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
        list.append(num)
    return list

def champion_data_change(data):
    array = []
    for i in range(0, len(data)):
        price = 0
        str = data['champion'][i]
        list = str.split("}")
        del list[-1]
        del list[-1]
        for v in list:
            star = int(v[v.find("star") + 7])
            if star == 3:
                star = 9
            elif star == 2:
                star = 3
            else:
                star = 1
            if v.find("Ahri") != -1:
                price += 2*star
            if v.find("Annie") != -1:
                price += 2 * star
            if v.find("Ashe") != -1:
                price += 3*star
            if v.find("AurelionSol") != -1:
                price += 5*star
            if v.find("Blitzcrank") != -1:
                price += 2*star
            if v.find("Caitlyn") != -1:
                price += 1*star
            if v.find("ChoGath") != -1:
                price += 4*star
            if v.find("Darius") != -1:
                price += 2*star
            if v.find("Ekko") != -1:
                price += 5*star
            if v.find("Ezreal") != -1:
                price += 3*star
            if v.find("Fiora") != -1:
                price += 1*star
            if v.find("Fizz") != -1:
                price += 4*star
            if v.find("Gangplank") != -1:
                price += 5*star
            if v.find("Graves") != -1:
                price += 1*star
            if v.find("Irelia") != -1:
                price += 4*star
            if v.find("JarvanIV") != -1:
                price += 1*star
            if v.find("Jayce") != -1:
                price += 3*star
            if v.find("Jhin") != -1:
                price += 4*star
            if v.find("Jinx") != -1:
                price += 4*star
            if v.find("KaiSa") != -1:
                price += 2*star
            if v.find("Karma") != -1:
                price += 3*star
            if v.find("Kassadin") != -1:
                price += 3*star
            if v.find("Kayle") != -1:
                price += 4*star
            if v.find("KhaZix") != -1:
                price += 1*star
            if v.find("Leona") != -1:
                price += 1*star
            if v.find("Lucian") != -1:
                price += 2*star
            if v.find("Lulu") != -1:
                price += 5*star
            if v.find("Lux") != -1:
                price += 3*star
            if v.find("Malphite") != -1:
                price += 1*star
            if v.find("MasterYi") != -1:
                price += 3*star
            if v.find("MissFortune") != -1:
                price += 5*star
            if v.find("Mordekaiser") != -1:
                price += 2*star
            if v.find("Neeko") != -1:
                price += 3*star
            if v.find("Poppy") != -1:
                price += 1*star
            if v.find("Rakan") != -1:
                price += 2*star
            if v.find("Rumble") != -1:
                price += 3*star
            if v.find("Shaco") != -1:
                price += 3*star
            if v.find("Shen") != -1:
                price += 2*star
            if v.find("Sona") != -1:
                price += 2*star
            if v.find("Soraka") != -1:
                price += 4*star
            if v.find("Syndra") != -1:
                price += 3*star
            if v.find("Thresh") != -1:
                price += 5*star
            if v.find("TwistedFate") != -1:
                price += 1*star
            if v.find("VelKoz") != -1:
                price += 4*star
            if v.find("Vi") != -1:
                price += 3*star
            if v.find("Wukong") != -1:
                price += 4*star
            if v.find("Xayah") != -1:
                price += 1*star
            if v.find("Xerath") != -1:
                price += 5*star
            if v.find("XinZhao") != -1:
                price += 2*star
            if v.find("Yasuo") != -1:
                price += 2*star
            if v.find("Ziggs") != -1:
                price += 1*star
            if v.find("Zoe") != -1:
                price += 1*star
        array.append(price)
    return array

def item_change(csv_data):
    list_a = []
    for i in range(0, len(csv_data)):
        num = 0
        step = 0
        count = 0
        str = csv_data['champion'][i]
        str = str.replace(" ", "")
        for j in range(len(str)):
            if str[j] == '[':
                step = 1
                continue
            if step == 1:
                if str[j] == ']':
                    if count == 2:
                        num += 3
                        count = 0
                    if count == 1:
                        num += 1
                        count = 0
                    step = 0
                    continue
                if str[j] == ',':
                    if count == 2:
                        num += 3
                        count = 0
                    if count == 1:
                        num += 1
                        count = 0
                    continue
                if str[j] != ',' or str[j] != ']':
                    count += 1
        list_a.append(num)
    return list_a

def load_match_data(filename):
    #filename is String
    names = ['gameId', 'gameDuration', 'level', 'lastRound', 'Ranked', 'ingameDuration', 'combination', 'champion']
    csv_data = pd.read_csv(filename, names=names, low_memory=False)
    csv_data.drop('gameId', axis=1, inplace=True)
    csv_data.drop('gameDuration', axis=1, inplace=True)
    csv_data.drop('ingameDuration', axis=1, inplace=True)
    csv_data.drop(index = 0, axis = 0, inplace = True)
    csv_data.to_json("test.json", orient="records")
    data = pd.read_json("test.json")
    return data

if __name__ == '__main__':
    data = load_match_data("TFT_Challenger_MatchData.csv")
    combination_score = combination_data_change(data)
    champion_value = champion_data_change(data)
    item_count = item_change(data)
    df = pd.DataFrame()
    df["level"] = data["level"]
    df["lastRound"] = data["lastRound"]
    df["Ranked"] = data["Ranked"]
    df["item_count"] = item_count
    df["champion_value"] = champion_value
    df["combination_score"] = combination_score
    print(df)
