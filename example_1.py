# Example using regular classes

class Address:
    def __init__(
            self, 
            street_num: int, 
            street_name:str, 
            city:str, 
            state:str, 
            zip_code: int
        ):
        self.street_num = street_num
        self.street_name = street_name
        self.city = city
        self.state = state
        self.zip_code = zip_code


# Note: `n_books = None` makes the attribute optional
class Author:
    def __init__(
            self, 
            first_name: str, 
            last_name: str, 
            address: Address,
            n_books: int = None
        ):
        self.first_name = first_name
        self.last_name = last_name
        self.n_books = n_books
        self.address = address

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def is_prolific(self):
        return self.n_books > 100
        

address = Address(651, "Essex Street", "Brooklyn", "NY", 11208)
author = Author("Isaac", "Asimov", address)

assert author.full_name == "Isaac Asimov"
