from autometrics import autometrics
from prometheus_client import generate_latest

from . import app


# Let's start by adding a simple route that returns a string
# and instrument it with autometrics
@app.route("/")
@autometrics
async def hello():
    return "Hello world!"


# We will also add a metrics endpoint that returns the Prometheus metrics
@app.route("/metrics")
async def metrics():
    return generate_latest()


# Server will start automatically in CodeSandbox, you will find it a browser tab on the side
# In another tab title Autometrics you can find the Explorer, click the "Start Exploring" button
# and expand the metrics for the `01-start` module. You will find some basic metrics
# for the `hello` handler including request rate, latency, and error rate.

# Now let's do something more interesting. Open the `02-error.py` file and follow the instructions there.
