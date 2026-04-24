class HashTable:
    def __init__(self) -> None:
        self.collection = {}

    def hash(self, value: str) -> int:
        return sum([ord(c) for c in value])

    def add(self, key: str, value) -> None:
        hash_value = hash(key)

        if hash_value in self.collection:
            self.collection[hash_value][key] = value
        else:
            self.collection[hash_value] = value

    def remove():
        pass

    def lookup():
        pass
