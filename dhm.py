a=[i*2 for i in range(1,10)]
print(a)

b=[2,4,6,8,10]
gen_b=(i for i in b)
print(gen_b)
print(next(gen_b))
print(next(gen_b))
print(next(gen_b))
print(next(gen_b))
print(next(gen_b))

try:
    raise Exception
    print(next(gen_b))
    print(next(gen_b))
    print(next(gen_b))


except Exception:
    print("Я подбросил Exception")

except StopIteration:
    print("Я поймал StopIteration")
finally:
    print("я всё равно распечатаю свой текст")




c=[i*2 for i in range(1,10)]

def generator_function():
    for i in range(1,10):
        yield i * 5
        yield i * 10
        yield i*2
        if i >= 0:
            yield i*0

q=generator_function()
for item in q:
    print(item)



a=(i*0 for i in range(1,10) if i>=0)
print(a)

for i in a:
    print(i)









