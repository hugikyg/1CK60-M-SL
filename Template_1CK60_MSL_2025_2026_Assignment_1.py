import math
from scipy.stats import poisson

from math import factorial

import pandas as pd

# %% Please fill out  the information below
# If you decide to perform the assignment alone, then set the variables for the second student as follows: student2 name=“empty”, and student2 surname=“empty”
student1_name = "Sinjini"
student1_surname = "Pande"

student2_name = "Eliza"
student2_surname = "Oborzynska"


# A little reminder to fill in your personal information.
if (student1_name == "" or student1_surname == "" 
      or student2_name == ""
    or student2_surname == "" ):
    print("Please enter your personal information.")
    
    
# Read data files
data_Q1_Q3_Q4 = pd.read_csv("Data_Q1_Q3_Q4.csv", index_col=0)  
data_Q2 = pd.read_csv("Data_Q2.csv", index_col=0)    

# %% Question 1

def Q1a_EBOitem(S,c_a,m,t):
    # S is the stock level.
    # c_a is the SKU's acquisition cost.
    # m is the number of failures per period.
    # t is the repair leadtime.
    
    ans = 0
    method1 = False
    method2 = True
    
    if(method1):
        mu = m * t
        ans = 0.0
        r = 0
        cutoff = 1e-12   

        while True:
            tail_prob = poisson.sf(S + r, mu)
            if tail_prob < cutoff:     
                break
            ans += tail_prob
            r += 1
    
    if(method2):  
        probabilitiesX = []
        probabilityX0 = math.exp(-1 * (m * t))
        probabilitiesX.append(probabilityX0)
        for k in range(1, S + 1):
            calculate = ((m * t) / k) * probabilitiesX[k - 1]
            probabilitiesX.append(calculate)
            
        const = (m * t) - S
        sum = 0
        for k in range(S + 1):
            sum = sum + ((S - k) * probabilitiesX[k])
        ans = const + sum

    return ans

def Q1b_EBO(S_list,c_a_list,m_list,t_list):
    # S_list[i] is the stock level of SKU i.
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.

    ans = 0

    for i in range(len(S_list)):
        ans += Q1a_EBOitem(
            S_list[i],
            c_a_list[i],
            m_list[i],
            t_list[i]
        )
        
    # Your output should be a number.
        
    # Your output should be a number.
    return ans

def Q1c_PBOitem(S,c_a,m,t):
    # S is the stock level.
    # c_a is the SKU's acquisition cost.
    # m is the number of failures per period.
    # t is the repair leadtime.
    
    ans = 0 
    method1 = False
    method2 = True
    
    if(method1):
        mu = m * t   # mean demand during lead time
        ans = poisson.sf(S, mu) 
    
    if(method2):  
        probabilitiesX = []
        probabilityX0 = math.exp(-1 * (m * t))
        probabilitiesX.append(probabilityX0)
        ans = ans + probabilityX0
        for k in range(1, S + 1):
            calculate = ((m * t) / k) * probabilitiesX[k - 1]
            probabilitiesX.append(calculate)
            ans = ans + calculate
        ans = 1 - ans
            
    # Your output should be a number.

    return ans


def Q1d_PBO(S_list,c_a_list,m_list,t_list):
    # S_list[i] is the stock level of SKU i.
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.

    ans = 0

    for i in range(len(S_list)):
        ans += Q1c_PBOitem(
            S_list[i],
            c_a_list[i],
            m_list[i],
            t_list[i]
        )
        
    # Your output should be a number.
    
    return ans

def Q1e_Costs(S_list,c_a_list,m_list,t_list):
    # S_list[i] is the stock level of SKU i.
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.

    ans = 0

    for i in range(len(S_list)):
        ans += S_list[i] * c_a_list[i]
        
    # Your output should be a number.
    
    
    return ans


