print("------Electricity Bill Calculation------")
unit1= int(input('enter the 1st floor unit:'))
unit2= int(input('enter the 2nd floor unit:'))
unit3= int(input('enter the 3rd floor unit:'))
floor1=unit1*7
print(f'first floor electricity bill:{floor1}')
floor2=unit2*7
print(f'second floor electricity bill:{floor2}')
floor3=unit3*8
print(f'third floor electricity bill:{floor3}')
total=float(input('enter the total bill:'))
mbill=(total-(floor1+floor2+floor3))/2  #mbill-maintainance amount
print(f'maintainance amount:{mbill}')
print(f'final first floor bill:{floor1+mbill}')
print(f'final second floor bill:{floor2+mbill}')
print(f'final third floor bill:{floor3}')
