#dict and set

performance = {"Jeffery":"A", "Jerry":"B","Jack":"C"}
print "Jerry's performance is:",performance["Jerry"]

performance["Woody"] = "A+"
print "Woody's performance is:",performance["Woody"]

print "Is Annie in performance list? ", "Anni" in performance

# performance.pop("Woody")
# print performance["Woody"]

colleague = set(["Annie","Jerry","Jeffery"])
print colleague

colleague.add("Victor")
print colleague

s = set([1, 1, 2, 2, 3, 3])
print s