# opinion.py
# This file defines the Person class for modeling opinion dynamics, but it's currently broken. Try to identify the problems. When you've identified the problem, test out a fix.

import random

#----- BEGIN Person Class -----#

class Person:
  def __init__(self, opinion):
    self.opinion = opinion  #float in [0,1]
    self.friends = [] #list of Person objects, representing the people i like

  """
  A method for extending the friend list to include a given list of Person objects.
  Parameters: new_friends - a list of Person objects
  """
  def befriend(self,new_friends):
    self.friends.extend(new_friends)


  """
  A method for updating my opinion to be the average opinion of myself and all of my friends.
  TODO: The method below is missing four "self."s on its variables. Figure out where they need to go.
  """
  def update(self):
    total = opinion
    for friend in friends:
      total += friend.opinion
    opinion = total/(len(friends)+1)

#----- END Person Class -----#

"""
A function for updating a random Person from a list of Person objects.
Parameters: people_list - a list of People objects
TODO: The function below contains an error. Figure out where it is using the test code below.
"""
def update_step(people_list):
  i = random.randrange(len(people_list))
  people_list[i].update(self)


"""
We'll use this main function to test out our Person class and experiment with the update_step() function.
"""
def main():
  pass
  ## Test for update() - Write your own test code here:


  ## Test for update_step(): the following code should print three lines of numbers. What do they represent?
  # pop = [Person(0),Person(1),Person(0)]
  # pop[0].befriend([pop[1],pop[2]])
  # pop[1].befriend([pop[2]])
  # pop[2].befriend([pop[0]])

  # for i in range(10):
  #   update_step(pop)

  # for i in range(3):
  #   print(i,pop[i].opinion)

main()