from abc import ABC, abstractmethod

class Item(ABC):
  @abstractmethod
  def __init__(self, title, genre):
    self.title = title
    self.genre = genre

  def __str__(self):
    return f"Název: {self.title} \nŽánr: {self.genre} "

  def get_total_time(self):
    pass

class Movie (Item):

  def __init__(self, title, genre, time):
    super().__init__(title, genre)
    self.time = time
  
  def __str__(self):
    return super().__str__() + f"\nDélka: {self.time} min\n================"

  def get_total_time(self):
    return self.time

class Serial (Item):

  def __init__(self, title, genre, number_episodes, episode_time):
    super().__init__(title, genre)
    self.number_episodes = number_episodes
    self.episode_time = episode_time
    
  def __str__(self):
    return super().__str__() + f"\nPočet epizod: {self.number_episodes} \nDélka epizody: {self.episode_time} min\n================"
  
  def get_total_time(self):
    total_time = self.number_episodes * self.episode_time
    return total_time

class User:

  def __init__(self, user_name):
    self.user_name = user_name
    self.watching_time = 0
    self.seen_items = []

  def __str__(self):
    if self.watching_time > 60:
      hours = self.watching_time //60
      minutes = self.watching_time % 60
      time = str(hours) + " hod " + str(minutes) + " min"
    else:
      time = str(self.watching_time) + " min"
    return f"Uživatel: {self.user_name}\nCelkový čas sledování: {time} \nZhlédnuté tituly: {self.seen_items}\n================" 

  def add_seen_items(self, time, title):
    seen_items = ""
    seen_items += title
    self.seen_items.append(seen_items)
    self.watching_time += time
    return self.watching_time   
    
def seen_item (user: User, item: Item):
  time = item.get_total_time()
  user.add_seen_items(time, item.title)
  

troja = Movie("Troja", "historický", 157)
print(troja)
friends = Serial("Friends", "sitcom", 240, 22)
print(friends)
titanic = Movie("Titanic", "drama, romantický", 194)
print(titanic)
chandler = User("Chandler")
helena = User("Helena")
print(chandler)
print(helena)


seen_item(helena, titanic)
print(helena)
seen_item(helena, friends)
print(helena)
seen_item(helena, troja)
print(helena)
seen_item(chandler, troja)
print(chandler)

