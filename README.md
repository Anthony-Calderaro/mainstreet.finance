## Mainstreet

[Mainstreet](mainstreet.finance) is a suite of open source financial tools for financial analysis.

# Mission

To increase the transparency and availability of freely available, public financial data for investors and researchers. Our platform and our services are explicitly anti-speculative and biased towards the [value investing](https://en.wikipedia.org/wiki/Value_investing) ideology popularized by Benjamin Graham and David Dodd and continuously proven by their disciples at [Berkshire Hathaway](https://en.wikipedia.org/wiki/Berkshire_Hathaway). We reject the notion that successful investing occurrs by anything other than thorough financial analysis and emotional discipline, although we submit that for many years thorough insights into markets has been disproportionally unavailable to _main street_ investors due to the sheet volume of information that exists.

# Tools

1. [Mainstreet.Finance](Mainstreet.Finance) (Nextjs, MDX, react charts) serves as a home page for the application
2. ERICA (Electronically Retreive Indexed Corporate Analytics) a REST API which allows you to query data sourced from [EDGAR](https://www.sec.gov/edgar.shtml)
3. KQ: Our bot which automatically retreives, computes, and uploads new annual (10-K) and quarterly (10-Q) filings from public companies.

# Infrastructure:

Each Stock is a document in Lambda with all historical data (Massive dataset) and EDGAR reference numbers, cik numbers
Each stock's data is then summarized and piped into a relational table for each PTC (~4k) Run this on Supabase?

# Sitemap

`/`: landing page
`/security/search?name=''&cik=''}`: Search by name or cik
`/security/id`: data for a specific security pulled from Dynamodb

<!-- # Roadmap
free Brokerage
educational tool (stock simulation)
Educational resources: Financial Accounting like stripe docs
The real costs: Risk, Fees, Inflation, Principle, Opportunity

Bonds
Forex
-->

<!-- # Later do Our goal is to develop tools which enable every person to have identical access to the most granular level information about companies, industries, and markets. This requires a number of features:
1. Our tools must be as affordable as possible, and we therefore rely heavily on open source technologies.
2. To ensure that no individual or entity abuses the technological advances of these tools, all of our software will be open source as well.
3. To actively pursue our charitable cause, we will make intentional decisions which make it difficult for people who wish to use our tools for speculation or frequent trading -- which we define as buying and selling a security within a time frame such that they must pay ordinary rather than capital gains tax. This means we will not have live charts, quotes, or real-time data other than what is made at the moment a request is made.
4. Evangelize and teach financial education. As the single most important factor in any learning endeavor is attention, we are therefore mission-bound to be anti-sponsorship, anti-advertisement, and anti-promotional. We do not collect user data, we do not sell query data, we do not provide advertising or business oppoprtunities for sponsorship.
5. How we make money: We provide hosted solutions of all our open source tools, which can be accessed at a free tier and a premium tier. As our code is open source, we allow users to configure their own setups -->

## scraping.js (1010 Bot)

1010 is our bot which retrieves, scrubs, and processes new 10-Q and 10-Q filings as they are released. This process involves:

1. Pulling the latest data from the SEC's EDGAR filings
2. Scrubbing the data and formatting it for upload
3. Pushing the data to our various databases
4. Uploading the raw data for users to [export]()

# Software Packages

1. Puppeteer for searching EDGAR and pull the data
2. Python in [Jupytr Notebooks]() for data science and API communication

The puppeteer logic is held in `scraping.js` and is currently run manually as data is updated on the SEC's webpage

# Todo:

1. Automatically determine when new data is available from EDGAR
2. Automatically run scraping.js in response to data updates
