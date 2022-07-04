s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end)) # 5
print(s.find("q"))  # -1

ch = "o"
s = 'Some words'
print(s.rfind(ch))  # 6

s = 'Some words'
print(s.rindex(ch))  # 6