def Q1f_FRitem(S, c_a, m, t):
    # S is the stock level.
    # c_a is the SKU's acquisition cost.
    # m is the number of failures per period.
    # t is the repair leadtime.
    
    ans = 0

    method1 = True
    method2 = False
    
    if(method1):
        mu = m * t   # mean demand during lead time
        ans = poisson.cdf(S - 1, mu) 
    
    if(method2):  
        probabilitiesX = []
        probabilityX0 = math.exp(-1 * (m * t))
        probabilitiesX.append(probabilityX0)
        ans = ans + probabilityX0
        for k in range(1, S):
            calculate = ((m * t) / k) * probabilitiesX[k - 1]
            probabilitiesX.append(calculate)
            ans = ans + calculate
        
    # Your output should be a number.
    
    
    return ans

def Q1g_FR(S_list,c_a_list,m_list,t_list):
    # S_list[i] is the stock level of SKU i.
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.

    ans = 0

    totalFailures = 0
    for k in range(1, len(m_list)):
        totalFailures += m_list[k]
    
    for k in range(1, len(m_list)):
        ans += (m_list[k] / totalFailures) * Q1f_FRitem(S_list[k], c_a_list[k], m_list[k], t_list[k])
    # Your output should be a number.
    
    
    return ans


def Q1h_WTitem(S, c_a, m, t):
    # S is the stock level.
    # c_a is the SKU's acquisition cost.
    # m is the number of failures per period.
    # t is the repair leadtime.
    
    ans = 0

    ans = Q1a_EBOitem(S,c_a,m,t) / m
        
    # Your output should be a number.
    
    
    return ans

def Q1i_WT(S_list, c_a_list, m_list, t_list):
    # S_list[i] is the stock level of SKU i.
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.

    ans = 0
    
    totalFailures = 0
    for k in range(1, len(m_list)):
        totalFailures += m_list[k]

    ans = Q1b_EBO(S_list,c_a_list,m_list,t_list) / totalFailures
        
    # Your output should be a number.
    
    
    return ans
    
    



print("\n           ==== SOLUTION QUESTION 1 ====          \n")

S_A_list = list(data_Q1_Q3_Q4.iloc[0:15,0])
S_B_list = list(data_Q1_Q3_Q4.iloc[0:15,1])
S_C_list = list(data_Q1_Q3_Q4.iloc[0:15,2])

c_a_list = list(data_Q1_Q3_Q4.iloc[0:15,3])
m_list = list(data_Q1_Q3_Q4.iloc[0:15,4])
t_list =list(data_Q1_Q3_Q4.iloc[0:15,5])


print("Rounded")
print("For question 1a:")
print(f"{'SKU':<6}{'EBO_i (A)':>12}{'EBO_i (B)':>12}{'EBO_i (C)':>12}")
print("-" * 42)

for i in range(len(S_A_list)):
    ebo_i_A = round(Q1a_EBOitem(S_A_list[i], c_a_list[i], m_list[i], t_list[i]),3)
    ebo_i_B = round(Q1a_EBOitem(S_B_list[i], c_a_list[i], m_list[i], t_list[i]),3)
    ebo_i_C = round(Q1a_EBOitem(S_C_list[i], c_a_list[i], m_list[i], t_list[i]),3)
    print(f"{i+1:<6}{ebo_i_A:>12}{ebo_i_B:>12}{ebo_i_C:>12}")
    
    

#Added this to check if the method Q1b_EBO works correctly. 
#Rounded values of q1a were to much rounded to accuratly calcualte the sum.
print("Rounded 6 decimals")

print("For question 1a:")
print(f"{'SKU':<6}{'EBO_i (A)':>12}{'EBO_i (B)':>12}{'EBO_i (C)':>12}")
print("-" * 42)
for i in range(len(S_A_list)):
    ebo_i_A = round(Q1a_EBOitem(S_A_list[i], c_a_list[i], m_list[i], t_list[i]),6)
    ebo_i_B = round(Q1a_EBOitem(S_B_list[i], c_a_list[i], m_list[i], t_list[i]),6)
    ebo_i_C = round(Q1a_EBOitem(S_C_list[i], c_a_list[i], m_list[i], t_list[i]),6)
    print(f"{i+1:<6}{ebo_i_A:>12}{ebo_i_B:>12}{ebo_i_C:>12}")
#Summed the values that are in this table and they are the same as the values
#calculated with the method Q1b_EBO
    
