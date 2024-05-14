import asyncio
import pathlib
from pwhtmltopdf import HtmlToPdf


async def this_from_url():
    async with HtmlToPdf() as htp:
        await htp.from_url("https://diot-siaci-analytics.com/rapportFictif/alerting_sismique/", "from_url.pdf")


async def this_from_file():
    async with HtmlToPdf() as htp:
        # Make sure the current directory has a test.html file
        await htp.from_file("test.html", "from_file.pdf")


async def this_from_string():
    async with HtmlToPdf() as htp:
        content = pathlib.Path("test.html").read_text()
        await htp.from_string(content, "from_string.pdf")


if __name__ == '__main__':
    asyncio.run(this_from_url())