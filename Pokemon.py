import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_pokemon_data(command):
    import openpyxl as xl

    wb = xl.load_workbook('Pokemons Dataset.xlsx')
    sheet = wb.active
    max_rows = sheet.max_row
    max_columns = sheet.max_column

    output = []
    command = command.capitalize()

    def pokemon_list():
        pokemon_list = []
        for i in range(1, max_rows):
            pokemon_list.append(sheet.cell(i + 1, 1).value)
        return pokemon_list

    if command in pokemon_list():
        index = pokemon_list().index(command) + 2

        for item in range(1, max_columns + 1):
            output.append(sheet.cell(index, item).value)

        pokemon, primary_type, secondary_type, attack, defence, HP, sp_attack, sp_defence, speed, total, strong_against, weak_against = \
        output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7], output[8], output[9], \
        output[10], output[11]
        if secondary_type is None:
            result = f"{pokemon} is {primary_type} type pokemon,\nit's attack power is {attack},\ndefence power is {defence},\nHP is {HP},\nspecial attack power is {sp_attack},\nspecial defence power is {sp_defence},\nspeed is {speed},\nit's total power is {total},\n{pokemon} is strong against {strong_against} type pokemons.\nit is weak against {weak_against} type pokemons."
        else:
            result = f"{pokemon} is {primary_type} and {secondary_type} type pokemon,\nit's attack power is {attack},\ndefence power is {defence},\nHP is {HP},\nspecial attack power is {sp_attack},\nspecial defence power is {sp_defence},\nspeed is {speed},\nit's total power is {total},\n{pokemon} is strong against {strong_against} type pokemons.\nit is weak against {weak_against} type pokemons."
    else:
        result = "There is no data about this Pokemon!"
    return result


pokemon = get_pokemon_data(input("Enter a Pokemon's Name: "))
print(pokemon)
speak(pokemon)