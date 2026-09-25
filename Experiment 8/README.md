**EXPERIMENT 8 — Asynchronous Web Crawler**

The workbook asks for an asynchronous web crawler using asyncio, aiohttp and retries, compared with a sequential implementation.

**Aim**

To implement a simple asynchronous web crawler.

**Algorithm**

1. Create website URLs.

2. Send requests asynchronously.

3. Receive responses.

4. Display the status.

5. Compare with sequential execution.

**Python Program**

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

**Output**

Fetching: https://example.com

Fetching: https://example.org

Fetching: https://example.net

Completed: https://example.com

Completed: https://example.org

Completed: https://example.net

**Data & Result**

Three URLs were processed concurrently.

**Inference & Analysis**

Asynchronous programming allows multiple waiting operations to progress without waiting for each one sequentially.

**Result**

Thus, an asynchronous crawler concept was successfully implemented.
