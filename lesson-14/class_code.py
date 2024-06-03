# 1 1 2 3 5 8
import time

def fibonacci(n, computed=None):
    if computed is None:
        computed = dict()

    if n == 1 or n == 2:
        return 1

    if(n - 1 in computed):
        n_1 = computed[n-1]
    else:
        n_1 = fibonacci(n-1, computed=computed)
        computed[n-1] = n_1

    if(n - 2 in computed):
        n_2 = computed[n-2]
    else:
        n_2 = fibonacci(n-2, computed=computed)
        computed[n-2] = n_2

    return n_1 + n_2


def fibonacci_2(n):
    if n == 1 or n == 2:
        return 1
    last_1 = 1
    last_2 = 1
    for i in range(2, n):
        tmp = last_1 + last_2
        last_2 = last_1
        last_1 = tmp

    return last_1


assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(10) == 55

assert fibonacci_2(1) == 1
assert fibonacci_2(2) == 1
assert fibonacci_2(3) == 2
assert fibonacci_2(10) == 55


time_1 = time.time()
fibonacci(900)
print(time.time() - time_1)

time_1 = time.time()
fibonacci_2(900)
print(time.time() - time_1)


print("fibonacci - ok")



def foo(n):
    store = [0]*(n+1)
    store[0], store[1] = 1, 1
    for i in range (2, n + 1):
        store[i] = store[i - 1] + store[i - 2]

    return store[n]


assert foo(1) == 1
assert foo(2) == 2
assert foo(3) == 3
assert foo(9) == 55


print("stairs foo - ok")

# [2,3,1,1,4] - True
# [2,3,1,1,0,4] - False

def jump(nums):
    max_jump = 0  #
    for i in range(len(nums)):
        # i = 0; max_jump = 0
        # i = 1; max_jump = 2
        # i = 2; max_jump = 4
        # i = 3; max_jump = 4
        # i = 4; max_jump = 4
        if i > max_jump:
            return False

        # i = 0; max_jump = 2
        # i = 1; max_jump = 4
        # i = 2; max_jump = 4
        # i = 3; max_jump = 4
        # i = 4; max_jump = 8
        max_jump = max(max_jump, i + nums[i])

        # i = 0; not work
        # i = 1; not work
        # i = 2; not work
        # i = 3; not work
        # i = 4; work
        if max_jump >= len(nums) - 1:
            return True

    return False


assert jump([2,3,1,1,4])
assert jump([2,3,1,1,0])
assert not jump([2,3,1,1,0,4])

print("jumps - ok")



# [1, 2, 1, 3, 1] == 1
# [1, 1, 2] == 1
# [2,3,4,1,1,1,1,1]

def task_4(nums):
    d = dict()

    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    max_num = max(d.items(), key=lambda t: t[1])[0]  # (1, 3)

    return max_num

def task_4_2(nums):
    current_count = 0
    current_num = None

    for num in nums:
        if current_count == 0:
            current_num = num

        if num == current_num:
            current_count += 1
        else:
            current_count -= 1

    return current_num



assert task_4([1, 2, 1, 3, 1]) == 1
assert task_4([1, 1, 3]) == 1




# [1,8,6,2,5,4,8,3,7] == 49

def max_s(columns):
    left = 0
    right = len(columns) - 1
    max_s = 0

    while left != right:
        a = right - left
        b = min(columns[left], columns[right])

        max_s = max(max_s, a * b)

        if columns[left] < columns[right]:
            left += 1
        else:
            right -= 1


    return max_s


assert max_s([1,8,6,2,5,4,8,3,7]) == 49


# [1, 2, 10, 3] - [60, 30, 6, 20]
# [1, 2, 10, 3, 0] - [0, 0, 0, 0, 60]
# [0, 2, 10, 3, 0] - [0, 0, 0, 0, 0]

def mult(nums):
    temp_mult = 1
    result = [0] * len(nums)
    for i in range(len(nums)):
        result[i] = temp_mult
        temp_mult *= nums[i]

    temp_mult = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= temp_mult
        temp_mult *= nums[i]

    return result



assert mult([1, 2, 10, 3]) == [60, 30, 6, 20]
assert mult([1, 2, 10, 3, 0]) == [0, 0, 0, 0, 60]
assert mult([1, 0, 10, 3, 0]) == [0, 0, 0, 0, 0]










