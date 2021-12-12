import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

def combination_data_change(csv_data):
    list = []
    for i in range(0, len(csv_data)):
        num = 0
        bronze = 1
        silver = 3
        gold = 5
        platinum = 9
        str = csv_data['combination'][i]
        if str.find("Void") != -1:
            if int(str[str.find("Void") + 7]) >= 3:
                num += gold
        if str.find("MechPilot") != -1:
            if int(str[str.find("MechPilot") + 12]) >= 3:
                num += gold
        if str.find("Rebel") != -1:
            if int(str[str.find("Rebel") + 8]) >= 9:
                num += platinum
            elif int(str[str.find("Rebel") + 8]) >= 6:
                num += gold
            elif int(str[str.find("Rebel") + 8]) >= 3:
                num += bronze
        if str.find("Valkyrie") != -1:
            if int(str[str.find("Valkyrie") + 11]) >= 2:
                num += gold
        if str.find("StarGuardian") != -1:
            if int(str[str.find("StarGuardian") + 15]) >= 6:
                num += gold
            elif int(str[str.find("StarGuardian") + 15]) >= 3:
                num += bronze
        if str.find("Cybernetic") != -1:
            if int(str[str.find("Cybernetic") + 13]) >= 6:
                num += gold
            elif int(str[str.find("Cybernetic") + 13]) >= 3:
                num += bronze
        if str.find("Chrono") != -1:
            if int(str[str.find("Chrono") + 9]) >= 6:
                num += gold
            elif int(str[str.find("Chrono") + 9]) >= 4:
                num += silver
            elif int(str[str.find("Chrono") + 9]) >= 4:
                num += bronze
        if str.find("DarkStar") != -1:
            if int(str[str.find("DarkStar") + 11]) >= 9:
                num += platinum
            elif int(str[str.find("DarkStar") + 11]) >= 6:
                num += gold
            elif int(str[str.find("DarkStar") + 11]) >= 3:
                num += bronze
        if str.find("SpacePirate") != -1:
            if int(str[str.find("SpacePirate") + 14]) >= 4:
                num += gold
            elif int(str[str.find("SpacePirate") + 14]) >= 2:
                num += bronze
        if str.find("Celestial") != -1:
            if int(str[str.find("Celestial") + 12]) >= 6:
                num += gold
            elif int(str[str.find("Celestial") + 12]) >= 4:
                num += silver
            elif int(str[str.find("Celestial") + 12]) >= 2:
                num += bronze
        if str.find("Blademaster") != -1:
            if int(str[str.find("Blademaster") + 14]) >= 9:
                num += platinum
            elif int(str[str.find("Blademaster") + 14]) >= 6:
                num += gold
            elif int(str[str.find("Blademaster") + 14]) >= 3:
                num += bronze
        if str.find("ManaReaver") != -1:
            if int(str[str.find("ManaReaver") + 13]) >= 2:
                num += gold
        if str.find("Sorcerer") != -1:
            if int(str[str.find("Sorcerer") + 11]) >= 8:
                num += platinum
            elif int(str[str.find("Sorcerer") + 11]) >= 6:
                num += gold
            elif int(str[str.find("Sorcerer") + 11]) >= 4:
                num += silver
            elif int(str[str.find("Sorcerer") + 11]) >= 2:
                num += bronze
        if str.find("Protector") != -1:
            if int(str[str.find("Protector") + 12]) >= 4:
                num += gold
            elif int(str[str.find("Protector") + 12]) >= 2:
                num += bronze
        if str.find("Vanguard") != -1:
            if int(str[str.find("Vanguard") + 11]) >= 4:
                num += platinum
            elif int(str[str.find("Vanguard") + 11]) >= 4:
                num += gold
            elif int(str[str.find("Vanguard") + 11]) >= 2:
                num += bronze
        if str.find("Mystic") != -1:
            if int(str[str.find("Mystic") + 9]) >= 4:
                num += gold
            elif int(str[str.find("Mystic") + 9]) >= 2:
                num += bronze
        if str.find("Brawler") != -1:
            if int(str[str.find("Brawler") + 10]) >= 4:
                num += gold
            elif int(str[str.find("Brawler") + 10]) >= 2:
                num += bronze
        if str.find("Mercenary") != -1:
            num += gold
        if str.find("Starship") != -1:
            num += gold
        if str.find("Infiltrator") != -1:
            if int(str[str.find("Infiltrator") + 14]) >= 6:
                num += platinum
            elif int(str[str.find("Infiltrator") + 14]) >= 4:
                num += gold
            elif int(str[str.find("Infiltrator") + 14]) >= 2:
                num += bronze
        if str.find("Sniper") != -1:
            if int(str[str.find("Sniper") + 9]) >= 2:
                num += gold
        if str.find("Blaster") != -1:
            if int(str[str.find("Blaster") + 10]) >= 4:
                num += gold
            elif int(str[str.find("Blaster") + 10]) >= 2:
                num += bronze
        if str.find("Demolitionist") != -1:
            if int(str[str.find("Demolitionist") + 16]) >= 2:
                num += gold
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
    tear_s = 2.3
    tear_a = 2
    tear_b = 1.7
    tear_c = 1.4
    tear_d = 1
    for i in range(0, len(csv_data)):
        num = 0
        step = 0
        count = 0
        str = csv_data['champion'][i]
        l = str.split("}")
        del l[-1]
        del l[-1]
        for v in l:
            v = v[v.find('[') + 1:v.find(']')]
            if str.find('11') != -1:
                num+=tear_a
            if str.find('12') != -1:
                num+=tear_s
            if str.find('13') != -1:
                num+=tear_c
            if str.find('14') != -1:
                num+=tear_b
            if str.find('15') != -1:
                num+=tear_s
            if str.find('16') != -1:
                num+=tear_b
            if str.find('17') != -1:
                num+=tear_b
            if str.find('19') != -1:
                num+=tear_a
            if str.find('22') != -1:
                num+=tear_c
            if str.find('23') != -1:
                num+=tear_b
            if str.find('24') != -1:
                num+=tear_b
            if str.find('25') != -1:
                num+=tear_a
            if str.find('26') != -1:
                num+=tear_b
            if str.find('27') != -1:
                num+=tear_c
            if str.find('29') != -1:
                num+=tear_b
            if str.find('33') != -1:
                num+=tear_b
            if str.find('34') != -1:
                num+=tear_c
            if str.find('35') != -1:
                num+=tear_b
            if str.find('36') != -1:
                num+=tear_s
            if str.find('37') != -1:
                num+=tear_s
            if str.find('39') != -1:
                num+=tear_a
            if str.find('44') != -1:
                num+=tear_s
            if str.find('45') != -1:
                num+=tear_d
            if str.find('46') != -1:
                num+=tear_c
            if str.find('47') != -1:
                num+=tear_c
            if str.find('49') != -1:
                num+=tear_s
            if str.find('55') != -1:
                num+=tear_b
            if str.find('56') != -1:
                num+=tear_d
            if str.find('57') != -1:
                num+=tear_s
            if str.find('59') != -1:
                num+=tear_b
            if str.find('66') != -1:
                num+=tear_a
            if str.find('67') != -1:
                num+=tear_s
            if str.find('69') != -1:
                num+=tear_c
            if str.find('77') != -1:
                num+=tear_b
            if str.find('79') != -1:
                num+=tear_b
            if str.find('99') != -1:
                num+=tear_a
        list_a.append(num)
    return list_a

