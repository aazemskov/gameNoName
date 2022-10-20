#aazemskov# Давай свои комменты будем выделять - #aazemskov# | #Zak# - чтобы понимать где чей коммент

import random as r
import sqlite3 as sql

#Zak# Пока ни для чего не используется, просто база с двумя таблицами
dbConnection = sql.connect("gamedata.db")
dbCursor = dbConnection.cursor()

sql_create_inventory_table = """ CREATE TABLE IF NOT EXISTS inventory (
                                    item_name text NOT NULL,
                                    quantity integer,
                                    item_description
                                ); """
sql_create_quests_table = """ CREATE TABLE IF NOT EXISTS quests (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    goal text
                                ); """
dbCursor.execute(sql_create_inventory_table)
dbCursor.execute(sql_create_quests_table)

#sql_add_test_item = """ INSERT INTO inventory (item_name, quantity) values ('test_item', 1); """
#dbCursor.execute(sql_add_test_item)
#dbConnection.commit()

#res = dbCursor.execute("SELECT * FROM inventory;")
#print(res.fetchall())


hp = 0
gold = 0
damage = 0
dexterity = 0 #Zak# Параметра уклонения пока нет. Уклонение считается просто от ловкости
armor = 0

def printParameters():
    print(f"У тебя {hp} жизней, {damage} урона и {gold} монет. Твоя ловкость {dexterity} и у тебя {armor} брони")

def printInventory():
    print(f"Тут будет вывод инвентаря, но сейчас его нет")

def printQuests():
    print(f"Тут будет вывод квестов, но сейчас нет нет")

def printHp():
    print("У тебя", hp, "жизней.")

def printgold():
    print("У тебя", gold, "монет.")

def printDamage():
    print("У тебя", damage, "урона.")

def printArmor():
    print("У тебя", armor, "брони.")

def statsRenew():
    global damage
    global dexterity
    global armor

def addItem():
    print("У тебя", armor, "брони.")
    statsRenew()

def loseItem():


def meetShop():
    global hp
    global damage
    global gold
    global armor

    def buy(cost):
        global gold
        if gold >= cost:
            gold -= cost
            printgold()
            return True
        print("У тебя маловато монет!")
        return False

    weaponLvl = r.randint(1, 3)
    weaponDmg = r.randint(1, 5) * weaponLvl
    weapons = ["Двуручный топор", "Железный меч", "Магический посох", "Французский багет", "Длинный лук", "Арбалет"]
    weaponRarities = ["Сломанный", "Редкий", "Легендарный"]
    weaponRarity = weaponRarities[weaponLvl - 1]
    weaponCost = r.randint(3, 10) * weaponLvl
    weapon = r.choice(weapons)
    armorLvl = r.randint(1, 3)
    armorTypes = ["Кожаная броня", "Кольчужный доспех", "Мифрильный доспех"]
    armorInStock = armorTypes[armorLvl - 1]
    armorСost = armorLvl * 4

    oneHpCost = 5
    threeHpCost = 12

    print("На пути тебе встретился торговец!")
    printParameters()
    choiceToEnter = input("Что ты будешь делать? 1) Посмотреть товары 2) Уйти 8) Характеристики 9) Инвентарь 0) Квесты: ").lower()

    while choiceToEnter != "2":
        if choiceToEnter == "1":
            print("1) Уйти")
            print("2) Малое зелье здоровья (+1 hp) -", oneHpCost, "монет;")
            print("3) Большое зелье здоровья (+3 hp) -", threeHpCost, "монет;")
            print(f"4) {weaponRarity} {weapon} (+{weaponDmg} dmg) - {weaponCost} монет")
            print(f"5) {armorInStock} (+{armorLvl} block) - {armorСost} монет")
            print(f"8) Характеристики")
            print(f"9) Инвентарь")
            print(f"0) Квесты")
            choiceToBuy = input("Что хочешь приобрести: ")

            while choiceToBuy != "1":
                if choiceToBuy == "2":
                    if buy(oneHpCost):
                        hp += 1
                        printHp()
                elif choiceToBuy == "3":
                    if buy(threeHpCost):
                        hp += 3
                        printHp()
                elif choiceToBuy == "4":
                    if buy(weaponCost):
                        damage = weaponDmg
                        printDamage()
                elif choiceToBuy == "5":
                    if buy(armorСost):
                        armor = armorLvl
                        printArmor()
                elif choiceToBuy == "8":
                    printParameters()
                elif choiceToBuy == "9":
                    printInventory()
                elif choiceToBuy == "0":
                    printQuests()
                else:
                    print("Я такое не продаю.")
                choiceToBuy = input("Что хочешь приобрести: ")
        if choiceToEnter == "2":
            break
        elif choiceToEnter == "8":
            printParameters()
        elif choiceToEnter == "9":
            printInventory()
        elif choiceToEnter == "0":
            printQuests()
        choiceToEnter = input("Перед тобой торговец 1) Посмотреть товары 2) Уйти 8) Характеристики 9) Инвентарь 0) Квесты: ").lower()

