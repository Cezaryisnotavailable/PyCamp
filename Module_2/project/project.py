from logger import get_logger
from requests import get


def load_leaked_passwords():
    url = "https://haveibeenpwned.com/API/v3"

    with get(url) as content:
        for row in content.json():
            print(row)


def load_passwords(leaked_passwords):
    path_to_file = "passwords.txt"
    logger = get_logger()

    try:
        with open(path_to_file, mode="r", encoding="UTF-8") as passwords, open("safe_passwords", mode="w") as safe_passwords:
            for line in passwords:
                password = line.strip()
                if password in leaked_passwords:
                    pass

    except IOError:
        logger.error("Loading failed")
    else:
        logger.info("Password loaded successfully")
        return text_data


leaked_passwords = load_leaked_passwords()
print(leaked_passwords)
# loaded_passwords = load_passwords(leaked_passwords)
# print(loaded_passwords)
