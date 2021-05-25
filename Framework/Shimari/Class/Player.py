from Framework.Shimari.Class.BASE import Base


class Player(Base):
    def __init__(self, X: tuple):
        super().__init__(X)
        self.__Attacking = ["🛡️", "1️⃣", "2️⃣", "3️⃣", "4️⃣"]

    @staticmethod
    def __CheckAttr(Type: int):
        if Type not in [0, 1, 2, 3, 4]:
            raise AttributeError("Attr not a registered Value!")
        return True

    def Attr(self, Reaction: str):
        i = self.__Attacking.index(Reaction)
        if self.__CheckAttr(i):
            return i
        raise AttributeError("Attr not a registered Value!")

    def POSTdata(self):
        text = f"```yaml\n" \
               f"Animus: {self.Animus}\n" \
               f"Leben: {self.Hp}\n" \
               f"Schaden: 1 = 5%, 2 = 15%, 3 = 35%\n" \
               f"```"
        return text

    def AFTERdata(self, Damage: str):
        text = f"```yaml\n" \
               f"Leben: {self.Hp}\n" \
               f"Animus: {self.Animus}\n" \
               f"Schaden: {Damage}\n" \
               f"```"
        return text
