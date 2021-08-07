import discord
import random
from discord.ext import commands


class TicTacToe(commands.Cog):
    def __init__(self, client):
        self.client = client

    # GLOBAL VARIABLES
    player1 = ""
    player2 = ""
    turn = ""
    gameOver = True

    board = []

    winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    # TIC_TAC_TOE COMMAND
    @commands.command()
    async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member):
        channel = self.client.get_channel(843501907028475924)
        global count
        global player1
        global player2
        global turn
        global gameOver

        if self.gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                     ":white_large_square:", ":white_large_square:", ":white_large_square:",
                     ":white_large_square:", ":white_large_square:", ":white_large_square:"]
            turn = ""
            self.gameOver = False
            count = 0

            player1 = p1
            player2 = p2

            # PRINTING WHITE_LARGE_SQUARE BOARD
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await channel.send(line)
                    line = ""
                else:
                    line += " " + board[x]

            # DETERMINE WHO GO FIRST
            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await channel.send("It is <@" + str(player1.id) + ">'s turn.")
            elif num == 2:
                turn = player2
                await channel.send("It is <@" + str(player2.id) + ">'s turn.")
        else:
            await channel.send("Game already in progress! Finish it before starting a new one.")

    #TIC_TAC_TOE_ERROR HANDLER
    @tictactoe.error
    async def tictactoe_error(self, ctx, error):
        channel = self.client.get_channel(843501907028475924)
        if isinstance(error, commands.MissingRequiredArgument):
            await channel.send("Required 2 different player names.")

    # PLACE COMMAND
    @commands.command()
    async def place(self, ctx, pos: int):
        channel = self.client.get_channel(843501907028475924)
        global turn
        global player1
        global player2
        global board
        global count
        global gameOver

        if not self.gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                    board[pos - 1] = mark
                    count += 1

                    # PRINT MARK ON THE BOARD
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await channel.send(line)
                            line = ""
                        else:
                            line += " " + board[x]

                    self.checkWinner(self.winningConditions, mark)

                    if self.gameOver == True:
                        await channel.send(mark + " wins!")
                    elif count >= 9:
                        self.gameOver = True
                        await channel.send("It's a tie!")

                    # SWITCH TURNS
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                else:
                    await channel.send("Choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
            else:
                await channel.send("It is not your turn.")
        else:
            await channel.send("Please start a new game using the !tictactoe command.")

    @place.error
    async def place_error(self, ctx, error):
        channel = self.client.get_channel(843501907028475924)
        if isinstance(error, commands.MissingRequiredArgument):
            await channel.send("Missing argument.")

    # CHECKING WINNER
    def checkWinner(self, winningConditions, mark):
        global gameOver
        for condition in winningConditions:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                self.gameOver = True


def setup(client):
    client.add_cog(TicTacToe(client))
