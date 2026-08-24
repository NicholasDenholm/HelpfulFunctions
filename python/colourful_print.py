def echo(text, color="red"):
    reset ='\033[0m'
    colour = color.strip().upper()
    match colour:
        case "RED":
            result ='\033[31m'
        case "GREEN":
            result ='\033[32m'
        case "BLUE":
            result ='\033[34m'
        case "RED":
            result ='\033[31m'
        case _:
            result ='\033[31m'
    
    if result:
        # print(f"\033[31m{text}\033[0m") 
        print(f"{result}{text}{reset}") 
    else:
        print(text)

echo("Warning!", "purple")
echo("Warning!", "GReen  ")
echo("Warning!", "Blue")