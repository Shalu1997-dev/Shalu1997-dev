
import datetime  
birthday=input("What is your next B'day Date? (in DD/MM/YYYY) ")  
birthdate=datetime.datetime.strptime(birthday,"%d/%m/%Y").date()  
today=datetime.date.today();  
years= today.year-birthdate.year;  
print( "Your are " +" "+ str(years) +" "+" You are Getting old !")