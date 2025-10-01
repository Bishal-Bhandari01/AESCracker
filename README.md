# AESCracker File Decryption Tool

A high-performance Python tool for brute-force decrypting AES-encrypted files using wordlists. Designed specifically for CTF challenges and penetration testing scenarios where you need to recover passwords for AES-encrypted archives.

## Features
- **Fast Decryption**: Optimized buffer handling for efficient file operations
- **Progress Monitoring**: Real-time progress with attempt counts and speed metrics
- **Error Handling**: Robust error handling for corrupted files and I/O issues
- **Memory Efficient**: Stream-based processing for large files
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Unicode Support**: Handles various character encodings in wordlists

## Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Dependencies
```bash
pip install pyAesCrypt
```
### Quick Setup
```bash
git clone https://github.com/Bishal-Bhandari01/AESCracker.git
cd AESCracker
```
## Usage
```bash 
python3 fast_crack_aes.py <encrypted_file.aes> <wordlist.txt>
```
## Example
<strong>Decrypt a backup file using rockyou.txt:</strong>
```bash
python3 fast_crack_aes.py backup.zip.aes rockyou.txt
```
- You can also output the data:
```bash
python3 fast_crack_aes.py backup.zip.aes rockyou.txt decrypted_backup.zip
or
python3 fast_crack_aes.py backup.zip.aes rockyou.txt decrypted_backup.txt
```
## Arguments
- ```encrypted_file.aes```: Path to the AES-encrypted file (must have .aes extension)
- ```wordlist.txt```: Path to password wordlist file
- ```output_file```: (Optional) Path for decrypted output (default: "decrypted_output")
## How It Works
1. <strong>File Validation</strong>: Verifies encrypted file and wordlist exist and are readable
2. <strong>Stream Processing</strong>: Uses buffer-based streaming for memory efficiency
3. <strong>Password Attempts</strong>: Iterates through wordlist, attempting each password
4. <strong>Success Detection</strong>: Valid decryption is detected by successful file output
5. <strong>Progress Reporting</strong>: Provides real-time feedback on attempts and speed
## Performance
1. <strong>Buffer Size</strong>: 64KB buffer for optimal performance
2. <strong>Speed</strong>: Typically processes 1000+ passwords per second
3. <strong>Memory</strong>: Low memory footprint even with large files
4. <strong>Resilient</strong>: Continues on encoding errors in wordlists
## Use Cases
### CTF Challenges
- Decrypting encrypted flags or evidence files
- Recovering passwords from encrypted backups
- Cracking AES-protected configuration files
### Penetration Testing
- Testing password strength of encrypted backups
- Recovering lost passwords for business continuity
- Security assessment of encryption implementations
### Digital Forensics
- Accessing encrypted evidence files
- Password recovery for legal investigations
- Data recovery operations
## Example Output
```bash
[+] Target file: secret_backup.zip.aes
[+] Wordlist: rockyou.txt
[+] Output file: decrypted_backup.zip
[+] Starting decryption attempts...

[*] Attempts: 1,000 | Rate: 1250 pass/sec | Current: password123...
[*] Attempts: 2,000 | Rate: 1280 pass/sec | Current: letmein456...

[+] SUCCESS!
[+] Password found: summer2024
[+] Attempts: 2,347
[+] Time elapsed: 1.84 seconds
[+] Decrypted file saved to: decrypted_backup.zip
```
## File Support
Works with any file type encrypted using AES-Crypt format:
- 📁 ZIP archives
- 📄 Text files
- 🗃️ Database backups
- 🔧 Configuration files
- 📷 Media files
- And any other file type
## Common Wordlists
- <strong>rockyou.txt</strong> - Comprehensive common passwords
- <strong>SecLists</strong> - Collection of multiple wordlists
- <strong>CrackStation</strong> - Large password dictionary
- <strong>Custom wordlists</strong> - Organization-specific passwords
## Security Notes
⚠️ <strong>Legal Use Only</strong>: This tool is intended for:
- Authorized penetration testing
- CTF challenges and educational purposes
- Personal data recovery (your own files)
- Legal forensic investigations
🚫 <strong>Do not use for:</strong>
- Unauthorized access to systems
- Illegal data recovery
- Malicious activities
## Troubleshooting
### Common Issues
<strong>"File not found" error</strong>
- Verify file paths are correct
- Check file permissions
<strong>"ModuleNotFoundError: No module named 'pyAesCrypt'"</strong>
```bash
Run pip install pyAesCrypt
```
<strong>Slow performance</strong>
- Use SSD storage for wordlist files
- Ensure adequate system resources
<strong>Unicode errors</strong>
- Tool handles encoding errors automatically
- For problematic wordlists, try different encoding
## Contributing
- Fork the repository
- Create a feature branch ```(git checkout -b feature/improvement)```
- Commit your changes ```(git commit -am 'Add new feature')```
- Push to the branch ```(git push origin feature/improvement)```
- Create a Pull Request
## Acknowledgement
- Built with ```pyAesCrypt```
- Inspired by CTF challenges and real-world penetration testing scenarios

Thanks to the security community for continuous improvement

## Disclamier
Use this tool responsibly and only on systems you own or have explicit permission to test. The developers are not responsible for misuse.
