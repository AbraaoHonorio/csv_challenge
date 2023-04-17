class Bill:
    def __init__(self, id, title, sponsor_id):
        self.id = id
        self.title = title
        self.sponsor_id = sponsor_id

    def __repr__(self):
        return f"Bills({self.id!r}, {self.title!r}, {self.sponsor_id!r})"