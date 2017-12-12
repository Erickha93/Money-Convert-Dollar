from pcinput import getFloat
'''
Write a program that:asks user for an amount of money in dollars and money
(use input function)Your code should print back the amount entered by the user
Your program should list the monetary equivalent of the amount entered in
100 dollar bills, 50 dollar bills, 20 dollar bills, 10 dollar bills, 5 dollar
bills, 1 dollar bills, 25 cent coins, 10 cent coins, 5 cent coins, and 1 cent
coins. Your program should report the maximum number of 100 dollar bills you
can use, then the maximum numer of 50 dollar bils, 20 dollar bills, etc.
'''
## 589.66   186.41
money = getFloat("Enter amount of money: ")

#----------------Variable------------
Dollar_In_Hundred = 100
Dollar_In_Fifty = 50
Dollar_In_Twenty = 20
Dollar_In_Ten = 10
Dollar_In_Five = 5

Cent_In_Dollar = 1
Cent_In_Quarter = 0.25
Cent_In_Dime = 0.10
Cent_In_Nickel = 0.05
Cent_In_Cent = 0.01
#--------------Calculation----------
hundred = int(money / Dollar_In_Hundred)
money -= hundred * Dollar_In_Hundred
fifty = int(money / Dollar_In_Fifty)
money -= fifty * Dollar_In_Fifty
twenty = int(money / Dollar_In_Twenty)
money -= twenty * Dollar_In_Twenty
ten = int(money / Dollar_In_Ten)
money -= ten * Dollar_In_Ten
five = int(money / Dollar_In_Five)
money -= five * Dollar_In_Five

one = int(money / Cent_In_Dollar)
money -= one * Cent_In_Dollar
quarter = int(money / Cent_In_Quarter)
money -= quarter * Cent_In_Quarter
dime = int(money / Cent_In_Dime)
money -= dime * Cent_In_Dime
nickel = int(money / Cent_In_Nickel)
money -= nickel * Cent_In_Nickel
money = round(money, 2)                 #add round decimal to cent
Cent = int(money / Cent_In_Cent)

#-------------Output----------------
print(hundred, " 100 dollar bills")
print(fifty, " 50 dollar bills")
print(twenty, " 20 dollar bills")
print(ten, " 10 dollar bills")
print(five, "  5 dollar bills")

print(one, "  1 dollar bills")
print(quarter, " 25 cent coins")
print(dime, " 10 cent coins")
print(nickel, "  5 cent coins")
print(Cent, "  1 cent coins")

