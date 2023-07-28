import allure
from decorators import open_github, search_repository, go_to_repo, open_issues, find_issue
from allure_commons.types import Severity


@allure.label("owner", "r.shelestov")
@allure.story("Шаги с декоратором @allure.step")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
def test_decorators():
    open_github()
    search_repository("eroshenkoam/allure-example")
    go_to_repo("eroshenkoam/allure-example")
    open_issues()
    find_issue("65")
