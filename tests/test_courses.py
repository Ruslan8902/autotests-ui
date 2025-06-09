import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()

    courses_empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_empty_icon).to_be_visible()

    courses_empty_title = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_empty_title).to_be_visible()

    courses_empty_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_empty_text).to_be_visible()