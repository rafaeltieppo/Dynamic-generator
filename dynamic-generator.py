import random

data = ["2017", "2018", "2019", "2020"]

nomes_iniciais = ["Allan", "Ana", "Augusto", "Bárbara", "Carlos", "Daniel", "Danilo", "Diogo", "Elian", "Éryk", "Felipe", "Gabriel", "Gustavo", "Helena", "Jaqueline", "Kailane", "Larissa", "Lavinia", "Leonardo", "Leticia", "Matheus", "Ricardo", "Michael", "Paula", "Rafael", "Raul", "Rodrigo", "Victória", "Vitor"]

sobrenomes = ["Silva", "Moreira", "Bueno", "Oliveira", "Souza", "Soares", "Medeiros", "Moraes", "Bento", "Lopes", "Soares", "Vital", "Ferreira", "Rocha", "Frasson", "Dias", "Debernardi", "Pardim", "Barbosa", "Panigassi", "Imenes", "Belli", "Medeiros", "Tieppo", "Faria", "Mariano", "Pereira", "Aparecido", "Rosa", "Corrêa", "Hugo"] 

turmas = ["a", "b", "c", "d", "e"]

anos = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "1_1", "2_2", "3_3"]

disciplinas = ["Wellington_Portugues", "Reenye_Matematica", "Carlos_Fisica", "Elian_Biologia", "Carlos_Quimica", "Jaqueline_História", "Felipe_Geografia", "Jaqueline_Filosofia", "Jaqueline_Sociologia", "Allan_Inglês", "Emily_Artes"]

arquivo = open("teste.csv", "w") 
arquivo.write("Data;Ano;Turma;Nome;Advertencias;Faltas;Professor_Disciplina;Média da turma;")
for teste in data:
    for ano in anos:
        for turma in turmas: 
            series = ano + ";" + turma
            professor_sala = random.choice(disciplinas)
            media_turma = random.randint(0,10)
            for nomes in nomes_iniciais: #for nomes in range(0,10)
                nome_completo = random.choice(nomes_iniciais) + " " + random.choice(sobrenomes)
                advertencias = random.randint(0, 3)
                faltas = random.randint(0,5)
                arquivo.write("\n" + teste + ";" + series + ";" + nome_completo + ";" + str(advertencias) + ";" + str(faltas) + ";" + professor_sala + ";" + str(media_turma))

arquivo.close()
print("Arquivo gerado e preenchido com sucesso")