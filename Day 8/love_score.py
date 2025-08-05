def calculate_love_score(name1, name2):
    count_T = 0
    count_F= 0
    combained_name = (name1 + name2).lower()
    for char in combained_name:
        if char in "true":
            count_T +=1
        if char in "love":
            count_F +=1
    print(f"Your Love Score = {count_T}{count_F}")

name1 = input("Enter Your Name: ")
name2 = input("Enter Your Partner Name: ")

calculate_love_score(name1,name2)