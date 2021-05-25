import random
from Framework.Shimari.Class.BASE import Base
from Framework.Shimari.Core import BucketType, BucketError, ConstructorError


class AI(Base):
    """AI is used to create a Non-Player entity by inheriting from Base, using BucketType.Difficulty and an Overwrite bool for the BucketMap Protocol."""
    def __init__(self, X: tuple, Difficulty, Opponent: Base = None, Overwrite: bool = False):
        super().__init__(X, Overwrite=Overwrite)

        if type(Difficulty()) in [BucketType.Difficulty.Easy, BucketType.Difficulty.Normal, BucketType.Difficulty.Hard]:
            self.Difficulty = Difficulty

            if Opponent is None and isinstance(Difficulty(), BucketType.Difficulty.Hard):
                raise ConstructorError(AttributeError, "Opponent is a required argument for this BucketType!")
            self.__Opponent = Opponent
            return
        raise BucketError("Invalid BucketType")

    def BUCKET(self, Type):
        if type(Type()) not in [BucketType.Difficulty.Easy, BucketType.Difficulty.Normal, BucketType.Difficulty.Hard]:
            raise BucketError("Invalid BucketType")
        self.Difficulty = Type

    def ACRQfight(self):
        if isinstance(self.Difficulty(), BucketType.Difficulty.Easy):
            i = random.randint(0, 3)
            self.Protocol.ADD("ACRQfight", BucketType.Difficulty.Easy.__name__,
                              {"Type": i, "Hp": self.Hp, "Animus": self.Animus})
            return i

        elif isinstance(self.Difficulty(), BucketType.Difficulty.Normal):
            if self.Hp < self.Data.Hp / 3:
                if random.randint(1, 10) < 6:
                    retr = 0
                else:
                    retr = random.randint(1, 2)
            elif self.Animus >= 40:
                retr = 3
            elif self.Animus <= 25:
                retr = random.randint(1, 2)
            elif self.Animus <= 10:
                retr = 1
            else:
                retr = random.randint(0, 2)

            self.Protocol.ADD("ACRQfight", BucketType.Difficulty.Normal.__name__,
                              {"Type": retr, "Hp": self.Hp, "Animus": self.Animus})
            return retr

        elif isinstance(self.Difficulty(), BucketType.Difficulty.Hard):
            if self.__Opponent.LastAttr == "Shield":
                retr = 1
            elif self.Hp <= self.Data.Hp / 3 or self.Hp - 15 <= self.Data.Hp / 3:
                if random.randint(1, 10) < 6:
                    retr = 0
                else:
                    retr = random.randint(1, 2)
            elif self.Animus >= 30:
                retr = 3
            elif self.Animus <= 20:
                if random.randint(1, 10) <= 9:
                    retr = 0
                else:
                    retr = random.randint(1, 3)
            else:
                retr = random.randint(0, 2)

            self.Protocol.ADD("ACRQfight", BucketType.Difficulty.Hard.__name__,
                              {"Type": retr, "Hp": self.Hp, "Animus": self.Animus})
            return retr
