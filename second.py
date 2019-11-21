def count(arr, n, sum): 
    count = 0 
    for i in range(0, n): 
        for j in range(i+1, n): 
            if arr[i] + arr[j] == sum: 
                count += 1   
                print(arr[i],arr[j]) 
    return count   
arr = [3,4,5,2,1,6] 
n = len(arr) 
sum = 7
print("Count of pairs is", 
      count(arr, n, sum)) 

  