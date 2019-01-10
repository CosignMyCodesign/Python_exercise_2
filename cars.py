# 1. Create an empty set named showroom.
showroom = set()
# 2. Add four of your favorite car model names to the set.
showroom.add("Rubicon") 
showroom.add("Camaro") 
showroom.add("Wrangler")
showroom.add("E320")
print(showroom)
# 3. Print the length of your set.
print("showroom's length =", len(showroom))
# 4. Pick one of the items in your show room and add it to the set again.
showroom.add("Rubicon")
# 5. Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)
# 6. Using update(), add two more car models to your showroom with another set.
showroom.update({"Corvette", "Supra"})
print(showroom)
# 7. You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("Corvette")
print(showroom)

# 1. Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached      you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the         same as in the showroom set.
junkyard = {"civic", "pilot", "monte-carlo", "Camaro", "Wrangler"}
# 2. Use the intersection method to see which cars exist in both the showroom and that junkyard.
print(showroom.intersection(junkyard))
# 3. Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
print("Showroom U Junkyard", showroom.union(junkyard))
# 4. Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.
showroom.discard("civic")
print("take out civic", showroom)