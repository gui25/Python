import sqlite3

conn = sqlite3.connect('game.db')

conn.execute('create table IF NOT EXISTS Personagem(id integer primary key autoincrement, nome text, xp integer, damage integer, life integer,classe text)')

print('\nBem vindo ao RPG\n')
option = 0
while option >= 0:
    option = int(input('\nEscolha a opção:\n0 para sair\n1 para criar um personagem\n2 para escolher um personagem criado\n3 para excluir um personagem'))
    
    if option == 0:
        option = -1
        print('saindo...')

    if option == 1:
        flag=0
        nome = input('\nDigite o seu nome:')
        xp = 10
        
        while flag != 5:
            classe = input('\nDigite:\nM para ser um mago\nG para um Guerreiro\nL para ser um ladrão ')
            if classe == 'm' or classe == 'M':
                classe = 'Mago'
                life = 15
                damage = 25
                print('\nO ',classe,' chamado ',nome,' criado com sucesso!')
                flag = 5
            elif classe == 'g' or classe == 'G':
                classe = 'Guerreiro'
                life = 28
                damage = 15
                print('\nPersonagem criado com sucesso!')
                flag = 5
            elif classe == 'L' or classe == 'l':
                classe = 'Ladrão'
                life = 15
                damage = 17
                print('\nPersonagem criado com sucesso!')
                flag = 5
            else:
                print('\nOpção invalida, Digite novamente.')
        conn.execute('insert into Personagem (nome,xp,damage,life,classe) values (?,?,?,?,?)',(nome,xp,damage,life,classe))
        conn.commit()
        
    if option == 2:

        for row in conn.execute('select * from Personagem'):
            ID,nome,xp,damage,life,classe = row
            print("| O ID é:", ID, " | O NOME é:", nome, " | O DANO é: ", damage, " | A VIDA é: ", life, " | A CLASSE é ", classe," | ")
    if option == 3:
        for row in conn.execute('select * from Personagem'):
            ID,nome,xp,damage,life,classe = row
            print("| O ID é:", ID, " | O NOME é:", nome, " | O DANO é: ", damage, " | A VIDA é: ", life, " | A CLASSE é ", classe," | ")

        IdExluir = int(input('Digite o ID do personagem que deseja excluir: '))
        conn.execute('delete from Personagem where ID = ?',(IdExluir,))
        conn.commit()
        print('\nPersonagem excluido com sucesso!')