def monsterHit(dmg):
    global hp
    global armor
    global dexterity
    monsterHitTry = r.randint(1, 10)
    if monsterHitTry > dexterity and dmg > armor:
        hp -= (dmg - armor)
        print("Монстр атаковал и у тебя осталось", hp, "жизней.")
    elif monsterHitTry <= dexterity:
        print("Монстр атаковал, но ты увернулся! У тебя осталось", hp, "жизней.")
    elif dmg <= armor:
        print("Монстр атаковал, но ты заблокировал весь уровен! У тебя осталось", hp, "жизней.")

def playerHit(mHp, mEvasion, mArmor):
    global damage
    playerHitTry = r.randint(1, 10)
    if playerHitTry > mEvasion and damage > mArmor:
        mHp -= (damage - mArmor)
        print("Ты атаковал монстра и у него осталось", mHp, "жизней.")
    elif playerHitTry <= mEvasion:
        print("Ты атаковал монстра, но он увернулся! У него осталось", mHp, "жизней.")
    elif damage <= mArmor:
        print("Ты атаковал монстра, но не смог пробить его броню! Нужно оружие помощнее. У него осталось", mHp,
              "жизней.")
    return mHp

def meetMonster():
    global hp
    global gold
    monsterLvl = r.randint(1, 3)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsterEvasion = monsterLvl
    monsterArmor = monsterLvl - 1
    monsters = ["Жопошник", "Кракозябрь", "Поцык", "КозакЪ"]
    monsterRarities = ["Дырявый", "чОткий", "Старый", "Дипломированный"] #aazemskov# добавил им "редкости"
    monsterRarity = monsterRarities[r.randint(1, 4) - 1] #aazemskov# ну и рандомная редкость
    monster = r.choice(monsters)
    print(f"Ты набрел на монстра - {monsterRarity} {monster}, у него {monsterLvl} уровень, {monsterHp} жизней, {monsterDmg} урона и {monsterArmor} брони.")
    printParameters()

    while monsterHp > 0:
        choice = input("Что будешь делать? 1) Атака 2) Убежать 8) Характеристики 9) Инвентарь 0) Квесты: ").lower()

        if choice == "1":
            monsterHp = playerHit(monsterHp, monsterEvasion, monsterArmor)
            if monsterHp > 0:
                monsterHit(monsterDmg)
        elif choice == "2":
            chance = r.randint(0, monsterLvl)
            if chance == 0:
                print("Тебе удалось сбежать с поля боя!")
                break
            else:
                print("Монстр оказался чересчур сильным и догнал тебя...")
                monsterHit(monsterDmg)
        elif choice == "8":
            printParameters()
        elif choice == "9":
            printInventory()
        elif choice == "0":
            printQuests()
        else:
            continue

        if monsterHp > 0:
            monsterHit = r.randint(1, 10)
            if monsterHit > dexterity:
                hp -= monsterDmg
                print("Монстр атаковал и у тебя осталось", hp, "жизней.")
            elif monsterHit <= dexterity:
                print("Монстр атаковал, но ты увернулся! У тебя осталось", hp, "жизней.")
        if hp <= 0:
            break
    else:
        loot = r.randint(0, 2) + monsterLvl
        gold += loot
        print("Тебе удалось одолеть монстра, за что ты получил", loot, "монет.")
        printgold()

def meetNothing():
    print(""" - Здесь холодно и грустно, путник. Поговори со мной...
 - Кто здесь???""")
    choice = input("Любая клавиша - продолжить. 8) Характеристики 9) Инвентарь 0) Квесты: ")
    while choice == "8" or choice == "9" or choice=="0":
        if choice == "8":
            printParameters()
        if choice == "9":
            printInventory()
        if choice == "0":
            printQuests()
        choice = input("Любая клавиша - продолжить. 8) Характеристики 9) Инвентарь 0) Квесты: ")

def initGame(initHp, initgold, initDamage, initDext, initArmor):
    global hp
    global gold
    global damage
    global dexterity
    global armor

    hp = initHp
    gold = initgold
    damage = initDamage
    dexterity = initDext
    armor = initArmor

    print("Ты отправился в странствие навстречу приключениям и опасностям. Удачного путешествия!")
    printParameters()


def gameLoop():
    situation = r.randint(0, 10)
    if situation == 0:
        meetShop()
    elif situation == 1:
        meetMonster()
    else:
        meetNothing()


initGame(3, 500, 1, 1, 1)

while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала (да/нет): ").lower() == "да":
            initGame(3, 500, 1, 1, 1)
        else:
            break