# Domain Registration Checker

This Python script checks if domains are registered using the `whois` library. It reads a list of domains from the `domains.txt` file, checks each domain, and writes the registered domains to the `valid.txt` file.

## Features

* Uses the `whois` library to retrieve domain information.
* Uses `colorama` for colored output in the console.
* Reads a list of domains from the `domains.txt` file.
* Writes registered domains to the `valid.txt` file.
* Handles errors such as a missing `domains.txt` file and `whois` errors.

## Required Libraries

* `whois`: `pip install python-whois`
* `colorama`: `pip install colorama`

## Usage

1.  **Install the required libraries:**

    ```bash
    pip install python-whois colorama
    ```

2.  **Create the `domains.txt` file:**

    Create a file named `domains.txt` in the same directory as the script. Each domain should be on a separate line. For example:

    ```
    google.com
    example.net
    invalid-domain-example.xyz
    ```

3.  **Run the script:**

    Run the Python script:

    ```bash
    python check.py
    ```


## Results

* The script will print the results of each domain check to the console.
* Registered domains will be written to the `valid.txt` file.

## Console Output

* **Green text:** Domain is registered.
* **Red text:** Domain is not registered.
* **Yellow text:** Warning about an error during domain check.

## Error Handling

* If the `domains.txt` file is not found, the script will print an error message and exit.
* If an error occurs while using `whois`, the script will print a warning and continue checking other domains.
* If an error occurs while writing to the `valid.txt` file, the script will print an error message.
