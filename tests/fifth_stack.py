from main import FifthStackLanguage


def test_command_sequence():
    interpreter = FifthStackLanguage()

    assert interpreter.execute("PUSH 5") == "stack is [5]"
    assert interpreter.execute("PUSH 3") == "stack is [5, 3]"
    assert interpreter.execute("+") == "stack is [8]"
    assert interpreter.execute("DUP") == "stack is [8, 8]"
    assert interpreter.execute("PUSH 2") == "stack is [8, 8, 2]"
    assert interpreter.execute("*") == "stack is [8, 16]"
    assert interpreter.execute("SWAP") == "stack is [16, 8]"
    assert interpreter.execute("/") == "stack is [2]"
    assert interpreter.execute("POP") == "stack is []"
    assert interpreter.execute("POP") == "ERROR"
    assert interpreter.execute("PUSH 10") == "stack is [10]"
    assert interpreter.execute("PUSH 0") == "stack is [10, 0]"
    assert interpreter.execute("/") == "ERROR"
