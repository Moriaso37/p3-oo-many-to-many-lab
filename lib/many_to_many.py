class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        # Return contracts related to this book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Return unique authors related to this book via contracts
        return list({contract.author for contract in self.contracts()})



class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # Return list of contracts related to this author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Return list of books via contracts
        return list({contract.book for contract in self.contracts()})  # use set to avoid duplicates

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not (isinstance(royalties, int) or isinstance(royalties, float)):
            raise Exception("royalties must be a number")
        # Create and return new Contract
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Sum royalties across all contracts
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not (isinstance(royalties, int) or isinstance(royalties, float)):
            raise Exception("royalties must be a number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        return [contract for contract in cls.all if contract.date == date]
