# bounce.py
#
# Exercise 1.5
height = 100 #first drop in meters
bounces = 1 
rebound = 3/5

while bounces < 11;
    print(bounces, height * rebound)
    bounces = bounces + 1
    height = height * rebound
print('Number of bounces', bounces)
print('Height', height)
  
