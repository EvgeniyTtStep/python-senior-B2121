if 2 + 2 == 4:
    print("Test Ok 2 + 2 = 4")

try:
    assert 2 + 2 == 5, "error assert"
except AssertionError as e:
    print(e)

