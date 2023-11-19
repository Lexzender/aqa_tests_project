import time

from selene import browser,have,command,be


def test_search_hootel():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("https://russpass.ru")

    browser.element(".OnboardingModal_onboarding-window__content__aId7h").should(be.visible)
    browser.element(".OnboardingModal_onboarding-window__content__aId7h .button").click()

    browser.element("[placeholder='Поиск']").type("Москва")
    browser.element("//span[normalize-space(.)='Жилье']").click()
    browser.element("//button[normalize-space(.)='Найти']").click()
    browser.element(".filterButton_button__zL1VD").click()


    browser.element("//label[@for='children']/..//button[@class='counter__button'][2]").click()
    browser.element("//div[normalize-space(.)='Возраст ребенка']").click()
    browser.all("#children-options").element_by(have.exact_text("3 года")).click()
    browser.element("//button[normalize-space(.)='Найти']").click()
    result = browser.all("#catalogCardsId")
    for i in result:
        i.should(be.visible)


    browser.quit()


