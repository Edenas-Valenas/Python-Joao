heure = float (input("Combien d'heures se sont écoulées? "))
minutes = float (input("Combien de minutes se sont écoulées? "))
secondes = float (input("Combien de secondes se sont écoulées? "))

heure = heure * 3600
minutes = minutes * 60
print(str(heure + minutes + secondes) + " secondes se sont écoulées au total")