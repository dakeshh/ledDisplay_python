from random import randrange

def DisplayBoard(board):
    count = 0;
    for k, v in board.items():
        print("{0}{1:-^12}{2}{3:-^12}{4}{5:-^12}{6}".format("+", "-", "+", "-", "+", "-", "+"))
        print("{0}{1:^12}{2}{3:^12}{4}{5:^12}{6}".format("|", " ", "|", " ", "|", " ", "|"))
        print("{0}{1:^12}{2}{3:^12}{4}{5:^12}{6}".format("|", v[str(count+1)], "|", v[str(count+2)], "|", v[str(count+3)], "|"))
        print("{0}{1:^12}{2}{3:^12}{4}{5:^12}{6}".format("|", " ", "|", " ", "|", " ", "|"))
        count = count + 3;
    print("{0}{1:-^12}{2}{3:-^12}{4}{5:-^12}{6}".format("+", "-", "+", "-", "+", "-", "+"))

def EnterMove(board, inp=None):
    inUS = "";
    if inp == "user":
        inUS = "O";
        inp = int(input("Enter your move: "));
        while True:
            if inp > 9 or inp < 0:
                inp = int(input("Enter your move (between 0 to 8 ONLY ): "));
            else:
                while True:
                    if str(inp) not in MakeListOfFreeFields(board):
                        inp = int(input("Enter your move (between 0 to 8 ONLY ): AND among " + str(MakeListOfFreeFields(board)) + ": "));
                        continue;
                    else:
                        break;
                break;
    elif inp == "system":
        inUS = "X";
        inp = randrange(10);
        #print("inside =" + str(inp))
        while True:
            if str(inp) not in MakeListOfFreeFields(board):
                inp = randrange(10);
                continue;
            else:
                break;
    else:
        return None;

    for k, v in board.items():
        if str(inp) not in v:
            continue;
        else:
            dummy = dict(v).copy();
            dummy[str(inp)] = str(inUS);
            board[k] = dummy

    DisplayBoard(board)



def MakeListOfFreeFields(board):
    dummy = [];
    count = 0;

    for k, v in board.items():

        if v[str(count+1)] != "O" and v[str(count+1)] != "X":
            dummy.append(str(count+1));

        if v[str(count+2)] != "O" and v[str(count+2)] != "X":
            dummy.append(str(count+2));

        if v[str(count+3)] != "O" and v[str(count+3)] != "X":
            dummy.append(str(count+3));

        count = count + 3;

    return dummy;


def VictoryFor(board, sign=None):
    count = 0;
    for k, v in board.items():
        if v[str(count + 1)] == "O" and v[str(count + 2)] == "O" and v[str(count + 3)] == "O":
            print("User won !");
            return True;
        elif v[str(count + 1)] == "X" and v[str(count + 2)] == "X" and v[str(count + 3)] == "X":
            print("System won !")
            return True;
        count = count + 3;

    count = 0;
    for col in range(1, 4):
        if board[str(count + 1)][str(col)] == "O" and board[str(count + 2)][str(col + 3)] == "O" and \
                board[str(count + 3)][str(col + 6)] == "O":
            print("User won !");
            return True;
        elif board[str(count + 1)][str(col)] == "X" and board[str(count + 2)][str(col + 3)] == "X" and \
                board[str(count + 3)][str(col + 6)] == "X":
            print("System won !");
            return True;

    if (board["1"]["1"] == "O" and board["2"]["5"] == "O" and board["3"]["9"] == "O") or \
            (board["1"]["3"] == "O" and board["2"]["5"] == "O" and board["3"]["7"] == "O"):
        print("User won !");
        return True;

    elif (board["1"]["1"] == "X" and board["2"]["5"] == "X" and board["3"]["9"] == "X") or \
            (board["1"]["3"] == "X" and board["2"]["5"] == "X" and board["3"]["7"] == "X"):
        print("System won !");
        return True;

def DrawMove(board):
    DisplayBoard(board);
    print("----------------------------------------------------------------------------");
    for i in range(8):
        if i % 2 == 0:
            EnterMove(board, "user")
            if VictoryFor(board):
                break;
        else:
            EnterMove(board, inp="system")
            if VictoryFor(board):
                break;
            print("----------------------------------------------------------------------------");



board = {"1":{"1":"1", "2":"2", "3":"3"},
         "2":{"4":"4", "5":"X", "6":"6"},
         "3":{"7":"7", "8":"8", "9":"9"}}
DrawMove(board);


