




# """
# 変数の説明

# """

# RESIDENT_TAX_RATIO = 0.1

# def calculate_tax_ratio(revenue):
#     if revenue <= 1950000:
#         return 0.05
#     if 1950000 < revenue <= 3300000:
#         return 0.1
#     if 3300000 < revenue <= 6950000:
#         return 0.2
#     if 6950000 < revenue <= 9000000:
#         return 0.23
#     if 9000000 < revenue <= 18000000:
#         return 0.33
#     if 18000000 < revenue <= 40000000:
#         return 0.4
#     if 40000000 < revenue:
#         return 0.45


# def calculate_total_tax(revenue):
#     income_tax = revenue * calculate_tax_ratio(revenue)
#     resident_tax = RESIDENT_TAX_RATIO * revenue
#     total_tax = income_tax + resident_tax
#     return total_tax




# class Financial_Situation():

#     def __init__(self, initial_revenue, expenses):
#         self.initial_revenue = initial_revenue
#         self.total_revenue = self.initial_revenue
#         self.expenses = expenses
#         self.total_expenses = self.expenses
#         self.pure_revenue = self.initial_revenue - self.expenses

#     def calculate_tax(self):
#         income_tax = calculate_tax_ratio(self.pure_revenue) * self.pure_revenue
#         resident_tax = 0.1 * self.pure_revenue
#         total_tax = income_tax + resident_tax
#         return total_tax
    
#     # def calculate_marginal_tax_to_pay(self, marginal_revenue):
#     #     self.total_revenue += marginal_revenue
#     #     self.pure_revenue = self.total_revenue - self.expenses
#     #     income_tax = calculate_tax_ratio(self.pure_revenue) * self.pure_revenue
#     #     resident_tax = 0.1 * self.pure_revenue
#     #     total_tax = income_tax + resident_tax
#     #     tax_on_a_yen = total_tax/self.total_revenue
#     #     tax_on_initial_revenue = self.initial_revenue * tax_on_a_yen
#     #     tax_on_marginal_revenue = marginal_revenue * tax_on_a_yen
#     #     return {'tax on initial revenue': tax_on_initial_revenue, 'tax on marginal revenue':tax_on_marginal_revenue }

#     def calculate_marginal_tax(self, marginal_revenue):
#         total_revenue = self.initial_revenue + marginal_revenue
#         pure_revenue = total_revenue - self.total_expenses
#         income_tax = calculate_tax_ratio(pure_revenue) * pure_revenue
#         resident_tax = 0.1 * pure_revenue
#         total_tax = income_tax + resident_tax
#         tax_on_a_yen = total_tax/total_revenue
#         tax_on_initial_revenue = self.initial_revenue * tax_on_a_yen
#         tax_on_marginal_revenue = marginal_revenue * tax_on_a_yen
#         difference_of_tax_on_initial_revenue = tax_on_initial_revenue - self.calculate_tax()
#         tax_on_marginal_revenue_when_margial_reveneu_pays_all_tax = total_tax - self.calculate_tax()
#         remain_when_margial_reveneu_pays_all_tax = marginal_revenue - tax_on_marginal_revenue_when_margial_reveneu_pays_all_tax
#         return {
#             'total tax': total_tax,
#             'diffrence of tax on inital revenue':difference_of_tax_on_initial_revenue,
#             'tax on initial revenue': tax_on_initial_revenue, 
#             'tax on marginal revenue':tax_on_marginal_revenue,
#             'tax on marginal reveneu when marginal reveneu pays all tax':tax_on_marginal_revenue_when_margial_reveneu_pays_all_tax,
#             'remain when marginal reveneu pays all tax':remain_when_margial_reveneu_pays_all_tax}
        
#     def calculate_necessary_revenue(self,money_wanted):
#         # 20万円のものを買いたいなと思った時、今の所得水準と経費を所与とした時、追加でいくらの売り上げを立てればいいのか。
#         total_money = money_wanted + self.initial_revenue
#         total_income_tax = calculate_tax_ratio(total_money) * total_money
#         total_resident_tax = 0.1 * total_money
#         total_tax = total_income_tax + total_resident_tax
#         initial_income_tax = calculate_tax_ratio(self.initial_revenue) * self.initial_revenue
#         initial_resident_tax = 0.1 * self.initial_revenue
#         total_initial_tax = initial_income_tax + initial_resident_tax
#         additional_tax_by_money_wanted = total_tax - total_initial_tax
#         nessesary_revenue = additional_tax_by_money_wanted + money_wanted
#         return nessesary_revenue




#     def add_revenue(self, additional_revenue):
#         self.total_revenue += additional_revenue
    
