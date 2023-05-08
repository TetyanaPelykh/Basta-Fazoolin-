#Create a Menu class
class Menu:
  #Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  #Give our Menu class a string representation method that will tell you the name of the menu. Also, indicate in this representation when the menu is available.
  def __repr__(self):
    #Try out our string representation. If you call print(brunch) it should print out something like the following: brunch menu available from 11am to 4pm
    return self.name + " esta disponible desde las " + str(self.start_time) + " hasta las " + str(self.end_time)

  #Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items, a list of the names of purchased items. Have calculate_bill return the total price of a purchase consisting of all the items in purchased_items.
  def calculate_bill(self, purchased_items):
    bill = 0 
    for purchased_item in purchased_items: 
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill
    
#Let’s create our first menu: brunch. Brunch is served from 11am to 4pm. The following items are sold during brunch:{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("Brunch", brunch_items, 11.00, 16.00)


#Let’s create our second menu item early_bird. Early-bird Dinners are served from 3pm to 6pm. The following items are available during the early-bird menu:{'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}
early_bird = Menu("Early-bird Dinners", early_bird_items, 15.00, 18.00)


#Let’s create our third menu, dinner. Dinner is served from 5pm to 11pm. The following items are available for dinner:{'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}
dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}
dinner = Menu("Dinner", dinner_items, 17.00, 23.00)


#And let’s create our last menu, kids. The kids menu is available from 11am until 9pm. The following items are available on the kids menu.{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("Kids menu", kids_items, 11.00, 21.00)

#Test out Menu.calculate_bill(). We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. Pass that into brunch.calculate_bill() and print out the price.
print(brunch.calculate_bill(["pancakes"] + ["home fries"] + ["coffee"]))

#What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan mushroom ravioli. Calculate the bill with .calculate_bill().
print(early_bird.calculate_bill(["salumeria plate"] + ["mushroom ravioli (vegan)"]))

menus = [brunch, early_bird, dinner, kids]
#create a Franchise class.
class Franchise:
  #Give the Franchise class a constructor. Take in an address, and assign it to self.address. Also take in a list of menus and assign it to self.menus.
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  #Give our Franchises a string representation so that we’ll be able to tell them apart. If we print out a Franchise it should tell us the address of the restaurant.
  def __repr__(self):
    print(self.address)
  
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)

    return available_menus
  

#Let’s create our first two franchises! Our flagship store is located at "1232 West End Road" and our new installment is located at "12 East Mulberry Street". Pass in all four menus along with these addresses to define flagship_store and new_installment.
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

#Let’s test out our .available_menus() method! Call it with 12 noon as an argument and print out the results.
print(flagship_store.available_menus(12.0))
#Let’s do another test! See what is printed if we call .available_menus() with 5pm as an argument and print out the results.
print(flagship_store.available_menus(17.0))

franchises = [flagship_store, new_installment]
#First let’s define a Business class.
class Business:
  #Give Business a constructor. A Business needs a name and a list of franchises.
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
#Let’s create our first Business. The name is "Basta Fazoolin' with my Heart" and the two franchises are flagship_store and new_installment.
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
#Before we create our new business, we’ll need a Franchise and before our Franchise we’ll need a menu. The items for our Take a’ Arepa available from 10am until 8pm are the following:{'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50} Save this to a variable called arepas_menu.
arepa_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_menu = Menu("Take a’ Arepa", arepa_items, 10.00, 20.00)
#Next let’s create our first Take a’ Arepa franchise! Our new restaurant is located at "189 Fitzgerald Avenue". Save the Franchise object to a variable called arepas_place.
arepas_place = Franchise("189 Fitzgerald Avenue", menus)
#Now let’s make our new Business! The business is called "Take a' Arepa"!
arepa = Business("Take a’ Arepa", [arepas_place])
