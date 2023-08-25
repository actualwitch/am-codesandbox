from quart import Quart

from _01_start import _01_start
from _02_error import _02_error

app = Quart(__name__)
app.register_blueprint(_01_start)
app.register_blueprint(_02_error)

if __name__ == "__main__":
    app.run()
