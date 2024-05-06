from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
import asyncio

async def get_screenshot():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False, slow_mo=50)
        page = await browser.new_page()
        await page.goto('https://torgi.gov.ru')
        await page.screenshot(path='torgi.gov.ru2.png', full_page=True)
        await browser.close()
        
asyncio.run(get_screenshot())
        
