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
    if random.random() < 0.1:
        raise Exception("Something went wrong!")


@autometrics
def get_answer():
    answer = 20 + 22
    return answer


@autometrics
def format_string(answer):
    return f"The answer is {answer}!"


# Now let's add a route that calls the unstable function and returns the result.


@_02_error.route("/error")
@autometrics
async def error():
    answer = get_answer()
    await unstable_function()
    return format_string(answer)
