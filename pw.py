import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # 设置浏览器类型为 Chromium
        browser = await p.chromium.launch(headless=True)
        # 创建一个新的浏览器页面
        page = await browser.new_page()

        # 访问新版Bing网站
        await page.goto('https://www.bing.com/new')
        await page.screenshot(path='bing.png')
        # 点击登录按钮
        await page.click('a#id_l')

        # 等待登录框出现并输入账号和密码
        await page.wait_for_selector('input#i0116')
        await page.fill('input#i0116', '37640893@qq.com')
        await page.click('input#idSIButton9')
        await page.wait_for_selector('input#i0118')
        await page.fill('input#i0118', 'wonb131421')
        await page.screenshot(path='bing1.png')
        await page.click('input#idSIButton9')

        # 等待登录成功并点击聊天按钮
        await page.wait_for_selector('div#id_cht')
        await page.click('div#id_cht')

        # 等待聊天框出现并输入问题
        await page.wait_for_selector('input#id_q')
        await page.fill('input#id_q', 'What is the capital of France?')
        await page.keyboard.press('Enter')

        # 等待回答出现并输出
        await page.wait_for_selector('div#sw_next')
        answer = await page.inner_text('div#sw_next')
        print(f'The answer is: {answer}')

        # 关闭浏览器
        await browser.close()

asyncio.run(main())