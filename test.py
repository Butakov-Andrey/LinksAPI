from datetime import datetime


d = datetime.now().time()
d_new = d.strftime("%H%M%S%f")[:-2]

print(d)
print(d_new)
