import arrow
a = arrow.utcnow()
print("Current date and time:")
print(a)
print("\nReplace hour and minute with 5 and 35:")
print(a.replace(hour=5, minute=35))
print("\nReplace day with 2:")
print(a.replace(day=2))
print("\nReplace year with 2021:")
print(a.replace(year=2021))
print("\nReplace month with 11:")
print(a.replace(month=11)) 
print("\nReplace timezone with 'US/Pacific:")
print(a.replace(tzinfo='US/Pacific'))
