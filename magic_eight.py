
def request_question():
    question = input("What is your question? ")
    return question

in_progress = True
while in_progress == True:
    question = request_question()
    if question == "quit":
        in_progress = False
    elif question[-1] != "?":
        print("I'm sorry, I can only answer questions.)
