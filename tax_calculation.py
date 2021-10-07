
"""
変数の説明

total tax new profit:
新たな利益が実現した後の所得税と住民税の合計

gap btw tax on initial profit and same amount of profit after adding additional proft:　
新たな利益が実現する前の税金の合計と新たな利益が実現した時の同量の利益に対する税金の合計の差額

tax on initial profit:
新たな利益が実現したあとの税金の中で、当初の利益分にかかる税額

tax on additional profit:
新たな利益が実現したあとの税金の中で、新たな利益にかかる税額
    
tax on additional profit when additional profit pays all tax:
追加分の利益にかかる税金を追加分の利益から賄うとき(当初の利益にかかる税額を、当初と同額としたとき)の、追加分の利益にかかる税額

remain when additional profit pays all tax:
追加分の利益にかかる税金を追加分の利益から賄ったあとに残る、追加分の利益の金額

"""

import math


RESIDENT_TAX_RATIO = 0.1
# BASIC_DEDUCTION =

def calculate_income_tax_ratio(profit):
    if profit <= 1950000:
        return 0.05
    if 1950000 < profit <= 3300000:
        return 0.1
    if 3300000 < profit <= 6950000:
        return 0.2
    if 6950000 < profit <= 9000000:
        return 0.23
    if 9000000 < profit <= 18000000:
        return 0.33
    if 18000000 < profit <= 40000000:
        return 0.4
    if 40000000 < profit:
        return 0.45

def calculate_resident_tax(profit):
    resident_tax = RESIDENT_TAX_RATIO * profit
    return resident_tax

def calculate_income_tax(profit):
    income_tax = calculate_income_tax_ratio(profit) * profit
    return income_tax


def calculate_total_tax(profit):
    total_tax = calculate_income_tax(profit) + calculate_resident_tax(profit)
    return total_tax


def number_for_add(num):
    if 0 < num <=1:
        return 0
    if 1 < num <= 5:
        return 1
    if 5 < num <= 10:
        return 5
    if 10 < num <= 50:
        return 10
    if 50 < num <= 100:
        return 50
    if 100 < num <= 500:
        return 100
    if 500 < num <= 1000:
        return 500
    if 1000 < num <= 5000:
        return 1000
    if 5000 < num <= 10000:
        return 5000
    if 10000 < num <= 50000:
        return 10000
    if 50000 < num <= 100000:
        return 50000
    if 100000 < num <= 500000:
        return 100000
    if 500000 < num <= 1000000:
        return 500000
    if  1000000 < num:
        return 1000000




class Financial_Situation():

    def __init__(self, revenue, expenses):
        self.revenue = revenue
        self.expenses = expenses
        self.profit = self.revenue - self.expenses - BASIC_DEDUCTION

    def calculate_resident_tax(self):
        resident_tax = RESIDENT_TAX_RATIO * self.profit
        return math.floor(resident_tax)

    def calculate_income_tax(self):
        income_tax = calculate_income_tax_ratio(self.profit) * self.profit
        return math.floor(income_tax)
    
    def calculate_total_tax(self):
        total_tax = self.calculate_income_tax() + self.calculate_resident_tax()
        return math.floor(total_tax)
    
    def show_all_information(self):
        all_information = {
            'revenue': self.revenue,
            'expenses':self.expenses,
            'profit':self.profit,
            'income tax':self.calculate_income_tax(),
            'resident tax':self.calculate_resident_tax(),
            'total tax': self.calculate_total_tax()
        }

        return all_information

    def calculate_additional_tax(self, additional_revenue, additional_expenses = 0):
        additional_profit = additional_revenue - additional_expenses
        new_profit = self.profit + additional_profit
        total_tax = calculate_total_tax(new_profit)
        tax_per_one_yen = total_tax/new_profit
        tax_on_initial_profit = self.profit * tax_per_one_yen
        tax_on_additional_profit = additional_profit * tax_per_one_yen
        gap_btw_tax_on_initial_profit_and_last_profit = tax_on_initial_profit - calculate_total_tax(self.profit)
        tax_on_additional_profit_when_additional_profit_pays_all_tax = total_tax - calculate_total_tax(self.profit)
        remains_when_additional_profit_pays_all_tax = additional_profit - tax_on_additional_profit_when_additional_profit_pays_all_tax
        return {
            'total tax on new profit': math.floor(total_tax),
            'gap btw tax on initial profit and same amount of profit after adding additional proft':math.floor(gap_btw_tax_on_initial_profit_and_last_profit),
            'tax on initial profit': math.floor(tax_on_initial_profit), 
            'tax on additional profit': math.floor(tax_on_additional_profit),
            'tax on additional profit when additional profit pays all tax': math.floor(tax_on_additional_profit_when_additional_profit_pays_all_tax),
            'remains when additional profit pays all tax': math.floor(remains_when_additional_profit_pays_all_tax)
            }
    

    # def change_profit(self, revenue, expenses):
    #     self.profit = revenue - expenses


    # def change_revenue(self, differential_revenue):
    #     self.revenue += differential_revenue


    # def change_expenses(self, differential_expenses):
    #     self.expenses += differential_expenses



    def function(self, target_num):
        return target_num - calculate_total_tax(self.profit + target_num) + calculate_total_tax(self.profit)


    def calculate_target_revenue(self, necessary_money):
        addition = 0
        money_to_earn = necessary_money + addition
        target_num = money_to_earn + addition
        epsilon = 10000

        if necessary_money - epsilon <= self.function(target_num) <= necessary_money + epsilon:
            return math.floor(target_num)
        
        while self.function(target_num) < necessary_money:
            addition = number_for_add(necessary_money)
            money_to_earn = money_to_earn + addition
            target_num = money_to_earn
            
        max_num = target_num
        min_num = target_num - addition
        median_num = (max_num-min_num)/2 + min_num
        while True:
            if self.function(min_num) < necessary_money <= self.function(median_num):
                max_num = median_num
                median_num = (max_num-min_num)/2 + min_num
                if necessary_money - epsilon <= self.function(max_num) <= necessary_money + epsilon:
                    target_num = max_num
                    return math.floor(target_num)
                    break
                else:
                    continue
        
            elif self.function(median_num) < necessary_money <= self.function(max_num):
                min_num = median_num
                median_num = (max_num-min_num)/2 + min_num
                if necessary_money - epsilon <= self.function(min_num) <= necessary_money + epsilon:
                    target_num = min_num
                    return math.floor(target_num)
                    break
                
                else:
                    continue


# REVENUE = 
# EXPENSES = 

# financial_situation_1_in_2021 = Financial_Situation(REVENUE, EXPENSES)

# print(financial_situation_1_in_2021.show_all_information())