sumEBOa = Q1b_EBO(S_A_list, c_a_list, m_list, t_list)
sumEBOb = Q1b_EBO(S_B_list, c_a_list, m_list, t_list)
sumEBOc = Q1b_EBO(S_C_list, c_a_list, m_list, t_list)
                                                                                                                          
print("For question 1b, the EBO for policy A is ", sumEBOa)
print("For question 1b, the EBO for policy B is ", sumEBOb)
print("For question 1b, the EBO for policy C is ", sumEBOc)

print("For question 1c:")
print(f"{'SKU':<6}{'PBO_i (A)':>12}{'PBO_i (B)':>12}{'PBO_i (C)':>12}")
print("-" * 42)

for i in range(len(S_A_list)):
    pbo_i_A = Q1c_PBOitem(S_A_list[i], c_a_list[i], m_list[i], t_list[i])
    pbo_i_B = Q1c_PBOitem(S_B_list[i], c_a_list[i], m_list[i], t_list[i])
    pbo_i_C = Q1c_PBOitem(S_C_list[i], c_a_list[i], m_list[i], t_list[i])
    print(f"{i+1:<6}{pbo_i_A:>12.2f}{pbo_i_B:>12.2f}{pbo_i_C:>12.2f}")
    
sumPBOa = Q1d_PBO(S_A_list, c_a_list, m_list, t_list)
sumPBOb = Q1d_PBO(S_B_list, c_a_list, m_list, t_list)
sumPBOc = Q1d_PBO(S_C_list, c_a_list, m_list, t_list)

print()

print("For question 1d, the PBO for policy A is  ", sumPBOa)
print("For question 1d, the PBO for policy B is  ", sumPBOb)
print("For question 1d, the PBO for policy C is  ", sumPBOc)

print()
aquisitionCostsA = Q1e_Costs(S_A_list, c_a_list, m_list, t_list)
aquisitionCostsB = Q1e_Costs(S_B_list, c_a_list, m_list, t_list)
aquisitionCostsC = Q1e_Costs(S_C_list, c_a_list, m_list, t_list)

print("For question 1e, the total acquisition for policy A is ", aquisitionCostsA)
print("For question 1e, the total acquisition for policy B is ", aquisitionCostsB)
print("For question 1e, the total acquisition for policy C is ", aquisitionCostsC)

print()

print("For question 1f:")
print(f"{'SKU':<6}{'FR_i (A)':>12}{'FR_i (B)':>12}{'FR_i (C)':>12}")
print("-" * 42)

for i in range(len(S_A_list)):
    fr_i_A = Q1f_FRitem(S_A_list[i], c_a_list[i], m_list[i], t_list[i])
    fr_i_B = Q1f_FRitem(S_B_list[i], c_a_list[i], m_list[i], t_list[i])
    fr_i_C = Q1f_FRitem(S_C_list[i], c_a_list[i], m_list[i], t_list[i])
    print(f"{i+1:<6}{fr_i_A:>12.2f}{fr_i_B:>12.2f}{fr_i_C:>12.2f}")

print()
aggregateFillRateA = Q1g_FR(S_A_list, c_a_list, m_list, t_list)
aggregateFillRateB = Q1g_FR(S_B_list, c_a_list, m_list, t_list)
aggregateFillRateC = Q1g_FR(S_C_list, c_a_list, m_list, t_list)

print("For question 1g, the aggregate fill rate for policy A is ", aggregateFillRateA)
print("For question 1g, the aggregate fill rate for policy B is ", aggregateFillRateB)
print("For question 1g, the aggregate fill rate for policy C is ", aggregateFillRateC)

print("For question 1h:")
print(f"{'SKU':<6}{'WT_i (A)':>12}{'WT_i (B)':>12}{'WT_i (C)':>12}")
print("-" * 42)

for i in range(len(S_A_list)):
    wt_i_A = Q1h_WTitem(S_A_list[i], c_a_list[i], m_list[i], t_list[i])
    wt_i_B = Q1h_WTitem(S_B_list[i], c_a_list[i], m_list[i], t_list[i])
    wt_i_C = Q1h_WTitem(S_C_list[i], c_a_list[i], m_list[i], t_list[i])
    print(f"{i+1:<6}{wt_i_A:>12.2f}{wt_i_B:>12.2f}{wt_i_C:>12.2f}")

