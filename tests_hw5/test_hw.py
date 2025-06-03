from selene import browser


def test_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Natasha').press_tab()
    browser.element('#lastName').type('Sidorova').press_tab()
    browser.element('#userEmail').type('natasha771@mail.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('+79652014545')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1977"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="3"]').click()
    browser.element('[aria-label="Choose Sunday, April 3rd, 1977"]').click()
    browser.element('#subjectsInput').type('Kuku').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()

