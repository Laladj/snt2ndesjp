#capital d'une banque
from datetime import date #permet d'avoir l'année, à ignorer
todays_date = date.today()#permet d'avoir l'année, à ignorer
capital = float(input("entrez le capital "))
taeg = float(input("entrez le taux d'interet décimal "))
annees = int(input("entrew le nombre d'années ou vous souhaitez laisser votre capital "))
x = 0
if capital < 0 or taeg < 0:
	print("erreur")
	quit()
elif taeg == 0:
	x = capital
else: x=capital*taeg**annees

print(f"vous aurez {x} à la fin de l'année {todays_date.year + annees}")#permet d'avoir l'année, à ignorer 
