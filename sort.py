#sort
#sorted(iterable[, key][, reverse])

L = [-10, 10, 2,7,20,1,-20]
print sorted(L)
print sorted(L, reverse=True)
print sorted(L, key=abs)

colleague=["Woody","Jerry","Annie","Victor"]
print sorted(colleague)
print str.lower("AbCdEfGh")
print str.upper("AbCdEfGh")

score = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# print score[0][0]
# print score[0][1]
def by_name(x):
    return x[0]
    
def by_score(x):
    return x[1]

print sorted(score,key=by_name)
print sorted(score,key=by_score)