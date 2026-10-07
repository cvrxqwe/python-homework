class City:
    # Constructor (template with empty or default values)
    def __init__(self, name="", region="", country="", population=0, postal_code="", phone_code=""):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    # Method to input data from the keyboard
    def input_data(self):
        print("--- City Data Input ---")
        self.name = input("Enter city name: ")
        self.region = input("Enter region/state name: ")
        self.country = input("Enter country name: ")

        while True:
            try:
                self.population = int(input("Enter population (numbers only): "))
                if self.population < 0:
                    print("Population cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Error! You must enter an integer.")

        self.postal_code = input("Enter postal code: ")
        self.phone_code = input("Enter phone code: ")

    # Method for formatted data output
    def display_data(self):
        print("\n=== City Information ===")
        print(f"City:         {self.name}")
        print(f"Region:       {self.region}")
        print(f"Country:      {self.country}")
        print(f"Population:   {self.population} people")
        print(f"Postal Code:  {self.postal_code}")
        print(f"Phone Code:   {self.phone_code}")
        print("========================\n")

    # Additional operation 1: Updating population (e.g., after a census)
    def update_population(self, new_population):
        if new_population >= 0:
            self.population = new_population
            print(f"[Success] The population of {self.name} has been updated to {self.population} people.")
        else:
            print("[Error] Population cannot be negative.")

    # Additional operation 2: Quick retrieval of full geolocation as a string
    def get_full_location(self):
        return f"{self.name} ({self.region}, {self.country})"


# ==========================================
# Class Testing
# ==========================================

# 1. Create an empty city object
my_city = City()

# 2. Fill it with data (the program will ask for input in the console)
my_city.input_data()

# 3. Display on the screen
my_city.display_data()

# 4. Check additional methods
print(f"Short info: {my_city.get_full_location()}")
my_city.update_population(300000)