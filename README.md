# Software Testing and Quality Assurance Mini Project
# Ecommerce Project Setup

This guide will help you set up and run the Ecommerce project locally on your system. The steps involve using XAMPP for the local server and MySQL for the database, as well as running a Selenium script for testing.

## Prerequisites

1. **XAMPP**: A local web server stack that includes Apache, MySQL, and PHP.
2. **Python**: You need Python installed to run the Selenium script (`script.py`).
3. **Selenium**: Install Selenium using `pip` to run the test scripts.

### 1. Install XAMPP
- Download and install XAMPP from [the official website](https://www.apachefriends.org/index.html).
- Follow the installation instructions for your operating system.

### 2. Download the Project
- Clone or download the Ecommerce GitHub repository to your local machine.

### 3. Set up the Project in XAMPP

1. **Move the Project to XAMPP's `htdocs` Folder**:
   - Copy the entire Ecommerce project folder into XAMPP's `htdocs` directory.
     - By default, `htdocs` is located in the XAMPP installation directory (e.g., `C:\xampp\htdocs` on Windows or `/opt/lampp/htdocs/` on Linux).

2. **Start XAMPP**:
   - Open the **XAMPP Control Panel** and start both the **Apache** and **MySQL** modules.

### 4. Set Up the Database

1. **Access phpMyAdmin**:
   - Open your web browser and go to: `http://localhost/phpmyadmin/`.
   - This will open the phpMyAdmin interface for managing MySQL databases.

2. **Create the Database**:
   - In phpMyAdmin, click on the **Databases** tab.
   - In the "Create database" field, enter `ecommerce` (or another name if preferred).
   - Click **Create**.

3. **Import the Database**:
   - Click on the newly created `ecommerce` database.
   - Navigate to the **Import** tab.
   - Click **Choose File** and select the `.sql` file from the Ecommerce project directory (usually found in the `ecommerce` directory).
   - Click **Go** to import the database.

### 5. Run the Selenium Script

1. **Install Python and Selenium**:
   - If you haven't installed Python yet, download and install it from [python.org](https://www.python.org/).
   - Install the Selenium Python package by running:
     ```bash
     pip install selenium
     ```

2. **Run the Selenium Script**:
   - Navigate to the directory containing the `script.py` file.
   - Run the script using Python:
     ```bash
     python script.py
     ```

### 6. Verify Everything is Working

- You should be able to access the local Ecommerce site by visiting `http://localhost/ecommerce` in your browser.
- The Selenium script should execute its tasks automatically.

## Troubleshooting

- **Apache or MySQL not starting**: Ensure there are no other applications (like Skype) using the same ports (80 for Apache, 3306 for MySQL).
- **Database import issues**: If the import fails, check if the `.sql` file is properly formatted and try importing it again.
- **Selenium issues**: Ensure you have the correct web driver (e.g., ChromeDriver) for Selenium and that it's installed on your system.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy coding! 🚀
