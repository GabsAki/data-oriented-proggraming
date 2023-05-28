# Example using dataclasses

from dataclasses import dataclass, asdict

@dataclass
class AuthorData:
    """Class for keeping track of an author in the system"""
    first_name: str
    last_name: str
    n_books: str


def calculate_name(first_name:str, last_name:str):
    return f"{first_name} {last_name}"

def is_prolific(n_books: int):
    return n_books > 100

# 'Isaac Asimov'
author_data = AuthorData("Isaac", "Asimov", 500)
print("Printing the output of the calculate_name function:")
print(calculate_name(author_data.first_name, author_data.last_name))

@dataclass(frozen=True)
class UserData:
    """Class for keeping track of a user in the system"""
    first_name: str
    last_name: str
    email: str

# 'John Doe'
user_data = UserData("John", "Doe", "john.doe@gmail.com")
print("\nPrinting the output of the calculate_name function with UserData class:")
print(calculate_name(user_data.first_name, user_data.last_name))

assert calculate_name("Isaac", "Asimov") == "Isaac Asimov"

author_dict = asdict(author_data)

print("\nPrinting the output of dict operations:")
# {'first_name': 'Isaac', 'last_name': 'Asimov', 'n_books': 500}
print("Original dict:")
print(author_dict)

# Access dict values
# 'Isaac'
print("\nGetting attribute `first_name`:")
print(author_dict.get("first_name"))


# Add new field to dict
# {'first_name': 'Isaac', 'last_name': 'Asimov', 'n_books': 500, 'alive': False}
author_dict["alive"] = False
print("\nAdding new field `alive`:")
print(author_dict)

# Update existing field.
# {'first_name': 'Isaac', 'last_name': 'Asimov', 'n_books': 703, 'alive': False}
print("\nChanging the attribute `n_books`:")
author_dict["n_books"] = 703
print(author_dict)

# Dataclass can be changed
print("\nPrinting changes being done to dataclass:")
print(author_data)
author_data.first_name = "Yuri"
print(author_data)

# But with the frozen attribute it becomes immutable
print("\nTrying to change dataclass with frozen attribute:")
print(user_data)
try:
    user_data.first_name = "Yuri"
except:
    print("Could not alter dataclass")
print(user_data)
