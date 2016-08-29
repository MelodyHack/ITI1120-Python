
#Course: ITI 1120

import random   
def perform_test(MultAdd, n):
     '''(int, int)-> (string) depends on if the answer is correct or not
         This function takes a number of questions the user wants to be tested on
         and takes another number to see if the user wants to be tested either on
         addition or multiplication and in the end it returns a string depending on:
         if you get less than 60%, between 60% and 80%, or over 80%
         Precontion: MultAdd must be 0 or 1
                     n must be a positive integer number 
     '''
     score =0
     for i in range(n):
          m1 = random.randint(1,9)
          m2 = random.randint(1,9)
          if MultAdd ==0:
               Answer = m1 + m2
               UserAnswer = int(input(str(m1)+" + "+str(m2)+" = "))
               if UserAnswer == Answer:
                    score += 1
               else:
                    print("Incorect - the answer is ",m1+m2)

          elif MultAdd ==1:
               Answer = m1 * m2
               UserAnswer = int(input(str(m1)+" * "+str(m2)+" = "))

               if UserAnswer == Answer:
                    score =score+1
               else:
                    print("Incorect - the answer is ",m1*m2)

     return score


n = int(input("Welcome to addition / multiplication test\n \nHow many questions would you like to be tested on?\nEnter a non negative integer for the answer:")) 

if n== 0:
     print("Good. Bye.")
else:
     print("This software tests you with",n,"questions .....")
     MultAdd = int(input("0) Addition\n1)Multiplication\nPlease make a selection (0 or 1):"))                         
     x= perform_test(MultAdd,n)
     ScorePercent = ((x/ n)*100)
     if ScorePercent <60:
          print("Please study more and ask your teacher for help")
     elif ScorePercent >= 60 and ScorePercent < 80:
          print("Not too bad but please study and practice some more")  
     elif ScorePercent >= 80:
          print("Well done! Congratulations")
 
 
