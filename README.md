# login-page

#  Login Page using Python and Flask

This is a simple **Login System Web App** built using **Python (Flask)**.  
It includes features like user login, register, and password recovery (forget password).

---

##  Features

-  User Registration
-  Secure Login
-  Forgot Password Recovery Option
-  Form validation
-  Clean UI using HTML + CSS

---

##  Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS
- **Storage**: JSON file for user data (`user.json`)

---

##  How to Run Locally

### 1. Clone this repo

```bash
git clone https://github.com/shinetech123/login-page.git
cd login-page


login-page/
│
├── app.py                    # Flask backend - main Python file
├── user.json                 # Stores user data (username, password, etc.)
│
├── templates/                # HTML pages (Tailwind styled)
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── forgot_password.html
│
└── static/                   # (Optional) For custom CSS or images
    └── (keep empty or add files later)

for runnable 

##clone this repo.

git clone https://github.com/shinetech123/login-page.git
cd login-page

#install flask
 pip install flask

# run the flask app 
  python app.py
