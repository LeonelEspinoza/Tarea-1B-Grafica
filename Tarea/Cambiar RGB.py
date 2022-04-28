def cambiarRGB(s):
    s[0]=round(s[0]/255,2)
    s[1]=round(s[1]/255,2)
    s[2]=round(s[2]/255,2)
    return s
print(cambiarRGB([247,119,35]))    
print(cambiarRGB([253,232,98]))
print(cambiarRGB([115,63,60]))
print(cambiarRGB([185,75,48]))
print(cambiarRGB([254,175,56]))
s=cambiarRGB([247,119,35])
print(type(s[0])==float)

