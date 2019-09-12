# pixieLogger
## About
pixieLogger is a lightweight example of a cross-platform keylogging apparatus intended for use in security testing. This tool is intended to capture user input through a global keyboard listener and temporarily store said information in a dictionary using a microtimestamp as the key with the keyboard input as the value. Every 5 minutes a post request is sent to the supplied endPoint which will store the payload.

## Compiling;
Compilition of this software is expected to be done on the relevant targeted platforms using a Python to XX compiler.
Something like py2exe / py2app or cx_freeze.

## Notice:
This tool is intended to capture sensitive information and securely transfer said information to a third party endPoint using HTTPS/TLS, this is intended for demonstration purposes only and should be used responsibly. By using this software you agree to idemnify any and all Pixies including myself from any and all implicit or explicit legal responsibilities.
