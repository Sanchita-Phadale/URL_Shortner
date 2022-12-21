import pyshorteners
s = pyshorteners.Shortener()

url = input("Enter any url: ")
print("Shortened Url: ", s.chilpit.short(url))
