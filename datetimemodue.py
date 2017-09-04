import datetime

print("-----------------------------------------")
print("Current Date and Time:->", datetime.datetime.today()) # today and now functions both are same
print("Current Date and Time:->", datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S'))
print("Form the date:-", datetime.datetime(2015, 5, 15, 17, 15))
print("Difference:->", datetime.datetime.now() - datetime.datetime(2015, 5, 15, 17, 15 ))
print("Current Date ->", datetime.date.today()) # today and now functions both are same



print("-----------------------------------------")