from clearConsole import clearConsole
from health_bar import health_bar


def stats(player, name):
    print(
        f"""
    -------------
    Name: {name}
    Hp: {health_bar(player)}
    Damage: {player.dmg}
    -------------
    """)
    input("     Press any button to go back to menu").casefold()
    clearConsole()
