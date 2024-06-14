from {{cookiecutter.package_name|lower}}.module import add


def test_add_returns_correct_sum():
    assert add(1, 2, 3) == 6
