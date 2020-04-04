import sqlite3

conn = sqlite3.connect('personagem.db')

conn.execute('create table IF NOT EXISTS Status(id integer primary key autoincrement, nome text, xp integer, damage integer, life integer,classe char)')

option = 0
while option >= 0:
    print(""" Bem vindo ao nosso maravilhoso game!!!\n Neste jogo de RPG no seu terminal você irá\n Primeiramente criar seu personagem, por enquanto há poucas opções de char\n Mas logo logo com nossas atualizações você irá vivenciar um jogo incrivel!!\n E sim, um jogo de terminal(cmd)\n Bom Jogo!!""")
    option = int(input('\nEscolha a opção:\n0 para sair\n1 para criar um personagem\n2 para escolher um personagem criado\n'))
    
    if option == 0:
        option = -1
        print('saindo...')

    if option == 1:
        name = input('\nDigite o seu nome:')
        xp = 10
        damage = 15
        life = 30
        classe = input('\nDigite:\nM para ser um mago\nG para um Guerreiro\nL para ser um ladrão')
        conn.execute('insert into Status (nome,xp,damage,life,classe) values (?,?,?,?,?)',(name,xp,damage,life,classe))
        conn.commit()
        
    if option == 2:

        for row in conn.execute('select * from Status'):
            ID,nome,xp,damage,life,classe = row
            print("O ID é:", ID, "O nome é:", nome, " O dano é: ", damage, "A vida é: ", life, "A classe é ", classe)









