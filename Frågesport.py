points=0

#Fråga 1
print("1. Vem skapade den första algoritmen?")
print("A) Ada Lovelace")
print("B) Grace Hopper")
print("C) Margaret Hamilton")
print("D) Johan Wrangö")


answer=input("Svar:")
if answer.upper() == "A":
    print("Rätt!")
    points+=1
else:
    print("Fel")

#Fråga 2
print("2. När skapde Ada Lovelace den första algoritmen?")
print("A) 1900-talet")
print("B) 1500-talet")
print("C) 1800-talet")
print("D) 1700-talet")


answer=input("Svar:")
if answer.upper() == "C":
    print("Rätt!")
    points+=1
else:
    print("Fel")

#Fråga 3
print("3. Vad introducerades på 1900-talet för att programmera tidiga datorer?")
print("A) Matte")
print("B) Python")
print("C) Hålkort")
print("D) Keyboards")


answer=input("Svar:")
if answer.upper() == "C":
    print("Rätt!")
    points+=1
else:
    print("Fel")

#Fråga 4
print("4. Vilka arbetade mest progamering på 1940-talet?")
print("A) Män")
print("B) Kvinnor")
print("C) Både män och kvinnor")
print("D) Ingen jobbade med progamering")


answer=input("Svar:")
if answer.upper() == "B":
    print("Rätt!")
    points+=1
else:
    print("Fel")

#Fråga 5
print("5. Vilket språk utväcklade Grace Hopper?")
print("A) CBAT")
print("B) C++")
print("C) Engelska")
print("D) COBOL")


answer=input("Svar:")
if answer.upper() == "D":
    print("Rätt!")
    points+=1
else:
    print("Fel")

#Fråga 6
print("6. Margaret Hamilton ledde mjukvaruutvecklingen på vilket program?")
print("A) Apolloprogrammet")
print("B) Operation Barbarossa")
print("C) Manhattan Project")
print("D) All of the above")


answer=input("Svar:")
if answer.upper() == "A":
    print("Rätt!")
    points+=1
else:
    print("Fel")

#Fråga 7
print("7. När blev programering ett högstatusyrke?")
print("A) 60/70-talet")
print("B) 40-talet")
print("C) 80/90-talet")
print("D) 50-talet")


answer=input("Svar:")
if answer.upper() == "A":
    print("Rätt!")
    points+=1
else:
    print("Fel")

#Fråga 8
print("8. När spreds internet?")
print("A) 1990")
print("B) 2010")
print("C) 1970")
print("D) 1980")


answer=input("Svar:")
if answer.upper() == "A":
    print("Rätt!")
    points+=1
else:
    print("Fel")

#Fråga 9
print("9. Man använder html, css och vad för sidor?")
print("A) Python")
print("B) JavaScrip")
print("C) C#")
print("D) Spanska")


answer=input("Svar:")
if answer.upper() == "B":
    print("Rätt!")
    points+=1
else:
    print("Fel")

#Fråga 10
print("10. Hur används programering idag?")
print("A) Spel och datorer")
print("B) Sjukvården")
print("C) Forskning")
print("D) All of the above")


answer=input("Svar:")
if answer.upper() == "D":
    print("Rätt!")
    points+=1
else:
    print("Fel")

print("Du fick:"+str(points)+"/10")

if points == 10:
    print("Utmärkt, du kan allt!")
elif points <=9 and points>=7:
     print("Wow, nästan alla rätt!")
else:
    print("Kanske borde plugga mer")
