#CE PROGRAME sert a convertire les temperature

while " ":
    print("Repondez par A ou par B")
    answer = input ("Quelle unitée souhaitez vous convertir ? ")
    A = "fahrenheit"
    B = "celsius"
        
    if answer == "A":
        f = input ("fahrhenheit:" )
        c = ( int(f) - 32) * 5//9
        print ( str(c) + "c°" )
        break
    
    elif answer == "B":
        c = input ("celsius:")
        f = ( int(c) * 9/5) + 32
        print ( str(f) + "F°")
        break