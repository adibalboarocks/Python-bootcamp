import random

def display (board):
       print(f'''
               {board[1]} | {board[2]} |{board[3]}\n
             --------------\n
               {board[4]} | {board[5]} |{board[6]}\n
             --------------\n
               {board[7]} | {board[8]} | {board[9]}\n
                   ''')
    
def valid_input():
    while True:
        pos = input("enter position. Choose a number  from 1 to 9: ")
        if pos !=' ':
            if int(pos) in range(1,10):
                return int(pos)
                break
            else:
                   print("not valid position\n")
        else:
            print("thank you for playing tic tac toe")
            exit()
def valid_pos(turn,board):
    print(f'{turn} chance')
    t=valid_input()
    list=[]
    while True:
        
        if board[t] in range(1,10) and t not in list:
            board[t]=turn
            display(board)
            list.append(t)
            break 
        else:
            print("Cannot overwrite, select another location")
            t=valid_input()
            continue

def userInput(board,symbol):
    sym1,sym2= symbol[random.randint(0,1)]
    print(f'{sym1} is going first\n\n')
    display(board)
    for i in range(9):
      
      if i%2==0:
        turn = ' '+sym1+' '
        valid_pos(turn,board)
        
      else:
        turn = ' '+sym2+' '
        valid_pos(turn,board)
        
      if i in range(4,8) and check(board)==1:
               print(f'"{turn}"WON')
               display(board)
               return False
               break
      if i==8 :
        print("Neither WON,It is a tie")
        return False
        break
    

def game():
    board=["to adjust loc",1,2,3,4,5,6,7,8,9]
    symbol=[('X','O'),('O','X')]
    
    while True:
           marker=input('\nEnter your Marker: ').upper()
           if marker == 'X' or marker=='O':
               userInput(board,symbol)
               break
            
           
           else:
                  print("wrong marker choose an option again the markers are X and Y")
           
                  continue
    

def check(board):
    check = 0
    if board[1] == board[2] == board[3] != '    ' or board[4] == board[5] == board[6] != '    ' or board[7] == board[8] == board[9] != '    ':
           check=1
    elif board[1] == board[4] == board[7] != '    ' or board[2] == board[5] == board[8] != '    ' or board[3] == board[6] == board[9] != '    ':
        check=1
    elif  board[1] == board[5] == board[9] != '    ' or board[3] == board[5] == board[7] != '    ':
        check=1
    return check
def main():
    game()
    while input("do you want to play again (Y/N)?").upper()== 'Y':
         game()

         
main()
    
