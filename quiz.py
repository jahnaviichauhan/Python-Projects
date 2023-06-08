
name = input("What's your name? \n")
print(" ")
print("Hey "+ name + " !")
print("Welcome! This allows you to check your knowledge in the four main subject of elementary school. Select any one of the four numbers to opt for the subject and perform quiz of the same.")

print(" 1 : English")
print(" 2 : Mathematics")
print(" 3 : Science")
print(" 4 : Social Studies")
print("Choose any number from 1 to 4 to choose subject :")
n=int(input(""))
a=0
if n==1:
    print("Welcome to the english section of the quiz. Here you will be answering 5 questions based on english grammar.")
    
    print("Question 1 : ")
    print("""
    Identify the part of speech for the underlined word:
    Her sister is the oldest member of the g\u0332r\u0332o\u0332u\u0332p\u0332.
    A. Pronoun
    B. Noun
    C. Adjective
    D. Adverb""")
    ans=input("")
    if ans=='B' or ans=='b' or ans=='2':
        print("Correct! Great work! :)")
        a=a+1
    else:
        print("Wrong answr :(")
    
    print("Question 2 : ")
    print('''Which word is a proper noun?
    A. Country
    B. Nepal
    C. Boy
    D. Table''')
    ans=input("")
    if ans=='B' or ans=='b' or ans=='2':
        print("Correct! Great work! :)")
        a=a+1
    else:
        print("Wrong answr :(")
        
        print("Question 3 : ")
    print('''What is the collective noun for a group of whales?
    A. Pod
    B. Disco
    C. Group
    D. Hump back''')
    ans=input("")
    if ans=='A' or ans=='a' or ans=='1':
        print("Correct! Great work! :)")
        a=a+1
    else:
        print("Wrong answr :(")
        
        print("Question 4 : ")
    print('''Which word is an abstract noun?
    A. Disappointment
    B. Art
    C. Chair
    D. Gorilla''')
    ans=input("")
    if ans=='A' or ans=='a' or ans=='1':
        print("Correct! Great work! :)")
        a=a+1
    else:
        print("Wrong answr :(")
        
        print("Question 5 : ")
    print('''We generally form adverbs by adding to the verbs
    A. By
    B. Ing
    C. Ous
    D. Er''')
    ans=input("")
    if ans=='A' or ans=='a' or ans=='1':
        print("Correct! Great work! :)")
        a=a+1
    else:
        print("Wrong answr :(")
        
        print("Your score : " + a +"/5")
        print("Thank you for attempting this quiz. :)")
        
elif n==2:
    print("Welcome to the mathematics section of the quiz. Here you will be answering 5 questions based on mathematics.")
    
    
    print("Question 1 : ")
    print("""158=___ + 106. What number will come in the blank to make the number sentence correct?
    A. 52
    B. 152
    C. 158
    D. 264""")
    ans=input("")
    if ans=='A' or ans=='a' or ans=='1':
        print("Correct! Great work! :)")
        a=a+1
    else:
        print("Wrong answr :(")
        
    print("Question 2 : ")
    print('''The simplest form of 16/24 is: 
    A. 3/5
    B. 2/3
    C. 2/5
    D. 1/3''')
    ans=input("")
    if ans=='B' or ans=='b' or ans=='2':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
        print("Question 3 : ")
    print('''Gaurav has 918 marbles. He wants to make packets of marbles, with nine marbles in each pack. How many packs will he be able to make?
    A. 12
    B. 102
    C. 120
    D. 1062''')
    ans=input("")
    if ans=='B' or ans=='b' or ans=='2':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
        print("Question 4 : ")
    print('''Which of these lies between 6.3 and 6.6?   
A. 6.2
B. 6.9
C. 6.05
D. 6.41''')
    ans=input("")
    if ans=='D' or ans=='d' or ans=='4':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
        print("Question 5 : ")
    print(''' A teacher brought some toffees to her class. After giving three toffees each to 15 students who had completed their assignments, she has 60 toffees left with her. How many toffees did she bring to the class?
A. 15
B. 45
C.78
D. 105
''')
    ans=input("")
    if ans=='A' or ans=='a' or ans=='1':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
        print("Your score : " + a +"/5")
        print("Thank you for attempting this quiz. :)")
        
elif n==3:
    print("Welcome to the science section of the quiz. Here you will be answering 5 questions based on science.")
    print("Question 1 : ")
    print(""" 
The SI unit of speed is:
A. M/s
B. Cm/kg
C. Km/h
D. V/A""")
    ans=input("")
    if ans=='A' or ans=='a' or ans=='1':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
    print("Question 2 : ")
    print('''The process by which plants make their food is called:
A. Transpiration
B. Photosynthesis
C. Translocation
D. Perspiration''')
    ans=input("")
    if ans=='B' or ans=='b' or ans=='2':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
        print("Question 3 : ")
    print('''The solar cell receives energy from...
A. Sunlight
B. Artificial light
C. Earth
D. Moon''')
    ans=input("")
    if ans=='A' or ans=='a' or ans=='1':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
        print("Question 4 : ")
    print('''There are ... planets in our solar system.
A. 7
B. 8
C. 9
D. 11''')
    ans=input("")
    if ans=='B' or ans=='b' or ans=='2':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
        print("Question 5 : ")
    print(''' The moon is a:
A. Satellite
B. Plant
C. Round
D. Glowing object
''')
    ans=input("")
    if ans=='A' or ans=='a' or ans=='1':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
        print("Your score : " + a +"/5")
        print("Thank you for attempting this quiz. :)")
        
     
        
elif n==4:
    print("Welcome to the social studies section of the quiz. Here you will be answering 5 questions based on social studies.")
    print("Question 1 : ")
    print(""" 
Largest ocean in world
A. Arctic Ocean
B. Indian Ocean
C. Pacific Ocean
D. Atlantic Ocean""")
    ans=input("")
    if ans=='C' or ans=='c' or ans=='3':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
    print("Question 2 : ")
    print('''Which planet is also morning and evening star?
A. Venus
B. Mar
C. Mercury
D. Jupiter''')
    ans=input("")
    if ans=='A' or ans=='a' or ans=='1':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
        print("Question 3 : ")
    print('''Which planet is the biggest?
A. Saturn
B. Uranus
C. Jupiter
D. Mars''')
    ans=input("")
    if ans=='C' or ans=='c' or ans=='3':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
        print("Question 4 : ")
    print('''What is a map?
A. Globe
B. Drawing of the earth’s surface on a flat paper according to scale
C. Projection
D. None of these''')
    ans=input("")
    if ans=='B' or ans=='b' or ans=='2':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
        print("Question 5 : ")
    print(''' For what purpose magnetic compass is used?
A. For measuring distance
B. For showing symbols
C. For finding the directions
D. For all of these
''')
    ans=input("")
    if ans=='C' or ans=='c' or ans=='3':
        print("Correct! Great work! :)")
        a+=1
    else:
        print("Wrong answr :(")
        
        print("Your score : " + a +"/5")
        print("Thank you for attempting this quiz. :)")
     
        
    
    
   
        
    
        
    
else:
    print("This is an invalid input. Input any number from 1 to 4. Thank you.")
        
    
    
