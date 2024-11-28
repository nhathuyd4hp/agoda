class Hotel:
    def __init__(self, id, name, description, address, location):
        self.id = id
        self.name = name
        self.description = description
        self.address = address
        self.url = ""
        self.location = location
        

    def __str__(self) -> str:
        return f"id: {self.id}\nname: {self.name}\ndescription: {self.description}\naddress: {self.address}\nurl: {self.url}\nlocation: {self.location}"
