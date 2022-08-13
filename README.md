# django_poll_app

* List page
![](https://i.imgur.com/KGWL0Jk.png)

* Result page
  ![](https://i.imgur.com/suIjmnY.png)

Poll Application
* Register, Login, Logout account
* Question with two types, ```radio``` or ```checkbox```

<!-- GETTING STARTED -->
## Getting Started
### Prerequisites

* Python    
    1. [Install Python](https://www.python.org/)
    2. cmd:
        ```
        pip install pipenv
        ```

### Installation
Open cmd and follow the steps below
1. Clone the repo
   ```
   git clone https://github.com/AdamHsu2501/Django_poll_app.git
   ```
2. Into folder
   ```
   cd django_poll_app
   ```
3. Install virtual environment
   ```
   pipenv install
   ```
4. Run virtual environment
   ```
   pipenv Shell
   ```
5. Into Django folder
   ```
   cd config
   ```
6. Run server
   ```
   python manage.py runserver
   ```
7. open broswer with http://127.0.0.1:8000/ 
    * Login with Username ```admin``` and Password ```admin```, or register new account.
    * http://127.0.0.1:8000/admin can create question with two types, ```radio``` or ```checkbox```.
