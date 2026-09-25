import asyncio

async def crawl(url):
    print("Fetching:", url)
    await asyncio.sleep(1)
    print("Completed:", url)

async def main():
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net"
    ]

    await asyncio.gather(*(crawl(url) for url in urls))

asyncio.run(main())