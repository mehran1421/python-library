from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

slices=[120,80,30,20]
labels=['sixty','forty','extral','extral2']
explode=[0,0,0.1,0]

#edgecolor=رنگ خط های جدا کننده
#explode=جدا کننده چند سانتی رنگ از بقیه رنگ ها
#shadow=حالت 3بعدی میدهد
#autopct=درصد هارا در نمودار نشان میدهد
plt.pie(slices,labels=labels,explode=explode,shadow=True,
        autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")
plt.show()