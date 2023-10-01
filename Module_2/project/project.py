from logger import get_logger
from requests import get
from hashlib import sha1

logger = get_logger()


def hex_password(password):
    hashed_password = sha1(str(password).encode("utf-8"))
    hexed_password = hashed_password.hexdigest()
    return hexed_password.upper()


def prefix_hexed_password(hexed_password):
    return hexed_password[0:5]


def download_prefix_hashes(prefix):
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = get(url)
    if response.status_code == 200:
        content = response.text
        cleaned_hashes = []

        for line in content.split("\n"):
            if line:
                suffix = line.split(":")[0].strip().upper()
                cleaned_hashes.append(prefix.upper() + suffix)
        return cleaned_hashes

    else:
        logger.error(f"Error with API: status code: {response.status_code}")


def check_passwords():
    try:
        with open("passwords.txt", mode="r", encoding="UTF-8") as passwords, \
                open("safe_passwords", mode="w") as safe_passwords:
            for line in passwords:
                password = line.strip()
                hexed_password = hex_password(password)
                leaked_passwords = download_prefix_hashes(prefix_hexed_password(hexed_password))

                if hexed_password in leaked_passwords:
                    logger.warning(f"Leaked password {password}")
                else:
                    safe_passwords.write(password + "\n")

    except IOError:
        logger.error("Loading failed")
    else:
        logger.info("Passwords checked successfully")


def check_password_if_leaked(password):
    hexed_password = hex_password(password)
    leaked_passwords = download_prefix_hashes(prefix_hexed_password(hexed_password))
    if hexed_password in leaked_passwords:
        logger.warning(f"Leaked password. Change your password!")
        return True
    else:
        logger.info(f"Your password has not been leaked")
        return False


if __name__ == "__main__":
    # check_passwords()
    check_password_if_leaked(input("Check your password "))
