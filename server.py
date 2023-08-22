from autometrics import autometrics
from quart import Quart

app = Quart(__name__)


@autometrics
@app.route("/")
async def hello():
    return "Hello world!"


if __name__ == "__main__":
    app.run()
