from libs.ConsoleColors import TextColor

# Function to get colored input
def colored_input(prompt, color):
    return input(color + prompt + TextColor.RESET)

def essential_input(prompt):
    return input(TextColor.CYAN + prompt + TextColor.RESET)

def optional_input(prompt):
    return input(TextColor.GREEN + prompt + TextColor.RESET)

def msg_success(str):
    print(TextColor.BLUE + str + TextColor.RESET)

def msg_error(str):
    print(TextColor.RED + str + TextColor.RESET)

def msg_warning(str):
    print(TextColor.YELLOW + str + TextColor.RESET)

def msg_info(str):
    print(TextColor.CYAN + str + TextColor.RESET)

def msg_debug(str):
    print(TextColor.MAGENTA + str + TextColor.RESET)

def msg_normal(str):
    print(str)

def show_progress(str):
   spaces = " " * 30  # Assuming you want 60 spaces
   print(f"{TextColor.GREEN}{str}{spaces}{TextColor.RESET}", end='\r')