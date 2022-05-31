def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "YOU DID NOT PROVIDE ANY DATA"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
print(format_name(input("What is ur first name?") , input("What is ur last name?")))
