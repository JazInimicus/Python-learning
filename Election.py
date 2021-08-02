total = int(input("How many votes were there in total? : "))
first = int(input("How many voted for the first candidat? : "))
second = int(input("How many voted for the second candidat? : "))

third = total - first - second

print("The third candidat had ", third, " votes then.")

p1 = (first / total) * 100
p2 = (second / total) * 100
p3 = (third / total) * 100

print("Candidate 1 got ", p1 , "% of the votes")
print("Candidate 2 got ", p2 , "% of the votes")
print("Candidate 3 got ", p3 , "% of the votes")