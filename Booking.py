class Booking:    
    lineList = []
    def __init__(self, bookingNumber, passenger , uniqueFlight) -> None:
        self.bookingNumber = bookingNumber
        self.Passenger = passenger
        self.UniqueFlight = uniqueFlight
        
        
        
class Passenger:
    def __init__(self, passengerNumber, fName, Lname, DOB, email, mobile) -> None:
        self.passengerNumber = passengerNumber
        self.fNmame = fName
        self.lName = Lname
        self.DOB = DOB
        self.email = email
        self.moblie = mobile
        
class UniqueFlight:
    def  __init__(self, flightNumber, departs, arrives, departTime, flightlength) -> None:
        self.flightNumber = flightNumber
        self.departs = departs
        self.arrives = arrives
        self.departTime = departTime
        self.flightlength = flightlength
        
        
class LineItem:
    def __init__(self, name, descriton, price, qty, totlalPrice) -> None:
        self.name = name
        self.descriton = descriton
        self.price = price
        self.qty = qty
        self.totalPrice = totlalPrice