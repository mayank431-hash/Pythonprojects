import datetime
dob=input("ENter the date of birth in (DD-MM-YYYY) format:")
dob=datetime.datetime.strptime(dob,"%d-%m-%Y").date()
today=datetime.date.today()
age=today.year-dob.year
if(today.month,today.day)<(dob.month,dob.day):
    age-=1

print("your age is:",age,"years")