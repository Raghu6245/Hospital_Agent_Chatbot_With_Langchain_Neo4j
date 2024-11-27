from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Now, access your environment variables
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

print("Neo4j URI:", NEO4J_URI)
print("Neo4j Username:", NEO4J_USERNAME)
