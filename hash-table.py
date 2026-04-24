class HashTable:
    def __init__(self) -> None:
        self.collection = {}

    def hash(self, value: str) -> int:
        return sum(ord(c) for c in value)

    def add(self, key: str, value) -> None:
        hash_key = self.hash(key)
        self.collection.setdefault(hash_key, {})[key] = value

    def remove(self, key: str) -> None:
        hash_key = self.hash(key)
        if hash_key in self.collection:
            self.collection[hash_key].pop(key, None)

    def lookup(self, key: str):
        hash_key = self.hash(key)
        return self.collection.get(hash_key, {}).get(key)
