import yaml
from pathlib import Path
from Framework.Shimari.Core import BucketType, BucketError
import requests


class YAML:
    def __init__(self, Typ: BucketType.List or BucketType.Unpack or BucketType.Config):
        self.__Typ = Typ
        self.__Data = Path(__file__).parent / "Database/Data.yaml"
        path = Path(__file__).parent / "Database/Config.yaml"
        with path.open() as Conf:
            Config = yaml.safe_load(Conf)
        self.Config = Config
        if type(Typ()) not in [BucketType.Unpack, BucketType.List, BucketType.Config]:
            raise BucketError("Invalid BucketType")

    class __Object(object):
        pass

    def BUCKET(self, Typ: BucketType):
        self.__Typ = Typ

    def GET(self, arg: tuple or int = None):
        if isinstance(arg, tuple):
            arg1, arg2 = arg
        else:
            arg1 = arg
        if isinstance(self.__Typ(), BucketType.List):
            with open(self.__Data, "r") as File:
                container = yaml.safe_load(File)
            return container["Control"]
        if isinstance(self.__Typ(), BucketType.Unpack):
            with open(self.__Data, "r") as File:
                container = yaml.safe_load(File)
            data = container["ID"][arg1]

            o = self.__Object()
            o.Name = data["Name"]
            o.Motto = data["Motto"]
            o.Avatar = data["Avatar"]
            o.Type = data["Type"]
            data = data["KaDa"]
            o.Animus = data["Animus"]
            o.Hp = data["Hp"]
            o.Damage = data["Elements"]["Dmg"]
            o.Resistance = data["Elements"]["Res"]
            return o
        if isinstance(self.__Typ(), BucketType.Config):
            with open(self.__Data) as File:
                container = yaml.safe_load(File)
            return container["Balancing"]

    def Update(self):
        data = requests.get(self.Config["URLS"][0])

        with open(self.Config["FILES"][0], "wb") as File:
            File.write(data.content)
