### Exception Handling


# Exception  -  error

# i=int(input('enter a number'))
# print('number given:',i)

#  try:
#      i=int(input('enter a number:'))
#      print('Number given:',i)
#  except:
#      print('something wrong')  


#  try:
#      i=int(input('enter number1:'))
#      j=int(input('enter number2'))
#      print('Division:',i)
#  except ValueError:
#      print('wrong value given')
#  except ZeroDivisionError:
#      print('error in division')
#  except NameError:
#      print('defination error')
#  except:
#      print('unknown error')            




# class AgeError(Exception):
#     pass
 
 
# age=int(input('enter age'))
# 
# if age>=18:
#     print('ok')
# else:
#     raise AgeError('age must be 18+')    