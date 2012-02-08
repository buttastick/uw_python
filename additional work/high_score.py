highest_score = 0
scores = {}

result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores[score] = name
    
result_f.close()

for score, name in scores.items():
    print name + " had a score of " + score + "."
    
#scores.sort() -- when scores was a list, not a dictionary [] vs. {}
#scores.reverse()
#print ("The highest score was: ")
#print (highest_score)

print ("\n")

for each_score in sorted(scores.keys(), reverse = True):
    print ("Surfer " + scores[each_score] + " scored " + each_score + ".")