print()
aggregateMeanWaitingTimeA = Q1i_WT(S_A_list, c_a_list, m_list, t_list)
aggregateMeanWaitingTimeB = Q1i_WT(S_B_list, c_a_list, m_list, t_list)
aggregateMeanWaitingTimeC = Q1i_WT(S_C_list, c_a_list, m_list, t_list)

print("For question 1i, the aggregate mean waiting time for policy A is ", aggregateMeanWaitingTimeA)
print("For question 1i, the aggregate mean waiting time for policy B is ", aggregateMeanWaitingTimeB)
print("For question 1i, the aggregate mean waiting time for policy C is ", aggregateMeanWaitingTimeC)



# %% Question 2

def Q2b_NewDemandRates(d_list):
    # d_list is a list containing the demands over all periods for a SKU.
    
    ans = 0
    
    ans = sum(d_list)
    ans = ans / len(d_list)
    return ans

# This code modifies the average demand rate estimates in the csv file.
for i in range(len(data_Q2)):
    
    data_Q2.iloc[i,3]=Q2b_NewDemandRates(data_Q2.iloc[i,4:])

data_Q2.to_csv("Data_Q2.csv")



def Q2c_Greedy(c_a_list,m_list,t_list, target_ebo):
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # target_ebo is the ebo objective.


    S_output=[0]*len(c_a_list)

    # YOUR CODE GOES HERE.
    EBO_old = [0]*len(c_a_list)
    EBO_new = [0]*len(c_a_list)
    gamma = [0]*len(c_a_list)
    currentEBO = Q1b_EBO(S_output,c_a_list,m_list,t_list)
    print("Curretn EBO = ", currentEBO)
    increasingIndex = 0
    
    for i in range(len(c_a_list)):
        EBO_old[i] = Q1a_EBOitem(S_output[i],c_a_list[i],m_list[i],t_list[i])
    
    while (Q1b_EBO(S_output,c_a_list,m_list,t_list) > target_ebo):
        for i in range(len(c_a_list)):
            EBO_new[i] = Q1a_EBOitem(S_output[i] + 1,c_a_list[i],m_list[i],t_list[i])
            gamma[i] = (-1 * (EBO_new[i] -  EBO_old[i])) / c_a_list[i]
        for i in range(len(c_a_list) - 1):
            if (gamma[increasingIndex] < gamma[i + 1]):
                increasingIndex = i + 1
        S_output[increasingIndex] = S_output[increasingIndex] + 1
        EBO_old[increasingIndex] = Q1a_EBOitem(S_output[increasingIndex],c_a_list[increasingIndex],m_list[increasingIndex],t_list[increasingIndex])
        increasingIndex = 0
        
    # Output a list of stock levels.
    return S_output




def Q2d_ItemApproach(c_a_list, m_list, t_list, target_ebo):
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # target_ebo is the ebo objective.


    S_output=[0]*len(c_a_list)
    EBOi = [0]*len(c_a_list)
    totalM = 0
    for i in range(len(c_a_list)):
        totalM += m_list[i]
        
    for i in range(len(c_a_list)):
        EBOi[i] = (m_list[i] / totalM) * target_ebo
    
    for i in range(len(c_a_list)):
        while (Q1a_EBOitem(S_output[i],c_a_list[i],m_list[i],t_list[i]) > EBOi[i]):
            S_output[i] += 1
    # Output a list of stock levels.
    return S_output


print("\n           ==== SOLUTION QUESTION 2 ====          \n")

c_a_list_1 = list(data_Q2.iloc[0:25,0])
m_list_1 = list(data_Q2.iloc[0:25,3])
t_list_1 =list(data_Q2.iloc[0:25,1])

c_a_list_2 = list(data_Q2.iloc[25:50,0])
m_list_2 = list(data_Q2.iloc[25:50,3])
t_list_2 =list(data_Q2.iloc[25:50,1])

target_ebo = 0.5

