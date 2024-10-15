# Rebekah Beltran
# Oct 14, 2024
# this program keeps track of the total number of bottles collected for seven days,
# then calculates the total number of bottles returned for the week and the amount paid out.



keepGoing = 'y'
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0

while keepGoing == 'y':     
      # code to set value of variable totalBottles
      NBR_OF_DAYS = 7
      totalBottles = 0
      todayBottles = 0
      counter = 1
      while counter <= NBR_OF_DAYS:
          print('Enter number of bottles returned for day #' + str(counter) + ':')
          todayBottles = int(input())
          totalBottles = totalBottles + todayBottles
          counter += 1
      # code to set value of variable totalPayout
      PAYOUT_PER_BOTTLE = .10
      totalPayout = 0
      totalPayout = totalBottles * PAYOUT_PER_BOTTLE
      # code to print the number of total bottles and total payout
      print('total number of bottles collected ' + str(totalBottles))
      print(f'the total paid out is {totalPayout:.2f}')
      print('Do you want to enter another weeks worth of data?')
      print('Enter y or n')
      keepGoing=input()
      
