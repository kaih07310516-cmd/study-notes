sh = input('enter hours:')
sr = input('enter rate:')
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("error")
    quit()
print(fh,fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * fh * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("pay:",xp)