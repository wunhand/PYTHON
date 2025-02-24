statement_1 = "I will go to the park"
statement_2 = statement_1.replace("park", "school")
print(statement_2)

statement_3 = "I found the golden goblet."
statement_find = statement_3.find("goblet")
print(statement_find)

name = "David"
number_arms = 2
number_legs = 2
statement_4 = name, "has", str(number_arms), "arms and", str(number_legs), "legs."
print(statement_4)

name = "David"
number_arms = 2
number_legs = 2
statement_5 = name + " has " + str(number_arms) + " arms and " + str(number_legs) + " legs."
print(statement_5)

name = "David"
number_arms = 2
number_legs = 2
statement_6 = f"{name} has {number_arms} arms and {number_legs} legs."
print(statement_6)

name = "David"
number_arms = 2
number_legs = 2
statement_7 = "{} has {} arms and {} legs.".format(name, number_arms, number_legs)
print(statement_7)

name = "David"
number_arms = 2
number_legs = 2
statement_8 = "{0} has {1} arms and {2} legs.".format(name, number_arms, number_legs)
print(statement_8)

name = "David"
number_arms = 2
number_legs = 2
statement_9 = "{0} has {2} arms and {1} legs.".format(name, number_arms, number_legs)
print(statement_9)

name = "David"
number_arms = 2
number_legs = 2
statement_10 = f"{name} has {number_arms+number_legs} arms and legs together."
print(statement_10)

statement_11 = "{name} has {num_arms} arms and {num_legs} legs.".format(name="David", num_arms=2, num_legs=2)
print(statement_11)