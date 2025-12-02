import os # , sys
import sys
import pandas as pd
import numpy

# Write functions to check if two answers are close enough together.

# Check if two numbers are close.
def match_number(n1,n2,allowed_error=0.001):
    
    if n1!=0:
        return abs(abs(n1-n2))/n1<allowed_error
    else:
        return abs(n1-n2)<allowed_error
    
def match_number_lessthan(expected, actual):
    """
    Checks if 'actual' is less than or equal to 'expected'.
    Returns True if actual <= expected, False otherwise.
    """
    return actual <= expected
    

# Check if two lists of numbers are close.
# Note the lists should consist of numbers.
def match_list(list1,list2,allowed_error=0.001):
    
    # Lists must be of the same length.
    if len(list1)!=len(list2):
        return False
    
    for i in range(len(list1)):
        l1 = list1[i]
        l2 = list2[i]
        
        # Check if the dictionary we are comparing to has the correct data structure.
        if not (isinstance(l2, int) or isinstance(l2, float) 
                or isinstance(l2, numpy.float64)):
            return False
        
        # If the items are not close enough together return False.
        if not match_number(l1,l2):
            return False
        
    return True



# Check if two dictionaries of numbers are close.
# Note the dictionaries should consist of numbers.
def match_dict(dict1,dict2,allowed_error=0.001):
    
    # Lists must be of the same length.
    if dict1.keys()!=dict1.keys():
        return False
    
    for k in dict1.keys():
        d1 = dict1[k]
        d2 = dict2[k]
        
        # Check if the dictionary we are comparing to has the correct data structure.
        if type(1)!=type(d2) and type(0.9)!=type(d2):
            return False
        
        # If the items are not close enough together return False.
        if not match_number(d1,d2):
            return False
        
    return True

# Add the folder submission to the path of files where our scipt looks.
# This allows us to call the students' script as student(.py).
# The students' code should be in the Submissions.
sys.path.insert(0, 'Submissions/')

# Generate a list of all the submissions by students.
files = []
for file in os.listdir(r"Submissions"):
    if file.endswith(".py"):
     
        
        # Jump over the dobr_rsnq file
        if file=='dobr_rsnq.py': continue
        
        files.append(os.path.splitext(file)[0])

# The following dictionary will have as keys the different questions and 
# for each question it will have a list of lists corresponding to test cases.
# So test_cases_dict[1][1] is the first test case of the first problem.
# test_cases_dict[1][1] is a list of two lists. The first list is the input and
# the second list is the output.
test_cases = dict()

# test_cases should be in the same folder as the auto grader.
f = open("test_cases.txt", "r")
lines = f.readlines()
question = 0
reading = 0 # 0 for input, 1 for output

for l in lines:
    test_case = -1

    # Set the current question being read in.
    if l[0]=="Q":
        # Q indicates that the next question 
        question = l.strip("\n")
        test_cases[question]=[]
    elif l[0:5]=="Input":
        reading = 0
        test_case +=1
        # Add a list to store input
        # One could argue that the list containing the answers is unnecessary.
        test_cases[question].append([[],[]])
    elif l[0:6]=="Output":
        reading = 1
    # Skip over white lines.
    elif l[0]=="\n":
        continue
    else:
        # The eval function evaluates text and interprets it as a variable.
        test_cases[question][test_case][reading].append(eval(l))
    # If the line start with a "{" it is a dictionary

# Create a data frame to store the results in.
df = pd.DataFrame(files,columns=["File name"])