# Stock calculation for greedy appraoch group 1
Greedy_optimal_stock_levels_group1 = Q2c_Greedy(c_a_list_1,m_list_1,t_list_1, target_ebo)
# EBO calculation
greedyEBO_group1 = Q1b_EBO(Greedy_optimal_stock_levels_group1,c_a_list_1,m_list_1,t_list_1)
# Costs
costsGreedy_group1 = Q1e_Costs(Greedy_optimal_stock_levels_group1,c_a_list_1,m_list_1,t_list_1)

# Stock calculation for greedy appraoch group 2
Greedy_optimal_stock_levels_group2 = Q2c_Greedy(c_a_list_2,m_list_2,t_list_2, target_ebo)
# EBO calculation
greedyEBO_group2 = Q1b_EBO(Greedy_optimal_stock_levels_group2,c_a_list_2,m_list_2,t_list_2)
# Costs
costsGreedy_group2 = Q1e_Costs(Greedy_optimal_stock_levels_group2,c_a_list_2,m_list_2,t_list_2)

# Stock calculation for item appraoch group 1
Item_optimal_stock_levels_group1 = Q2d_ItemApproach(c_a_list_1,m_list_1,t_list_1, target_ebo)
# EBO calculation
itemEBO_group1 = Q1b_EBO(Item_optimal_stock_levels_group1,c_a_list_1,m_list_1,t_list_1)
# Costs
costsItem_group1 = Q1e_Costs(Item_optimal_stock_levels_group1,c_a_list_1,m_list_1,t_list_1)

# Stock calculation for Item appraoch group 2
Item_optimal_stock_levels_group2 = Q2d_ItemApproach(c_a_list_2,m_list_2,t_list_2, target_ebo)
# EBO calculation
itemEBO_group2 = Q1b_EBO(Item_optimal_stock_levels_group2,c_a_list_2,m_list_2,t_list_2)
# Costs
costsItem_group2 = Q1e_Costs(Item_optimal_stock_levels_group2,c_a_list_2,m_list_2,t_list_2)


print("Greedy approach group 1:")
print("The optimal stock levels with greedy approach are for group 1", Greedy_optimal_stock_levels_group1)
print("The EBO with greedy approach is ", greedyEBO_group1)
print("The cost with greedy approach is ", costsGreedy_group1)

print("Greedy approach group 2:")
print("The optimal stock levels with greedy approach are for group 2 ", Greedy_optimal_stock_levels_group2)
print("The EBO with greedy approach is ", greedyEBO_group2)
print("The cost with greedy approach is ", costsGreedy_group2)

print("Item approach group 1:")
print("The optimal stock levels with item approach are group 1", Item_optimal_stock_levels_group1)
print("The EBO with item approach is ", itemEBO_group1)
print("The cost with item approach is ", costsItem_group1)

print("Item approach group 2:")
print("The optimal stock levels with item approach are grpup 2", Item_optimal_stock_levels_group2)
print("The EBO with item approach is ", itemEBO_group2)
print("The cost with item approach is ", costsItem_group2)



# %% Question 3



def Q3a_itemWT_Consultant1(c_a_list,m_list,t_list,target_W):
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # target_W is the waiting time objective.


    S_output=[0]*len(c_a_list)

    M = sum(m_list)
    for i in range(len(c_a_list)):
        target_Wi = (m_list[i] / M) * target_W
        while Q1h_WTitem(S_output[i], c_a_list[i], m_list[i], t_list[i]) > target_Wi:
            S_output[i] += 1
            
    # Output a list of stock levels.
    return S_output






def Q3b_itemWT_Consultant2(c_a_list,m_list,t_list,target_W):
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # target_W is the waiting time objective.


    S_output=[0]*len(c_a_list)
    
    M = sum(m_list)
    for i in range(len(c_a_list)):
        target_Wi = target_W
        while Q1h_WTitem(S_output[i], c_a_list[i], m_list[i], t_list[i]) > target_Wi:
            S_output[i] += 1

    # Output a list of stock levels.
    return S_output


def Q3c_itemWT_Consultant3(c_a_list, m_list, t_list, target_W):
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # target_W is the waiting time objective.

    S_output = [0] * len(c_a_list)
    
    M = sum(m_list)

    target_Wi = target_W / M
    
    for i in range(len(c_a_list)):
        while Q1h_WTitem(S_output[i], c_a_list[i], m_list[i], t_list[i]) > target_Wi:
            S_output[i] += 1

    return S_output




