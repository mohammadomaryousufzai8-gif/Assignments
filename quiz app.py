print("-"*38)
# INTERDUCTION:
print(" IN THE NAME OF ALLAH ")
print("Instructor: MR.GHARANAI")
print("Prepared by: MOHAMMAD OMAR YOUSUFZAI ")
print("Welcome to the simplest python quiz!!!")
print("-"*38)
# QUESTIONS:
print("number1: who is the richest man in the world?")
print("a) Elon Musk")
print("b) Bil gates")
print("c) Wren Buffet")
print("d) None")
score=0
ANSWER= input("numberYour answer (a)(b)(c)(d): ")
if ANSWER.lower()=="a":
    print("you are correct! Excellent go ahead ")
    score=+1
else:
    print("Wrong! The correct answer is 'a' ")
  
print(f"your final score: {score} out of 3 ")
print("-"*38)
print("number2: who is the owner of the TESLA?")
print("a) Elon ")
print("b) Bil-gates")
print("c) Elon Musk")
print("d) a is correct")
ANSWER=input("numberYour answer (a)(b)(c)(d): ")
if ANSWER.lower()=="c":
    print("you are correct! appreciate")
    score=score+1
    print(f"your final score: {score} out of 3 ")
else:
    print("Wrong! The correct answer is 'c' ")
  
print("-"*38)
print("number3: who invent the electricity?")
print("a) Nicola Tesla")
print("b) Edison")
print("c) I don't know")
print("d) Charles Babbage")
ANSWER=input("numberYour answer (a)(b)(c)(d): ")
if ANSWER.lower()=="b":
    print("you are correct! Well done ")
    score=score+1
else:
    print("Wrong! The correct answer is 'b' ")
  
print(f"your final score: {score} out of 3 ")
print("-"*38)
# FINAL RESULT
print(" FINAL RESULT:")
if (score==3):
    print("excellent")
elif (score==2):
    print("good")
elif (score==1):
    print("not bad")
else:
    print("you are a failer!!!")
  