from selene import browser, by, be
from allure_commons.types import Severity
import allure


@allure.label("owner", "r.shelestov")
@allure.story("Чистый Selene (без шагов)")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
def test_selene(browser_setup):
    browser.open("https://github.com/")

    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#65")).should(be.visible)
