### FlashSet ###
# By Julien Hajikhani #

import random
import time

class flashset():

    def __init__(self,dictionary={},guesses=3):
    
        if len(dictionary)<1:
            print('You must have at least 1 flashcard.')
            
        else:
            self.d=dictionary
            self.g=guesses


    def __repr__(self):
        return f'flashset({self.d})'


    def add(self,key,value):
        self.d[key]=value
        print(f'{key} was added to your flashset with a value of {value}.\n')


    def remove(self,key):

        if len(self.d)==1:
            print("Can't remove. You won't have enough flashcards.")
        else:
            del self.d[key]
            print(f'{key} was removed from your flashset.\n')


    def flip(self,key):

        if key not in list(self.d.keys()):
            print(f'A flashcard with {key} does not exist.')
            
        else:
            print(str(self.d[key]))


    def guesses(self,number):
        self.g=int(number)
        
        if number<1:
            print('Try a bigger number. The minimum number of guesses is 1.')
            
        elif number==1:
            print('HARD MODE! 1 guess per card.')
            
        else:
            print(f'{self.g} guesses per card.')


    #UNUSED TIMER FUNCTION
    def timer(self,number):

       if number<1:
            print("Give yourself a little more time than that, you're only human after all")
            
       if number>60:
           print(f"{number} seconds seems a little excessive, don't ya think? Try a minute or less.")
           
       elif number==1:
           self.t=int(number)
           print('Only 1 second per card?! Good luck!')
           
       else:
           self.t=int(number)
           print(f'You will have {number} seconds per card')

    def test(self):
        
        correct=0
        incorrect={}
        keys=list(self.d.keys())
        
        skipped={}
        skippedKeys=list(skipped.keys())

        questionNumber=0
        random.shuffle(keys)

        print('Quiz time! Press enter to skip a question or "exit" to stop the test.\n')
        
        for key in keys:
            attempts=0
            questionNumber+=1
            
            while True:
                value=input(str(questionNumber)+'. '+str(key)+': ')

                #Answer is correct
                if value==self.d[key]:
                    print('Correct!\n')
                    correct+=1
                    break

                #Exit the test
                elif value=='stop':
                    print()
                    print('Stopping the test.')
                    return

                #Skip a question
                elif value=='':
                    skipped[key]=self.d[key]
                    print('Skipped\n')
                    break

                #Answer is incorrect
                else:

                    #Out of guesses
                    if attempts+1>=self.g:
                        incorrect[key]=self.d[key]
                        print(f'Incorrect, the correct answer was {self.d[key]}.\n')
                        break

                    #Have guesses left
                    elif attempts+1<self.g:
                        attempts+=1
                        print('Try again.',self.g-attempts,'attempts left.\n')


        print()
        print('You got',correct,'out of ',len(self.d),'correct.\n')

        #100%
        if incorrect=={}:
            print('Incredible job! You got 100%')
            
        #Print incorrect
        else:
            print(f'You guessed {len(incorrect)} card(s) incorrectly:\n')

            for item in incorrect:
                print(f'{item}:{self.d[item]}\n')
        
            #If any were skipped
            if skipped!={}:
                print(f'You skipped {len(skipped)} card(s):\n')
                
                for item in skipped:
                    print(f'{item}:{self.d[item]}\n')   
            
    
        
f=flashset({'ㅂ':'q', 'ㅈ':'w', 'ㄷ':'e', 'ㄱ':'r', 'ㅅ':'t', \
              'ㅛ':'y', 'ㅕ':'u', 'ㅑ':'i', 'ㅐ':'o', 'ㅔ':'p', \
              'ㅁ':'a', 'ㄴ':'s', 'ㅇ':'d', 'ㄹ':'f', 'ㅎ':'g', \
              'ㅗ':'h', 'ㅓ':'j', 'ㅏ':'k', 'ㅣ':'l', 'ㅋ':'z', \
              'ㅌ':'x', 'ㅊ':'c', 'ㅍ':'v', 'ㅠ':'b', 'ㅜ':'n', \
              'ㅡ':'m', 'ㅃ':'Q', 'ㅉ':'W', 'ㄸ':'E', 'ㄲ':'R', \
              'ㅆ':'T', 'ㅒ':'O', 'ㅖ':'P'})

#f = flashset({'apple':'red','banana':'yellow','grapes':'green','orange':'orange', 'lemon':'yellow'})
#f.test()
