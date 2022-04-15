"""
Action Stack Class

    Fields:
        - actions: list of actions
    
    Methods:
        - __init__:
            initialize the action stack
        - push:
            push an action to the stack
        - pop:
            pop an action from the stack
        - is_empty:
            check if the stack is empty
        - resolve:
            pop actions from the stack one at a time, if the action's
            action_succeeds field is set to true, resolve the action.
        - print_state:
            iterate through the actions in the action stack, printing each of
            them.
"""
