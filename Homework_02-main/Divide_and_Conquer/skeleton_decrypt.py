
def reverse_karatsuba(data) -> tuple:
    if isinstance(data, tuple):
        return data
    else:
        var1= reverse_karatsuba(data[0])
        z1 = reverse_karatsuba(data[1])
        var3= reverse_karatsuba(data[2])

        x = (var3* 100)+((z1 - var3- var1) * 10)+var1
        y = (var3* 10)+((z1 -var3 - var1)// 10)+(var1 // 100)
        return x, y
    
'''def reverse_karatsuba(data):
    if isinstance(data, tuple):
        return data
    else:
        z0 = reverse_karatsuba(data[0])
        z1 = reverse_karatsuba(data[1])
        z2 = reverse_karatsuba(data[2])
        x = (z2 * 100) + ((z1 - z2 - z0) * 10) + z0
        y = (z2 * 10) + ((z1 - z2 - z0) // 10) + (z0 // 100)
        return x, y  '''


def main(filename) -> list[tuple[int, int]]:
    result = []
    with open(filename, 'r') as file:
        N = int(file.readline().strip())
        for _ in range(N):
            tree = eval(file.readline().strip())  
            result.append(reverse_karatsuba(tree))
    return result


def karatsuba(x,y):
    if x <10 or y <10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2
    high1, low1= split(x, n2)
    high2, low2= split(y, n2)
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1+ high1), (low2+high2))
    z2 = karatsuba(high1,high2)
    return (z2 *10**(2 * n2)) + ((z1 - z2 - z0) * 10**n2)+z0

def split(num, n):
    high = num // 10**n
    low =num % 10**n

    return high, low




# Test the functions with the sample input
#print(main("input.txt"))  # Replace "input.txt" with the actual filename