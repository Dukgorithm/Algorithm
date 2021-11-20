# 12시 -> 24시 시간으로 변환

def timeConversion(s):
    time = int(s[:2])

    if s[-2:-1]=='P' and time%24<12:
        time += 12
    elif s[-2:-1]=='A' and time>=12:
        time %= 12
    return (str(time%24).rjust(2, '0')+s[2:-2])

print(timeConversion("07:05:45PM")) # 19:05:45
print(timeConversion("17:05:45AM")) # 17:05:45
print(timeConversion("17:05:45PM")) # 17:05:45
print(timeConversion("00:05:45PM")) # 12:05:45
print(timeConversion("24:05:45AM")) # 00:05:45
print(timeConversion("07:05:45PM")) # 19:05:45