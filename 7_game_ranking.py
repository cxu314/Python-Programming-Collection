class User:
    """A class of users of the game

    Attributes:
        rank: An integer number of user's current rank.
        star: An integer number of user's current stars.
        rank_star: A dictionary of the number of stars users
                   have before they can gain anonther rank.
    """
    def __init__(self):
        self.rank = 25
        self.star = 0
        self.rank_star = {
            1: 5,
            2: 5,
            3: 5,
            4: 5,
            5: 5,
            6: 5,
            7: 5,
            8: 5,
            9: 5,
            10: 5,
            11: 4,
            12: 4,
            13: 4,
            14: 4,
            15: 4,
            16: 3,
            17: 3,
            18: 3,
            19: 3,
            20: 3,
            21: 2,
            22: 2,
            23: 2,
            24: 2,
            25: 2
        }

    def add_star(self):
        """
        This function makes a user gain a star.
        """
        self.star += 1
        if self.rank > 0:
            if self.star > self.rank_star[self.rank]:
                self.add_rank()

    def lose_star(self):
        """
        This function makes a user lose a star.
        """
        if self.rank > 0 and self.rank <= 20:
            self.star -= 1
            if self.star < 0:
                self.lose_rank()

    def add_rank(self):
        """
        This function makes a user gain a rank.
        """
        self.rank -= 1
        self.star = 1

    def lose_rank(self):
        """
        This function makes a user lose a rank.
        """
        if self.rank > 0 and self.rank < 20:
            self.rank += 1
            self.star = self.rank_star[self.rank] - 1
        elif self.rank == 20:
            self.star = 0


def rank(matches):
    """
    This function takes a string like "WLW"
    which indicates the match history of the game
    and return the current rank of the user.
    """
    user = User()
    matches = list(matches)

    for i in range(len(matches)):
        if matches[i] == 'W':
            # win

            # bonus star
            if user.rank >= 6 and user.rank <= 25:
                if i >= 2:
                    if matches[i-1] == 'W' and matches[i-2] == 'W':
                        user.add_star()

            user.add_star()
        elif matches[i] == 'L':
            # lose
            user.lose_star()

    # return rank
    if user.rank == 0:
        return('Legend')
    else:
        return(user.rank)


if __name__ == "__main__":
    import sys

    matches = sys.argv[1]

    print(rank(matches))
