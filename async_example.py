import asyncio
import aiohttp

app_urls = ["http://www.youtube.com",
            "http://www.facebook.com",
            "http://www.baidu.com",
            "http://www.yahoo.com",
            "http://www.amazon.com",
            "http://en.wikipedia.org",
            "http://www.reddit.com",
            "http://www.google.com",
            "http://www.twitter.com",
            "http://www.live.com",
            "http://www.taobao.com",
            "http://www.bing.com",
            "http://www.instagram.com",
            "http://www.weibo.com",
            "http://www.sina.com.cn",
            "http://www.linkedin.com",
            "http://www.yahoo.co.jp",
            "http://www.msn.com",
            "http://www.vk.com",
            "http://www.imdb.com"]


async def get_url(session, app_url):
    s = time.perf_counter()
    print(f"{app_url} started!")
    async with session.get(app_url) as response:
        print(f"{app_url} got!")

        try:
            await response.text()
        except UnicodeDecodeError as identifier:
            print(f"{app_url} Error: {identifier}! Status: {response.status}, Charset: {response.charset}")
        
        print(f"{app_url} finished! Status: {response.status}, Charset: {response.charset}")
        elapsed = time.perf_counter() - s
        print(f"{app_url} executed in {elapsed:0.2f} seconds.\n")

async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[get_url(session, app_url) for app_url in app_urls])

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
