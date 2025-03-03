def coroutine_example(name):
    print("start coroutine...name:", name)
    x = yield name  # 调用next()时，产出yield右边的值后暂停；调用send()时，产出值赋给x，并往下运行
    print("send值:", x)


coro = coroutine_example("Zarten")
print("next的返回值:", next(coro))
print("send的返回值:", coro.send(6))
