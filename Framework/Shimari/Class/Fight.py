import random
import discord
from Framework.Shimari.Class.BASE import Base, BucketType
from Framework.Shimari.Class.AI import AI
from Framework.Shimari.Tasks.DataHandler import YAML


class Evaluator:
    def __init__(self, BASE: list[tuple[discord.Member, Base]]):
        self.BASE = []
        self.USER = []
        for obj in BASE:
            self.BASE.append(obj[1])
            self.USER.append(obj[0])
        self.CurrentPlayer = 0
        self.__YAML = YAML(BucketType.Config)

    @property
    def CurrBASE(self):
        return self.BASE[self.CurrentPlayer]

    @property
    def CurrUser(self):
        if not isinstance(self.USER[self.CurrentPlayer], AI):
            return self.USER[self.CurrentPlayer]
        return None

    @staticmethod
    def __Diff(Animus: int, Type: int):
        if Type in [1, 2, 3, 4]:
            diff = round(Animus * YAML(BucketType.Config).GET()["Fight"]["Subtract"][Type - 1])
            while diff > 55:
                diff -= random.randint(1, 6)
        else:
            diff = round(Animus * YAML(BucketType.Config).GET()["Fight"]["Block"])
        return diff

    def Disqualify(self, Player: Base):
        try:
            i = self.BASE.index(Player)
            del self.BASE[i]
            del self.USER[i]
        except:
            raise AttributeError("Invalid Player!")

    def Animus(self):
        for X in self.BASE:
            X.Animus += random.randint(self.__YAML.GET()["Fight"]["Animus"][0], self.__YAML.GET()["Fight"]["Animus"][1])

    def Fight(self, Attack: [0, 1, 2, 3, 4]):
        Attacker = self.BASE[self.CurrentPlayer]
        self.CurrentPlayer += 1
        if self.CurrentPlayer > len(self.BASE) - 1:
            self.CurrentPlayer = 0
        Defender = self.BASE[self.CurrentPlayer]
        Attacker.Protocol.ADD("Fight", {"Operator": type(Attacker), "Type": Attack, "Hp": Attacker.Hp, "Animus": Attacker.Animus})

        if Attack == 0:
            diff = self.__Diff(Attacker.Animus, Attack)
            Attacker.Animus -= diff
            Attacker.LastAttr = "Shield"
            return "Schild!"

        if Attack in [1, 2, 3]:
            diff = self.__Diff(Attacker.Animus, Attack)
            Attacker.Animus -= diff
            Attacker.LastAttr = f"{Attack}"
            data = YAML(BucketType.Config).GET()
            data = data["Fight"]["Elements"]
            bonus = data["Res"] if Attacker.Damage == Defender.Resistance else data[Attacker.Rarity]
            Damage = round(diff * 1.1 + bonus)
            if Defender.LastAttr == "Shield":
                return "Geblockt!"
            if random.randint(1, 10) == 1:
                return "Ausgewichen!"
            Defender.Hp -= Damage
            return Damage

        if Attack == 4:
            raise ValueError("Function not yet implemented!")
