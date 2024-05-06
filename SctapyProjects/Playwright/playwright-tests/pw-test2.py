from playwright.async_api import async_playwright, Browser, Page, ProxySettings
from playwright.sync_api import sync_playwright
import asyncio
import os

import playwright
# from .util import VZLJOT_PROXY

async def get_screenshot():
    async with async_playwright() as p:
        # if (os.environ.get('USERDOMAIN', 'NOT_VZLJOT') == 'VZLJOT'):
        #     ps: ProxySettings = {'server': 'http//proxy:3128', 'username': 'SibiryakovDO', 'password': 'vzlsoFia1302' }
        #     browser = await p.firefox.launch(headless=False, slow_mo=50, proxy=ps)
        # else:
        browser = await p.firefox.launch(headless=False, slow_mo=50)
            

        # browser.
        page = await browser.new_page()
        
        await page.goto('https://torgi.gov.ru')
        await page.screenshot(path='torgi.gov.ru4.png', full_page=True)
        await browser.close()
        
asyncio.run(get_screenshot())
        
