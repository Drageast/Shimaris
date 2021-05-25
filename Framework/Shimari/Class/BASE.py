from Framework.Shimari.Core import BucketType, BucketMap, ConstructorError
from Framework.Shimari.Tasks.DataHandler import YAML
import discord


class Base:
    """Used to create a Shimari from a tuple, creates a Standardised Protocol from the BucketMap -- Base for all Shimari related Operations"""
    def __init__(self, X: tuple, Overwrite: bool = False):
        if not isinstance(X, tuple) or not len(str(X[0])) == 4:
            raise ConstructorError(AttributeError, "Constructor needs to be a tuple, consisting of ID and Rarity!")
        ID, Rarity = X
        try:
            data = YAML(BucketType.Unpack).GET(ID)
        except Exception:
            raise ConstructorError(AttributeError, "Constructor needs a valid tuple for constructing!")

        self.Protocol = BucketMap(2056, Overwrite=Overwrite)
        self.LastAttr = None
        self.ID = ID
        self.Avatar = data.Avatar
        self.Rarity = Rarity
        self.Name = data.Name
        self.Motto = data.Motto
        self.Type = data.Type
        self.Animus = data.Animus
        self.Hp = data.Hp
        self.Damage = data.Damage
        self.Resistance = data.Resistance
        self.Data = data
        self.__stats(self.Data)

        while "1" in self.Motto:
            self.Motto = self.Motto.replace("1", "ä")
        while "2" in self.Motto:
            self.Motto = self.Motto.replace("2", "ö")
        while "3" in self.Motto:
            self.Motto = self.Motto.replace("3", "ü")

    class __Farben:

        PlaceHolder = discord.Colour(0xff00ff)

        Normal = discord.Colour(0x5e5e5e)

        Selten = discord.Colour(0xac6ec)

        Legendaer = discord.Colour(0xf508e4)

        Exotisch = discord.Colour(0xf7db6b)

    def __stats(self, data):
        if self.Hp == data.Hp:
            balance = YAML(BucketType.Config).GET()
            balance = balance["Stats"]
            if self.Rarity == 1:
                stats = balance[1]
                self.Hp += stats[0]
                self.Animus += stats[1]
            if self.Rarity == 2:
                stats = balance[2]
                self.Hp += stats[0]
                self.Animus += stats[1]
            if self.Rarity == 3:
                stats = balance[3]
                self.Hp += stats[0]
                self.Animus += stats[1]
            if self.Rarity == 4:
                stats = balance[4]
                self.Hp += stats[0]
                self.Animus += stats[1]

    def GetRarity(self):
        return "Normal" if self.Rarity == 1 else ("Selten" if self.Rarity == 2 else ("Legendär" if self.Rarity == 3 else "Exotisch"))

    def COLOUR(self):
        return self.__Farben.Normal if self.Rarity == 1 else (self.__Farben.Selten if self.Rarity == 2 else (self.__Farben.Legendaer if self.Rarity == 3 else self.__Farben.Exotisch))

    def URL(self):
        return self.Avatar[self.Rarity - 1]

    def PRICE(self):
        data = YAML(BucketType.Config).GET()["Shop"]["Price"]

        return data[self.Rarity - 1]

    def __str__(self):
        __text = \
        f'```yaml\n' \
        f'Name: \n{self.Name}\n' \
        f'Motto:\n{self.Motto}\n' \
        f'Seltenheit: \n{self.GetRarity()}\n' \
        f'Legacy:\n{self.Type}\n' \
        f'\n' \
        f'Animus:\n{self.Animus}\n' \
        f'Leben:\n{self.Hp}\n' \
        f'Element:\n{self.Damage}\n' \
        f'Resistenz:\n{self.Resistance}\n' \
        f'```'
        return __text

    def Tuple(self):
        x = (self.ID, self.Rarity)
        return x
