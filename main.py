import random as r
import sqlite3 as sql

# Пока ни для чего не используется, просто база с двумя таблицами
dbConnection = sql.connect("gamedata.db")
dbCursor = dbConnection.cursor()
sql_create_inventory_table = """ CREATE TABLE IF NOT EXISTS inventory (
                                    id integer PRIMARY KEY,
                                    item_name text NOT NULL,
                                    item_type text,
                                    quantity integer
                                ); """
sql_create_quests_table = """ CREATE TABLE IF NOT EXISTS quests (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    goal text
                                ); """
dbCursor.execute(sql_create_inventory_table)
dbCursor.execute(sql_create_quests_table)


hp = 0
coins = 0
damage = 0
dexterity = 0 # Параметра уклонения пока нет. Уклонение считается просто от ловкости
armor = 0 # Пока не применяется в бою

def printParameters():
    print("У тебя {0} жизней, {1} урона и {2} монет. Твоя ловкость {3} и у тебя {4} брони".format(hp, damage, coins, dexterity, armor))


def printHp():
    print("У тебя", hp, "жизней.")


def printCoins():
    print("У тебя", coins, "монет.")


def printDamage():
    print("У тебя", damage, "урона.")

def printArmor():
    print("У тебя", armor, "брони.")


def meetShop():
    global hp
    global damage
    global coins
    global armor

    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            printCoins()
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

    while input("Что ты будешь делать (зайти/уйти): ").lower() == "зайти":
        print("1) Одна единица здоровья -", oneHpCost, "монет;")
        print("2) Три единицы здоровья -", threeHpCost, "монет;")
        print("3) {0} {1} - {2} монет".format(weaponRarity, weapon, weaponCost))
        print("4) {0} - {1} монет".format(armorInStock, armorСost))

        choice = input("Что хочешь приобрести: ")
        if choice == "1":
            if buy(oneHpCost):
                hp += 1
                printHp()
        elif choice == "2":
            if buy(threeHpCost):
                hp += 3
                printHp()
        elif choice == "3":
            if buy(weaponCost):
                damage = weaponDmg
                printDamage()
        elif choice == "4":
            if buy(armorСost):
                armor = armorLvl
                printArmor()
        else:
            print("Я такое не продаю.")


def meetMonster():
    global hp
    global coins

    monsterLvl = r.randint(1, 3)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsterEvasion = monsterLvl
    monsterArmor = monsterLvl
    monsters = ["Grock", "Clop", "Cholop", "Madrock", "Lilbitch"]

    monster = r.choice(monsters)

    print(
        "Ты набрел на монстра - {0}, у него {1} уровень, {2} жизней и {3} урона.".format(monster, monsterLvl, monsterHp,
                                                                                         monsterDmg))
    printParameters()

    while monsterHp > 0:
        choice = input("Что будешь делать (атака/бег): ").lower()

        if choice == "атака":
            playerHit = r.randint(1, 10)
            if playerHit > monsterEvasion:
                monsterHp -= damage
                print("Ты атаковал монстра и у него осталось", monsterHp, "жизней.")
            elif playerHit <= monsterEvasion:
                print("Ты атаковал монстра, но он увернулся! У него осталось", monsterHp, "жизней.")
        elif choice == "бег":
            chance = r.randint(0, monsterLvl)
            runawayHit = r.randint(1, 10)
            if chance == 0:
                print("Тебе удалось сбежать с поля боя!")
                break
            else:
                print("Монстр оказался чересчур сильным и догнал тебя...")
                if runawayHit < dexterity:
                    print("... Но тебе удалось увернуться от его последнего удара!")
                    break
        else:
            continue

        if monsterHp > 0:
            monterHit = r.randint(1, 10)
            if monterHit > dexterity:
                hp -= monsterDmg
                print("Монстр атаковал и у тебя осталось", hp, "жизней.")
            elif monterHit <= dexterity:
                print("Монстр атаковал, но ты увернулся! У тебя осталось", hp, "жизней.")
        if hp <= 0:
            break
    else:
        loot = r.randint(0, 2) + monsterLvl
        coins += loot
        print("Тебе удалось одолеть монстра, за что ты получил", loot, "монет.")
        printCoins()


def initGame(initHp, initCoins, initDamage, initDext, initArmor):
    global hp
    global coins
    global damage
    global dexterity
    global armor

    hp = initHp
    coins = initCoins
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
        input("Блуждаем...")


initGame(3, 500, 1, 1, 0)

while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала (да/нет): ").lower() == "да":
            initGame(3, 500, 1, 1, 0)
        else:
            break