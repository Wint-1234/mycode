#!/usr/bin/env python3

# Modules
import html

# trivia dictionary
trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

# Code for question
def main():
    
    # Retrieve values from trivia and remove weird data
    question = trivia["question"]
    a = html.unescape(trivia["correct_answer"])
    b = html.unescape(trivia["incorrect_answers"][0])
    c = html.unescape(trivia["incorrect_answers"][1])
    d = html.unescape(trivia["incorrect_answers"][2])

    # Print question/answers
    print("")
    print(question)
    print("\tA: " + a)
    print("\tB: " + b)
    print("\tC: " + c)
    print("\tD: " + d)
    
    # Gather answer from user and format 
    answer = input("\nEnter a letter as your response (A, B, C, D)\n>")
    answer = answer.lower()
    
    # Check answer and provide feedback
    if answer == "a": 
        print("You guessed right!")
    else: 
        print("You guessed wrong, better luck next time.")
        
# Run main         
if __name__ == "__main__":
    main()
