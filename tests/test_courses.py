import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list():
    from playwright.sync_api import sync_playwright, expect

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        expect(registration_email_input).to_be_visible()
        registration_email_input.fill('"user.name@gmail.com"')

        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        expect(registration_username_input).to_be_visible()
        registration_username_input.fill('username')

        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        expect(registration_password_input).to_be_visible()
        registration_password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        expect(registration_button).to_be_visible()
        registration_button.click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()

        courses_empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_empty_icon).to_be_visible()

        courses_empty_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_empty_title).to_be_visible()

        courses_empty_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_empty_text).to_be_visible()