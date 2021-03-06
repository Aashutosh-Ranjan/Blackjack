class BlackJack():
    
    suits = [' of Hearts',' of Spades',' of Diamonds',' of Clubs']
    cards = ['1/11','2','3','4','5','6','7','8','9','10','King','Queen','Jack']
    
   
    
    def __init__(self,deck,ddict):
        self.deck = deck
        self.ddict = ddict
        
    
    def shuffle(deckk):
        import random
        keys  =  list(deckk)
        random.shuffle(keys)
        dict={key:deckk[key] for key in keys}
        return dict
    
    def use_deck():
        dec={}
        for i in BlackJack.suits:
            for j in BlackJack.cards:
                if j == 'King' or j=='Queen' or j=='Jack':
                    dec[j+i]=10
                elif j == '1/11':
                    dec["Ace"+i]=j
                else:
                    dec[j+i]=int(j)

        return dec

        
        
        
        
    def hit(self):
        import random
        x = random.choice(list(self.deck.keys()))
        
        if('Ace' in x):
            
            if 'player' in self.ddict:
                ace = (input('You have got an ACE card, do you want 1/11 ? '))
                while(ace not in ['1','11']):
                    ace = (input('Invalid input, choose 1/11 '))
                self.ddict[x]=int(ace)
                self.deck.pop(x)
            else: 
                self.ddict[x]=11
                self.deck.pop(x)
        
        else:
            
            self.ddict[x]=self.deck[x]
            self.deck.pop(x)
        return sum(list(self.ddict.values()))

rem_bet = 100
name=''

def blackj():
    
    
    import random
    from IPython.display import clear_output
    deck = {}
    global rem_bet,name
    player = {'player':0}
    dealer = {}
    

    deck=BlackJack.use_deck()
    deck = BlackJack.shuffle(deck)
    
    if name=='':
        name = input("Enter your name: ")
        while(name=='' or len(name.strip())==0):
            name =input("Enter a valid name ")
    
    
    while(True):
        player_bet=input(f'{name}, the Maximum available chip available for bidding is {rem_bet}$, Enter the Bet Amount \
between 1 and {rem_bet} : ')
        try:
            player_bet=float(player_bet)
            if(player_bet<1 or player_bet>rem_bet):
                continue
        except:
            continue
    
        
        break
    clear_output()
    while(len(dealer)!= 2):
        while(len(player)!= 3):
            x = random.choice(list(deck.keys()))
            if('Ace' in x):
                ace = (input(f'{name}, your card is {x}, choose 1 or 11? '))
                while(ace not in ['1','11']):
                    ace = input("choose between 1 and 11 only ")
                player[x]=float(ace)
                deck.pop(x)
            else:
                
                player[x]=deck[x]
                deck.pop(x)
        y = random.choice(list(deck.keys()))
        if('Ace' in y):
                    
            dealer[y]=11
            deck.pop(y)
        else:
            
            dealer[y]=deck[y]
            deck.pop(y)
    print(f'{name}, your cards are {list(player.keys())[1:]} and \nsum is {sum(list(player.values()))}.')
    dcrd = list(dealer.keys())[-1]
    print(f"One of the Dealer's card is {dcrd} and no is {dealer[dcrd]} ")


    if(sum(list(player.values()))>21):
        print(f'{name}, you are Busted! as your cards are {list(player.keys())[1:]} and \nsum is {sum(list(player.values()))}.')
        rem_bet=rem_bet-player_bet
    else:
        
        while(True):
            pi = input(f'{name}, Do you want to hit(0) or stand(1) [0/1]? \n')
            try:
                pi=int(pi)
                if(pi not in [0,1]):
                    continue
            except:
                continue
            break
                    
        while(int(pi)==0):
            if (BlackJack(deck,player).hit()>21):
                clear_output()
                print(f'{name}, you are BUSTED as your cards are {list(player.keys())[1:]} and \nsum= {sum(list(player.values()))} exceeded 21 ')
                rem_bet=rem_bet-player_bet
                break
            else:
                clear_output()
                print(f"{name}, your cards are {list(player.keys())[1:]} and \
sum is {sum(list(player.values()))}.\nOne of the Dealer's card is {dcrd} and no is {dealer[dcrd]} ")
                while(True):
                    pi = input(f'{name}, Do you want to hit(0) or stand(1) [0/1]? \n')
                    try:
                        pi=int(pi)
                        if(pi not in [0,1]):
                            continue
                    except:
                        continue
                    break
                
                continue
        
        
        if(int(pi) == 1):
            if(sum(list(dealer.values()))>= 17):
                if(sum(list(dealer.values()))>sum(list(player.values()))):
                    clear_output()
                    print(f'Dealer won the game as cards are {list(dealer.keys())} and \nsum is {sum(list(dealer.values()))} ')
                    print(f'{name}, lost the Game')
                    rem_bet=rem_bet-player_bet
                else:
                    clear_output()
                    print(f'Dealer lost the game as cards are {list(dealer.keys())} and \nsum is {sum(list(dealer.values()))} ')
                    print(f'{name} won the Game as cards are {list(player.keys())[1:]} and \nsum= {sum(list(player.values()))}')
                    rem_bet=rem_bet+player_bet
            else:

                while(sum(list(dealer.values()))<17):

                    BlackJack(deck,dealer).hit()
                    clear_output()
                    print(f'Dealer cards are {list(dealer.keys())} and \nsum is {sum(list(dealer.values()))} ')

                if(sum(list(dealer.values()))>sum(list(player.values()))):
                    clear_output()
                    print(f"DEALER WON the game,\nas {name}'s cards are {list(player.keys())[1:]} and \nsum is {sum(list(player.values()))} ")
                    rem_bet=rem_bet-player_bet
                else:
                    clear_output()
                    print(f"{name} WON THE GAME,\nas Dealer's cards are {list(dealer.keys())} and \nsum is {sum(list(dealer.values()))} ")
                    rem_bet=rem_bet+player_bet
            
    if rem_bet==0:
        print(f'{name}, you are out of money for betting.')
        return ('Thankyou for playing!')
    else:
    
        replay = input("Do you want to play again? Y/N: ")

        while(replay.upper() not in ['Y','N']):
            replay = input('Invalid Input give answer only in Y/N: ')
        if(replay.lower()  ==  'y'):
            blackj()
        elif(replay.lower()  ==  'n'):
            print('Thank you for playing the game')
    
    
        
blackj()
