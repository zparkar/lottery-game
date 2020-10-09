# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:02:00 2020

@author: ZPARKAR2
"""
import quantumrandom
from random import randint

class LotteryGame:
    
    def __init__(self,numbers_to_match,number_of_tickets_purchased):
        self.lottery_list=[]
        self.numbers_to_match=numbers_to_match
        self.number_of_tickets_purchased=number_of_tickets_purchased
        self.ticket_items=[]
        self.tickets=[]
        self.results=[]
        self.ticket_dict={}
        self.ticket_results_dict={}

        
        
    def generate_own_tickets(self):
        for i in range(1,self.number_of_tickets_purchased+1):
            print(f"\nTicket {i}:")
            self.ticket_items=[]
            while len(self.ticket_items)<6:
                number=input("Please enter a number between 1 and 59: ")
                if number.isdigit()==False or int(number)<1 or int(number)>59:
                    print("Please enter a valid number!")
                    continue
                elif int(number) in self.ticket_items:
                    print("You already entered that number. Please choose a different number.")
                    continue
                else:
                    while int(number) not in self.ticket_items:
                        self.ticket_items.append(int(number))
            self.ticket_dict[f"Ticket {i}"]=self.ticket_items
            print(f"Ticket {i}: {self.ticket_items}")
            self.tickets.append(self.ticket_items)
             
            
    def generate_random_tickets(self):
        print(f"\nYou have bought {self.number_of_tickets_purchased} ticket(s)")
        print("Generating ticket(s)....")
        for i in range(1,self.number_of_tickets_purchased+1):
            self.ticket_items=[]
            while len(self.ticket_items)<6:
                number=int(randint(1, 60))
                while number not in self.ticket_items:
                    self.ticket_items.append(number)
            self.ticket_dict[f"Ticket {i}"]=self.ticket_items
            print(f"Ticket {i}: {self.ticket_items}")
            self.tickets.append(self.ticket_items)
            
    
    def generate_winning_numbers(self):
        while len(self.lottery_list)<6:
            number=int(randint(1, 60))
            while number not in self.lottery_list:
                self.lottery_list.append(number)

    def display_message(self):
        print(f"\nAny ticket matching {self.numbers_to_match} of these numbers wins a prize!: ")
        print(self.lottery_list)
        
        
    def check_each_ticket_result(self):
        x=0
        for item in self.tickets:
            matched_numbers=0
            for i in item:
                if i in self.lottery_list:
                    matched_numbers+=1
            self.results.append(matched_numbers)
            x+=1
            self.ticket_results_dict[f"Ticket {x}"]=matched_numbers
            
    
    def display_result(self):
        winning_tickets=0
        for i in self.results:
            if i>=self.numbers_to_match:
                winning_tickets+=1
        print(f"\nYou have {winning_tickets} winning ticket(s):")
        for key, value in self.ticket_results_dict.items():
            if int(value)>=self.numbers_to_match:
                print(f"-{key}")
        if max(self.results)>=self.numbers_to_match:
            print(f"\nYour best ticket matched {max(self.results)} number(s)!")
            if max(self.results)==2:
                print("You have won £10!")
            elif max(self.results)==3:
                print("You have won £100!")
            elif max(self.results)==4:
                print("You have won £1000!")
            elif max(self.results)==5:
                print("You have won £10000!")
            elif max(self.results)==6:
                print("Congratulations! You have won the Jackpot of £100,000!")      
        else: 
            print("\nBetter luck next time!")
            
                
    def how_many_tickets_to_win(self):
        self.number_of_tickets_purchased=1
        self.generate_winning_numbers()
        self.generate_random_tickets()
        print(f"Winning numbers: {self.lottery_list}")
        x=1
        while True:
            for item in self.tickets:
                matched_numbers=0
                for i in item:
                    if i in self.lottery_list:
                        matched_numbers+=1
            if matched_numbers!=self.numbers_to_match:
                self.generate_random_tickets()
                x+=1
                print(f"Total tries: {x}")
                print(f"Winning numbers: {self.lottery_list}")
                continue
            else:
                print(f"To match {self.numbers_to_match} number(s) you had to buy {x} tickets.")
                break


                
            
                

            
            
            
            