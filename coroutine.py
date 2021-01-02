import asyncio
import time

# # Using generator
# def consumer():
#     print("Consumer Start")
#     i = 0
#     for i in range(10):
#         print(f"Iteration: {i}")
#         n = yield i
#         print(f"n = {n}")
#         i += 1

# c = consumer()
# print(c.send(None))
# print(c.send("shark"))
# print("--------------")
# for i in c:
#     print(i)


# Using Coroutines
async def say_after(delay, what):
    for j in range(5):
        for i in range(4):
            print(what, end=" ")
        print()
        await asyncio.sleep(delay)



async def main():

    print(f"started at {time.strftime('%X')}")

    await asyncio.gather(
        say_after(3, 'hello'),
        say_after(2, 'world'),
    )

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
