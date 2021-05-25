import discord
from Framework.Shimari.Core import BucketType
from Framework.Shimari.Class.BASE import Base
from Framework.Shimari.Class.AI import AI
from Framework.Shimari.Class.Fight import Evaluator


class GameHandler(Evaluator):
    """Used for Handling the Evaluator by inheriting from it -- Can comprehend with an infinite amount of Participants, but only one AI is advised."""
    def __init__(self, client: discord.Client, Participants: list[tuple[discord.Member, Base]]):
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
        return lambda message: message.author == self.CurrUser and message == Message

    async def reactor(self, message: discord.Message):
        boolean = False
        Information = None
        while boolean is False:
            try:
                reaction, user = self.client.wait_for("reaction_add", check=self.__check(message), timeout=120)
            except:
                self.Disqualify(self.CurrBASE)
                boolean = True
            if str(reaction.emoji) not in self.Reactions:
                await message.remove_reaction(reaction.emoji, user)
            else:
                Information = self.CurrBASE.Attr(str(reaction.emoji))
                boolean = True
        return Information




ai = AI((3015, 2), Difficulty=BucketType.Difficulty.Easy, Overwrite=True)
s1 = Base((7747, 3), True)
s2 = Base((8673, 4), True)
g = GameHandler("", [("", s1), ("", s2), (None, ai)])

g.Fight(0)
g.Fight(3)
g.Fight(2)
g.Fight(3)
g.Fight(0)
g.Fight(3)
g.Fight(2)
g.Fight(3)
g.Fight(0)
g.Fight(3)
g.Fight(2)
g.Fight(3)
