nome = "Renato"
idade = 34
profissao = "Programador"
linguagem = "Python"

pessoa = {"nome": "Renato", "idade": 34, "profissao": "Programador", "linguagem": "Python"}

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}." .format(linguagem, profissao, idade, nome))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabahlo como {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa))
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")
