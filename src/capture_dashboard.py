import asyncio
from pyppeteer import launch
import os

SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

async def capture_dashboard():
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()

    # Go to your local Streamlit dashboard
    await page.goto('http://localhost:8501', {'waitUntil': 'networkidle2'})

    # Full dashboard screenshot
    await page.screenshot({'path': os.path.join(SCREENSHOT_DIR, 'dashboard_full.png'), 'fullPage': True})

    # You can also capture specific sections by selector if needed
    # Example: Capture only charts
    charts = await page.querySelectorAll('div.stPlotlyChart')
    for i, chart in enumerate(charts, start=1):
        await chart.screenshot({'path': os.path.join(SCREENSHOT_DIR, f'chart_{i}.png')})

    await browser.close()
    print(f"✅ Screenshots saved in '{SCREENSHOT_DIR}'")

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(capture_dashboard())
