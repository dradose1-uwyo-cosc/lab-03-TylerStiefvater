# Tyler Stiefvater
## [Assignment 3]
## [Submission date: 09/25/24]
## Worked with/sources 
## Project Quirks/ Things that don't work
states=['Wyoming','Colorado','Montana']
print(states)
print(states[0])
print(states[-1])
print(f"{states[1].upper()} is south of {states[0].upper()}")

states.append('Washington')
states.append('Oregon')
states.append('California')
print(states)
states[-2]="Maine"
print(states)
states[2]="Texas"
print(states)
del states[3]
print(states)
states.remove("Texas")
print(states)

print(sorted(states))
print(states)
states.sort(reverse=True)
print(states)
states.reverse()
print(states)