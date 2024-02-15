## Database Schema



![db_schema.png](db_schema.png)


---

##  Repository Structure

```sh
└── checkbox/
    ├── alembic
    │   ├── README
    │   ├── script.py.mako
    │   ├── versions 
    │   └── env.py   
    ├── db
    │   └── engine.py 
    ├── models
    │   └── models.py
    ├── schemas
    │   ├── auth.py
    │   └── receipt.py  
    ├── sucutity
    │   └── auth.py  
    ├── services 
    │   └── receipt
    │       └── receipt.py
    ├── templates
    │   └── receipt_template.html
    ├── tests
    │   ├── ....
    ├── .env
    ├── .gitignore
    ├── dependecies.py
    ├── docker-compose.yaml
    ├── enums.py
    ├── main.py
    ├── alembic.ini
    ├── README.md
    └── requirements.txt
    

```

---


##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.12`
* **Docker**

###  Installation

1. Clone the async-ml-inference repository:

```sh
git clone https://github.com/graandda/orderboxapi
```

2. Change to the project directory:

```sh
cd orderboxapi
```

3. Create environment:

```sh
python3.12 -m venv venv
```

4. Activate environment:
```sh
source venv/bin/activate
```

5. Install the dependencies:
```sh
pip install -r requirements.txt
```

6. Rename .env.example to .env:
```sh
mv .env.example .env
```

7. Run database in docker:
```sh
docker-compose up -d
```

8. Create migrations:
```sh
alembic init alembic
```

9. Run migrations:
```sh
alembic upgrade head
```


###  Running API



Use the following command to run server:

```sh
python main.py
```

URL: http://127.0.0.1:8000/docs/

---



###  Tests

To execute tests, run:

```sh
not implemented yet
```

---



