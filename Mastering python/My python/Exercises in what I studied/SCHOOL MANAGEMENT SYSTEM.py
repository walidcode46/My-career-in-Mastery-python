# ==========================================================
# PROJECT: SCHOOL MANAGEMENT SYSTEM (LEVEL 1)
# ==========================================================

# --- المرحلة 1: المعلومات الأساسية (Variables & Strings) ---
# 1. عرف متغيرات للسمية (First Name)، الكنية (Last Name)، والسن (Age).
# 2. جمعهم فمتغير واحد سميتو full_name.
# 3. طبع full_name بحروف كبار (UPPERCASE).
# 4. طبع عدد الحروف اللي فـ full_name.


# --- المرحلة 2: القرارات (Conditions & Logical Operators) ---
# 1. دير شرط If/Else: يلا كان السن >= 18 طبع "Adult"، يلا كان صغر طبع "Minor".
# 2. دير شرط بـ 'and': يلا كان السن بين 15 و 18، طبع "Eligible for CS Club".


# --- المرحلة 3: تسيير البيانات (Lists & Loops) ---
# 1. صاوب List سميتها grades فيها 5 ديال النقط (مثلا: 14, 16, 10, 19, 11).
# 2. دير For Loop كدور على هاد النقط وتطبع كل وحدة بوحدها.
# 3. وسط Loop، حسب المجموع (Total) ديال النقط كاملين.
# 4. مورا الـ Loop، حسب المعدل (Average) وطبع النتيجة.


# --- المرحلة 4: التنظيم (Functions) ---
# 1. حول كود حساب المعدل لـ Function سميتها calculate_avg كتاخد List وترجع رقم.
# 2. صاوب Function تانية سميتها greet_user كتاخد السمية وترجع رسالة ترحيب.

# --- المرحلة 5: الترتيب (Algorithms - Bubble Sort) ---
# 1. استعمل الخوارزمية ديال Bubble Sort باش ترتب الـ List ديال النقط (grades).
# 2. طبع النقط مرتبين من الصغير للكبير.

# ========================================================== 

print("==========================================================")
print("==== PROJECT: SCHOOL MANAGEMENT SYSTEM (LEVEL 1) =========")
print("==========================================================\n")

print("-----------------------------------------------------------") 

first_Name = input("What is your Name : ")
Last_Name  = input("What is your Last Name : ")
Level       = input("What is your Level : ")

print("-----------------------------------------------------------")
Full_Name =f" Your Name is {first_Name.upper()}\n Your Lanst Name is {Last_Name.upper()}\n Your Age is {Level.upper()}"
print(Full_Name) 

print("-----------------------------------------------------------")

User = float(input("How Old Are You ?\n > "))

if User >= 18 :
    print("You Are in Adult") 
elif User <= 15 :
    print("You Are in Minor") 
else:
    print("Eligible for CS Club") 

grades = [10, 15, 20, 17, 18, 19]
total = 0 
min_grade = grades[0]
print("-----------------------------------------------------------")

print("Students' grades :")
for index in range(len(grades)):
    print(f"> {grades[index]}")

print("-----------------------------------------------------------")

print("Total student grades :")
for T in grades:
    total = total + T
print(f"> {total} ") 
    
print("-----------------------------------------------------------")

print("Greater Justice :")  
for min in grades:
    if min > min_grade:
        min_grade = min

print(f"> {min_grade}")

print("-----------------------------------------------------------") 

print("Lesser Justice : ") 
for min2 in grades:
    if min2 < min_grade:
        min_grade = min2

print(f"> {min_grade}") 

print("-----------------------------------------------------------")  
