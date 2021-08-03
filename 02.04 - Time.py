h1 = int(input("Please put in the hour of the first time : "))
m1 = int(input("Please put in the minutes of the first time : "))
s1 = int(input("Please put in the seconds of the first time : "))

t1 = s1 + (m1 * 60) + (h1 * 60 *60)

print(h1, " : " , m1 , " and " , s1 , " seconds are in seconds since midnight : " , t1 , "\n")


h2 = int(input("Please put in the hour of the second time : "))
m2 = int(input("Please put in the minutes of the second time : "))
s2 = int(input("Please put in the seconds of the second time : "))

t2 = s2 + (m2 * 60) + (h2 * 60 *60)

print(h2, " : " , m2 , " and " , s2 , " seconds are in seconds since midnight : " , t2 , "\n")

print("The difference between the two times is: \n")
print(h2 - h1 , " hours, " , m2 - m1 , " minutes and " , s2 - s1 , " seconds.")