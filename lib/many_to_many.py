class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list({contract.author for contract in self.contracts()})


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise ValueError("book must be an instance of Book")
        if not isinstance(date, str):
            raise ValueError("date must be a string")
        if not isinstance(royalties, int):
            raise ValueError("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date=None):
        if date:
            return [contract for contract in cls.all if contract.date == date]
        else:
            return sorted(cls.all, key=lambda contract: contract.date)

