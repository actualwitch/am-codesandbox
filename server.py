from autometrics import autometrics
from quart import Quart, render_template

app = Quart(__name__)


@autometrics
@app.route("/")
async def hello():
    return await render_template("index.html")


if __name__ == "__main__":
    app.run()
