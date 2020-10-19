def consumer():
    print("Consumer Start")
    i = 0
    for i in range(10):
        print(f"Iteration: {i}")
        n = yield i
        print(f"n = {n}")
        i += 1

c = consumer()
print(c.send(None))
print(c.send("shark"))
print("--------------")
for i in c:
    print(i)