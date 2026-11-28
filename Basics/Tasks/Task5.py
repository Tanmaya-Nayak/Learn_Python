# Q1: Join Tuples if similar initial element
#
# While working with Python tuples,
# we can have a problem in which we need to perform concatenation of records from the similarity of initial element.
# This problem can have applications in data domains such as Data Science.
#
# For eg.
#
# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)]

"""
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

test = []

for i in test_list:
    for j in range(len(test)):
        if test[j][0] == i[0]:
            test[j] = test[j] + i[1:]
            break
    else:
        test.append(i)

print(test)
"""

# Q2: Multiply Adjacent elements (both side) and take sum of right and lest side multiplication result.
#
# For eg.
#
# The original tuple : (1, 5, 7, 8, 10)
# Resultant tuple after multiplication :
#
# (1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)
#
# output-(5, 40, 91, 136, 80)

"""
I = (1, 5, 7, 8, 10)
J = ()

for i in range(len(I)):
    if i == 0:
        J = J + (I[i] * I[i + 1],)
    elif i > 0 and i < len(I) - 1:
        J = J + (I[i] * I[i - 1] + I[i] * I[i + 1],)
    elif i == len(I) - 1:
        J = J + (I[i] * I[i - 1],)
print(J)
"""

# Q3: Check is tuples are same or not?
#
# Two tuples would be same if both tuples have same element at same index
#
# t1 = (1,2,3,0)
# t2 = (0,1,2,3)
#
# t1 and t2 are not same

"""
t1 = (1, 2, 3, 0)
t2 = (0, 1, 2, 3)

T1 = len(t1)
T2 = len(t2)

if T1 != T2:
    print("t1 and t2 are not same")

else:
    Flag = True

    for i in range(T1):
        if t1[i] == t2[i]:
            continue
        else:
            Flag = False
            break

    if Flag:
        print("t1 and t2 are same")
    else:
        print("t1 and t2 are not same")
"""

# Q4: Count no of tuples, list and set from a list
#
# list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
#
# Output:
#
# List-2
# Set-2
# Tuples-1

"""
list1 = [{"hi", "bye"}, {"Geeks", "forGeeks"}, ("a", "b"), ["hi", "bye"], ["a", "b"]]
Tuples = 0
List = 0
Set = 0

for i in list1:
    if type(i) == tuple:
        Tuples += 1
    elif type(i) == list:
        List += 1
    elif type(i) == set:
        Set += 1
print("List - ", List)
print("Set - ", Set)
print("Tuples - ", Tuples)
"""
"""
for i in list1:
    if isinstance(i, tuple):
        Tuples += 1
    elif isinstance(i, list):
        List += 1
    elif isinstance(i, set):
        Set += 1
"""

# Q5: Shortlist Students for a Job role
#
# Ask user to input students record and store in tuples for each record.
# Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.
#
# Show every students record in form of tuples if matches all required criteria.
#
# It is assumed that there will be only one primry skill.
#
# If no such candidate found, print No such candidate
#
# Input:
#
# Enter No of records- 2
# Enter Details of student-1
# Enter Student name- Manohar
# Enter Higher Education- B.Tech
# Enter Primary Skill- Python
# Enter Year of Graduation- 2022
# Enter Details of student-2
# Enter Student name- Ponian
# Enter Higher Education- B.Sc.
# Enter Primary Skill- C++
# Enter Year of Graduation- 2020
#
# Enter Job Role Requirement
# Enter Skill- Python
# Enter Higher Education- B.Tech
# Enter Year of Graduation- 2022
#
# Output
#
# ('Manohar', 'B.tech', 'Python', '2022')

"""
Trecords = int(input("Enter No. of records: "))

print("Enter Job Role Requirement")
RSkill = input("Enter Skill- ")
RHighEdu = input("Enter Higher Education- ")
RYoGrad = input("Enter Year of Graduation- ")

Output = []
i = 1

while i <= Trecords:
    print("Enter Details of Student -", i)

    Sname = input("Enter Student Name- ")
    SHighEdu = input("Enter Higher Education- ")
    SPSkill = input("Enter Primary Skill- ")
    SYoGrad = input("Enter Year of Graduation- ")

    if SHighEdu == RHighEdu and SPSkill == RSkill and SYoGrad == RYoGrad:
        Student = (Sname, SHighEdu, SPSkill, SYoGrad)
        Output.append(Student)

    i += 1

if Output:
    for i in Output:
        print(i)
else:
    print("No such candidate")
"""
