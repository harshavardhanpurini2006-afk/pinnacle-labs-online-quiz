
print("Welcome to Online Quiz Platform")

name = input("Enter your name: ")
print("Hello", name)
print("Let's start the quiz!")

score = 0

# Question 1
print("\nQuestion 1:")
print("Which language are we using?")
print("1. Java")
print("2. Python")
print("3. C++")
print("4. HTML")

while True:
    answer = input("Enter your answer (1-4): ")

    if answer == "2":
        print("Correct Answer!")
        score += 1
        break

    elif answer in ["1", "3", "4"]:
        print("Wrong Answer! Try again.")

    else:
        print("Invalid Input! Enter 1 to 4.")


while True:
    answer = input("Enter your answer (1-4): ")

    if answer == "1":
        print("Correct Answer!")
        score += 1
        break

    elif answer in ["2", "3", "4"]:
        print("Wrong Answer! Try again.")

    else:
        print("Invalid Input! Enter 1 to 4.")

while True:
    answer = input("Enter your answer (1-4): ")

    if answer == "1":
        print("Correct Answer!")
        score += 1
        break

    elif answer in ["2", "3", "4"]:
        print("Wrong Answer! Try again.")

    else:
        print("Invalid Input! Enter 1 to 4.")
# Final Result
print("\nQuiz Completed!")
print("Your Score:", score, "/ 3")

percentage = (score / 3) * 100
print("Percentage:", round(percentage, 2), "%")
if percentage >= 80:
    print("Grade: A")

elif percentage >= 60:
    print("Grade: B")

elif percentage >= 40:
    print("Grade: C")

else:
    print("Grade: Fail")
