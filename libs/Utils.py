import ConsoleColors

# Function to get colored input
def colored_input(prompt, color):
    return input(color + prompt + ConsoleColors.TextColor.RESET)

def essential_input(prompt, color):
    return input(ConsoleColors.TextColor.CYAN + prompt + ConsoleColors.TextColor.RESET)

def optional_input(prompt, color):
    return input(ConsoleColors.TextColor.GREEN + prompt + ConsoleColors.TextColor.RESET)

def msg_success(str):
    print(ConsoleColors.TextColor.BLUE + str + ConsoleColors.TextColor.RESET)

def msg_error(str):
    print(ConsoleColors.TextColor.RED + str + ConsoleColors.TextColor.RESET)

def msg_warning(str):
    print(ConsoleColors.TextColor.YELLOW + str + ConsoleColors.TextColor.RESET)

def msg_info(str):
    print(ConsoleColors.TextColor.CYAN + str + ConsoleColors.TextColor.RESET)

def msg_debug(str):
    print(ConsoleColors.TextColor.MAGENTA + str + ConsoleColors.TextColor.RESET)

def msg_normal(str):
    print(str)