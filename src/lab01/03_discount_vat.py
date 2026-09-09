price = int(input("Цена: "))
discount = int(input("Скидка: "))
vat = int(input("НДС: "))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base:>12.2f} ₽")
print(f"НДС: {vat_amount:>12.2f} ₽")
print(f"Итого к оплате: {total:>12.2f} ₽")