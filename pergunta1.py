numero = int(input("Digite um número: "))
i=0
pertenceFiboNacci = 0
fiboNacciList=[1]
while i<numero:
  fiboNacciList.append(fiboNacciList[i]+fiboNacciList[i-1])
  i = i + 1
  if fiboNacciList[i]==numero:
      print("O numero informado pertence a sequência de Fibonacci")
      pertenceFiboNacci = 1
      break
if pertenceFiboNacci==0:
    print("O numero informado não pertence a sequência de Fibonacci")