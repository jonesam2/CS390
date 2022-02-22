import random

heads = 0
tails = 0

choose = input("Hey! Heads or Tails? ")

inputt = int(input("Please enter the number of times you would like to flip a coin. "))

expected = int(inputt * 0.5)  #50/50 chance of it landing on heads


for num in range (1,inputt+1):
    result = random.randint(1,2)
    if result == 1:
        heads += 1
    if result == 2:
        tails += 1
    if inputt > 1000000 and num % 100 == 0:
        print("Still loading. Number of", choose, "at this time is:", heads)



if choose.lower() == "heads":
    print("Heads:", heads, "Tails:", tails)
    print("Our expected result for heads is:", expected, "out of", inputt)
    print("Our actual result was:", heads, "out of", inputt)
    print("The difference between the expected result and actual result is:", abs(heads - expected))

if choose.lower() == "tails":
    print("Heads:", heads, "Tails:", tails)
    print("Our expected result for tails is:", expected, "out of", inputt)
    print("Our actual result was:", tails, "out of", inputt)
    print("The difference between the expected result and actual result is:", abs(tails - expected))