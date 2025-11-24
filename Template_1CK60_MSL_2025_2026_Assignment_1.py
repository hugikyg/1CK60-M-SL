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
# data_Q2 = pd.read_csv("Data_Q2.csv", index_col=0)    

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
        ans += c_a_list[i] * S_list[i]

    # Your output should be a number.
    
    
    return ans


def Q1f_FRitem(S, c_a, m, t):
    # S is the stock level.
    # c_a is the SKU's acquisition cost.
    # m is the number of failures per period.
    # t is the repair leadtime.
    
    ans = 0

    mu = m * t
    
    if mu == 0:
        return 1.0

    ebo_i = Q1a_EBOitem(S, c_a, m, t)
    ans = (1.0 - (ebo_i / mu))
        
    # Your output should be a number.
    
    
    return ans

def Q1g_FR(S_list,c_a_list,m_list,t_list):
    # S_list[i] is the stock level of SKU i.
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.

    ans = 0

    # YOUR CODE GOES HERE.
        
    # Your output should be a number.
    
    
    return ans


def Q1h_WTitem(S, c_a, m, t):
    # S is the stock level.
    # c_a is the SKU's acquisition cost.
    # m is the number of failures per period.
    # t is the repair leadtime.
    
    ans = 0

    # YOUR CODE GOES HERE.
        
    # Your output should be a number.
    
    
    return ans

def Q1i_WT(S_list, c_a_list, m_list, t_list):
    # S_list[i] is the stock level of SKU i.
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.

    ans = 0

    # YOUR CODE GOES HERE.
        
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

print("For question 1d, the PBO for policy A is  ", sumPBOa)
print("For question 1d, the PBO for policy B is  ", sumPBOb)
print("For question 1d, the PBO for policy C is  ", sumPBOc)


print("For question 1e, the total acquisition for policy A is   ....................")
print("For question 1e, the total acquisition for policy B is   ....................")
print("For question 1e, the total acquisition for policy C is   ....................")

print("For question 1f:")
print(f"{'SKU':<6}{'FR_i (A)':>12}{'FR_i (B)':>12}{'FR_i (C)':>12}")
print("-" * 42)

for i in range(len(S_A_list)):
    fr_i_A = Q1f_FRitem(S_A_list[i], c_a_list[i], m_list[i], t_list[i])
    fr_i_B = Q1f_FRitem(S_B_list[i], c_a_list[i], m_list[i], t_list[i])
    fr_i_C = Q1f_FRitem(S_C_list[i], c_a_list[i], m_list[i], t_list[i])
    print(f"{i+1:<6}{fr_i_A:>12.2f}{fr_i_B:>12.2f}{fr_i_C:>12.2f}")



print("For question 1g, the aggregate fill rate for policy A is   ....................")
print("For question 1g, the aggregate fill rate for policy B is   ....................")
print("For question 1g, the aggregate fill rate for policy C is   ....................")

print("For question 1h:")
print(f"{'SKU':<6}{'WT_i (A)':>12}{'WT_i (B)':>12}{'WT_i (C)':>12}")
print("-" * 42)

for i in range(len(S_A_list)):
    wt_i_A = Q1h_WTitem(S_A_list[i], c_a_list[i], m_list[i], t_list[i])
    wt_i_B = Q1h_WTitem(S_B_list[i], c_a_list[i], m_list[i], t_list[i])
    wt_i_C = Q1h_WTitem(S_C_list[i], c_a_list[i], m_list[i], t_list[i])
    print(f"{i+1:<6}{wt_i_A:>12.2f}{wt_i_B:>12.2f}{wt_i_C:>12.2f}")

print("For question 1i, the aggregate mean waiting time for policy A is   ....................")
print("For question 1i, the aggregate mean waiting time for policy B is   ....................")
print("For question 1i, the aggregate mean waiting time for policy C is   ....................")



# %% Question 2

def Q2b_NewDemandRates(d_list):
    # d_list is a list containing the demands over all periods for a SKU.
    
    ans = 0
    
    # YOUR CODE GOES HERE.
    
    # Your output should be a number.
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

    # Output a list of stock levels.
    return S_output




