from calculator import Calc


class TestCalc:
    def test_add(self):
        assert 4 == Calc.add(2, 2)
        assert 10 == Calc.add(5, 5)

    def test_sub(self):
        assert 10 == Calc.sub(20, 10)
        assert 100 == Calc.sub(100, 0)

    def test_multi(self):
        assert 100 == Calc.multi(10, 10)
        assert 50 == Calc.multi(5, 10)
