This Python script offers a graphical user interface (GUI) for decrypting text files encrypted using a substitution cipher with a specified key. Here's an overview of its functionality:

<p align="center">
    <img width="467" alt="Dekrpt" src="https://github.com/jogamel/substitution_cipher_decryption/assets/123499578/a6345e16-4710-41d0-a282-8a93a8041901">
<p/>

The source code: *dekrpt.py*

**Importing Libraries**: The script imports necessary libraries, including tkinter for GUI components and filedialog for file browsing dialogs.

**Decrypt Text Function**: This function (decrypt_text) takes three parameters: the path of the input file, the path of the output file, and the decryption key. It reads the encrypted text from the input file, converts it to lowercase, performs decryption using a substitution cipher based on the provided key, and writes the decrypted text to the output file.

**Browse File Function**: This function (browse_file) is called when the user clicks the "Browse" button next to the input file entry. It opens a file dialog for selecting a file and populates the corresponding entry field with the selected file path.

**Decrypt Function**: This function (decrypt) is invoked when the user clicks the "Decrypt" button. It retrieves the input file path, output file path, and decryption key from the GUI inputs, calls the decrypt_text function, and displays the result in the GUI.

**GUI Setup**: The script creates a tkinter window (window). It then creates labels, entry fields, and buttons for input file selection, output file selection, key entry, decryption, and result display.

**Main Loop**: Finally, it starts the tkinter event loop (window.mainloop()), which keeps the GUI application running until the user closes the window.

This script provides a convenient way to decrypt text files encrypted with a substitution cipher, offering a user-friendly interface for the decryption process.

**Find the link to the encryption here**
https://github.com/jogamel/substitution_cipher_encryption
