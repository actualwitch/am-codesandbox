from autometrics import autometrics
from autometrics.objectives import Objective, ObjectiveLatency, ObjectivePercentile
from quart import Blueprint
from _02_error import get_answer, format_string, unstable_function

_03_slo = Blueprint("_03_slo", __name__)


# Now that we have some visibility into how our application is performing,
# let's build on that by adding some Service Level Objectives (SLOs).
# These are metrics that are used to define the reliability of the service.

# We will start by defining an objective that we want to track.

my_objective = Objective(
    name="my_objective",
    latency=ObjectiveLatency.Ms100,
    percentile=ObjectivePercentile.P95,
)

# Now we'll apply that objective to our function using the `@autometrics` decorator.


@autometrics(objective=my_objective)
@_03_slo.route("/slo")
async def get_answer():
    answer = get_answer()
    await unstable_function()
    return format_string(answer)


# Now let's run the server and see what happens. Open the SLO tab in the Autometrics
# Explorer and check out our new metrics.
