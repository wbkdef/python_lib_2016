
import decorators

@decorators.pre_process_inputs(int, str, dict(a=1, b=2))
def bla(a, b, c):
    return [a, b, c]

def test_pre_process_inputs():
    assert bla(5.4, 7, 'b') == [5, '7', 2]
