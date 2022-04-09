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
    self.seen_items = []

  def __str__(self):
    watching_time = 0
    seen_titles = []
    for item in self.seen_items:
      watching_time += item.get_total_time()
      seen_titles.append(item.title)
    if watching_time > 60:
      hours = watching_time //60
      minutes = watching_time % 60
      time = str(hours) + " hod " + str(minutes) + " min"
    else:
      time = str(watching_time) + " min"
    return f"Uživatel(ka): {self.user_name}\nCelkový čas sledování: {time} \nZhlédnuté tituly: {seen_titles}\n================" 

  def add_seen_item(self, item):
    self.seen_items.append(item)
    return f"Uživatel(ka): {self.user_name} viděl(a): {item.title} Čas sledování: {item.get_total_time()} min\n================\n" + self.__str__()  
    

troja = Movie("Troja", "historický", 157)
friends = Serial("Friends", "sitcom", 240, 22)
titanic = Movie("Titanic", "drama, romantický", 194)
chandler = User("Chandler")
helena = User("Helena")

print(helena.add_seen_item(titanic))
print(chandler.add_seen_item(friends))
print(helena.add_seen_item(troja))
print(chandler.add_seen_item(troja))

