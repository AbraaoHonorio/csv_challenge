class Legislator:

    def __init__(self, id: int, name: str):
        self.id = int(id)
        self.name = name

    def __repr__(self):
        return f"Legislators({self.id!r}, {self.name!r})"