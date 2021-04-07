# Create a class called SteamUser. Upon initialization it should receive username (string), 
# games (list). It should also have an attribute called played_hours (0 by default). Add three 
# methodsto the class:
#   - play(game, hours) o   If the game is in the user games increase the played_hours by the 
#                           given hours and return "{username} is playing {game}"
#                       o   Otherwise, return "{game} is not in library"
#   - buy_game(game)    o   If the game is not already in the user's games, add it and return 
#                           "{username} bought {game}"
#                       o   Otherwise return "{game} is already in your library"
#   - stats()           o   returns "{username} has {games_count} games. Total play time: {played_hours}"

# Btw, Fortnite is only on Epic, not on Steam, so it is per default not in the Steam library... ;)


class SteamUser():

    played_hours = 0
    games_count = 0

    def __init__(self, username:str, games: list):
        self.username = username
        self.games = games
        self.games_count += len(games)
        # print ("A user has been created")

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, game):
        if game in self.games:
            return f"{game} is already in your library"
        else:
            # append the game to the list of games
            self.games.append(game)
            self.games_count += 1
            return f"{self.username} bought {game}"
    
    def stats(self):
        return f"{self.username} has {self.games_count} games. Total play time: {self.played_hours} hours."


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])

# print(user.games)

print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))

# print(user.games)

print(user.stats())
