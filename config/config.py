from environs import Env

# environs kutubxonasidan foydalanib .env faylini o`qib olamiz
env = Env()
env.read_env()

# .env faylidagi ma`lumotlarni o`qib olamiz

# API parametrlari
SECRET_KEY = env.str("SECRET_KEY")
ALGORITHM = env.str("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = env.int("ACCESS_TOKEN_EXPIRE_MINUTES")

# Baza ma`umotlari
DB_CONNECTION=env.str("DB_CONNECTION")
DB_HOST=env.str("DB_HOST")
DB_PORT=env.str("DB_PORT")
DB_DATABASE=env.str("DB_DATABASE")
DB_USERNAME=env.str("DB_USERNAME")
DB_PASSWORD=env.str("DB_PASSWORD")
