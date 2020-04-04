import sqlite3
import randint

conn = sqlite3.connect('game.db')

conn.execute('create table IF NOT EXISTS Personagem(id integer primary key autoincrement, nome text, xp integer, gold integer, damage integer, life integer,classe text)')

print('\nBem vindo ao RPG\n')
option = 0
while option >= 0:
    option = int(input('\nEscolha a opção:\n0 para sair\n1 para criar um personagem\n2 para escolher um personagem criado\n3 para excluir um personagem\n'))
    
    if option == 0:
        option = -1
        print('saindo...')

    if option == 1:
        flag=0
        nome = input('\nDigite o seu nome:')
        xp = 10
        gold = 1
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
        conn.execute('insert into Personagem (nome,xp,gold,damage,life,classe) values (?,?,?,?,?,?)',(nome,xp,gold,damage,life,classe))
        conn.commit()
        
    if option == 2:
        selec = 0
        print("\n")
        for row in conn.execute('select * from Personagem'):
            ID,nome,xp,gold,damage,life,classe = row
            print('| O ID é:', ID, ' | O NOME é:', nome, ' | O DANO é: ', damage, ' | QUANTIDADE DE OURO: ', gold, ' | A VIDA é: ', life, ' | A CLASSE é ', classe,' | ')

        selec = input('Selecione pelo ID o personagem que deseja jogar')
        for row in conn.execute('select * from Personagem where ID = ?',(selec,)):
            ID,nome,xp,gold,damage,life,classe = row
            print('\nVocê selecionou o ',classe,' conhecido como ',nome)
            jogo(ID,nome,xp,gold,damage,life,classe)


    if option == 3:
        print("\n")
        for row in conn.execute('select * from Personagem'):
            ID,nome,xp,gold,damage,life,classe = row
            print('| O ID é:', ID, ' | O NOME é:', nome, ' | O DANO é: ', damage, ' | QUANTIDADE DE OURO: ', gold, ' | A VIDA é: ', life, ' | A CLASSE é ', classe,' | ')

        IdExluir = int(input('\nDigite o ID do personagem que deseja excluir: '))
        confirm = 0
        for row in conn.execute('select * from Personagem'):
            ID,nome,xp,gold,damage,life,classe = row
            if(ID==IdExluir):
                print('\nPersonagem excluido com sucesso!')
                confirm = 5
                conn.execute('delete from Personagem where ID = ?',(IdExluir,))
                conn.commit()
        if(confirm != 5):
            print('\nID não encontrado.')


def jogo(ID,nome,xp,gold,damage,life,classe):
    atuallife = life
    atualxp = xp
    atualdamage = damage
    atualgold = gold
    run = 0
    escolha = ('\n O que você deseja fazer:\n1 - Explorar caverna\n')
    if escolha == 1:
        rand = randint(0,9)
        if rand == 1:

            print('\nVocê encontrou com um goblin!')
            enemylife = 13
            enemydamage = 10
            run = 0
            print('\nEle não quis nem conversar e uma batalha começou:')

            while enemylife != 0 or atuallife != 0 or run >= 8:
                print('\nTurno do goblin:')
                damagegiven = randint(0,enemydamage)
                print('\nVocê levou ',damagegiven,' de dano')
                atuallife = atuallife - damagegiven
                print('\nStatus (',nome,'): vida atual',atuallife)
                option = int(input('1 pra  fugir ou 2 pra lutar:'))
                if option == 1:
                    run = randint(0,10)
                    if(run >= 8):
                        print('\n Você fugiu com sucesso!')
                elif option == 2:
                    print('\nSeu turno:')
                    damagegiven = randint(0,atualdamage)
                    print('\nVocê deu ',damagegiven,' de dano')
                    print('\nSeu inimigo está com ',enemylife,' de vida')
                else:
                    print('\nVocê ficou sem reação, não ira lutar dessa vez.')
            else:
                if enemylife == 0:
                    winxp = randint(30,60)
                    print('Você ganhou ',winxp,'xp.\nParabéns!')
                if atuallife == 0:
                    lostgold = randint(0,atualgold)
                    atualgold = atualgold - lostgold
                    print('Um curandeiro encontrou seu corpo e o trouxe de volta.')
                    print('Porém quando morto você perdeu ',lostgold,' de ouro')
                    
                
                    


            
    
        








