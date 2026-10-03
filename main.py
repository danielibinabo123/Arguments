def total_calc(bill_amount, tip_percentage):
    total=bill_amount*(1+0.01*tip_percentage)
    total=round(total,2)
    print(f"please pay ${total}")

bill=float(input("enter the bill:"))
tip=20
total_calc(bill,tip)