"""Day 4"""
from read_from_file import get_input_data


def transpose_board(board: list[list[int]]) -> list[list[int]]:
    """Returns the transpose of a board."""

    return [[board[i][j] for i in range(0, 5)] for j in range(0, 5)]


class BingoPlayer:

    def __init__(self, board: list[list[int]]) -> None:

        self.board = board
        self.marked_board = [[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0]]

    def check_number(self, bingo_number: int) -> None:
        """Checks to see if the number is on the boards, marks it if so."""

        for i in range(0, 5):
            for j in range(0, 5):
                if self.board[i][j] == bingo_number:
                    self.marked_board[i][j] = 1
                    return None

        return None

    def has_won(self) -> bool:
        """Returns true if the player has won, False otherwise."""

        # Check rows
        if any(sum(row) == 5
               for row in self.marked_board):

            return True

        # Check columns
        if any(sum(row) == 5
               for row in transpose_board(self.marked_board)):

            return True

        return False

    def calculate_score(self, winning_number: int) -> int:
        """Calculates the score of a winning player."""

        if not self.has_won():
            raise ValueError("Player hasn't won!")

        unmarked_sum = sum(self.board[i][j]
                           for i in range(0, 5)
                           for j in range(0, 5)
                           if not self.marked_board[i][j])

        return unmarked_sum * winning_number


def get_bingo_inputs(line: str) -> list[int]:
    """Returns a list of bingo inputs."""

    bingo_inputs_char = line.split(",")
    return list(map(int, bingo_inputs_char))


def get_bingo_board(board_lines: list[str]) -> list[list[int]]:
    """Returns a Bingo board."""

    for i in range(0, len(board_lines)):
        board_lines[i] = [int(num) for num in board_lines[i].split(" ")
                          if num != '']

    return board_lines


def setup_game(lines: list[str]) -> list:
    """Formats the data into
        - A list of integers (Bingo inputs)
        - A list of grids (player boards)
        Instantiates players and boards."""

    # Remove whitespace
    inputs = [line for line in lines if line != '']

    bingo_inputs = get_bingo_inputs(inputs[0])

    players = []

    for i in range(0, (len(inputs)-1)//5):

        bingo_board = get_bingo_board(inputs[5*i+1: 5*i+6])

        players.append(BingoPlayer(bingo_board))

    return bingo_inputs, players


def take_turn(input_number: int, players: list[BingoPlayer]) -> tuple[BingoPlayer, int] | None:
    """Simulates a single bingo turn. If a player wins, returns them and their score."""

    winners = []
    for player in players:
        player.check_number(input_number)
        if player.has_won():
            winners.append((player, player.calculate_score(input_number)))
    return winners


def play_bingo(players: list[BingoPlayer], bingo_numbers: list[int]) -> int:
    """ First Star
        Plays a game of Bingo!"""

    for number in bingo_numbers:
        winners = take_turn(number, players)
        if len(winners) != 0:
            return winners[0][1]


def lose_bingo(players: list[BingoPlayer], bingo_numbers: list[int]) -> int:
    """ Second Star
        Plays a game of Bingo, revealing the score of the last player."""

    for number in bingo_numbers:
        winners = take_turn(number, players)
        for winner in winners:
            if len(players) == 1:
                return players[0].calculate_score(number)

            players.remove(winner[0])


if __name__ == "__main__":
    input_data = get_input_data(4)

    input_numbers, player_list = setup_game(input_data)

    print(play_bingo(players=player_list, bingo_numbers=input_numbers))

    print(lose_bingo(players=player_list, bingo_numbers=input_numbers))
