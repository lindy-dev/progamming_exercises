name = "Shreyas Rao" 
age = 30 # not a lie
height = 183 # in cm
weight = 82.7 # in kg
eyes = "Brown" 
teeth = "White"
hair = "Black"

print(f"Let's talk about {name}.")
print(f"He's {height} cms tall.")
print(f"He's {weight} kgs heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.") 

# try more format characters 
my_greeting = "Hello,\t"
my_first_name = "Shreyas"
my_last_name = "Rao"
my_age = 24
# Print all the info 
print("%r my name is %s %s, and I am %d years old" % (my_greeting, my_first_name, my_last_name, my_age))

# Try to write some variables that convert the centimeters and kilograms to inches and pounds 
centimeters_per_inch = 1/2.54
kilo_per_pound = 1/0.4535

print(f"He's is %f inches tall." % (height* centimeters_per_inch))
print("He's %f kilos heavy." % (weight * kilo_per_pound))
