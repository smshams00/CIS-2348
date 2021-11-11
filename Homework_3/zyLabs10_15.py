# Syed Shams
# 1820287

class Team:
    def __init__(self, team_name='none', team_wins=0, team_losses=0):
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses

    def get_win_percentage(self):
        win_percentage = self.team_wins / (self.team_wins + self.team_losses)
        return win_percentage


if __name__ == "__main__":
    realTeam = Team()

    TeamN = input()
    TeamW = int(input())
    TeamL = int(input())

    realTeam.team_name = TeamN
    realTeam.team_wins = TeamW
    realTeam.team_losses = TeamL

    result = realTeam.get_win_percentage()

    if result > 0.5:
        print("Congratulations, Team {} has a winning average!".format(TeamN))
    else:
        print("Team {} has a losing average.".format(TeamN))
