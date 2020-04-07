import sqlite3
from random import randint

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
                life = 45
                damage = 35
                print('\nO ',classe,' chamado ',nome,' criado com sucesso!')
                flag = 5
            elif classe == 'g' or classe == 'G':
                classe = 'Guerreiro'
                life = 60
                damage = 25
                print('\nPersonagem criado com sucesso!')
                flag = 5
            elif classe == 'L' or classe == 'l':
                classe = 'Ladrão'
                life = 40
                damage = 20
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
        print("\n")
        selec = input('Selecione pelo ID o personagem que deseja jogar: ')
        for row in conn.execute('select * from Personagem where ID = ?',(selec,)):
            ID,nome,xp,gold,damage,life,classe = row
            print('\nVocê selecionou o ',classe,' conhecido como ',nome)
            
            escolha = 0
            while escolha >= 0:
                run = 0
                atuallife = life
                atualxp = xp
                atualdamage = damage
                atualgold = gold

                escolha = int(input('\nO que você deseja fazer:\n0 - ir para o menu\n1 - Status do personagem\n2 - Explorar caverna\n'))

                if escolha == 0:
                    escolha = -1
                    print('\nsaindo...')
                
                if escolha == 1:
                    for row in conn.execute('select * from Personagem where ID = ?',(selec)):
                        ID,nome,xp,gold,damage,life,classe = row
                        print('| ID:', ID, ' | NOME:', nome, ' | DANO: ', damage, ' | QUANTIDADE DE OURO: ', gold, ' | VIDA: ', life,' | Quantidade de XP: ', xp,' | CLASSE: ', classe,' | ')
                elif escolha == 2:
                    rand = randint(1,10)

                    if rand == 1:

                        print('\nVocê encontrou com um goblin!')
                        enemylife = 13
                        enemydamage = 10
                        print('\nEle não quis nem conversar e uma batalha começou:')
                        print(atuallife)
                        print(enemylife)
                        print(run)

                        while enemylife >= 0 and atuallife >= 0 and run <= 8:
                            run = 0
                            print('\nTurno do goblin:')
                            damagegiven = randint(0,enemydamage)
                            print('\nVocê levou ',damagegiven,' de dano')
                            atuallife = atuallife - damagegiven
                            print('\nStatus (',nome,'): vida atual',atuallife)
                            if atuallife >= 0:
                                option = int(input('1 pra  fugir ou 2 pra lutar:'))

                                if option == 1:
                                    run = randint(0,10)
                                    if(run >= 8):
                                        print('\n Você fugiu com sucesso!')
                                elif option == 2:
                                    print('\nSeu turno:')
                                    damagegiven = randint(int(atualdamage/2),atualdamage)
                                    enemylife = enemylife - damagegiven
                                    print('\nVocê deu ',damagegiven,' de dano')
                                    print('\nSeu inimigo está com ',enemylife,' de vida')
                                else:
                                    print('\nVocê ficou sem reação, não ira lutar dessa vez.')
                        else:
                            if enemylife <= 0:
                                    atualxp = randint(30,60)
                                    wingold = randint(10,36)
                                    atualgold = wingold + atualgold
                                    print('Você ganhou ',atualxp,'xp e ',wingold,' de ouro.\nParabéns!')
                                    conn.execute('update Personagem set xp = ? ,gold = ?',(atualxp + xp,atualgold))
                                    conn.commit()

                            if atuallife <= 0:
                                    lostgold = randint(0,atualgold)
                                    atualgold = atualgold - lostgold
                                    print('Um curandeiro encontrou seu corpo e o trouxe de volta.')
                                    print('Porém quando morto você perdeu ',lostgold,' de ouro')
                                    conn.execute('update Personagem set gold = ?',(atualgold + gold))
                                    conn.commit()
                    if rand == 2:
                        print('Segunda possibilidade!')
                    if rand == 3:
                        print('Terceira possibilidade!')
                    if rand == 4:
                        print('Quarta possibilidade!')
                    if rand == 5:
                        print('Quinta possibilidade!')
                    if rand == 6:
                        print('Sexta possibilidade!')
                    if rand == 7:
                        print('Sétima possibilidade!')
                    if rand == 8:
                        print('Oitava possibilidade!')
                    if rand == 9:
                        print('Nona possibilidade!')
                    if rand == 10:
                        print('Décima possibilidade!')
                else
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



                    
                
                    


            
    
        








