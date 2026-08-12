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

# x = input('Enter Num \n')

# def my_function (x): 
#         square = x*x 
#         cube = x*x*x 
#         my_tuple = (square,cube) 
#         print('Square:',my_tuple[0], 'Cube:',my_tuple[1])  
#         return my_tuple

# if not x.isdigit(): 
#     print('you entered an invalid number') 
# else:    
#     x = int(x)   
#     try:
#         my_function(x) 

#     except Exception as e : 
#         print('try again', e)

#------------------------------------------- count factor occurences. 

# n = input('enter number n \n') 
# f = input('enter factor f \n')
# n = int(n) 
# f = int(f) 

# def my_function(n,f):
 
#     count = 0 
#     while n % f == 0 : 
#         n = n//f
#         count = count +1 

#     print(count, '(since',n, 'is divisible by', f,')') 
#     return count 


# my_function(n,f) 

#----------------------------- sum of digits. 

# n = input('Enter Number \n') 
# n = int(n) 

# def my_function(n): 
#     sum = 0
#     digits = []
    

#     while n > 0: 
#         digits.insert(0,n % 10) 

#         n = n // 10 

#     i = 0
#     while i < len(digits): 
#         sum = digits[i] + sum 
#         i = i + 1 

#     print('the sum is ',sum)

#     return sum 

# my_function(n)

#---------------------------- Finding max and min of in an array. 

# my_list = [12, 2, 44, 15, 13] 

# min = my_list[0] 
# max = my_list[0]


# for i in range(len(my_list)): 
   
#     if(max < my_list[i]): 
#         max = my_list[i]
#     elif(min > my_list[i]): 
#         min = my_list[i]

# print('Max ',max,'\n','Min ',min,'\n')


#------------------------------------ count vowels in a string 

word = str(input('Enter word \n')) 
#word = str('Coding Exercise') 
word = word.lower()
word = word.strip()  

vowel = 0
i = 0 
for i in word:
    if i == 'a' or i =='e' or i == 'i' or i == 'o' or i == 'u': 
        vowel = vowel +1 

print (vowel, 'Vowels ' )  
    

