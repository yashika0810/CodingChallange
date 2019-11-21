def count(arr, n): 
    count = 0 
    even = 0
    for i in range(0, n): 
        for j in range(i+1, n): 
          sum= arr[i] + arr[j]
          if sum%5==0: 
                count += 1   
                print("Pairs whose sum is divisible by 5",arr[i],arr[j]) 
          if sum%2==0:
                even +=1
                print("pair of even no" ,arr[i],arr[j])

    return count
    return even   
arr = [3,4,5,2,1,6] 
n = len(arr) 
print(count(arr, n)) 

  
