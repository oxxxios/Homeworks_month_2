class Mers:
   def __init__(self, title, model, weight, hp, nm, max_speed, color):
      self.title = title
      self.model = model
      self.weight = weight
      self.hp = hp
      self.nm = nm
      self.max = max_speed
      self.color = color

      def start_engine(self):
         print(f"{self.title} {self.model}")

      def stop_engine (self):
         print(f"{self.title} {self.model} stop engine")

      def info(self):
         print(f"title:{self.title}\n"
               f"model:{self.model}\n"
               f"weight:{self.weight}\n"
               f"hp:{self.hp}\n"
               f"nm:{self.nm}\n"
               f"max speed:{self.max}\n"
               f"color:{self.color}\n")

      Mers1 = Mers('Mers', 'idk', 300, 550, 600, 130, "red")
      Mers1.start_engine()
      Mers1.stop_engine()
      Mers1.info()