import json
import sqlite3

conn = sqlite3.connect('personagem.db')

#conn.execute('create table IF NOT EXISTS Aluno(id integer primary key autoincrement, nome text, xp integer, damage integer, life integer,classe char)')

option = 0
while option >= 0:
    option = int(input('\nEscolha a opção:\n0 para sair\n1 para criar um personagem\n2 para escolher um personagem criado\n'))
    
    if option == 0:
        option = -1
        print('saindo...')

    if option == 1:
        name = input('\nDigite o seu nome:')
        xp = 10
        damage = 15
        life = 30
        classe = input('\nDigite:\nM para ser um mago\nG para um Guerreiro\nL para ser um ladrão ')
        conn.execute('insert into Aluno (nome,xp,damage,life,classe) values (?,?,?,?,?)',(name,xp,15,30,classe))
        conn.commit()
        
    if option == 2:
        dados = []
        for row in conn.execute('select * from Aluno where id = 1'):
            print(row)
            
            
        # for row in conn.execute('select * from Aluno order by id'):
        #     print('Nome: ',row)








