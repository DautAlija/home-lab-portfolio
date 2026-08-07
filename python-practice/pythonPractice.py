import math 
#print('hello world') 
#------------------------- checking even or odd input. 
#x = int(input('Enter a number: \n'))  
#
#if x % 2 == 0: 
#    print ('even')

#else : 
#    print('odd') 

#----------------------- list splitting 

# nums = [12,5,8,21,14,3]
# numEven =[] 
# numOdd =[] 

#for x in nums :  
 #   if x % 2 == 0 : 
  #      numEven.append(x)
   # else : 
    #    numOdd.append(x)
       
#print('odd Nums ', numOdd) 
#print('even Nums ', numEven) 
#print ('Og list ', nums) 

# -------------------------------------------------------------  Prime number 
# x = int(input('Enter num \n'))
# isPrime = True

# if x <= 1: 
#      print ('not prime') 
#      exit
# else:  
#     limit = int(math.sqrt(x)) 
#     for i in range(2, limit+1): 
#         if x % i == 0: 
#         # print ('not prime ',i) 
#          isPrime = False
        
#         else: 
#           #  print('prime ', i)
#           isPrime =True

# if isPrime : 
#    print('Prime') 
# else: 
#    print('Not Prime') 

#------------------- palindrome number check. 

# x = input('Enter Number \n') 

# try:  
#     palindrome = True 

#     if not x.isdigit(): 
#         print('try again') 
#     else: 
#         s =  str(x) 
#         reverseS = s[:: -1] 

#     if s != reverseS: 
#         palindrome = False 

#     if palindrome: 
#         print(s, ' This is a palindrome')
#     else: 
#         print(s, ' This is not a palindrome')

# except: 
#     print('not a valid number ') 

#--------------------------- sef answer 

# if not x.isdigit():
#   print("try again")
# else:
#   s = str(x)
#   reverseS = s[:: -1]


# if s == reverseS:
#   print("yes")
# else:
#   print("no")

#-------------------------------------- square and cube generator

x = input('Enter Num \n')

def my_function (x): 
        square = x*x 
        cube = x*x*x 
        my_tuple = (square,cube) 
        print('Square:',my_tuple[0], 'Cube:',my_tuple[1])  
        return my_tuple

if not x.isdigit(): 
    print('not number') 
else:    
    x = int(x)   
    try:
        my_function(x) 

    except Exception as e : 
        print('try again', e)