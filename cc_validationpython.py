def cc_validation(CardNumber):
     
    Total_digits = len(CardNumber)
     if Total_digits == 0:
          return False
    Sum_of_digits = 0
    isSecond = False
     
    for i in range(Total_digits - 1, -1, -1):
        d = ord(CardNumber[i]) - ord('0')
     
        if (isSecond == True):
            d = d * 2
  
        # Addition of two digits for conversion into single digit
        
        Sum_of_digits += d // 10
        Sum_of_digits += d % 10
  
        isSecond = not isSecond
     
    if (Sum_of_digits % 10 == 0):
        return True
    else:
        return False
 
# Driver code   
if __name__=="__main__":
     
    CardNumber = input(" Enter your Credit card number :- ")
     
    if (cc_validation(CardNumber)):
        print("{0} is a valid credit card number provided. ".format(CardNumber))
    else:
        print("{0} is not a valid credit card number, kindly re-check the number ".format(CardNumber))
