import allure
from selene import browser, be, by


def test_github_issue():
    browser.open("https://github.com/")
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").type("qaguru_autotest_lesson_5").press_enter()
    browser.element("[href='/IExpLouDI/qaguru_autotest_lesson_5']").click()
    browser.element("[href='/IExpLouDI/qaguru_autotest_lesson_5/issues']").click()

    browser.element("//a[text()='Issue for allure test']").should(be.visible)


def test_github_with_lambda_steps():
    with allure.step("Открываем гит хаб"):
        browser.open("https://github.com/")

    with allure.step("Открываем строку поиска и вносим название репозитория"):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").type("qaguru_autotest_lesson_5").press_enter()

    with allure.step("Выбираем найденный репозиторий"):
        browser.element("[href='/IExpLouDI/qaguru_autotest_lesson_5']").click()

    with allure.step("Переходим в раздел issues"):
        browser.element("[href='/IExpLouDI/qaguru_autotest_lesson_5/issues']").click()

    with allure.step("Проверяем наличие issues с требуемым названием"):
        browser.element("//a[text()='Issue for allure test']").should(be.visible)


def test_github_with_decorator_steps():
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
