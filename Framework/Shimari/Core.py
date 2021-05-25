class YAMLError(Exception):
    def __init__(self, Argument):
        self.Argument = Argument


class ShimariError(Exception):
    def __init__(self, Argument):
        self.Argument = Argument


class BucketError(Exception):
    def __init__(self, Argument):
        self.Argument = Argument


class ConstructorError(Exception):
    def __init__(self, original, error):
        self.error = error
        self.error.original = original


class BucketMap:
    def __init__(self, Size: int, Overwrite: bool = False):
        self.__Storage = []
        self.Overwrite = Overwrite
        self.__Size = Size
        self.__Last = 0

        if Size < 1:
            raise ConstructorError(AttributeError, "You need to create at least 1 Bucket!")
        if Size > 2056:
            raise ConstructorError(AttributeError, "You cannot create more than 2056 Buckets!")
        if not Size % 2 == 0:
            raise ConstructorError(AttributeError, "Your Bucket number needs to be even!")
        for i in range(Size):
            self.__Storage.append([])

    def ADD(self, *Item):
        if self.__Last <= self.__Size - 1:
            for obj in Item:
                self.__Storage[self.__Last].append(obj)
            self.__Last += 1
            return
        if self.Overwrite is True:
            self.__Last = 0
            self.__Storage[self.__Last] = {"OVERWRITTEN": []}
            for obj in Item:
                self.__Storage[self.__Last]["OVERWRITTEN"].append(obj)
            self.__Last += 1
            return
        raise AttributeError("Bucket is full!")

    def FIND(self, Item=None, Index=None):
        if Item:
            for i, obj in enumerate(self.__Storage):
                if obj[0] == Item:
                    return i, obj
            raise AttributeError("Item not in Buckets!")
        if Index:
            try:
                return Index, self.__Storage[Index]
            except:
                raise AttributeError("Index not in Buckets!")

    def DEL(self, Index):
        try:
            del self.__Storage[Index]
        except:
            raise AttributeError("Index not in Buckets!")

    def GROW(self, NewSize: int):
        if NewSize <= self.__Size:
            raise ValueError("Size is smaller than before!")

        diff = NewSize - self.__Size
        self.__Size = NewSize
        for _ in range(diff):
            self.__Storage.append([])

    def __RemoveEmpty(self):
        newStorage = [obj for obj in self.__Storage if obj]
        self.__Storage = newStorage
        self.__Size = len(self.__Storage)
        self.__Last = len(self.__Storage) - 1
        return self.__Storage

    def __PrintEmpty(self):
        newStorage = [obj for obj in self.__Storage if obj]
        return newStorage

    @property
    def FullProtocol(self):
        return self.__Storage

    @property
    def EditedProtocol(self):
        return self.__PrintEmpty()


class BucketType:
    class List:
        pass

    class Unpack:
        pass

    class Config:
        pass

    class Difficulty:

        class Easy:
            pass

        class Normal:
            pass

        class Hard:
            pass
