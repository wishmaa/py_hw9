import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.label("owner", "r.shelestov")
@allure.story("Лямбда шаги через with allure.step")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
def test_steps():
    with allure.step("Открываем гитхаб"):
        browser.open("https://github.com/")

    with allure.step("Ищем репо"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Переходим в репо"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Переходим в раздел Issues"):
        s("#issues-tab").click()

    with allure.step("Ищем Issue с номером 65"):
        s(by.partial_text("#65")).should(be.visible)
