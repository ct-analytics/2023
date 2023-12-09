import re

f = "day 1/day1.txt"

calibration_values = []
digits = {'one':'1',
          'two':'2',
          'three':'3',
          'four':'4',
          'five':'5',
          'six':'6',
          'seven':'7',
          'eight':'8',
          'nine':'9'}
search_pattern = re.compile(r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))')

with open(f,'r') as document:
    for i, l in enumerate(document):
        # print(f"{i}: {l}")
        numbers = search_pattern.findall(l)
        # print(numbers)
        for n in range(len(numbers)):
            if numbers[n] in digits.keys():
                numbers[n] = digits[numbers[n]]

        # print(f"{i}: {numbers}")
        calibration_values.append(int(numbers[0]+numbers[-1]))
        

# print(calibration_values)
print(f"Calibration Value: {sum(calibration_values)}")