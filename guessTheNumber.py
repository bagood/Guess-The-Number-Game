class GuessingGame:

    def __init__(self): 
        """ Every game should stat with the player's score"""
        self.score = 0

    def Gameplay(self): 
        """ The gameplay in order"""
        self.GenerateRandomNumbers()
        print(self.Guess())
        print(self.Scoring())
    
    def GenerateRandomNumbers(self): 
        """ Generate random numbers"""
        from random import randint
        self.rand_num = randint(1,10)
        return self.rand_num
    
    def Guess(self): 
        """ The player makes a guess of number between 1 - 10 """
        while True:   
            try:
                while True:
                    num = int(input("please guess a number between 1 - 10 : ")) 
                    self.guess = num
                    if num <= 0 or num > 10:
                        print("You must answer me with a number between 1 - 10")
                    if num > 0 and num <= 10:
                        break
            except ValueError:
                print("That's not a number!") 
            else:
                break
        return(f"your answer is {num}")
        
    def Scoring(self): 
        """ System that determines wether the player guesses is right or wrong"""
        while self.guess != self.rand_num:
            if self.guess == self.rand_num:
                break 
            elif self.guess > self.rand_num:
                print("Too high, try again")
                print(self.Guess())
            else:
                print("Too low, try again")
                print(self.Guess())
        self.score += 1
        return f"You guessed it, your score is {self.score}"

    def WannaContinue(self): 
        """ Let's play again """
        want_cont = input("Do you want too continue(yes/no): ")
        if want_cont == "yes":
            while want_cont == "yes":
                self.Gameplay()
                want_cont = input("Do you want too continue(yes/no): ")
                if want_cont == "no":
                    break 
        return "Thank you for playing games with me \U0001f600"
        
g = GuessingGame() 
g.GenerateRandomNumbers()
print(g.Guess())
print(g.Scoring())
print(g.WannaContinue())
