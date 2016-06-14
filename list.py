#list
import os

colleague = ["Jerry", "Jeffery","Victor","Annie"]
print colleague
print colleague[0]
print colleague[1]
print colleague[2]
print colleague[3]

colleague.append ("Asa")
print colleague

colleague.pop()
print colleague

colleague.pop(1)
print colleague

colleague.insert(1,"Jack")
print colleague

colleague[1] = "Aike"
print colleague

L = [x*x for x in range(1,11,2)]
print L

file = [d for d in os.listdir('.')]
print file