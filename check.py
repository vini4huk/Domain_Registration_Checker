import whois
from colorama import Fore, Style

def check_domain_registration(domain):
    try:
        domain_info = whois.whois(domain)
        
        # Handling case where creation_date is a list
        if domain_info.creation_date:
            if isinstance(domain_info.creation_date, list):
                return bool(domain_info.creation_date[0])
            return True
        return False
    except whois.parser.PywhoisError:
        return False
    except Exception as e:
        print(f"{Fore.YELLOW}Warning: Could not check {domain} due to error: {e}{Style.RESET_ALL}")
        return False

def main():
    try:
        with open('domains.txt', 'r') as file:
            domains = file.readlines()
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File 'domains.txt' not found!{Style.RESET_ALL}")
        return
    
    try:
        with open('valid.txt', 'a') as valid_file:  # 'a' to append instead of overwrite
            for domain in domains:
                domain = domain.strip()
                if check_domain_registration(domain):
                    print(f"Domain {domain} {Fore.GREEN}is registered{Style.RESET_ALL}")
                    valid_file.write(domain + '\n')
                else:
                    print(f"Domain {domain} {Fore.RED}is not registered{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error writing to 'valid.txt': {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
