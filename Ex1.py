nome = str(input("Digite o seu nome: "))

salario_atual = float(input("Digite o seu salário atual: "))

if (salario_atual >= 0 and salario_atual <= 400):
    porcentagem = 15
    novo_salario = ((salario_atual * porcentagem) / 100) + salario_atual
    print(f"Nome: {nome}; porcentagem de aumento: {porcentagem}%; salário atual: R${salario_atual}; novo salário: R${novo_salario}")

elif (salario_atual >= 401 and salario_atual <= 700):
    porcentagem = 12
    novo_salario = ((salario_atual * porcentagem) / 100) + salario_atual
    print(f"Nome: {nome}; porcentagem de aumento: {porcentagem}%; salário atual: R${salario_atual}; novo salário: R${novo_salario}")

elif (salario_atual >= 701 and salario_atual <= 1000):
    porcentagem = 10
    novo_salario = ((salario_atual * porcentagem) / 100) + salario_atual
    print(f"Nome: {nome}; porcentagem de aumento: {porcentagem}%; salário atual: R${salario_atual}; novo salário: R${novo_salario}")

elif (salario_atual >= 1001 and salario_atual <= 1800):
    porcentagem = 7
    novo_salario = ((salario_atual * porcentagem) / 100) + salario_atual
    print(f"Nome: {nome}; porcentagem de aumento: {porcentagem}%; salário atual: R${salario_atual}; novo salário: R${novo_salario}")

elif (salario_atual >= 1801 and salario_atual <= 2500):
    porcentagem = 4
    novo_salario = ((salario_atual * porcentagem) / 100) + salario_atual
    print(f"Nome: {nome}; porcentagem de aumento: {porcentagem}%; salário atual: R${salario_atual}; novo salário: R${novo_salario}")

elif (salario_atual > 2500):
    porcentagem = 0
    novo_salario = ((salario_atual * porcentagem) / 100) + salario_atual
    print(f"Nome: {nome}; porcentagem de aumento: {porcentagem}%; salário atual: R${salario_atual}; novo salário: R${novo_salario}")