'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	Calculates The Amount Of Popeyes Chicken Pieces Each Student Receives As Well As Mr. Fabroa

Author:	Lui.G

Created:	07/12/2020
------------------------------------------------------------------------------
'''
# State What The Program Is When Runned (Just Cause)
print("*----| Chicken Pieces Per Student Calculator |----*")
print("")

# Ask User For the Ammount of Students And Chicken
students = int(input("How Many Students Attended Mr. Fabroa's Class Today? "))
print("---")
# Should be more than students
chickens = int(input("How Many Popeyes Chicken Sandwiches Did Mr. Fabroa Buy? "))

# Calculate How Many Chicken Each Student Gets And How Many Popeyes Chicken Pieces Mr. Fabroa Gets
fabroa_meal = chickens % students
chicken_per_student = chickens // students

# Output The Ammount Of Chicke Pieces Per Student And Mr. Fabroa
print("")
print("|-----------------------------------------------------|")
print(" Each Student Will Receive", chicken_per_student, "Popeyes Chicken Piece(s).")
print(" While Mr. Fabroa Will Get", fabroa_meal, "Popeyes Chicken Piece(s).")
print("|-----------------------------------------------------|")