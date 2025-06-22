print("Bill Split Calculator")

bill_amount = float(input())
tip_percentage = float(input())

tip_amount = bill_amount * (tip_percentage / 100)

print(f"Total (including tip): ${bill_amount + tip_amount}")

number_of_people = int(input())

print(f"Each person pays: ${(bill_amount + tip_amount) / number_of_people}")
