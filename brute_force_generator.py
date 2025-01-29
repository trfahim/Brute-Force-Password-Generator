from colorama import Fore
import pyfiglet,os


def banner():
    os.system("cls")
    text = pyfiglet.figlet_format("PASSWORD MAKER-1.0")
    print(Fore.RED+text)
    print("-"*50)

def generate_password_list(first_name, middle_name, last_name,
                           first_name_ca, 
                           first_name_lo,
                           first_name_ti,
                           middle_name_ca,
                           middle_name_lo,
                           middle_name_ti,
                           last_name_ca,
                           last_name_lo,
                           last_name_ti):
    passwords = []
    symbol_at = ("@")
    symbol_hash = ("#")
    symbol_and = ("&")
    
    passwords.append(f"{first_name}")
    passwords.append(f"{first_name_ca}")
    passwords.append(f"{first_name_lo}")
    passwords.append(f"{first_name_ti}")
    passwords.append(f"{first_name}{symbol_at}")
    passwords.append(f"{first_name_ca}{symbol_at}")
    passwords.append(f"{first_name_lo}{symbol_at}")
    passwords.append(f"{first_name_ti}{symbol_at}")
    passwords.append(f"{first_name}{symbol_hash}")
    passwords.append(f"{first_name_ca}{symbol_hash}")
    passwords.append(f"{first_name_lo}{symbol_hash}")
    passwords.append(f"{first_name_ti}{symbol_hash}")
    passwords.append(f"{first_name}{symbol_and}")
    passwords.append(f"{first_name_ca}{symbol_and}")
    passwords.append(f"{first_name_lo}{symbol_and}")
    passwords.append(f"{first_name_ti}{symbol_and}")
    
    passwords.append(f"{middle_name}")
    passwords.append(f"{middle_name_ca}")
    passwords.append(f"{middle_name_lo}")
    passwords.append(f"{middle_name_ti}")
                               
    passwords.append(f"{last_name}")
    passwords.append(f"{last_name_ca}")
    passwords.append(f"{last_name_lo}")
    passwords.append(f"{last_name_ti}")
    passwords.append(f"{last_name}{symbol_at}")
    passwords.append(f"{last_name_ca}{symbol_at}")
    passwords.append(f"{last_name_lo}{symbol_at}")
    passwords.append(f"{last_name_ti}{symbol_at}")
    passwords.append(f"{last_name}{symbol_hash}")
    passwords.append(f"{last_name_ca}{symbol_hash}")
    passwords.append(f"{last_name_lo}{symbol_hash}")
    passwords.append(f"{last_name_ti}{symbol_hash}")
    passwords.append(f"{last_name}{symbol_and}")
    passwords.append(f"{last_name_ca}{symbol_and}")
    passwords.append(f"{last_name_lo}{symbol_and}")
    passwords.append(f"{last_name_ti}{symbol_and}")
                               
    full_name_1 = f"{first_name}{middle_name}{last_name}" if middle_name else f"{first_name}{last_name}"
    passwords.append(f"{full_name_1}")
    passwords.append(f"{full_name_1.upper()}")
    passwords.append(f"{full_name_1.lower()}")
    passwords.append(f"{full_name_1.title()}")
    
    full_name_2 = f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"
    passwords.append(f"{full_name_2.upper()}")
    passwords.append(f"{full_name_2.lower()}")
    passwords.append(f"{full_name_2.title()}")

    for num in range(100001): 
        digit = str(num)  
        
        passwords.append(f"{first_name}{digit}")
        passwords.append(f"{first_name_ca}{digit}")
        passwords.append(f"{first_name_lo}{digit}")
        passwords.append(f"{first_name_ti}{digit}")
        
        #Symbol_firstname
        #symbol_hash = ("@") FIRSTNAME 
        passwords.append(f"{first_name}{symbol_at}{digit}")
        passwords.append(f"{first_name_ca}{symbol_at}{digit}")
        passwords.append(f"{first_name_lo}{symbol_at}{digit}")
        passwords.append(f"{first_name_ti}{symbol_at}{digit}")
        
        #symbol_hash = ("#") FIRSTNAME
        passwords.append(f"{first_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{first_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{first_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{first_name}{symbol_hash}{digit}")
        
        #symbol_and = ("&") FIRSTNAME
        passwords.append(f"{first_name_ca}{symbol_and}{digit}")
        passwords.append(f"{first_name}{symbol_and}{digit}")
        passwords.append(f"{first_name_lo}{symbol_and}{digit}")
        passwords.append(f"{first_name_ti}{symbol_and}{digit}")
        
        if middle_name: 
            passwords.append(f"{middle_name}{digit}")
            passwords.append(f"{middle_name_ca}{digit}")
            passwords.append(f"{middle_name_lo}{digit}")
            passwords.append(f"{middle_name_ti}{digit}")
            
            #Symbol_middlename
            # symbol_at = ("@") Middle Name
            passwords.append(f"{middle_name_ca}{symbol_at}{digit}")
            passwords.append(f"{middle_name_lo}{symbol_at}{digit}")
            passwords.append(f"{middle_name_ti}{symbol_at}{digit}")
            passwords.append(f"{middle_name}{symbol_at}{digit}")
            
            # symbol_hash = ("#")
            passwords.append(f"{middle_name_ca}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_lo}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_ti}{symbol_hash}{digit}")
            passwords.append(f"{middle_name}{symbol_hash}{digit}")
            
            # symbol_and = ("&")
            passwords.append(f"{middle_name_ca}{symbol_and}{digit}")
            passwords.append(f"{middle_name_lo}{symbol_and}{digit}")
            passwords.append(f"{middle_name_ti}{symbol_and}{digit}")
            passwords.append(f"{middle_name}{symbol_and}{digit}")
        
        #Symbol_lastname
        # symbol_at = ("@")
        passwords.append(f"{last_name_ca}{symbol_at}{digit}")
        passwords.append(f"{last_name_lo}{symbol_at}{digit}")
        passwords.append(f"{last_name_ti}{symbol_at}{digit}")
        passwords.append(f"{last_name}{symbol_at}{digit}")
        
        # symbol_hash = ("#")
        passwords.append(f"{last_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{last_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{last_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{last_name}{symbol_hash}{digit}")
        
        # symbol_and = ("&")
        passwords.append(f"{last_name_ca}{symbol_and}{digit}")
        passwords.append(f"{last_name_lo}{symbol_and}{digit}")
        passwords.append(f"{last_name_ti}{symbol_and}{digit}")
        passwords.append(f"{last_name}{symbol_and}{digit}")
        
        passwords.append(f"{last_name}{digit}")
        passwords.append(f"{last_name_ca}{digit}")
        passwords.append(f"{last_name_lo}{digit}")
        passwords.append(f"{last_name_ti}{digit}")
        
        full_name = f"{first_name}{middle_name}{last_name}" if middle_name else f"{first_name}{last_name}"
        passwords.append(f"{full_name}{digit}")
        passwords.append(f"{full_name.upper()}{digit}")
        passwords.append(f"{full_name.lower()}{digit}")
        passwords.append(f"{full_name.title()}{digit}")
        
        full_name_space = f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"
        passwords.append(f"{full_name_space}{digit}")
        passwords.append(f"{full_name_space.upper()}{digit}")
        passwords.append(f"{full_name_space.lower()}{digit}")
        passwords.append(f"{full_name_space.title()}{digit}")
        
        full_name_cap = f"{first_name.capitalize()}{middle_name.capitalize()}{last_name.capitalize()}" if middle_name else f"{first_name.capitalize()}{last_name.capitalize()}"
        passwords.append(f"{full_name_cap}{digit}")
    
    return passwords

