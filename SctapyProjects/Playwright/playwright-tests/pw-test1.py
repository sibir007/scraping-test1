from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio


def sync_playwright_script():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://torgi.gov.ru")
        print(page.title())
        # page.locator()
        browser.close()
        
async def async_plfaywright_script():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://torgi.gov.ru")
        print(await page.title())
        await browser.close()
        
asyncio.run(async_plfaywright_script())
        