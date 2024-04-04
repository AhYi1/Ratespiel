from random import randint

niedrige_num, hohe_num = 1, 20
zufall_num : int = randint(niedrige_num,hohe_num)
print(f"Rate eine Zahl von {niedrige_num} bis {hohe_num}.")

while True:
    try:
        nutzer_eingabe : int = int(input("Rate: "))
    except ValueError as e:
        print ("Bitte gib eine gültige Zahl ein")
        continue

    if nutzer_eingabe > zufall_num:
        print("Die Zahl ist niedriger") 
    elif nutzer_eingabe < zufall_num:
        print("Die Zahl ist höher")  
    else:
        print("Die Zahl ist richtig!!!")
        break