import allure
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selene.support import by
from selene.support.conditions import be


@allure.step("Открываем гитхаб")
def open_github():
    browser.open("https://github.com/")


@allure.step("Ищем репо {repo}")
def search_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()


@allure.step("Переходим в репо {repo}")
def go_to_repo(repo):
    s(by.link_text(repo)).click()


@allure.step("Переходим в раздел Issues")
def open_issues():
    s("#issues-tab").click()


@allure.step("Проверяем issue с номером {number}")
def find_issue(number):
    s(by.partial_text(number)).should(be.visible)
