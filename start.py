from quart import Quart
from autometrics import init

init(
    tracker="prometheus",
    enable_exemplars=True,
    service_name="am-codesandbox",
    version="0.0.1",
    commit="123456",
    branch="main",
)
app = Quart(__name__)

if __name__ == "__main__":
    import _01_start
    import _02_error

    app.run()