def load_match_data(filename):
    names = ['gameId', 'gameDuration', 'level', 'lastRound', 'Ranked', 'ingameDuration', 'combination', 'champion']
    csv_data = pd.read_csv(filename, names=names, low_memory=False)
    csv_data.drop('gameId', axis=1, inplace=True)
    csv_data.drop('gameDuration', axis=1, inplace=True)
    csv_data.drop('ingameDuration', axis=1, inplace=True)
    csv_data.drop(index = 0, axis = 0, inplace = True)
    drop_empty_data(csv_data)
    csv_data.to_json("test.json", orient="records")
    data = pd.read_json("test.json")
    return data

def drop_empty_data(data):
    str = "{}"
    for i in range(1, len(data)):
        str1 = data['champion'][i]
        if str1 == str:
            data.drop(index = i,axis = 0, inplace = True)

def revice_data(data):

    df = pd.DataFrame()
    df["level"] = data["level"]
    df["round"] = data["lastRound"]
    df["combination"] = combination_data_change(data)
    df["champion"] = champion_data_change(data)
    df["item"] = item_change(data)
    df["rank"] = data["Ranked"]

    return df

def normalize(data):
    nm = MinMaxScaler()
    df = nm.fit_transform(data)
    df_nm = pd.DataFrame(df, columns=["level", "round", "combination", "champion", "item", "Ranked"])
    df_nm.drop('Ranked', axis=1, inplace=True)
    return df_nm

def accurate_data(data):
    # 분석을 위한 정규화 데이터
    target = data["rank"]
    nm_data = normalize(data)

    x_train, x_test, y_train, y_test = train_test_split(nm_data, target, test_size=0.3, random_state=0, shuffle=True, stratify=target)

    model = GaussianNB()
    model.fit(x_train, y_train)

    expected = y_test
    predicate = model.predict(x_test)
    print(metrics.classification_report(y_test, predicate))
    print("rank accuracy : {}".format((accuracy_score(y_test, predicate))))
    
def accurate_sunbang(data):
    # 분석을 위한 정규화 데이터
    target = data["rank"]
    nm_data = normalize(data)
    sunbang = []
    
    for i in range(len(nm_data)):
        if target[i]>0 and target[i]<5 :
            sunbang.append(1)
        else :
            sunbang.append(0)

    x_train, x_test, y_train, y_test = train_test_split(nm_data, sunbang, test_size=0.3, random_state=0, shuffle=True, stratify=sunbang)

    model = GaussianNB()
    model.fit(x_train, y_train)

    expected = y_test
    predicate = model.predict(x_test)
    print(metrics.classification_report(y_test, predicate))
    print("sunbang accuracy : {}".format((accuracy_score(y_test, predicate))))
    
def groupby_data(data):
    group_rank = match_data.groupby('rank').mean()
    display(group_rank)
    return group_rank
    
def plot_avg(x, str):
    title = str + " avg per Rank"
    plt.figure(figsize=(16, 8))
    plt.title(title)
    plt.plot(x.index ,x[str], 'o--')
    plt.show()

if __name__ == '__main__':
    data = load_match_data("match_data.csv")
    #시각화를 위환 평균 매치 데이터
    match_data = revice_data(data)
    #등수별 평균 데이터
    group_data = groupby_data(match_data)
    
    # 평균데이터 그래프 그리기
    plot_avg(group_data, "level")
    plot_avg(group_data, "round")
    plot_avg(group_data, "combination")
    plot_avg(group_data, "champion")
    plot_avg(group_data, "item")
    
    # 모델의 정확도 출력
    accurate_data(match_data)
    accurate_sunbang(match_data)
