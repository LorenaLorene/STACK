from enum import Enum
from typing import List


class Command(Enum):
    PUSH = 'PUSH'
    POP = 'POP'
    DUP = 'DUP'
    SWAP = 'SWAP'


ARITHMETIC_COMMANDS = {'+', '-', '*', '/'}


class FifthStackLanguage:
    def __init__(self):
        self.stack: List[int] = []

    @staticmethod
    def command_valid(command: str) -> bool:
        parts = command.strip().split()
        if not parts:
            return False

        cmd = parts[0]
        if cmd not in Command._value2member_map_ and cmd not in ARITHMETIC_COMMANDS:
            return False

        if cmd == Command.PUSH.value:
            if len(parts) != 2:
                return False
            if not parts[1].lstrip('-').isdigit():
                return False

        elif cmd in Command._value2member_map_ or cmd in ARITHMETIC_COMMANDS:
            if len(parts) != 1:
                return False

        return True

    def apply_push(self, command: str):
        number = int(command.strip().split()[1])
        self.stack.append(number)
        return self.stack

    def apply_pop(self):
        if not self.stack:
            return "ERROR"
        self.stack.pop()
        return self.stack

    def apply_dup(self):
        if not self.stack:
            return "ERROR"
        self.stack.append(self.stack[-1])
        return self.stack

    def apply_swap(self):
        if len(self.stack) < 2:
            return "ERROR"
        self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        return self.stack

    def apply_arithmetic(self, operator: str):
        if len(self.stack) < 2:
            return "ERROR"
        b = self.stack.pop()
        a = self.stack.pop()

        if operator == "+":
            self.stack.append(a + b)
        elif operator == "-":
            self.stack.append(a - b)
        elif operator == "*":
            self.stack.append(a * b)
        elif operator == "/":
            if b == 0:
                return "ERROR"
            self.stack.append(a // b)
        else:
            return "ERROR"

        return self.stack

    def execute(self, command: str) -> str:
        if not command:
            return "ERROR"

        if not self.command_valid(command):
            return "ERROR"

        if command.startswith(Command.PUSH.value):
            result = self.apply_push(command)

        elif command == Command.POP.value:
            result = self.apply_pop()

        elif command == Command.DUP.value:
            result = self.apply_dup()

        elif command == Command.SWAP.value:
            result = self.apply_swap()

        elif command in ARITHMETIC_COMMANDS:
            result = self.apply_arithmetic(command)

        else:
            result = "ERROR"

        return f"stack is {result}" if result != "ERROR" else result
