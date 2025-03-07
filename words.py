#season = input("What is your favourite season: ")

# season_list = ["summer", "winter", "autumn" , "spring", "fall"]

# if season.lower().strip() in season_list:
    # print("That is a valid season.")
# else:
    # print("That is not a valid season.")


 # My attempt
answer_list = ["Genesis", "Exodus", "Numbers", "Leviticus"]
print("Genesis", "Exodus", "Numbers", "Leviticus")  

answer = input("What is the first book of the Bible: ")
if "Genesis".lower().strip() in answer: 
        print("Correct.") 
else:
   print("Incorrect.")






book = input("What is the first book in the Bible: ")
correct = ["a", "a)", "genesis", "a) genesis"]
incorrect = ["b", "b)", "exodus", "b) exodus", "c", "c)", "numbers", "c)", "numbers", "c) numbers", "d", "d)", "leviticus", "d) leviticus"]
             
if book.lower().strip() in correct:
      print("Correct")
elif book.lower().strip() in incorrect:
      print("Incorrect")
else: 
      print("Invalid")