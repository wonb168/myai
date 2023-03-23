const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  // 登录Microsoft账户
  await page.goto('https://login.microsoftonline.com/');
  await page.fill('#i0116', '37640893@qq.com'); // 输入你的电子邮件地址
  await page.click('#idSIButton9'); // 点击下一步
  await page.fill('#i0118', 'wonb131421'); // 输入你的密码
  await page.click('#idSIButton9'); // 点击登录

  // 访问Bing聊天页面
  await page.goto('https://www.bing.com/chat');

  // 提出一个问题
  await page.fill('#chatInput', 'new bing使用的gpt哪个版本？'); // 输入你要问的问题
  await page.click('#id_send'); // 点击发送按钮

  // 等待聊天回复
  await page.waitForSelector('#chatDisplay .message:last-child .message-body');

  // 获取聊天回复
  const reply = await page.$eval('#chatDisplay .message:last-child .message-body', el => el.textContent);
  console.log(`回复：${reply}`);

  await browser.close();
})();