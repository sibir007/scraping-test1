from playwright.async_api import async_playwright, Browser, Page, ProxySettings
from playwright.sync_api import sync_playwright
import asyncio
import os
from datetime import datetime
import playwright

SCREENSHOT_DIR = 'screenshots/'
FIREFOX_SHORTKEY_FULL_URL = 'https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html'
FIREFOX_SHORTKEY_URL = 'https://support.mozilla.org/en-US/kb/keyboard-shortcuts-perform-firefox-tasks-quickly'
UBUNTY_SHORTKEY = 'https://help.ubuntu.com/community/KeyboardShortcuts'
# from .util import VZLJOT_PROXY

async def get_screenshot(url: str, fname: str):
    async with async_playwright() as p:
        # if (os.environ.get('USERDOMAIN', 'NOT_VZLJOT') == 'VZLJOT'):
        #     ps: ProxySettings = {'server': 'http//proxy:3128', 'username': 'SibiryakovDO', 'password': 'vzlsoFia1302' }
        #     browser = await p.firefox.launch(headless=False, slow_mo=50, proxy=ps)
        # else:
        browser = await p.firefox.launch(headless=False, slow_mo=50)
            

        # browser.
        page = await browser.new_page(viewport={"width": 980, "height": 1080})
        
        await page.goto(url)
        
        now = datetime.now()
        date_time = now.strftime("%d-%m-%y_%h.%m.%s")
        screenshot_file_name = f'{date_time}-{fname}.png'  
        await page.screenshot(path=f'{SCREENSHOT_DIR}{screenshot_file_name}', full_page=True)
        await browser.close()


if __name__ == '__main__':
            
    asyncio.run(get_screenshot(UBUNTY_SHORTKEY, "fierfox-sk"))
        
