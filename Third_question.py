class1 = int(input("הכנס את מספר התלמידים בכיתה 1: "))
class2 = int(input("הכנס את מספר התלמידים בכיתה 2: "))
class3 = int(input("הכנס את מספר התלמידים בכיתה 3: "))
class4 = int(input("הכנס את מספר התלמידים בכיתה 4: "))

total_students = class1 + class2 + class3 + class4
average_students_per_class = total_students / 4
cost_per_student = 45
total_cost = total_students * cost_per_student

print(f"סך כל התלמידים המשתתפים בפעילות: {total_students}")
print(f"ממוצע התלמידים בכל כיתה: {average_students_per_class:.2f}")
print(f"עלות הפעלת הפרויקט למשרד החינוך: {total_cost} ₪")

