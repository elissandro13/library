class Price:
    def get_charge(self, days_rented: int) -> float:
        raise NotImplementedError

    def get_frequent_renter_points(self, days_rented: int) -> int:
        return 1  # padrão: 1 ponto para quase todos os casos

class RegulaPrice(Price):
    pass

class NewReleasePrice(Price):
    pass

class ChildrenPrice(Price):
    pass

class Book:

    REGULAR: int = 0
    NEW_RELEASE: int = 1
    CHILDREN: int = 2

    def __init__(self, title: str, price_code: int):
        self.title = title
        self.set_price_code(price_code)

    def set_price_code(self, price_code: int):
        if price_code == Book.REGULAR:
            self.price = RegularPrice()
        elif price_code == Book.NEW_RELEASE:
            self.price = NewReleasePrice()
        elif price_code == Book.CHILDREN:
            self.price = ChildrenPrice()
        else:
            raise ValueError("Invalid price code")

    def get_charge(self, days_rented: int) -> float:
        return self.price.get_charge(days_rented)

    def get_frequent_renter_points(self, days_rented: int) -> int:
        return self.price.get_frequent_renter_points(days_rented)

class Rental:
    def __init__(self, book: Book, days_rented: int):
        self.book = book
        self.days_rented = days_rented


   

    def get_charge(self) -> float:                
        return self.book.get_charge(self.days_rented)


    def get_frequent_renter_points(self) -> int:
        return self.book.get_frequent_renter_points(self.days_rented)

class Client:

    def __init__(self, name: str):
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)
    
    

    def statement(self) -> str:

        total_amount = 0
        frequent_renter_points = 0
        result = f"Rental summary for {self.name}\n"
        
        for rental in self.rentals:
            amount = rental.get_charge()

            # add frequent renter points
            frequent_renter_points += rental.get_frequent_renter_points()

            # show each rental result
            result += f"- {rental.book.title}: {amount}\n"
            total_amount += amount
        
        # show total result
        result += f"Total: {total_amount}\n"
        result += f"Points: {frequent_renter_points}"
        return result