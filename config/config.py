from environs import Env

# environs kutubxonasidan foydalanib .env faylini o`qib olamiz
env = Env()
env.read_env()

# .env faylidagi ma`lumotlarni o`qib olamiz

DB_CONNECTION=env.str("DB_CONNECTION")
DB_HOST=env.str("DB_HOST")
DB_PORT=env.str("DB_PORT")
DB_DATABASE=env.str("DB_DATABASE")
DB_USERNAME=env.str("DB_USERNAME")
DB_PASSWORD=env.str("DB_PASSWORD")