def Q2d_ItemApproach(c_a_list, m_list, t_list, target_ebo):
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # target_ebo is the ebo objective.


    S_output=[0]*len(c_a_list)

    # YOUR CODE GOES HERE.

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




print("The optimal stock levels with greedy approach are .................")
print("The EBO with greedy approach is   .................")
print("The cost with greedy approach is   .................")


print("The optimal stock levels with greedy approach are  .................")
print("The EBO with greedy approach is   .................")
print("The cost with greedy approach is   .................")



print("The optimal stock levels with item approach are  .................")
print("The EBO with item approach is   .................")
print("The cost with item approach is   .................")


print("The optimal stock levels with item approach are  .................")
print("The EBO with item approach is  .................")
print("The cost with item approach is   .................")



# %% Question 3



def Q3a_itemWT_Consultant1(c_a_list,m_list,t_list,target_W):
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # target_W is the waiting time objective.


    S_output=[0]*len(c_a_list)

    # YOUR CODE GOES HERE.

    # Output a list of stock levels.
    return S_output


def Q3b_itemWT_Consultant2(c_a_list,m_list,t_list,target_W):
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # target_W is the waiting time objective.


    S_output=[0]*len(c_a_list)

    # YOUR CODE GOES HERE.

    # Output a list of stock levels.
    return S_output


def Q3c_itemWT_Consultant3(c_a_list,m_list,t_list,target_W):
    # c_a_list[i] is the acquisition cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # target_W is the waiting time objective.


    S_output=[0]*len(c_a_list)

    # YOUR CODE GOES HERE.

    # Output a list of stock levels.
    return S_output



print("\n           ==== SOLUTION QUESTION 3 ====          \n")


c_a_list = list(data_Q1_Q3_Q4.iloc[0:15,3])
m_list = list(data_Q1_Q3_Q4.iloc[0:15,4])
t_list =list(data_Q1_Q3_Q4.iloc[0:15,5])
target_W = 0.05


print("The optimal stock levels from Consultant 1 are ..................")
print("The aggregate mean waiting time from Consultant 1 is  ..................")
print("The cost from Consultant 1 is   ..................")


print("The optimal stock levels from Consultant 2 are  ..................")
print("The aggregate mean waiting time from Consultant 2 is   ..................")
print("The cost from Consultant 2 is   ..................")


print("The optimal stock levels from Consultant 3 are  ..................")
print("The aggregate mean waiting time from Consultant 3 is   ..................")
print("The cost from Consultant 3 is   ..................")




# %% Question 4


def Q4a_GreedyWT(c_h_list, m_list, t_list, target_wt):
    # c_h_list[i] is the holding cost of SKU i.
    # m_list[i] is the number of failures per period of SKU i.
    # t_list[i] is the repair leadtime of SKU i.
    # target_wt is the waiting time objective.


    S_output=[0]*len(c_h_list)

    # YOUR CODE GOES HERE.

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

    # YOUR CODE GOES HERE.
        
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

    # YOUR CODE GOES HERE.
        
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

    # YOUR CODE GOES HERE.

    # Output a list of stock levels.
    return S_output




print("\n           ==== SOLUTION QUESTION 4 ====          \n")


c_h_list = list(data_Q1_Q3_Q4.iloc[0:15,6])
c_s_list = list(data_Q1_Q3_Q4.iloc[0:15,7])
m_list = list(data_Q1_Q3_Q4.iloc[0:15,4])
t_list =list(data_Q1_Q3_Q4.iloc[0:15,5])
t_s_list =list(data_Q1_Q3_Q4.iloc[0:15,8])
target_wt = 0.001


print("The optimal stock levels are ................")
print("The question 4, the annual holding cost is   ................")
print("The question 4, the aggregate mean waiting time is   ................")

    

print("The question 4, the optimal stock levels with shipping are  ................")
print("The question 4, total annual cost with shipping is   ................")
print("The question 4, the aggregate mean waiting time with shipping is   ................")

