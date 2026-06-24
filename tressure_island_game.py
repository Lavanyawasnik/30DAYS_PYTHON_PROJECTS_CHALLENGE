print('''           _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.' ||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-''')
print("welcome to treassure island game")
print("your mission is to find the tressure")
choice1 = input(" you're at a crossroad , where do you want to go?"
            "type left or right."). lower()
if choice1 == "left":
    choice2 = input("you've come to a lake , there is an island in the middle of the lake, type wait"
                    " to [wait] for a boat, type [swim] to swim across."). lower()
    if choice2 == "wait":
        choice3 = input("you arrive at the island unharmed. there is house with 3 doors.one red"
                        "one yellow and one blue, which colour do you choose?"). lower()

        if choice3 == "red":
            print("its a room full of fire. GAMEOVER")
        elif choice3 == "yellow":
            print("you found the tressure. YOUWIN")
        elif choice3 == "blue":
            print("you enter a room of beats. GAMEOVER.")
        else:
            print("you choose a door that doesnt exist. GAMEOVER")
    else:
        print("you got attacked by an angry trout . GAMEOVER")