from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

minutes=[1,2,3,4,5,6,7,8,9]

lables=['player1','player2','player3']


player1=[1,2,3,3,4,4,4,4,5]
player2=[1,1,1,1,2,2,2,3,4]
player3=[1,1,1,2,2,2,3,3,3]

plt.stackplot(minutes,player1,player2,player3,labels=lables)


plt.legend(loc='lower left')
# plt.legend(loc='upper left')
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")
plt.show()