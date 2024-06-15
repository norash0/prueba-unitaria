import pytest
from main import sum,rest,mult,div

@pytest.mark.parametrize(
    "input_x, input_y, esperado",
    [
        (-1, 5, 4),
        (-2, 5, 3),
        (5, sum(-9, -1), -5),
        (sum(-1, -4), -4, -9)
    ]
)

def test_sum(input_x, input_y, esperado):
    assert sum(input_x, input_y) == esperado

@pytest.mark.parametrize(
    "input_x, input_y, esperado",
    [
        (-1, 5, -6),
        (-2, 5, -7),
        (5, sum(-9, -1), 15),
        (sum(-1, -4), -4, -1)
    ]
)
def test_rest(input_x, input_y, esperado):
    assert rest(input_x, input_y) == esperado
    
@pytest.mark.parametrize(
    "input_x, input_y, esperado",
    [
        (-1, 5, -5),
        (-2, 5, -10),
        (5, sum(-9, -1), -50),
        (sum(-1, -4), -4, 20)
    ]
)
def test_mult(input_x, input_y, esperado):
    assert mult(input_x, input_y) == esperado
    
@pytest.mark.parametrize(
    "input_x, input_y, esperado",
    [
        (-1, 5, -0.2),
        (-2, 5, -0.4),
        (5, sum(-9, -1), -0.5),
        (-4, 0, None)
    ]
)
def test_div(input_x, input_y, esperado):
    assert div(input_x, input_y) == esperado