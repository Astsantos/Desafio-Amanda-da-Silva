#quando for colocar as frutas coloca elas uma por uma pliss

maca = 3.50
banana = 2.20
laranja = 1.80
pera = 3.00
uva = 5.00
mamao = 7.00
melancia = 8.00
melao = 8.00

total = 0
print("Bem-vindo à nossa loja de frutas!")
print("Aqui estão os preços das nossas frutas:")
print("1.Maçã: (R$3.50)")
print("2.Banana: (R$2.20)")  
print("3.Laranja: (R$1.80)")
print("4.Pera: (R$3.00)")
print("5.Uva: (R$5.00)")
print("6.Mamão: (R$7.00)")
print("7.Melancia: (R$8.00)")
print("8.Melao: (R$8.00)\n")

qtd_produtos = int(input("Quantas frutas você deseja comprar?: "))

for i in range(qtd_produtos):

#quando for colocar as frutas coloca elas uma por uma pliss

    opcao = int(input("\nEscolha as frutas(digite o número dela): "))
    quantidade = int(input("Quantidade/Quantidades: "))

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero. Tente novamente pliss.")
        continue

    if opcao == 1:
        valor_item = quantidade * maca
        total += valor_item

    elif opcao == 2:
        valor_item = quantidade * banana
        total += valor_item

    elif opcao == 3:
        valor_item = quantidade * laranja
        total += valor_item
    
    elif opcao == 4:
        valor_item = quantidade * pera
        total += valor_item

    elif opcao == 5:
        valor_item = quantidade * uva
        total += valor_item

    elif opcao == 6:
        valor_item = quantidade * mamao
        total += valor_item

    elif opcao == 7:
        valor_item = quantidade * melancia
        total += valor_item
    
    elif opcao == 8:
        valor_item = quantidade * melao
        total += valor_item

    else:
        print("Fruta inválida!")

print("\n------------------")
print(f"Obrigada por comprar conosco. Total da compra: R$ {total:.2f}")

if total > 100:
    desconto = total * 0.10
    valor_final = total - desconto

    print(f"Valor original: R$ {total:.2f}")
    print(f"Descontinho: R$ {desconto:.2f}")
    print(f"Valor total com o descontinho: R$ {valor_final:.2f}")