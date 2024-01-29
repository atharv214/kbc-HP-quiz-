print("Welcome to KBC(HP Quiz)","\nLet's Start the game")
question = ["What is the name of the wife of Harry Potter?\na) Hermione Granger b) Ginny Weasly\nc) Luna Lovegood d) Cho ",
            "What is the name of the pet owl of Harry Potter?\na) Hedwig b) Scabbers\nc) Bassilik d) Pigwidgeon ",
            "What is the name of the 6th movie of Harry Potter Series?\na) HP and the Half blood prince b) HP and the Philospher stone\nc) HP and the Chamber of Secrets d) HP and the Deathly Hallows",
            "Who is the Author of Harry Potter Book Series?\na)Ruskin Bond b) J.K. Rowling \nc) Munshi Premchand d) Chetan Bhagat",
            "Who was the lover of Jinny Potter?\na) Severus Snape b) Dumbledore\nc) Cedric Diogre d) Tom Riddle"
            ]
answers = ["b",
           "a",
           "a",
           "b",
           "a"]

print("Instructions:\nWirte 'a' for option a\nWirte 'b' for option b\nWirte 'c' for option c\nWirte 'd' for option d")

amount = 0
permit = input("do you want to start(y/n): ")
permit = permit.lower()
if (permit[0]=='y'):
    for i in range(len(question)):
        print(question[i])
        userAnswer = input("Give answer: ")
        if userAnswer==answers[i]:
            amount = amount+1000
            print("congratulations You have Won",amount)
        else:
            print("Sorry To Say But You Lost The Game",amount," Rupees will be Credit")
            break
        
        
        
if (permit[0]=='n'):
    print("oops, i will wait for next time")


