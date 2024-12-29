

# Password Manager

This Python script serves as a lightweight and secure password manager, enabling you to store and retrieve passwords safely. Using the `cryptography` library, it ensures that your sensitive data is encrypted and protected from unauthorized access.

---

## Features
- **Password Encryption:** Utilizes Fernet encryption for robust and reliable password protection.
- **Salted Key Derivation:** Enhances security with a salted PBKDF2 key derivation mechanism, resistant to brute-force attacks.
- **Command-Line Interface:** Intuitive commands to add and retrieve passwords with minimal setup.
- **Secure File Storage:** Stores encrypted passwords in a file named `credentials.enc` for secure and convenient access.

---

## Prerequisites
Ensure the following requirements are met before using the script:

- Python 3.6 or higher is installed on your system.
- The `cryptography` library is installed.

### Install Dependencies
Run the following command to install the required library:
```bash
pip install cryptography
```

---

## Usage

### Command Syntax
```bash
python password_manager.py [add|get]
```

### Commands
1. **Add a Password:**
   - Command: `python password_manager.py add`
   - Prompts you to input a password, encrypts it, and securely saves it to `credentials.enc`.

2. **Retrieve a Password:**
   - Command: `python password_manager.py get`
   - Prompts you for the encryption password, decrypts, and displays the stored password if the correct key is provided.

---

## How It Works
1. **Key Generation:**
   - A secure key is generated from a user-provided password using PBKDF2 with SHA-256, making it computationally expensive to brute-force.

2. **Password Encryption and Decryption:**
   - Uses the `cryptography.fernet` module for symmetric encryption and decryption.

3. **Secure Storage:**
   - The encrypted password is stored in a file named `credentials.enc`.

---

## Code Structure
### Key Functions
1. **`generate_key(password):`**  
   - Generates an encryption key using PBKDF2 and a fixed salt.

2. **`load_credentials(key):`**  
   - Loads and decrypts the encrypted password file.

3. **`save_credentials(key, credentials):`**  
   - Encrypts and saves the password to a file.

4. **`main():`**  
   - Manages the command-line arguments (`add` or `get`) and executes the respective functionality.

---

## Examples
### Adding a Password
```bash
python password_manager.py add
Enter a new password: ********
Password saved.
```

### Retrieving a Password
```bash
python password_manager.py get
Enter your password: ********
Retrieved password: mysecurepassword
```

---

## Known Issues & Limitations
1. **Hardcoded Salt:** The salt is currently hardcoded as `b'salt'`. For enhanced security, consider using a unique or securely stored salt value for each user.
2. **File Dependency:** If the `credentials.enc` file is deleted or corrupted, the stored password cannot be recovered.

---

## Future Enhancements
- Support for managing multiple passwords.
- Improved salt management for better security.
- Integration with a secure database or cloud storage.
- Addition of a graphical user interface (GUI) for non-technical users.

---

## Author
This password manager script was developed as an educational project to demonstrate best practices in secure password storage using Python and the `cryptography` library. Contributions and improvements are welcome.

---

## License
This project is open-source and licensed under the MIT License. See the LICENSE file for more details.

---

This version includes:
- A **Future Enhancements** section to indicate possible extensions.
- Improved clarity in the **Known Issues** section.
- Consistent formatting and concise language.

