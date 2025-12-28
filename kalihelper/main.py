import argparse
import sys
from kalihelper.hibp import check_password_pwned

# ========== COLOR CODES ==========
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
BOLD    = "\033[1m"
RESET   = "\033[0m"

# ========== BANNER ==========
def banner():
    print(f"""
{MAGENTA}{BOLD}
██╗  ██╗ █████╗ ██╗     ██╗██╗  ██╗███████╗██████╗ 
██║ ██╔╝██╔══██╗██║     ██║██║ ██╔╝██╔════╝██╔══██╗
█████╔╝ ███████║██║     ██║█████╔╝ █████╗  ██████╔╝
██╔═██╗ ██╔══██║██║     ██║██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██╗██║  ██║███████╗██║██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{RESET}
{CYAN}{BOLD}      🔐 HIBP PASSWORD CHECKER – KALI LINUX 🔐{RESET}
{BLUE}------------------------------------------------------{RESET}
{WHITE}  • Password-only  • Ethical  • No API Key Required{RESET}
{BLUE}------------------------------------------------------{RESET}
""")

# ========== MAIN ==========
def main():
    parser = argparse.ArgumentParser(
        description="Colorful KaliHelper – Password breach checker"
    )

    parser.add_argument(
        "-p", "--password",
        action="store_true",
        help="Check if a password has been leaked"
    )

    args = parser.parse_args()

    banner()

    if not args.password:
        print(f"{YELLOW}[!] Please use -p to check a password{RESET}")
        parser.print_help()
        sys.exit(0)

    # 🔓 Visible & highlighted input
    password = input(
        f"{CYAN}{BOLD}👉 Enter password (visible): {RESET}"
    )

    if not password.strip():
        print(f"{RED}{BOLD}[✖] Password cannot be empty{RESET}")
        sys.exit(1)

    print(f"\n{YELLOW}{BOLD}[+] Hashing password securely...{RESET}")
    print(f"{YELLOW}{BOLD}[+] Checking against breach database...{RESET}\n")

    try:
        found, count = check_password_pwned(password)
    except Exception as e:
        print(f"{RED}{BOLD}[!] Error: {e}{RESET}")
        sys.exit(1)

    if found:
        print(f"{RED}{BOLD}████  PASSWORD COMPROMISED  ████{RESET}")
        print(f"{RED}{BOLD}➜ Found {count} times in known breaches{RESET}")
    else:
        print(f"{GREEN}{BOLD}████  PASSWORD SAFE  ████{RESET}")
        print(f"{GREEN}{BOLD}➜ Not found in known breaches{RESET}")

    print(f"\n{BLUE}------------------------------------------------------{RESET}")
    print(f"{WHITE}{BOLD}✔ Check complete | Stay secure | KaliHelper{RESET}")
    print(f"{BLUE}------------------------------------------------------{RESET}")

# ========== ENTRY POINT ==========
if __name__ == "__main__":
    main()