def save_to_file(passwords, filename="Custom_Passwordlist.txt"):
    with open(filename, "w") as file:
        for password in passwords:
            file.write(password + "\n")
    banner()
    print(Fore.YELLOW+f"\nPassword list saved to {Fore.WHITE}'{filename}'\n")
    print(Fore.RED+"-"*50)

def main():
    banner()
    first_name = input(Fore.CYAN+f"\nEnter First Name:{Fore.GREEN} ").strip()
    middle_name = input(Fore.CYAN+f"Enter Middle Name (leave blank if none):{Fore.GREEN} ").strip()
    last_name = input(Fore.CYAN+f"Enter Last Name:{Fore.GREEN} ").strip()
    
    first_name_ca = first_name.upper()
    first_name_lo = first_name.lower()
    first_name_ti = first_name.title()
    middle_name_ca = middle_name.upper()
    middle_name_lo = middle_name.lower()
    middle_name_ti = middle_name.title()
    last_name_ca = last_name.upper()
    last_name_lo = last_name.lower()
    last_name_ti = last_name.title()

    file_name = (f"Brutefoce_Passwordlist_{first_name.upper()}.txt")
    
    password_list = generate_password_list(first_name, middle_name, last_name,
                                           first_name_ca, 
                                           first_name_lo,
                                           first_name_ti,
                                           middle_name_ca,
                                           middle_name_lo,
                                           middle_name_ti,
                                           last_name_ca,
                                           last_name_lo,
                                           last_name_ti)
                                    
    save_to_file(password_list)


if __name__ == "__main__":
    main()