for i in range(len(files)):
    student = __import__(files[i])
    
    # Helps in debugging when students make errors.
    print(i, files[i])
    
    # Write the students' information to the file.
    df.at[i,'student 1 name']=student.student1_name
    df.at[i,'student 1 surname']=student.student1_surname
    
    df.at[i,'student 2 name']=student.student2_name
    df.at[i,'student 2 surname']=student.student2_surname
    
    
    # QUESTION 1a
    # Set the answer to correct.
    # In the code below check if it contains an error.
    # Q1 means this is question 1
    df.at[i, 'Q1a'] = 3
    
    # For every question we loop over the different test cases.
    # In this case for Q1.
    for j in range(len(test_cases['Q1a'])):
        
        # Select the current tes case.
        current_test_case = test_cases['Q1a'][j]
        
        # Try-except catches certain errors.
        # This does not catch infinite loops.
        try:
            # Call the necessary variables to conduct the test.
            S = current_test_case[0][0]
            c_a = current_test_case[0][1]
            m = current_test_case[0][2]
            t = current_test_case[0][3]
            
            # Store the result of the exercise.
            result = student.Q1a_EBOitem(S,c_a,m,t)    
            
            #Check if the result matches the result we got for the test case.
            #This is done via the functions defined at the top.
            if not match_number(current_test_case[1][0],result):
                df.at[i, 'Q1a'] = 0
                
        except Exception as e:
            # E1 means  1
            df.at[i, 'Q1a'] = 0
            df.at[i, 'E1a'] = str(e)

    # QUESTION 1b
    df.at[i, 'Q1b'] = 3
    
    for j in range(len(test_cases['Q1b'])):
        
        current_test_case = test_cases['Q1b'][j]
        
        try:
            S_list = current_test_case[0][0]
            c_a_list = current_test_case[0][1]
            m_list = current_test_case[0][2]
            t_list = current_test_case[0][3]
            
            result = student.Q1b_EBO(S_list,c_a_list,m_list,t_list)       
            
            if not match_number(current_test_case[1][0],result):
                df.at[i, 'Q1b'] = 0
                
        except Exception as e:
            df.at[i, 'Q1b'] = 0
            df.at[i, 'E1b'] = str(e)
            
    # QUESTION 1c
    df.at[i, 'Q1c'] = 3
    
    for j in range(len(test_cases['Q1c'])):
        
        current_test_case = test_cases['Q1c'][j]
        
        try:
            S = current_test_case[0][0]
            c_a = current_test_case[0][1]
            m = current_test_case[0][2]
            t = current_test_case[0][3]
            
            result = student.Q1c_PBOitem(S,c_a,m,t)        
            
            if not match_number(current_test_case[1][0],result):
                df.at[i, 'Q1c'] = 0
                
        except Exception as e:
            df.at[i, 'Q1c'] = 0
            df.at[i, 'E1c'] = str(e)
            
    # QUESTION 1d
    df.at[i, 'Q1d'] = 3
    
    for j in range(len(test_cases['Q1d'])):
        
        current_test_case = test_cases['Q1d'][j]
        
        try:
            S_list = current_test_case[0][0]
            c_a_list = current_test_case[0][1]
            m_list = current_test_case[0][2]
            t_list = current_test_case[0][3]
            
            result = student.Q1d_PBO(S_list,c_a_list,m_list,t_list)      
            
            if not match_number(current_test_case[1][0],result):
                df.at[i, 'Q1d'] = 0
                
        except Exception as e:
            df.at[i, 'Q1d'] = 0
            df.at[i, 'E1d'] = str(e)  
            
    # QUESTION 1e
    df.at[i, 'Q1e'] = 3
    
    for j in range(len(test_cases['Q1e'])):
        
        current_test_case = test_cases['Q1e'][j]
        
        try:
            S_list = current_test_case[0][0]
            c_a_list = current_test_case[0][1]
            m_list = current_test_case[0][2]
            t_list = current_test_case[0][3]
            
            result = student.Q1e_Costs(S_list,c_a_list,m_list,t_list)        
            
            if not match_number(current_test_case[1][0],result):
                df.at[i, 'Q1e'] = 0
                
        except Exception as e:
            df.at[i, 'Q1e'] = 0
            df.at[i, 'E1e'] = str(e) 
            
    # QUESTION 1f
    df.at[i, 'Q1f'] = 3
    
    for j in range(len(test_cases['Q1f'])):
        
        current_test_case = test_cases['Q1f'][j]
        
        try:
            S = current_test_case[0][0]
            c_a = current_test_case[0][1]
            m = current_test_case[0][2]
            t = current_test_case[0][3]
            
            result = student.Q1f_FRitem(S, c_a, m, t)        
            
            if not match_number(current_test_case[1][0],result):
                df.at[i, 'Q1f'] = 0
                
        except Exception as e:
            df.at[i, 'Q1f'] = 0
            df.at[i, 'E1f'] = str(e) 
            
    # QUESTION 1g
    df.at[i, 'Q1g'] = 3
    
    for j in range(len(test_cases['Q1g'])):
        
        current_test_case = test_cases['Q1g'][j]
        
        try:
            S_list = current_test_case[0][0]
            c_a_list = current_test_case[0][1]
            m_list = current_test_case[0][2]
            t_list = current_test_case[0][3]
            
            result = student.Q1g_FR(S_list,c_a_list,m_list,t_list)        
            
            if not match_number(current_test_case[1][0],result):
                df.at[i, 'Q1g'] = 0
                
        except Exception as e:
            df.at[i, 'Q1g'] = 0
            df.at[i, 'E1g'] = str(e) 
            
    # QUESTION 1h
    df.at[i, 'Q1h'] = 3
    
    for j in range(len(test_cases['Q1h'])):
        
        current_test_case = test_cases['Q1h'][j]
        
        try:
            S = current_test_case[0][0]
            c_a = current_test_case[0][1]
            m = current_test_case[0][2]
            t = current_test_case[0][3]
            
            result = student.Q1h_WTitem(S, c_a, m, t)       
            
            if not match_number(current_test_case[1][0],result):
                df.at[i, 'Q1h'] = 0
                
        except Exception as e:
            df.at[i, 'Q1h'] = 0
            df.at[i, 'E1h'] = str(e) 
            
    # QUESTION 1i
    df.at[i, 'Q1i'] = 3
    
    for j in range(len(test_cases['Q1i'])):
        
        current_test_case = test_cases['Q1i'][j]
        
        try:
            S_list = current_test_case[0][0]
            c_a_list = current_test_case[0][1]
            m_list = current_test_case[0][2]
            t_list = current_test_case[0][3]
            
            result = student.Q1i_WT(S_list, c_a_list, m_list, t_list)     
            
            if not match_number(current_test_case[1][0],result):
                df.at[i, 'Q1i'] = 0
                
        except Exception as e:
            df.at[i, 'Q1i'] = 0
            df.at[i, 'E1i'] = str(e) 
            

    # QUESTION 2b
    df.at[i, 'Q2b'] = 2
    
    for j in range(len(test_cases['Q2b'])):
        
        current_test_case = test_cases['Q2b'][j]
        
        try:
            d_list = current_test_case[0][0]
            
            
            result = student.Q2b_NewDemandRates(d_list)        
            
            if not match_number(current_test_case[1][0],result):
                df.at[i, 'Q2b'] = 0
                
        except Exception as e:
            df.at[i, 'Q2b'] = 0
            df.at[i, 'E2b'] = str(e)
            
    # QUESTION 2c
    df.at[i, 'Q2c'] = 5
    
    for j in range(len(test_cases['Q2c'])):
        
        current_test_case = test_cases['Q2c'][j]
        
        try:
            c_a_list = current_test_case[0][0]
            m_list = current_test_case[0][1]
            t_list = current_test_case[0][2]
            target_ebo = current_test_case[0][3]
            
            result = student.Q2c_Greedy(c_a_list,m_list,t_list, target_ebo)  
            
            if not match_list(current_test_case[1][0],result):
                df.at[i, 'Q2c'] = 0
                
        except Exception as e:
            # E1 = error 1
            df.at[i, 'Q2c'] = 0
            df.at[i, 'E2c'] = str(e)    
            
    # QUESTION 2d
    df.at[i, 'Q2d'] = 5
    
    for j in range(len(test_cases['Q2d'])):
        
        current_test_case = test_cases['Q2d'][j]
        
        try:
            c_a_list = current_test_case[0][0]
            m_list = current_test_case[0][1]
            t_list = current_test_case[0][2]
            target_ebo = current_test_case[0][3]
            
            result = student.Q2d_ItemApproach(c_a_list, m_list, t_list, target_ebo)
            
            if not match_list(current_test_case[1][0],result):
                df.at[i, 'Q2d'] = 0
                
        except Exception as e:
            # E1 = error 1
            df.at[i, 'Q2d'] = 0
            df.at[i, 'E2d'] = str(e) 
     
            
    # QUESTION 3a
    df.at[i, 'Q3a'] = 4
    
    for j in range(len(test_cases['Q3a'])):
        
        current_test_case = test_cases['Q3a'][j]
        
        try:
            c_a_list = current_test_case[0][0]
            m_list = current_test_case[0][1]
            t_list = current_test_case[0][2]
            target_W = current_test_case[0][3]
            
            result = student.Q3a_itemWT_Consultant1(c_a_list,m_list,t_list,target_W)  
            
            if not match_list(current_test_case[1][0],result):
                df.at[i, 'Q3a'] = 0
                
        except Exception as e:
            # E1 = error 1
            df.at[i, 'Q3a'] = 0
            df.at[i, 'E3a'] = str(e)    

    # QUESTION 3b
    df.at[i, 'Q3b'] = 4
    
    for j in range(len(test_cases['Q3b'])):
        
        current_test_case = test_cases['Q3b'][j]
        
        try:
            # Call the necessary variables to conduct the test.
            c_a_list = current_test_case[0][0]
            m_list = current_test_case[0][1]
            t_list = current_test_case[0][2]
            target_W = current_test_case[0][3]
            
            result = student.Q3b_itemWT_Consultant2(c_a_list,m_list,t_list,target_W)
            
            if not match_list(current_test_case[1][0],result):
                df.at[i, 'Q3b'] = 0
                
        except Exception as e:
            df.at[i, 'Q3b'] = 0
            df.at[i, 'E3b'] = str(e) 
            
    # QUESTION 3c
    df.at[i, 'Q3c'] = 4
    
    for j in range(len(test_cases['Q3c'])):
        
        current_test_case = test_cases['Q3c'][j]
        
        try:
            # Call the necessary variables to conduct the test.
            c_a_list = current_test_case[0][0]
            m_list = current_test_case[0][1]
            t_list = current_test_case[0][2]
            target_W = current_test_case[0][3]
            
            result = student.Q3c_itemWT_Consultant3(c_a_list,m_list,t_list,target_W)
            
            if not match_list(current_test_case[1][0],result):
                df.at[i, 'Q3c'] = 0
                
        except Exception as e:
            df.at[i, 'Q3c'] = 0
            df.at[i, 'E3c'] = str(e) 
 
   
 

    # QUESTION 4a
    df.at[i, 'Q4a'] = 4
    
    for j in range(len(test_cases['Q4a'])):
        
        current_test_case = test_cases['Q4a'][j]
        
        try:
            c_h_list = current_test_case[0][0]
            m_list = current_test_case[0][1]
            t_list = current_test_case[0][2]
            target_wt = current_test_case[0][3]
            
            result = student.Q4a_GreedyWT(c_h_list, m_list, t_list, target_wt)      
            
            if not match_list(current_test_case[1][0],result):
                df.at[i, 'Q4a'] = 0
                
        except Exception as e:
            df.at[i, 'Q4a'] = 0
            df.at[i, 'E4a'] = str(e)
            
    # QUESTION 4b
    df.at[i, 'Q4b'] = 4
    
    for j in range(len(test_cases['Q4b'])):
        
        current_test_case = test_cases['Q4b'][j]
        
        try:
            S_list = current_test_case[0][0]
            c_h_list = current_test_case[0][1]
            c_s_list = current_test_case[0][2]
            m_list = current_test_case[0][3]
            t_list = current_test_case[0][4]
            t_s_list = current_test_case[0][5]
            
            result = student.Q4b_Costs_Shipping(S_list, c_h_list, c_s_list, m_list, t_list, t_s_list)      
            
            if not match_number(current_test_case[1][0],result):
                df.at[i, 'Q4b'] = 0
                
        except Exception as e:
            df.at[i, 'Q4b'] = 0
            df.at[i, 'E4b'] = str(e)
            
    # QUESTION 4c
    df.at[i, 'Q4c'] = 4
    
    for j in range(len(test_cases['Q4c'])):
        
        current_test_case = test_cases['Q4c'][j]
        
        try:
            S_list = current_test_case[0][0]
            c_h_list = current_test_case[0][1]
            c_s_list = current_test_case[0][2]
            m_list = current_test_case[0][3]
            t_list = current_test_case[0][4]
            t_s_list = current_test_case[0][5]
            
            result = student.Q4c_WT_Shipping(S_list, c_h_list, c_s_list, m_list, t_list, t_s_list)     
            
            if not match_number(current_test_case[1][0],result):
                df.at[i, 'Q4c'] = 0
                
        except Exception as e:
            df.at[i, 'Q4c'] = 0
            df.at[i, 'E4c'] = str(e)
  
    # QUESTION 4d
    df.at[i, 'Q4d'] = 4
    
    for j in range(len(test_cases['Q4d'])):
        
        current_test_case = test_cases['Q4d'][j]
        
        try:
            c_h_list = current_test_case[0][0]
            c_s_list = current_test_case[0][1]
            m_list = current_test_case[0][2]
            t_list = current_test_case[0][3]
            t_s_list = current_test_case[0][4]
            target_wt = current_test_case[0][5]
            
            result = student.Q4d_GreedyWT_Shipping(c_h_list, c_s_list, m_list, t_list, t_s_list, target_wt)     
            
            if not match_list(current_test_case[1][0],result):
                df.at[i, 'Q4d'] = 0
                
        except Exception as e:
            df.at[i, 'Q4d'] = 0
            df.at[i, 'E4d'] = str(e)


df.to_excel("results.xlsx")