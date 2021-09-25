from app import change, make_change
from click.testing import CliRunner


def test_change():
    assert [{5: "quarters"}, {1: "nickels"}, {4: "pennies"}] == change(1.34)


def test_app():
    runner = CliRunner()
    result = runner.invoke(make_change, ["--amount", "1.34"])
    assert result.exit_code == 0
    assert "quarters: 5" in result.output
