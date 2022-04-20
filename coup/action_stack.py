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
        - peek:
            if the stack isn't empty, returns the top action on the stack
            without removing it from the stack, otherwise returns None.
        - is_empty:
            check if the stack is empty
        - resolve:
            pop actions from the stack one at a time, if the action's
            action_succeeds field is set to true, resolve the action.
        - print_state:
            iterate through the actions in the action stack, invoking their
            print_state methods.
"""


class ActionStack:
    def __init__(self):
        self.actions = []

    def push(self, action):
        self.actions.append(action)

    def pop(self):
        if not self.is_empty():
            return self.actions.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.actions[-1]
        return None

    def is_empty(self):
        return len(self.actions) == 0

    def resolve(self, gamestate):
        while not self.is_empty():
            action = self.pop()
            if action.succeeds:
                action.resolve(gamestate)

    def print_state(self):
        for action in self.actions:
            print(action)
