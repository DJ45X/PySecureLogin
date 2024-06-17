# Welcome to my Secure Login Project!
___

This Python project showcases my proficiency in password encryption and secure database storage techniques using salting and hashing methods with bcrypt. Designed as a command-line application rather than a full-fledged website, the project prioritizes a focused exploration of password security principles. By implementing bcrypt for hashing passwords and incorporating salting to mitigate common vulnerabilities, this project underscores the importance of robust password management practices in safeguarding user credentials.

As I advance in my cybersecurity journey, I recognize that mastering password encryption and security is fundamental to developing a comprehensive skill set in this field. This Python project serves as a practical demonstration of my commitment to learning and implementing robust security practices, essential for safeguarding sensitive information in digital environments.

Future additions may include password peppering to further demonstrate more complex password encryption methods.

**Technologies used include:**
- Python
- Bcrypt
- SQL (MariaDB was used in my environment)

This project is released under the MIT License, granting everyone the freedom to use, modify, and distribute the code as they see fit.
___
### Setup
1. Setup a SQL database such as MySQL or MariaDB
2. Using the supplied `example.env` as a template, create your own `.env` to store you DB connection credentials
3. Run `pip install -r requirements.txt` to install require packages
4. Run `python main.py`to start the app!
   
**Note:**
DB Table creation will be done automatically. See Testing below for further info.
___
### Usage
This application is intended to simulate user registration and log in. When you run the app, you'll be greeted with 3 options:
- `[1] - Register a new user`
- `[2] - Login`
- `[3] - Exit`

[1] will allow you to "register" a new user with a username and password. This is where a random salt is generated and assigned to the username within the database. Successful registration will have a simple message indicating success.

[2] is used for logging in with a registered user. A simple message will indicate whether the password supplied was incorrect, user doesn't exist, or successful login. This is where validation between the user's supplied password (hased with the user's stored salt) matches the salted hash stored in the database.

[3] will simply exit the program gracefully.

My main objective with this app was to learn and understand password encryption and salting. This python app demonstrates the knowledge I've learned.
___
### Testing
There are 2 scripts that can be used for testing. While both are utilized automatically when running `main.py`, you can use them individually as well.

- `db_connection_test.py` will test your connection with your database
- `db_init.py` will initialize the databse, checking if the 'users' table exists, creating it if it doesn't with the proper fields.
___
### Future Ideas
I plan to explore other methods to password encryption such as peppering and other hashing methods like bcrypt. OAuth is another implementation that would be worth exploring in the future. 