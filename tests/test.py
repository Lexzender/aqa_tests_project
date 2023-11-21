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


def test_open_card_hootel():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("https://russpass.ru")

    browser.element(".OnboardingModal_onboarding-window__content__aId7h").should(be.visible)
    browser.element(".OnboardingModal_onboarding-window__content__aId7h .button").click()

    browser.element("[placeholder='Поиск']").type("Москва")
    browser.element("//span[normalize-space(.)='Жилье']").click()
    browser.element("//button[normalize-space(.)='Найти']").click()
    browser.element(".catalogNota_items__5aFjU .catalogNota_item__mvFJo").click()
    browser.switch_to_next_tab()
    browser.element(".hotel-details__container").should(be.visible)

    browser.quit()

def test_fill_support_form():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("https://russpass.ru")
    browser.element("//div[contains(concat(' ',@class,' '),'headerButtonNota_title__8UJQM') and normalize-space(.)='Меню']").click()
    browser.element("//div[normalize-space(.)='Поддержка']").click()
    browser.element(".contacting-support").should(be.visible)
    browser.element(".contacting-support").perform(command.js.scroll_into_view)
    browser.element(".select-input").click()
    browser.all(".select-input__option").element_by(have.exact_text("Жалоба / Претензия")).click()
    browser.element("#email").type("test@mail.ru")
    browser.element("#name").type("testName")
    browser.element("#details").type("тестовая жалоба")
    browser.element("#contact_us").should(be.visible)

    browser.quit()



def test_check_bonus_display():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("https://russpass.ru/loyalty")
    browser.element(".bonuses__header-headline").should(be.visible).should(
        have.text("Путешествуйте с удовольствием и получайте за это подарки"))
    browser.element(".bonuses__header-caption").should(be.visible).should(
        have.text("Копите бонусы и обменивайте их на подарки из нашего каталога"))
    browser.element(".bonuses__section-header h2").should(be.visible).should(have.text("Как накопить бонусы"))
    browser.element('//div[@class="bonuses__grid-item"][1]').perform(command.js.scroll_into_view)
    browser.element('//div[@class="bonuses__grid-item"][1]').should(be.visible).should(
        have.text("Регистрируйтесь на сайте")).should(
        have.text("Храните в Профиле все покупки и скидки, добавляйте объекты в Избранное и стройте маршруты"))
    browser.element('//div[@class="bonuses__grid-item"][2]').should(be.visible).should(
        have.text("Бронируйте отели, покупайте билеты")).should(
        have.text("Планируйте путешествие и получайте бонусы за покупки"))
    browser.element('//div[@class="bonuses__grid-item"][3]').should(be.visible).should(
        have.text("Покупайте рекомендованные предложения")).should(
        have.text("Ищите карточки со специальным значком RUSSPASS и получайте повышенные бонусы"))
    browser.element('//div[@class="bonuses__grid-item"][4]').should(be.visible).should(
        have.text("Подписывайтесь на рассылку")).should(have.text("Получайте дополнительные бонусы за подписку"))
    browser.element('//div[@class="bonuses__grid-item"][5]').should(be.visible).should(
        have.text("Оценивайте отели, места и события")).should(
        have.text("Делитесь вашими впечатлениями и получайте бонусы"))

    browser.quit()

def test_activation_eng_ver():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("https://russpass.ru")

    browser.element(".OnboardingModal_onboarding-window__content__aId7h").should(be.visible)
    browser.element(".OnboardingModal_onboarding-window__content__aId7h .button").click()

    browser.element(".localSwitcher_wrapper__VC_5Q").click()
    browser.element("//div[normalize-space(.)='English']").click()
    browser.element("//div[normalize-space(.)='USD']").click()
    browser.element("//button[normalize-space(.)='Сохранить']").click()

    browser.element(".MainSearch_title__yuGrp").should(have.text("Plan Perfect Trip With")).should(
        have.text("RUSSPASS"))

    browser.quit()
