from collections import Counter
x = int(input())
y = Counter(map(int, input().split()))
z = int(input())

total = 0
for i in range(z):
    size, rate = map(int, input().split())
    if y[size]: 
        y[size] -= 1
        total += rate
print(total)

# Step 1: First we imported the counter from collections.
# Step 2: then we have taken the input of x i.e, the total number of shoes.
# Step 3: and we have taken the input of y i.e, the list of all shoe sizes. Then we used counter to arrange our list as a dictionary.
# Step 4: we’ve also taken the input of z i.e, the total number of customers.
# Step 5: then we created a variable to store the total.
# Step 6: then we created a for loop in the range of z(total number of customers)
# Step 7: inside for loop, we have taken the input of size and rate from each customer. Then we used an if condition to verify the input size is in y.
# Step 8: then we added all the rates in our total and printed it.