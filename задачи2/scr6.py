class Airline:
    def __init__(self):
        self.aircraft_list = []
        self.route_list = []
    
    def add_aircraft(self, aircraft):
        self.aircraft_list.append(aircraft)
    
    def remove_aircraft(self, aircraft):
        if aircraft in self.aircraft_list:
            self.aircraft_list.remove(aircraft)
    
    def create_route(self, route):
        self.route_list.append(route)
    
    def delete_route(self, route):
        if route in self.route_list:
            self.route_list.remove(route)
    
    def find_aircraft_by_model(self, model):
        return [aircraft for aircraft in self.aircraft_list if aircraft.model == model]
    
    def find_routes_by_city(self, city):
        return [route for route in self.route_list if city in (route.departure, route.destination)]

class Aircraft:
    def __init__(self, model, capacity, registration_number):
        self.model = model
        self.capacity = capacity
        self.registration_number = registration_number
    
    def __str__(self):
        return f"{self.model} (рег. номер: {self.registration_number}, мест: {self.capacity})"


class Route:
    def __init__(self, departure, destination, flight_number, aircraft):
        self.departure = departure
        self.destination = destination
        self.flight_number = flight_number
        self.aircraft = aircraft
    
    def __str__(self):
        return f"Рейс {self.flight_number}: {self.departure} -> {self.destination} ({self.aircraft.model})"

if __name__ == "__main__":
    airline = Airline()
    
    aircraft1 = Aircraft("Boeing 737", 180, "RA-73651")
    aircraft2 = Aircraft("Airbus A320", 150, "RA-32001")
    aircraft3 = Aircraft("Boeing 777", 300, "RA-77712")
    
    airline.add_aircraft(aircraft1)
    airline.add_aircraft(aircraft2)
    airline.add_aircraft(aircraft3)
    
    route1 = Route("Москва", "Санкт-Петербург", "SU-100", aircraft1)
    route2 = Route("Санкт-Петербург", "Сочи", "SU-200", aircraft2)
    route3 = Route("Москва", "Сочи", "SU-300", aircraft3)
    route4 = Route("Сочи", "Москва", "SU-301", aircraft3)
    
    airline.create_route(route1)
    airline.create_route(route2)
    airline.create_route(route3)
    airline.create_route(route4)
    
    print("Самолеты в авиакомпании:")
    for aircraft in airline.aircraft_list:
        print(f"- {aircraft}")
    
    print("\nМаршруты авиакомпании:")
    for route in airline.route_list:
        print(f"- {route}")
    
    print("\nПоиск самолетов Boeing 737:")
    boeing_737s = airline.find_aircraft_by_model("Boeing 737")
    for aircraft in boeing_737s:
        print(f"- {aircraft}")
    
    print("\nМаршруты из/в Сочи:")
    sochi_routes = airline.find_routes_by_city("Сочи")
    for route in sochi_routes:
        print(f"- {route}")

    airline.delete_route(route2)
    airline.remove_aircraft(aircraft2)
    
    print("\nПосле удаления:")
    print(f"Самолеты: {len(airline.aircraft_list)}")
    print(f"Маршруты: {len(airline.route_list)}")