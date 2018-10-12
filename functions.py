#################################################################################################
#   ****FUNCTIONS****                                                                           #
#   This tests whether or not a given function is injective, surjective, bijective, or neither  #
#   In addition, it will count the number of functions, injections, and bijections when         #
#   given a particular domain and codomain                                                      #
#                                                                                               #
#   Kehlsey Lewis                                                                               #
#   MTH 225(03)                                                                                 #
#                                                                                               #
#################################################################################################

################################################################################################
# is_inj: This takes in a dictionary and determines whether or not it is an injective function.
# It will return true if it is and false if it is not 
################################################################################################

def is_inj(diction):
    #default value for answer
    answer = True    
    #creating an empty list to keep track which domains and codomains have already been used
    list1=[]
    list2=[]
    
    #going through the dictionary values (codomain) to make sure there aren't duplicates 
    for value in diction.values():
        #if it isn't a duplicate it will be added to the check list
        if value not in list1:
            list1.append(value)
        #if it is a duplicate then it isn't an injective function
        else:
            answer = False
            
    #going through the keys and making sure that the function given is valid
    for key in diction.keys():
        if key not in list2:
            list2.append(key)
        #if key is a duplicate then it is not a function and not an injective function
        else:
            answer = False
    return answer

################################################################################################
# is_surj: This takes in a dictionary and a list. The function will deteremine whether or not it
# is surjective. It will return the Boolean value True if it is, and False if it is not.
################################################################################################

def is_surj(diction, codomain):
    #the default value
    answer = True
    
    #going through the codomain
    for x in codomain: 
        #making sure all codomains are accounted for
        if x not in diction.values():  
            #if a codomain is missing it will change the answer to false
            answer = False
            
    #going through the keys and making sure that the function given is valid        
    list2 = []       
    for key in diction.keys():
        if key not in list2:
            list2.append(key)
            
        #if key is a duplicate then it is not a function and not an injective function
        else:
            answer = False
            
    return answer

################################################################################################
# is_bij: This takes in a dictionary and a list. The function will deteremine whether or not it
# is bijective. It will return the Boolean value True if it is, and False if it is not.
################################################################################################

def is_bij(diction, codomain):
    #setting a default value
    answer = False
    
    #if it is both an injection and a surjection, then it is a bijection
    if is_inj(diction) == True and is_surj(diction, codomain) == True:
        answer = True
    return answer

################################################################################################
# count_func: This takes in a domain and a codomain. The function will  the number of functions
# that are possible with the given domain and codomain. It will return the total number.
################################################################################################

def count_func(domain, codomain):
    #going to go through the domain and codomain to remove duplicates to get exact amount of possibilities
   
    #creating an empty list to remove duplicates in the domain
    newdomain = []   
    #goes through the given domain and removes duplicates and adds them to the new list
    for x in domain:
        if x not in newdomain:
            newdomain.append(x)
            
    #creating an empty list to remove duplicates in the codomain 
    newcodomain = []   
    #goes through the given codomain and removes duplicates and adds them to the new list
    for y in codomain:
        if y not in newcodomain:
            newcodomain.append(y)
            
    
    #getting the length of the the new domain list
    domainLen = len(newdomain)
    #getting the length of the the new codomain list
    codomainLen = len(newcodomain)
    #the number total functions is the length of codomain to the length of domain power
    answer = codomainLen ** domainLen
    return answer

################################################################################################
# count_inj: This takes in a domain and codomain. The function will count the number of 
# injections possible for the given domain and codomain . It will return the total number.
################################################################################################

def count_inj(domain, codomain):
    
    #going to go through the domain and codomain to remove duplicates to get exact amount of possibilities
   
    #creating an empty list to remove duplicates in the domain
    newdomain = []   
    #goes through the given domain and removes duplicates and adds them to the new list
    for x in domain:
        if x not in newdomain:
            newdomain.append(x)
            
    #creating an empty list to remove duplicates in the codomain 
    newcodomain = []   
    #goes through the given codomain and removes duplicates and adds them to the new list
    for y in codomain:
        if y not in newcodomain:
            newcodomain.append(y)
            
    
    #getting the length of the the new domain list
    domainLen = len(newdomain)
    #getting the length of the the new codomain list
    codomainLen = len(newcodomain)
    
    #if there are less elements in the codomain than there are in the domain,
    #then there are no injections
    if codomainLen < domainLen:
        return 0 

    #if the number of elements are equal then have to check for repeated values
    elif codomainLen == domainLen:
        
        #making a list to hold checked values
        check = []
        #going through the codomain
        for x in codomain:
            #checking if the element is repeated
            if x not in check:
                check.append(x)
            else:
                #returns zero if there is a repeated value
                return 0
        return codomainLen * 2    
    
    #otherwise it will take the factorial of the codomains length
    else:
        n = codomainLen
        num = 1
        while n >= 1:
            num = num * n
            n = n - 1
        return num
################################################################################################
# count_inj: This takes in a domain and codomain. The function will count the number of 
# bijections possible for the given domain and codomain . It will return the total number.
################################################################################################
    
def count_bij(domain, codomain):
    
    #the number of elements have to be equal for there to be a bijection
    if len(codomain) == len(domain):
        
        #checking to make sure each codomain and domain have distinct elements
        #creating a check list
        check = []
        
        #checking over the domain elements
        for x in domain:
            #if it is not repeated it will be added to the check list
            if x not in check:
                check.append(x)
            else:
                #if an element is repeated, then a bijection is not possible
                return 0
        #creating second check list to check the codomain
        check_2=[]
        
        #checking over the codomain elements
        for y in codomain:
            #if the element is not repeated it will be added to the list
            if y not in check_2:
                check_2.append(y)
            else:
                #will return zero if its repeated
                return 0
         #if there are no problems then it will return the number of elements times 2   
        return len(codomain) * 2 
    
    else:
       return 0   
       