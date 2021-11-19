# 自力で バブルソートを実装する

from typing import List

def bubble_sort(numbers: List[int])->List[int]:
    len_numbers = len(numbers)

    for cnt_a in range(len_numbers):
        for cnt_b in range(len_numbers-1-cnt_a):
            if numbers[cnt_b] > numbers[cnt_b+1]:
                numbers[cnt_b] , numbers[cnt_b+1] = numbers[cnt_b+1],numbers[cnt_b]
    
    return numbers

if __name__ == '__main__':
    nums = [8,7,6,5,4,3]
    print(bubble_sort(nums))
