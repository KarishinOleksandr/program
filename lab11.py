set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.intersection(set2)
print(set3)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

def zmina(set1, set2):
    set11 = set1.difference(set2)
    set22 = set2.difference(set1)
    set3 = set11.union(set22)
    return print(set3)

zmina(set1, set2)

A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}

С= (A | B) - (A & B)

print(С)

list1 = [1, 2, 3, 4, 5, 6] 
list2 = [4, 5, 6, 7, 8] 

def jabka(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    list11 = list2.difference(list1)
    list12 = list1.difference(list2)
    list33 = sorted(list2.difference(list1))

    return print("Missing values in list1 = ",list11), print("Additional values in list1 = ",list12), print("Missing values in list2 = ",list12), print("Additional values in list2 = ",list33)

jabka(list1, list2)

def qwe(set1, set2):
    return len(set1.intersection(set2)) == 0

a = {23, 8, 56, 45, 78}
b = {42, 26, 55, 87}
z = {46, 87}

print("Compare A and B:", qwe(a, b))
print("Compare B and Z:", qwe(b, z))
print("Compare A and Z:", qwe(a, z))

nuzh = 1
verh = 50

user_inp = int(input("Введіть число: "))
if nuzh <= user_inp <= verh:
    print("The Number is Within a Range...")
elif user_inp < nuzh:
    print("Your Number is Low...")
else:
    print("Your Number is High...")

def golosni (inputt):
    gg = set("aeiouAEIOU")
    count = 0

    for char in inputt:
        if char in gg:
            count = count + 1

    return count

inputt = input("Enter a string: ")
result = golosni(inputt)
print("Number of vowels: ", result)