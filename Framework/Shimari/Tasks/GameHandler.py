import discord
from Framework.Shimari.Core import BucketType
from Framework.Shimari.Class.BASE import Base
from Framework.Shimari.Class.AI import AI
from Framework.Shimari.Class.Fight import Evaluator


class GameHandler(Evaluator):
    def __init__(self, client: discord.Client, *Participants):
        super().__init__(Participants)
        self.client = client
        self.Reactions = ["🛡️", "1️⃣", "2️⃣", "3️⃣", "4️⃣"]
        self.Failure = "🚫"

    def __del__(self):
        retr = {}

        for Shi in self.BASE:
            Protocol = Shi.Protocol.EditedProtocol
            retr[Shi.Tuple()] = {"Type": type(Shi), "Protocol": {"Length": len(Protocol), "Protocol": Protocol}}
        return print(retr)

    def __check(self, Message):
        return lambda message: message.author == self.Current and message == Message

    async def reactor(self, message: discord.Message):
        boolean = False
        Information = None
        while boolean is False:
            try:
                reaction, user = self.client.wait_for("reaction_add", check=self.__check(message), timeout=120)
            except:
                self.Disqualify(self.Current)
                boolean = True
            if str(reaction.emoji) not in self.Reactions:
                await message.remove_reaction(reaction.emoji, user)
            else:
                Information = self.Current.Attr(str(reaction.emoji))
                boolean = True
        return Information




ai = AI((3015, 2), BucketType.Difficulty.Easy)
s1 = Base((7747, 3))
s2 = Base((8673, 4))
g = GameHandler("", s1, s2, ai)

g.Fight(0)
g.Fight(3)
g.Fight(2)
g.Fight(3)
