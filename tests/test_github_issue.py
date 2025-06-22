from selene import browser, be, by


def test_github_issue():
    browser.open("https://github.com/")
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").type("qaguru_autotest_lesson_5").press_enter()
    browser.element("[href='/IExpLouDI/qaguru_autotest_lesson_5']").click()
    browser.element("[href='/IExpLouDI/qaguru_autotest_lesson_5/issues']").click()

    browser.element("//a[text()='Issue for allure test']").should(be.visible)
