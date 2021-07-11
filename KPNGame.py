import random

class Game:
    
    def computer_input(self):
        
        computer_choice = random.randint(0,2)
        
        if computer_choice == 0:
            computer_choice == "K"
            
        elif computer_choice == 1:
            computer_choice == "P"
            
        elif computer_choice == 2:
            computer_choice == "N"
            
        
        print("komputer wygral")
        
        return computer_choice
    
    def user_input(self):
        
        user_choice = input('co wybierasz  K P N ?     ')
        
        return user_choice
    
    def run(self,wybor1,wybor2):
        
        print("gra sie zaczyna")
        
        if wybor1 == wybor2:
            print("Remis")
        elif wybor1 == "K" and wybor2 == "P":
            print(f"{wybor1} - {wybor2}!")
            print("wygral komputer")
        elif wybor1 =="P" and wybor2 == "N":
            print(f"{wybor1} - {wybor2}!")
            print("wygral komputer")
        elif wybor1 == "N" and wybor2 == "K":
            print(f"{wybor1} - {wybor2}!")
            print("wygral komputer")
            
        else:
            print(f"{wybor1} - {wybor2}!")
            print("wygral gracz")
            
        
A = Game()
num = 0
while num < 3:
    a.run((A.user_input(),A.computer_input())
A.run(A.user_input(),A.computer_input())