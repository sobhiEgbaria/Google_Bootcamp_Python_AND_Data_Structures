from CS_day_12_solutions import *

def test_shape():
    shape = Shape("Shape")
    assert shape.name == "Shape"
    assert shape.area() == 0

def test_circle():
    circle = Circle("Circle", 5)
    assert circle.name == "Circle"
    assert circle.area() == 78.54

def test_rectangle():
    rectangle = Rectangle("Rectangle", 4, 5)
    assert rectangle.name == "Rectangle"
    assert rectangle.area() == 20

def test_square():
    square = Square("Square", 4)
    assert square.name == "Square"
    assert square.area() == 16

def test_triangle():
    triangle = Triangle("Triangle", 4, 5)
    assert triangle.name == "Triangle"
    assert triangle.area() == 10



def test_vehicle():
    vehicle = Vehicle("Toyota", "Camry", 2020, 1500)
    assert vehicle.make == "Toyota"
    assert vehicle.model == "Camry"
    assert vehicle.year == 2020
    assert vehicle.weight == 1500

def test_car():
    car = Car("Toyota", "Camry", 2020, 1500, 4)
    assert car.num_doors == 4

def test_truck():
    truck = Truck("Ford", "F-150", 2020, 2000, 800)
    assert truck.payload_capacity == 800


def test_bank_account():
    account = BankAccount("12345", 1000)
    assert account.account_number == "12345"
    assert account.balance == 1000
    account.deposit(100)
    assert account.balance == 1100
    account.withdraw(200)
    assert account.balance == 900

def test_savings_account():
    savings_account = SavingsAccount("12345", 1000)
    savings_account.add_interest(10)
    assert savings_account.balance == 1100



def test_employee():
    employee = Employee("John", 5000)
    assert employee.name == "John"
    assert employee.salary == 5000
    assert employee.annual_salary() == 60000
    employee.apply_raise(10)
    assert employee.salary == 5500

def test_manager():
    manager = Manager("Sarah", 7000, 1000)
    assert manager.name == "Sarah"
    assert manager.salary == 7000
    manager.apply_raise(10)
    assert manager.salary == 8700

def test_linear_search():
    assert linear_search([1, 3, 5, 7, 9], 5) == 2
    assert linear_search([1, 3, 5, 7, 9], 2) == -1


def test_binary_search():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 2) == -1

def test_graph_node():
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node1.add_neighbor(node2)
    assert node1.value == 1
    assert node1.neighbors[0].value == 2



def run_all_tests():
    test_shape()
    print("Passed test_shape")

    test_circle()
    print("Passed test_circle")

    test_rectangle()
    print("Passed test_rectangle")

    test_square()
    print("Passed test_square")

    test_triangle()
    print("Passed test_triangle")

    test_vehicle()
    print("Passed test_vehicle")

    test_car()
    print("Passed test_car")

    test_truck()
    print("Passed test_truck")

    test_bank_account()
    print("Passed test_bank_account")

    test_savings_account()
    print("Passed test_savings_account")

    test_employee()
    print("Passed test_employee")

    test_manager()
    print("Passed test_manager")

    test_linear_search()
    print("Passed test_linear_search")

    test_binary_search()
    print("Passed test_binary_search")

    test_graph_node()
    print("Passed test_graph_node")

    print("Passed all tests!!!")

run_all_tests()

