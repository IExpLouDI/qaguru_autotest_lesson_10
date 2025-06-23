import allure
from allure_commons.types import Severity
from selene import browser, be


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "suchkovvs")
@allure.feature("Создание задачи в репозитории пользователем")
@allure.story("Создание задачи в репозитории")
@allure.link("https://github.com", name="Testing url")
def test_github_with_dynamic_labels():
    open_git("https://github.com/")
    select_button_and_type_repo("qaguru_autotest_lesson_5")
    select_repo("qaguru_autotest_lesson_5")
    open_repo_issue()
    should_issue_be_visible("Issue for allure test")


@allure.step("Открываем гит хаб")
def open_git(url:str):
    browser.open(url)

@allure.step("Открываем строку поиска и вносим название репозитория")
def select_button_and_type_repo(repo_name:str):
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").type(repo_name).press_enter()

@allure.step("Выбираем найденный репозиторий")
def select_repo(repo_name:str):
    browser.element(f"[href='/IExpLouDI/{repo_name}']").click()

@allure.step("Переходим в раздел issues")
def open_repo_issue():
    browser.element("[href='/IExpLouDI/qaguru_autotest_lesson_5/issues']").click()

@allure.step("Проверяем наличие issues с требуемым названием")
def should_issue_be_visible(some_text:str):
    browser.element(f"//a[text()='{some_text}']").should(be.visible)