from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis using hostname 'redis' (service name in docker-compose)
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route("/")
def counter():
    count = r.incr("hits")  # Increment 'hits' key by 1
    return f"<h1>Page visited {count} times!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
