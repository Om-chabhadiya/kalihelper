import hashlib
import requests

def check_password_pwned(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        print("[!] Error connecting to HIBP API")
        return

    for line in response.text.splitlines():
        leaked_hash, count = line.split(":")
        if leaked_hash == suffix:
            print(f"[!] Password FOUND in breaches ({count} times)")
            return

    print("[+] Password NOT found in known breaches")
