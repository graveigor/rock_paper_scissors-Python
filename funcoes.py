import os
os.system('cls' if os.name == 'nt' else 'clear')

# Parametros de função

# Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. 
# Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

def calcular_idade(ano_nascimento, ano_atual):
    return(ano_atual - ano_nascimento)

nascimento = int(input("Digite o ano de seu nascimento: "))
atual = int(input("Digite o ano atual: "))
idade_atual = calcular_idade(nascimento, atual)
print(f"Sua idade é: {idade_atual}")

# Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.
# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

def exibir_caracteres(palavra):
    return len(palavra)
texto = input("Digite uma palavra: ")
print(f"Esta palavra possui {exibir_caracteres(texto)} caracteres nela!")


# Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. 
# Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:
# Se for antes das 12h, exibir "Bom dia";
# Entre 12h e 18h, exibir "Boa tarde";
# Após 18h, exibir "Boa noite".

def saudacao(hora):
    if hora < 12:
        return("Bom dia!")
    elif hora < 18:
        return("Boa tarde!")
    else:
        return("Boa noite!")
hora_atual = int(input("Digite o horário atual (0-23): "))
print(saudacao(hora_atual))
        
    