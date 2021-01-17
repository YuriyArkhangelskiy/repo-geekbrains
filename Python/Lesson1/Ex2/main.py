print("Enter time in seconds")
n = int(input())
print(n)
hours = n // 3600
seconds = n % 60
minutes = (n - hours * 3600 - seconds) // 60
print("Time is", "%02d:%02d:%02d" % (hours, minutes, seconds))
