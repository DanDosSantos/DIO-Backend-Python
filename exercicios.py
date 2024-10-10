entrada = input()
# Função responsável por extrair os domínios dos emails
def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula
    lista_emails = emails.split(';')
    
    # Lista para armazenar os domínios
    nova_lista = []
    
    for email in lista_emails:
        nova_lista.append(email.split('@')[1])
    
    return nova_lista

# Imprime a lista de strings com os domínios
print(extrair_dominios(entrada))





# Recebe a entrada do usuário como uma string e divide essa string nos caracteres ',' (vírgula)
temperaturas_celsius = input().split(',')

# Função para converter Celsius para Fahrenheit
def converter_celsius_para_fahrenheit(temperaturas_celsius):
    # Converte a lista de strings para uma lista de floats
    temperaturas_celsius = [float(temp) for temp in temperaturas_celsius]
    
    # Calcula as temperaturas em Fahrenheit para cada temperatura em Celsius
    temperaturas_fahrenheit = [(temp * 9/5) + 32 for temp in temperaturas_celsius]
    
    return temperaturas_fahrenheit

# Imprime o resultado das temperaturas convertidas para Fahrenheit
print(converter_celsius_para_fahrenheit(temperaturas_celsius))