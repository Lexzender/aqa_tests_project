import time

from selene import browser,have,command


def test_authorization_picaboo():
    browser.open("https://pikabu.ru/")

    browser.element('[placeholder="Логин"]').type("eltempo")
    browser.element('[placeholder="Пароль"]').type("HRX-a87-gca-iur")
    browser.element(".button_success").click()

    browser.element(".user__info-item .user__nick").should(have.text("eltempo"))




