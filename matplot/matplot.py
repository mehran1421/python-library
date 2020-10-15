from matplotlib import pyplot as plt

print(plt.style.available)
# انواع استایل دهی به نمودار ها
plt.style.use('fivethirtyeight')
plt.style.use('ggplot')
plt.xkcd()

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
# r=red ,b=blue and...
plt.plot(dev_x, dev_y, color='k',
         linestyle='--', marker='.', label="All Devs")

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(dev_x, py_dev_y, color='g', linewidth=3, marker='o', label="python")
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(dev_x, js_dev_y, color="#adad3b", linewidth=3, label="javascript")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")

# or create lable in function

# plt.legend(["All Devs","python"])
plt.legend()

plt.grid()
plt.savefig('plot.png')
plt.show()
