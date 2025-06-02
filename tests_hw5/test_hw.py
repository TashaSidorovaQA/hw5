from selene import browser


def test_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Natasha').press_tab()
    browser.element('#lastName').type('Sidorova').press_tab()
    browser.element('#userEmail').type('natasha771@mail.ru')
    browser.element('[data-value="Female"]').click
    browser.element('#userNumber').type('+79652014545')


