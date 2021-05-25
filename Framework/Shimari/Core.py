class BucketMap:
    def __init__(self, Size: int, Overwrite: bool = False):
        self.__Storage = []
        self.Overwrite = Overwrite
        self.__Size = Size
        self.__Last = 0

        if Size < 1 or Size > 2056 or Size % 2 != 0:
            raise AttributeError("Buckets exceed Size limit or Bucket Number is odd!")
        for i in range(Size):
            self.__Storage.append([])

    def ADD(self, *Item):
        if self.__Last <= self.__Size - 1:
            for obj in Item:
                self.__Storage[self.__Last].append(obj)
            self.__Last += 1
            return
        elif self.Overwrite is True:
            self.__Last = 0
            for obj in Item:
                self.__Storage[self.__Last].append(obj)
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


class YAMLError(Exception):
    def __init__(self, Argument):
        self.Argument = Argument


class ShimariError(Exception):
    def __init__(self, Argument):
        self.Argument = Argument


class BucketError(Exception):
    def __init__(self, Argument):
        self.Argument = Argument


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
