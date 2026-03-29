# Simple Password Generator

A lightweight Python script that generates a secure, randomized **12-character password** using a mix of uppercase letters, lowercase letters, digits, and special characters.

## Features
* **Secure Characters:** Uses the `string` module to include `ascii_letters`, `digits`, and `punctuation`.
* **No Dependencies:** Uses standard Python libraries (`random`, `string`)—no need to install external packages.
* **Instant Output:** Generates a new password immediately upon execution.

## How It Works
The script utilizes a generator expression to pull random characters from a combined pool of symbols:

1.  **Letters:** `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`
2.  **Numbers:** `0123456789`
3.  **Symbols:** `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`

## Prerequisites
* Python 3.x installed on your machine.

## Usage
1.  **Clone or download** the script file (e.g., `generator.py`).
2.  Open your terminal or command prompt.
3.  Run the script using the following command:
    ```bash
    python generator.py
    ```

### Example Output
```text
_____________________
|PASSWORD GENERATOR |
|___________________|
your generated password:
4&vP#zQ9!kL[
```

## Security Note
This script uses Python's `random` module, which is suitable for general use. For high-security applications (like banking or encryption keys), it is recommended to use the `secrets` module, which is cryptographically secure.

