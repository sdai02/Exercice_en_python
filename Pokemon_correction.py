# Correction TP1
#!/usr/bin/python

# 4th step
liste = []

# 1st step
def newPokemon():
# Function for create pokemon
    name = input("Enter the name of your Pokemon: ")
    type = input("Enter the type of your Pokemon (fire, water, plant, etc.): ")
    hp = int(input("Enter the HP of your Pokemon: "))
    attack = int(input("Enter the attack of your Pokemon: "))
    defense = int(input("Enter the defense of your Pokemon: "))

    # 2nd step
    pokemon = {
        "name": name,
        "type": type,
        "hp": hp,
        "attack": attack,
        "defense": defense
    }

    return pokemon

# region 3rd step
# Call newPokemon for interact with user and create pokemon
#pokemon1 = newPokemon()
#pokemon2 = newPokemon()
# endregion


# region 4th step
# Add both Pokemon to the list
#liste.append(pokemon1)
#list.append(pokemon2)
# endregion

# region 5th step
# Display the list of created Pokemon
#print("\nHere are the Pokemon you created:")
#print(f"1. Name: {pokemon1['name']}, Type: {pokemon1['type']}, HP: {pokemon1['hp']}, Attack: {pokemon1['attack']}, Defense: {pokemon1['defense']}")
#print(f"2. Name: {pokemon2['name']}, Type: {pokemon2['type']}, HP: {pokemon2['hp']}, Attack: {pokemon2['attack']}, Defense: {pokemon2['defense']}")
# endregion


def arrayChecker():
    if liste != None:
        message = "do you want creat a pokemon ?\n"

        print(f"{message}")

        condition = input("yes or no\n")

        while condition == "yes":

            pokemon1 = newPokemon()
            liste.append(pokemon1)
            print(f"Name :{pokemon1['name']}\n Type: {pokemon1['type']}\n HP: {pokemon1['hp']}\n Attack: {pokemon1['attack']}\n Defense: {pokemon1['defense']}\n")
            print(f"{message}")
            condition = input("yes or no\n")

            if condition == "no":
                break
           


arrayChecker()

