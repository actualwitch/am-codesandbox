from autometrics import autometrics
from prometheus_client import generate_latest
from quart import Quart

app = Quart(__name__)


@autometrics
@app.route("/")
async def hello():
    return "Hello world!"


@app.route("/metrics")
async def metrics():
    return generate_latest()


if __name__ == "__main__":
    app.run()