print("\n           ==== SOLUTION QUESTION 3 ====          \n")


c_a_list = list(data_Q1_Q3_Q4.iloc[0:15,3])
m_list = list(data_Q1_Q3_Q4.iloc[0:15,4])
t_list =list(data_Q1_Q3_Q4.iloc[0:15,5])
target_W = 0.05

S_cons1 = Q3a_itemWT_Consultant1(c_a_list, m_list, t_list, target_W)
W_cons1 = Q1i_WT(S_cons1, c_a_list, m_list, t_list)
C_cons1 = Q1e_Costs(S_cons1, c_a_list, m_list, t_list)

S_cons2 = Q3b_itemWT_Consultant2(c_a_list, m_list, t_list, target_W)
W_cons2 = Q1i_WT(S_cons2, c_a_list, m_list, t_list)
C_cons2 = Q1e_Costs(S_cons2, c_a_list, m_list, t_list)

S_cons3 = Q3c_itemWT_Consultant3(c_a_list, m_list, t_list, target_W)
W_cons3 = Q1i_WT(S_cons3, c_a_list, m_list, t_list)
C_cons3 = Q1e_Costs(S_cons3, c_a_list, m_list, t_list)


print("The optimal stock levels from Consultant 1 are ", S_cons1)
print("The aggregate mean waiting time from Consultant 1 is  ", W_cons1)
print("The cost from Consultant 1 is ", C_cons1)


print("The optimal stock levels from Consultant 2 are ", S_cons2)
print("The aggregate mean waiting time from Consultant 2 is ", W_cons2)
print("The cost from Consultant 2 is  ", C_cons2)


print("The optimal stock levels from Consultant 3 are ", S_cons3)
print("The aggregate mean waiting time from Consultant 3 is ", W_cons3)
print("The cost from Consultant 3 is  ", C_cons3)




# %% Question 4


def Q4a_GreedyWT(c_h_list, m_list, t_list, target_wt):
    # c_h_list[i] is the holding cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # target_wt is the waiting time objective.


    S_output=[0]*len(c_h_list)

    # YOUR CODE GOES HERE.
    W_old = [0]*len(c_a_list)
    W_new = [0]*len(c_a_list)
    gamma = [0]*len(c_a_list)
    currentW = Q1i_WT(S_output,c_h_list,m_list,t_list)
    print("Curretn W = ", currentW)
    increasingIndex = 0
    
    for i in range(len(c_a_list)):
        W_old[i] = Q1h_WTitem(S_output[i],c_h_list[i],m_list[i],t_list[i])
    
    while (Q1i_WT(S_output,c_h_list,m_list,t_list) > target_wt):
        for i in range(len(c_h_list)):
            W_new[i] = Q1h_WTitem(S_output[i] + 1,c_h_list[i],m_list[i],t_list[i])
            gamma[i] = (-1 * (W_new[i] -  W_old[i])) / c_h_list[i]
        for i in range(len(c_h_list) - 1):
            if (gamma[increasingIndex] < gamma[i + 1]):
                increasingIndex = i + 1
        S_output[increasingIndex] = S_output[increasingIndex] + 1
        W_old[increasingIndex] = Q1h_WTitem(S_output[increasingIndex],c_h_list[increasingIndex],m_list[increasingIndex],t_list[increasingIndex])
        increasingIndex = 0

    # Output a list of stock levels.
    return S_output

        
        

def Q4b_Costs_Shipping(S_list, c_h_list, c_s_list, m_list, t_list, t_s_list):
    # S_list[i] is the stock level of SKU i.
    # c_h_list[i] is the holding cost of SKU i.
    # c_s_list[i] is the additional cost for shipping SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # t_s_list[i] is the shipping lead time of SKU i.



    ans = 0

    for i in range(len(S_list)):
        ans += S_list[i] * (c_h_list[i] + c_s_list[i])
        
    # Your output should be a number.
    return ans



