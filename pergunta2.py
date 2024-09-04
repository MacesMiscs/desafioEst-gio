palavra=input("Digite uma palavra: ")
contagemLower=palavra.count("a")
contagemUpper=palavra.count("A")
contagemFinal=contagemLower+contagemUpper
if contagemFinal==0:
    print("A letra 'A' não aparece nessa palavra")
else:
    print("A letra 'A' aparece", contagemFinal, "vezes nessa palavra")