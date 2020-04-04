import sqlite3

conn = sqlite3.connect('personagem.db')

conn.execute('create table IF NOT EXISTS Status(id integer primary key autoincrement, nome text, xp integer, damage integer, life integer,classe text)')

option = 0
while option >= 0:
    option = int(input('\nEscolha a opção:\n0 para sair\n1 para criar um personagem\n2 para escolher um personagem criado\n'))
    
    if option == 0:
        option = -1
        print('saindo...')

    if option == 1:
        flag=0
        name = input('\nDigite o seu nome:')
        xp = 10
        damage = 15
        life = 30
        while flag != 5:
            classe = input('\nDigite:\nM para ser um mago\nG para um Guerreiro\nL para ser um ladrão ')
            if classe == 'm' or classe == 'M':
                classe = 'Mago'
                flag = 5
            if classe == 'g' or classe == 'G':
                classe = 'Guerreiro'
                flag = 5
            if classe == 'L' or classe == 'l':
                classe = 'Mago'
                flag = 5
        conn.execute('insert into Status (nome,xp,damage,life,classe) values (?,?,?,?,?)',(name,xp,damage,life,classe))
        conn.commit()
        
    if option == 2:

        for row in conn.execute('select * from Status'):
            ID,nome,xp,damage,life,classe = row
            print("| O ID é:", ID, " | O NOME é:", nome, " | O DANO é: ", damage, " | A VIDA é: ", life, " | A CLASSE é ", classe," | ")









