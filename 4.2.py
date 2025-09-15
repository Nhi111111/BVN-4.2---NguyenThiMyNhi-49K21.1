def mahoa(text, k):
    k = k % 26
    ctext = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')
            ctext += chr((ord(ch) - base + k) % 26 + base)
        else:
            ctext += ch
    return ctext

# chạy thử
p = "NguyenThiMyNhi"
k = 40
c = mahoa(p, k)
print("Ban ro:", p)
print("Ban ma:", c)