def Q4c_WT_Shipping(S_list, c_h_list, c_s_list, m_list, t_list, t_s_list):
    # S_list[i] is the stock level of SKU i.
    # c_h_list[i] is the holding cost of SKU i.
    # c_s_list[i] is the additional cost for shipping SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # t_s_list[i] is the shipping lead time of SKU i.



    ans = 0
    c_with_shipping=[0]*len(c_h_list)
    
    for i in range(len(S_list)):
        c_with_shipping[i] = c_h_list[i] + c_s_list[i]

    ans = Q1i_WT(S_list, c_with_shipping, m_list, t_list)
        
    # Your output should be a number.
    return ans



def Q4d_GreedyWT_Shipping(c_h_list, c_s_list, m_list, t_list, t_s_list, target_wt):
    # c_h_list[i] is the holding cost of SKU i.
    # c_s_list[i] is the additional cost for shipping SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # t_s_list[i] is the shipping lead time of SKU i.
    # target_wt is the waiting time objective.


    S_output=[0]*len(c_h_list)

    S_output = [0] * len(c_h_list)
    W_old = [0] * len(c_h_list)
    W_new = [0] * len(c_h_list)
    gamma = [0] * len(c_h_list)

    # Combine repair and shipping lead times
    t_total = [t_list[i] + t_s_list[i] for i in range(len(t_list))]

    # Combine costs
    c_total = [c_h_list[i] + c_s_list[i] for i in range(len(c_h_list))]

    # Compute initial W_i
    for i in range(len(c_h_list)):
        W_old[i] = Q1h_WTitem(S_output[i], c_total[i], m_list[i], t_total[i])

    # Compute current aggregate WT
    currentWT = Q1i_WT(S_output, c_total, m_list, t_total)
    print("Current WT = ", currentWT)

    increaseIndex = 0

    while Q1i_WT(S_output, c_total, m_list, t_total) > target_wt:
        for i in range(len(c_h_list)):
            W_new[i] = Q1h_WTitem(S_output[i] + 1, c_total[i], m_list[i], t_total[i])
            gamma[i] = (-1 * (W_new[i] - W_old[i])) / c_total[i]

        for i in range(len(c_h_list) - 1):
            if gamma[increaseIndex] < gamma[i + 1]:
                increaseIndex = i + 1

        S_output[increaseIndex] += 1
        W_old[increaseIndex] = Q1h_WTitem(S_output[increaseIndex], c_total[increaseIndex],
                                            m_list[increaseIndex], t_total[increaseIndex])
        increaseIndex = 0

    # Output a list of stock levels.
    return S_output




print("\n           ==== SOLUTION QUESTION 4 ====          \n")

c_h_list = list(data_Q1_Q3_Q4.iloc[0:15,6])
c_s_list = list(data_Q1_Q3_Q4.iloc[0:15,7])
m_list = list(data_Q1_Q3_Q4.iloc[0:15,4])
t_list =list(data_Q1_Q3_Q4.iloc[0:15,5])
t_s_list =list(data_Q1_Q3_Q4.iloc[0:15,8])
target_wt = 0.001

stockLevels_greedy = Q4a_GreedyWT(c_h_list, m_list, t_list, target_wt)
annualCost_noShip = Q1e_Costs(stockLevels_greedy, c_h_list, m_list, t_list)
aggregateWT_noShip = Q1i_WT(stockLevels_greedy, c_h_list, m_list, t_list)

stockLevels_greedy_ship = Q4d_GreedyWT_Shipping(c_h_list, c_s_list, m_list, t_list, t_s_list, target_wt)
annualCost_ship = Q4b_Costs_Shipping(stockLevels_greedy_ship, c_h_list, c_s_list, m_list, t_list, t_s_list)
aggregateWT_ship = Q4c_WT_Shipping(stockLevels_greedy_ship, c_h_list, c_s_list, m_list, t_list, t_s_list)

print("The optimal stock levels are ", stockLevels_greedy)
print("The annual holding cost is ", annualCost_noShip)
print("The aggregate mean waiting time is ", aggregateWT_noShip)

print("\nGreedy approach with shipping:")
print("The optimal stock levels with shipping are ", stockLevels_greedy_ship)
print("The total annual cost with shipping is ", annualCost_ship)
print("The aggregate mean waiting time with shipping is ", aggregateWT_ship)


