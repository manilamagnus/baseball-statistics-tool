#baseball stats game


team1 = input("enter team #1: ")
runsscored1 = float(input("enter runs scored: "))
runsallowed1 = float(input("enter runs allowed: "))

print("\n")

team2 = input("enter team #2: ")
runsscored2 = float(input("enter runs scored: "))
runsallowed2 = float(input("enter runs allowed: "))

team1score = (runsscored1 ** 2) / ((runsscored1 ** 2) + (runsallowed1 ** 2))
team2score = (runsscored2 ** 2) / ((runsscored2 ** 2) + (runsallowed2 ** 2))

if team1score > team2score:
    print("\n")
    percent1 = (team1score / (team1score + team2score)) * 100
    print("[Results]:")
    print("the " + team1 + " have a " + str(percent1) + " percent chance of winning")
elif team2score > team1score:
    print("\n")
    print("[Results]:")
    percent2 = (team2score / (team1score + team2score)) * 100
    print("the " + team2 + " have a " + str(percent2) + " percent chance of winning")


print("\n")
statsbutton = input("click [enter] for more stats")
print("\n")

if team1score > team2score:
    team1percentage = team1score * 100
    team2percentage = team2score * 100
    print("The " + team1 + "have a " + str(team1percentage) + (" winning percentage"))
    print("The " + team2 + "have a " + str(team2percentage) + (" winning percentage"))
elif team2score > team1score:
    team1percentage = team1score * 100
    team2percentage = team2score * 100
    print("The " + team2 + " have a " + str(team2percentage) + (" winning percentage"))
    print("The " + team1 + " have a " + str(team1percentage) + (" winning percentage"))







