# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 19:09:43 2020

@author: ZPARKAR2
"""

from lottery_game import LotteryGame

play_input_flag=False
restart_game_flag=True

print("Welcome to the National Lottery!")
while restart_game_flag==True:
    while play_input_flag==False:
    
        play=input("Would you like to buy your own tickets? (yes/no): ")
    
    
        if play.lower()=="yes":
            print("Great! How many tickets would you like to buy?")
            play_input_flag = True
            tickets_input_flag2=False
            while tickets_input_flag2==False:
            
                no_tickets=input("No. of tickets: ")
            
                if no_tickets.isdigit()==False or int(no_tickets)<=0 :
                    print("Please enter a valid number!")
                    continue
                
                else:
                    tickets_input_flag2=True
                    game1=LotteryGame(2,int(no_tickets))
                    game1.generate_own_tickets()
                    game1.generate_winning_numbers()
                    game1.display_message()
                    game1.check_each_ticket_result()
                    game1.display_result()
                    restart=input("Would you like to play again?: ")
                    if restart.lower()=="yes":
                        play_input_flag=False
                        continue
                    else:
                        print("\nThank you for playing")
                        restart_game_flag=False
                        break
        
        elif play.lower()=="no":
            print("Great! How many tickets would you like to buy?")
            play_input_flag = True
            tickets_input_flag=False
            while tickets_input_flag==False:
                no_tickets=input("No. of tickets: ")
            
                if no_tickets.isdigit()==False or int(no_tickets)<=0:
                    print("Please enter a valid number!")
                    continue
            
                else:
                    tickets_input_flag = True
                    game1=LotteryGame(2,int(no_tickets))
                    game1.generate_random_tickets()
                    game1.generate_winning_numbers()
                    game1.display_message()
                    game1.check_each_ticket_result()
                    game1.display_result()
                    restart=input("Would you like to play again?: ")
                    if restart.lower()=="yes":
                        play_input_flag=False
                        continue
                    else:
                        print("\nThank you for playing")
                        restart_game_flag=False
                        break
        else:
            print ("Please enter a valid response!")
            continue
    
        
    






        
    
