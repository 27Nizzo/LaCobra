# Podemos criar um dicionário usando pares dentro de "{}", separado por virgulas. Por Exemplo:

countryCapitals = {
                "Germany": "Berlim",
                "Canada":  "Ottawa",
                "England": "London",
                "Portugal": "Lisbon"
                # Key         # Value
                  }
print(countryCapitals)
# OutPut = {'England: London', 'Germany: Berlim', 'Canada: Ottawa', 'Portugal: Lisbon'}

#Nota: 
# -> As "keys" dos dicionários devem ser imutáveis, ou seja, não devem mudar. Não podemos mudar objetos, como as listas como "keys"
# -> Podemos criar um dicionário usando uma função ja existente no Python, a "dict()" 

# Para ter acesso aos items do dicionário em especifico podemos fazer da seguinte forma:

print(countryCapitals["Germany"])
print(countryCapitals["Portugal"])
# Ou, usamos a função get():

print(countryCapitals.get("Canada"))


# Adicionar itemns do dicionario

countryCapitals["Italy"] = "Rome"
                  # Key     # Value
print(countryCapitals)
# Output: {'Germany': 'Berlim', 'Canada': 'Ottawa', 'England': 'London', 'Portugal': 'Lisbon', 'Italy': 'Rome'}


# Remover items do dicionario

del countryCapitals["England"]
print(countryCapitals)
# Output: {'Germany': 'Berlim', 'Canada': 'Ottawa', 'Portugal': 'Lisbon', 'Italy': 'Rome'}

# Ou, com a função pop(): 

countryCapitals.pop("Canada")
print(countryCapitals)

# Para mudar items de dicionarios:

countryCapitals["Canada"] = "Toronto"
print(countryCapitals)

# Ou, coma função update():
countryCapitals.update({"Canada": "Ottawa"})
print(countryCapitals)

# Alguns métodos:
# *Função .key() -> Devolve as keys do dicionário
print(countryCapitals.keys())

# *Função .copy() -> devolve uma copia do dicionário
print(countryCapitals.copy())

# *Função .update()

# *Função .get()

# *Função .clear() -> que remove os items do dicionario
# countryCapitals.clear()
# print(countryCapitals)
# Output: {}

# *Função .popitem() -> retorna o dicionario sem o ultimo elemento
countryCapitals.popitem()
print(countryCapitals)
# Output: {'Germany': 'Berlim', 'Portugal': 'Lisbon', 'Italy': 'Rome'}

# Iteração dentro de um dicionario:
# Um dicionario é uma coleção de items ordenada, e por isso mantem a ordem dos mesmos, Nós podemos iterar dentro de um dicionario com um "for loop".
# Por Exemplo: 

countryCapitals2 = {
                    "United States": "Washinton D.C",
                    "France": "Paris"
                   } 

for country in countryCapitals2:
        print(country)

print()

for country in countryCapitals2:
        capital = countryCapitals2[country]
        print(capital)
print()
# Encontrar o comprimento do dicionario:
        
countryCapitals3 = {"England": "London", 
                    "Italy": "Rome"
                    }
print(len(countryCapitals3))
# Output: 2 

numbers = {10: "ten", 20: "twenty", 30: "thirty"}
print(len(numbers))
# Output: 3 
print()

# Dicionario de Membership:

fileTypes = {
        ".txt": "Text File",
        ".pdf": "PDF Document",
        ".jpg": "JPEG Image"
}

# Agora vamos checkar se se alguma key vai pertencer ao dicionario fileTypes:

print(".pdf" in fileTypes)
print(".mp3" in fileTypes)
print(".mp3" not in fileTypes)

