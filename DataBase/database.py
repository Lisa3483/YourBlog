from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker , declarative_base

# Подключение к базе данных
DATABASE_URL = "postgresql://postgres:123@localhost/YourBlog"
engine = create_engine(DATABASE_URL)

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Определение базового класса моделей
Base = declarative_base()

# Определение модели пользователя


# Создание таблицы в базе данных
def create_tables():
    Base.metadata.create_all(bind=engine)

# Получение экземпляра сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

create_tables()