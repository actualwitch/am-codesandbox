from quart import Quart
from autometrics import init

from _01_start import _01_start
from _02_error import _02_error

init(
    service_name="am-codesandbox",
    version="0.0.1",
    commit="123456",
    branch="main",
)
app = Quart(__name__)
app.register_blueprint(_01_start)
app.register_blueprint(_02_error)

if __name__ == "__main__":
    app.run()
