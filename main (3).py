# Define the base class Player
class Player:
  def play(self):
      print(" The playing cricket.")

# Define the derived class Batsmam
class Batsman(Player):
  def play(self):
      print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(Player):
  def play(self):
      print("The bowler is bowling.")

# create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call the play() method for each object 
batsman.play()
bowler.play()

  