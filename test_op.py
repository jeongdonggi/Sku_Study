from op import add, substract, multiply, devide

def test_add() -> None:
    alpha, beta = 1, 2
    result = multiply(alpha=alpha, beta=beta)
    assert alpha + beta == result, "Error: function 'add'"

def test_substract() -> None:
    alpha, beta = 1, 2
    result = multiply(alpha=alpha, beta=beta)
    assert alpha - beta == result, "Error: function 'substract'"

def test_mulityply() -> None:
    alpha, beta = 1, 2
    result = multiply(alpha=alpha, beta=beta)
    assert alpha * beta == result, "Error: function 'multiply'"

def test_devide() -> None:
    alpha, beta = 1, 2
    result = multiply(alpha=alpha, beta=beta)
    assert (alpha // beta, alpha % beta ) == result, "Error: function 'devide'"