# django_poll_app

1. Install Python <https://www.python.org/>
2. Open ****cmd****
    ```
    # download repo
    > git clone https://github.com/AdamHsu2501/Django_poll_app.git
    > cd django_poll_app
    
    # install pipenv
    > pip install pipenv
    
    # Install packages
    > pipenv install
    
    # Start virtual envirment
    > pipenv shell
    > cd config
    
    # Start server
    > python manage.py runserver
    ````
3. Open broswer with http://127.0.0.1:8000/. Login with Username ```admin``` Password ```admin``` or register new account.
    * Implement authentication login and registration, and redirect from ```/login``` and ```/register``` while logged in
        
    * http://127.0.0.1:8000/admin can create question with two types, ```radio``` or ```checkbox```.

* List page
![](https://i.imgur.com/KGWL0Jk.png)

* Result page
  ![](https://i.imgur.com/zbmZECC.png)