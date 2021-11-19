from typing import List

def shell_sort(numbers: List[int])->List:
    len_numbers = len(numbers)
    gap = len_numbers // 2

    while gap > 0 :
        for cnt_i in range(gap,len_numbers):
            temp = numbers[cnt_i]
            j= cnt_i
            while j >= gap and numbers[j-gap] > temp:
                numbers[j] = numbers[j-gap]
                j -= gap
            numbers[j] = temp

        gap  = gap //2
    return numbers

if __name__ == '__main__':
    nums = [5,6,9,2,3]
    print(shell_sort(nums))

