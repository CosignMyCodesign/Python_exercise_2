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