#     def initialize_revenue(self):
#         self.total_revenue = self.initial_revenue

#     def change_expense(self, new_expenses):
#         self.total_expenses = new_expenses
    
#     def initialize_expense(self):
#         self.total_expenses = self.expenses

    

# financial_situation = Financial_Situation(7654364, 973211)

# print(financial_situation.pure_revenue)
# print(financial_situation.calculate_tax())
# print(financial_situation.calculate_marginal_tax(1000000))
# print(financial_situation.initial_revenue)
# print(financial_situation.total_revenue)



# RESIDENT_TAX_RATIO = 0.1

# def calculate_income_tax_ratio(revenue):
#     if revenue <= 1950000:
#         return 0.05
#     if 1950000 < revenue <= 3300000:
#         return 0.1
#     if 3300000 < revenue <= 6950000:
#         return 0.2
#     if 6950000 < revenue <= 9000000:
#         return 0.23
#     if 9000000 < revenue <= 18000000:
#         return 0.33
#     if 18000000 < revenue <= 40000000:
#         return 0.4
#     if 40000000 < revenue:
#         return 0.45

# def calculate_resident_tax(revenue):
#     resident_tax = RESIDENT_TAX_RATIO * revenue
#     return resident_tax

# def calculate_income_tax(revenue):
#     income_tax = calculate_income_tax_ratio(revenue) * revenue
#     return income_tax


# def calculate_total_tax(revenue):
#     total_tax = calculate_income_tax(revenue) + calculate_resident_tax(revenue)
#     return total_tax

# def number_for_add(num):
#     if 0 < num <=1:
#         return 0
#     if 1 < num <= 5:
#         return 1
#     if 5 < num <= 10:
#         return 5
#     if 10 < num <= 50:
#         return 10
#     if 50 < num <= 100:
#         return 50
#     if 100 < num <= 500:
#         return 100
#     if 500 < num <= 1000:
#         return 500
#     if 1000 < num <= 5000:
#         return 1000
#     if 5000 < num <= 10000:
#         return 5000
#     if 10000 < num <= 50000:
#         return 10000
#     if 50000 < num <= 100000:
#         return 50000
#     if 100000 < num <= 500000:
#         return 100000
#     if 500000 < num <= 1000000:
#         return 500000
#     if  1000000 < num:
#         return 1000000


# def function(target_num):
#     return target_num - calculate_total_tax(revenue + target_num) + calculate_total_tax(revenue)


# revenue = 7000000




# def calculate_target_revenue(necessary_money):
#     addition = 0
#     money_to_earn = necessary_money + addition
#     target_num = money_to_earn + addition
#     epsilon = 10000

#     if necessary_money - epsilon <= function(target_num) <= necessary_money + epsilon:
#         return target_num
    
#     while function(target_num) < necessary_money:
#         addition = number_for_add(necessary_money)
#         money_to_earn = money_to_earn + addition
#         target_num = money_to_earn
        
#     max_num = target_num
#     min_num = target_num - addition
#     median_num = (max_num-min_num)/2 + min_num
#     while True:
#         if function(min_num) < necessary_money <= function(median_num):
#             max_num = median_num
#             median_num = (max_num-min_num)/2 + min_num
#             if necessary_money - epsilon <= function(max_num) <= necessary_money + epsilon:
#                 target_num = max_num
#                 return target_num
#                 break
#             else:
#                 continue
    
#         elif function(median_num) < necessary_money <= function(max_num):
#             min_num = median_num
#             median_num = (max_num-min_num)/2 + min_num
#             if necessary_money - epsilon <= function(min_num) <= necessary_money + epsilon:
#                 target_num = min_num
#                 return target_num
#                 break
            
#             else:
#                 continue
                    


# print(calculate_target_revenue(200000))




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
BASIC_DEDUCTION = 480000

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


"""
売り上げ1 = 7654364
売り上げ2 = 7555004
売り上げ3 = 7154320

経費1 = 864231
経費2 = 1457231


"""

financial_situation_1_in_2021 = Financial_Situation(7654364, 864231)

financial_situation_2_in_2021 = Financial_Situation(7654364, 1457231)

financial_situation_3_in_2021 = Financial_Situation(7154320, 864231)

financial_situation_4_in_2021 = Financial_Situation(7154320, 1457231)


print("##########################################")
print(financial_situation_1_in_2021.show_all_information())
print("##########################################")
print(financial_situation_2_in_2021.show_all_information())
print("##########################################")
print(financial_situation_3_in_2021.show_all_information())
print("##########################################")
print(financial_situation_4_in_2021.show_all_information())
print("##########################################")

