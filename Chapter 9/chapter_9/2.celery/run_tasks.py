
from tasks import add

for _ in range(100):
    result = add.delay(4, 4)
    print (result.get(timeout=5))
