#!/usr/bin/env python3

# Age percentages for person categories - 
# senior = 80-100%, adult = 64-79%, young adult = 48-63%, teenager = 32-47%, kid = 16-31%, baby = 0-15%
baby = 0
kid = 16
teenager = 32
young_adult = 48
adult = 64
senior = 80

# Messages that correspond with age category
baby_message = "You are a BABY at heart! You have a long way to go!"
kid_message = "You are still a KID! BTW, do you have any homework?"
teenager_message = "Embrace it, You are a TEENAGER!"
young_adult_message = "You are a YOUNG ADULT! Adulting can be challenging. Hang in there!"
adult_message = "Congrats, You are an ADULT! You clearly know what you're doing."
senior_message = "You are a SENIOR! You clearly got this life thing figured out."

# Quiz welcome message
welcome_message = """\nWelcome to \"How much of an adult are you\" quiz!
    This quiz will tell you how much an adult you really are based on 35 questions.
    Enter \"Done\" at any point if you would like to be evaluated based on current responses.\n\n"""

# Message to try again
try_again_message = "Please enter a valid response to the question --> Enter \"Yes\", \"No\", or \"Done\"\n\t>"

# Valid answers list
valid_answers = ["Yes", "No", "Done"]

# quiz questions put into a list
quiz_questions = [
  "Do you know how to do your own laundry?",
  "Can you cook at least three different recipes?",
  "Do you know where your phone, keys, and wallet are at this exact moment?",
  "Do you know how to change a tire?",
  "Do you have enough clean underwear right now to last at least three days?",
  "Do you set your own dentist appointments?",
  "Do you go to the dentist every six months?",
  "Do you floss every day?",
  "Do you set your own doctor's appointments?",
  "Is your phone screen currently not cracked?",
  "Is your house or apartment insured?",
  "Do you eat at least some vegetables every day?",
  "Do you arrive to school or work on time most days?",
  "Do you arrive to social events, like brunches or weddings, on time?",
  "Do you wash your dirty dishes or put them in the dishwasher right after you use them?",
  "Do you have at least one wedding- or job interview-appropriate outfit in your closet?",
  "Do you pay for your own cellphone plan?",
  "Do you pay for your own Netflix?",
  "Do you pay for your own flights?",
  "Do you pay for your own regular bills and utilities?",
  "Do you have at least one plant in the house that you've kept alive for more than six months?",
  "Do you have at least one pet animal in your house that you've kept alive for more than six months?",
  "Do you own the proper supplies to clean your home effectively?",
  "Do you actually use those supplies to clean your home regularly?",
  "Do you own a tool set or tool box?",
  "Do you have a good idea of what you want to do with your life?",
  "Do you do your own taxes or pay a professional to do them, as opposed to asking your parents?",
  "Do you have a savings account? It still counts if it's kinda empty.",
  "Have you ever cooked a meal for more than two people before?",
  "Can you properly hang a picture?",
  "Do you regularly read the news?",
  "Do you know how to iron or steam clothes?",
  "Do you know how to make your bed?",
  "Do you wash or change your bath towel at least once a week?",
  "Do you know what a 401(k) is?"
]

# Code for question
def main():

  # Keep track of user interaction
  yes_count = 0               # Number of times user answered "yes"
  questions_answered = 0      # Number of questions the user answered
  question_number = 1         # Keep track of what # question the user is currently on


  print(welcome_message)
  
  # For loop to iterate through entire pool of questions and gather user answers
  for question in quiz_questions:
    # Gather answer from user and format it 
    answer = input(f"{question_number}. {question} (Enter \"Yes\" or \"No\")\n\t>").title()
    
    # Loop until user enters a valid answer
    while answer not in valid_answers:
      answer = input(try_again_message).title()

    # Check answer and perform action based on feedback. "No" is irrelevant
    if answer == "Yes":
      yes_count += 1
    elif answer == "Done":
      break

    questions_answered += 1         # Update running tally of questions answered
    question_number += 1            # Update current question number

  # Try to gather result and perform action if there is no mathematical error.
  try:
    percentage_result = round(round((yes_count / questions_answered) * 100))
    print("\nYour Result:\n\tYou scored " + str(percentage_result) + "% meaning..." + determineCategory(percentage_result))
  except:
    print("\nYour Result:\n\tYou must have not answered any questions...silly goose!")

  # Prompt user if they would like to run the quiz again
  try_again_answer = input("\n\n*** Try again? (Enter Enter \"Yes\", \"No\", or \"Done\") ***\n\t>").title()
  while try_again_answer not in valid_answers:
      try_again_answer = input(try_again_message).title()
  
  # Check try_again_answer and perform action based on feedback. 
  if try_again_answer == "Yes":
    main()
  else:
    print("Thanks for playing. Goodbye!\n")


# Determine which message to return based on the percentage passed-in
def determineCategory(percentage):
  if percentage >= senior:
    return senior_message
  elif percentage >= adult:
    return adult_message
  elif percentage >= young_adult:
    return young_adult_message
  elif percentage >= teenager:
    return teenager_message
  elif percentage >= kid:
    return kid_message
  else:
    return baby_message

# Run main
if __name__ == "__main__":
  main()
