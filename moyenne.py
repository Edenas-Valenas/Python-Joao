
note_fr = int(input("Note en français? "))
note_math = int(input("Note en Mathématique? "))
note_nl = int(input("Note en nederland? "))
#moyenne = (int(note_fr) + int(note_math) + int(note_nl)) /3


#print("la moyenne est de " + str(moyenne))
#print("La note moyenne est de " + str((note_fr + note_math + note_nl)//3))

#print("La note moyenne est de " + str((int(input("Note en français? ")) + int(input("Note en Mathématique? ")) + int(input("Note en nederland? ")))//3))

print(f"La note moyenne est de {(note_fr + note_math + note_nl)//3}")
