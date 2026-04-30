from pages.calculator_page import CalculatorPage


def test_slow_calculator(browser):
    calculator = CalculatorPage(browser)
    calculator.open()
    calculator.set_delay("45")
    calculator.click_button("7").click_button("+").click_button("8").click_button("=")
    result = calculator.get_result()
    assert result == "15"
