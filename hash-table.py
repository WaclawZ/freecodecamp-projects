class HashTable:
    def __init__(self) -> None:
        self.collection = {}

    def hash(self, value: str) -> int:
        return sum([ord(c) for c in value])

    def add(self, key: str, value) -> None:
        hash_key = self.hash(key)

        if hash_key in self.collection:
            self.collection[hash_key][key] = value
        else:
            self.collection[hash_key] = value

    def remove(self, key: str) -> None:
        hash_key = self.hash(key)

        if hash_key in self.collection:
            del self.collection[hash_key]

    def lookup():
        pass
