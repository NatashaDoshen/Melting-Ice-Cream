  def __init__(self):
    super().__init__() # current step - add init
    self.scoops = 0

  def eat(self, scoops):
    if self.scoops < scoops:
      print("Not enough bites left!")
    else:
      self.scoops -= scoops

  def add(self, scoops):
    self.scoops += scoops
    if self.scoops > self.max_scoops:
      print("Too many scoops! Dropped ice cream.")
      self.scoops = 0


class IceCreamTruck:

  def __init__(self):
    super().__init__() # current step - add init
    self.sold = 0

  def order(self, scoops):
    ice_cream = IceCream()
    self.add(ice_cream, scoops)
    return ice_cream

  def add(self, ice_cream, scoops):
    ice_cream.add(scoops)
    self.sold += scoops


class DeluxeIceCreamTruck(IceCreamTruck):

  def order(self, scoops):
    ice_cream = super().order(scoops)
    ice_cream.add(1)
    return ice_cream


class Drinkable():

  def __init__(self):
    self.cups = 0

  def add(self, cups):
    self.cups +=cups

  def drink(self, cups):
    self.cups -=cups

class Lemonade(Drinkable):
  pass
  
class MeltingIceCream(IceCream, Drinkable):
   def elapse(self,t):
    melted = min(t, self.scoops)
    self.scoops -= melted
    self.cups += melted
    
