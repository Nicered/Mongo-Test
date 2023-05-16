from pymongo import MongoClient
import os
import dotenv

dotenv.load_dotenv(dotenv_path="./.env")

client = MongoClient(host=os.environ["MONGO_HOST"], port=int(os.environ["MONGO_PORT"]))