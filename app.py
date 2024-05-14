from flask import Flask, send_file

import asyncio

from pyppeteer import launch

 

app = Flask(__name__)

 

async def generate_pdf(url, output_file):

    browser = await launch()

    page = await browser.newPage()

    await page.goto(url)

    await page.pdf({'path': output_file, 'format': 'A4'})

    await browser.close()

 

@app.route('/generate_pdf')

def generate_pdf_endpoint():

    # URL to convert to PDF

    url = 'https://diot-siaci-analytics.com/rapportFictif/alerting_sismique/'

    # Output file path

    output_file = 'kk.pdf'

   

    asyncio.run(generate_pdf(url, output_file))

   

    # Return the PDF file as a response

    return send_file(output_file, as_attachment=True)

 

if __name__ == '__main__':

    app.run(debug=True)