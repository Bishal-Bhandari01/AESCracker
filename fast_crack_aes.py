#!/usr/bin/env python3
"""
AES-Crypt File Decryption Tool for HTB Challenges
Attempts to decrypt an AES-encrypted file using a wordlist
"""

import pyAesCrypt
import os
import sys
from pathlib import Path
import time

# Security: Buffer size for encryption/decryption operations
BUFFER_SIZE = 64 * 1024


def validate_file_exists(filepath):
    """Validate that the file exists and is readable."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    if not path.is_file():
        raise ValueError(f"Not a file: {filepath}")
    if not os.access(filepath, os.R_OK):
        raise PermissionError(f"File not readable: {filepath}")
    return str(path)


def attempt_decrypt(encrypted_file, password, output_file):
    """
    Attempt to decrypt the file with the given password.
    
    Args:
        encrypted_file: Path to the encrypted .aes file
        password: Password to try
        output_file: Path where decrypted content should be saved
    
    Returns:
        bool: True if decryption successful, False otherwise
    """
    try:
        # Attempt decryption
        pyAesCrypt.decryptFile(
            encrypted_file,
            output_file,
            password,
            BUFFER_SIZE
        )
        return True
    except ValueError as e:
        # Wrong password or corrupted file
        return False
    except Exception as e:
        # Other errors (file I/O, etc.)
        print(f"[!] Unexpected error: {e}", file=sys.stderr)
        return False


def crack_aes_file(encrypted_file, wordlist_file, output_file="decrypted_output"):
    """
    Main function to crack AES encrypted file using wordlist.
    
    Args:
        encrypted_file: Path to the .aes encrypted file
        wordlist_file: Path to the wordlist (e.g., rockyou.txt)
        output_file: Path for the decrypted output file
    """
    # Validate inputs
    try:
        encrypted_file = validate_file_exists(encrypted_file)
        wordlist_file = validate_file_exists(wordlist_file)
    except (FileNotFoundError, ValueError, PermissionError) as e:
        print(f"[!] Error: {e}", file=sys.stderr)
        return False
    
    print(f"[+] Target file: {encrypted_file}")
    print(f"[+] Wordlist: {wordlist_file}")
    print(f"[+] Output file: {output_file}")
    print("[+] Starting decryption attempts...\n")
    
    attempts = 0
    start_time = time.time()
    
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as wl:
            for line in wl:
                password = line.strip()
                
                # Skip empty lines
                if not password:
                    continue
                
                attempts += 1
                
                # Progress indicator every 1000 attempts
                if attempts % 1000 == 0:
                    elapsed = time.time() - start_time
                    rate = attempts / elapsed if elapsed > 0 else 0
                    print(f"[*] Attempts: {attempts:,} | Rate: {rate:.0f} pass/sec | Current: {password[:30]}...")
                
                # Attempt decryption
                if attempt_decrypt(encrypted_file, password, output_file):
                    elapsed = time.time() - start_time
                    print(f"\n[+] SUCCESS!")
                    print(f"[+] Password found: {password}")
                    print(f"[+] Attempts: {attempts:,}")
                    print(f"[+] Time elapsed: {elapsed:.2f} seconds")
                    print(f"[+] Decrypted file saved to: {output_file}")
                    return True
    
    except KeyboardInterrupt:
        print("\n[!] Operation cancelled by user")
        return False
    except Exception as e:
        print(f"\n[!] Error reading wordlist: {e}", file=sys.stderr)
        return False
    
    elapsed = time.time() - start_time
    print(f"\n[-] Password not found")
    print(f"[-] Total attempts: {attempts:,}")
    print(f"[-] Time elapsed: {elapsed:.2f} seconds")
    return False


def main():
    """Main entry point."""
    if len(sys.argv) < 3:
        print("Usage: python3 aes_decrypt.py <encrypted_file.aes> <wordlist.txt> [output_file]")
        print("\nExample:")
        print("  python3 aes_decrypt.py web_20250806_120723.zip.aes rockyou.txt decrypted.zip")
        sys.exit(1)
    
    encrypted_file = sys.argv[1]
    wordlist_file = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else "decrypted_output"
    
    # Check if output file already exists
    if os.path.exists(output_file):
        response = input(f"[?] Output file '{output_file}' already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("[!] Operation cancelled")
            sys.exit(0)
        os.remove(output_file)
    
    success = crack_aes_file(encrypted_file, wordlist_file, output_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()