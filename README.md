# Actions

Declarative steps.

Actions allows you to define consecutive steps in a declarative manner.

Basic example:

    from actions import action, Action, Actions

    @action(label="Step 1")
    def step_1():
        print "This is step 1"

    @action(label="Step 2")
    def step_2():
        print "This is step 2"

    actions = Actions(
        Action(step_1),
        Action(step_2)
    )

    actions()

    # Outputs:
    ## This is step 1
    ## This is step 2

Each action must be decorated with @action. The label of a decorated action can
later be retrieved for better outputting.

## Passing arguments

    from actions import action, Action, Actions

    @action(label="Step")
    def step(n):
        print "This is step %s" % n

    actions = Actions(
        Action(step, 1),
        Action(step, 2)
    )

    actions()

    # Outputs:
    ## This is step 1
    ## This is step 2

## Passing state

    from actions import action, Action, Actions, State, StatefulAction

    @action(label="Pre-step")
    def pre_step(n, result_store):
        print "This is prestep %s"

        result_store.calculation = n * 10

    def step(calculation):
        print "Result from calculation: %s" % calculation

    actions = Actions(
        StatefulAction(pre_step, 1, state=["calculation"]),
        Action(step, State("calculation"))
    )

    actions()

    # Outputs:
    ## This is prestep 1
    ## Result from calculation: 10


## Enabling / disabling actions

    from actions import action, Action, Actions, State, StatefulAction

    @action(label="Step 1")
    def step_1():
        print "This is step 1"

    @action(label="Step 2")
    def step_2(result_store):
        print "This is step 2"
        result_store.enabled_step_3 = False

    @action(label="Step 3")
    def step_3():
        print "This is step 3"

    @action(label="Step 4")
    def step_4():
        print "This is step 4"

    actions = Actions(
        Action(step_1, enabled=False),
        StatefulAction(step_2, state=["enabled_step_3"]),
        Action(step_3, enabled=State("enabled_step_3")),
        Action(step_4)
    )

    actions()

    # Outputs:
    ## This is step 2
    ## This is step 4


## Failing actions

You can fail individual actions by returning False:

    from actions import action, Action, ActionFailed, Actions

    @action(label="Step 1")
    def step_1():
        print "This is step 1"
        return False

    @action(label="Step 2")
    def step_2():
        print "This is step 2"

    actions = Actions(
        Action(step_1),
        Action(step_2)
    )

    try:
        actions()

    except ActionFailed, action_failed:
        print "%s failed" % action_failed.label

    # Outputs:
    ## This is step 1
    ## Step 1 failed

Action can also fail if they throw exceptions:

    from actions import action, Action, ActionFailed, Actions

    @action(label="Step 1")
    def step_1():
        print "This is step 1"
        a[0] = True # Reference error

    @action(label="Step 2")
    def step_2():
        print "This is step 2"

    actions = Actions(
        Action(step_1),
        Action(step_2)
    )

    try:
        actions()

    except ActionFailed, action_failed:
        print "%s failed" % action_failed.label

    # Outputs:
    ## This is step 1
    ## Step 1 failed

## Cleaning up

    from actions import action, Action, ActionFailed, Actions

    @action(label="Step 1")
    def step_1():
        print "This is step 1"
        a[0] = True # Reference error

    @action(label="Cleanup")
    def cleanup():
        print "Cleaning up"

    actions = Actions(
        Action(step_1),
        Action(cleanup, _finally=True)
    )

    try:
        actions()

    except ActionFailed, action_failed:
        print "%s failed" % action_failed.label

    # Outputs:
    ## This is step 1
    ## Cleaning up
    ## Step 1 failed

When an exception occurs within an action, the exception is logged to the
actions package logger.

## Getting Started

To install, `cd` into the actions directory (where this README is located)
then run:

    $ pip install .

Actions requires Python version 2.7.

If you're not running in a VM or container, it's best to run inside of a
virtual environment (if you have virtualenv installed):

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install .
