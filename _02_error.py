import asyncio
import random

from autometrics import autometrics
from quart import Blueprint

_02_error = Blueprint("_02_error", __name__)

# Let's add a route that will call another function that is unstable and introduces
# errors and jitter. We will also instrument both functions with autometrics.


@autometrics
async def unstable_function():
    await asyncio.sleep(random.random() * 2)
    if random.random() < 1:
        raise Exception("Something went wrong!")
    return "The answer is 42!"


# Now let's add a route that calls the unstable function and returns the result.


@_02_error.route("/error")
@autometrics
async def error():
    return await unstable_function()
