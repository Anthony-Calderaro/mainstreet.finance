const puppeteer = require('puppeteer');

const puppeteerOptions = {
  headless: false, // false to open an instance of Chrome so you can view what happens live
}

const gatherData = async () => {
  const browser = await puppeteer.launch(puppeteerOptions);
  const page = await browser.newPage();
  await page.goto('https://www.sec.gov/dera/data/financial-statement-and-notes-data-set.html');

  // Todo: Select the element to click, click it, download files, then run the analysis
  // const selector = 
  // await page.click(selector, clickOptions);


  // await browser.close();
};

// Execute
// gatherData();

