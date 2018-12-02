import re

with open('AOC2015_6.data', 'r') as f:
    data = f.read().split('\n')

# Part 1: how many lights are lit?
def on(up_corner,low_corner):
    global lights
    a,b = up_corner
    c,d = low_corner
    for i in range(a, c +1):
        for j in range(b,d+1):
            lights[i][j] = 1
            
def off(up_corner,low_corner):
    global lights
    a,b = up_corner
    c,d = low_corner
    for i in range(a, c +1):
        for j in range(b,d+1):
            lights[i][j] = 0

def toggle(up_corner,low_corner):
    global lights
    a,b = up_corner
    c,d = low_corner    
    for i in range(a, c +1):
        for j in range(b,d+1):
            lights[i][j] = 1 - lights[i][j]


lights = [[0 for i in range(1000)] for j in range(1000)]

ops = {'turn on':on, 'turn off':off, 'toggle':toggle}
for order in data:
    instruct, up_corner, low_corner = re.match(r'(\D+) (\d+,\d+)\D+(\d+,\d+)', order).groups()
    up_corner = [int(x) for x in up_corner.split(',')]
    low_corner = [int(x) for x in low_corner.split(',')]
    ops[instruct](up_corner, low_corner)

print('Part 1:', sum(sum(row) for row in lights)) 

# Part 2:   total brightness

def on_2(up_corner,low_corner):
    global lights
    a,b = up_corner
    c,d = low_corner
    for i in range(a, c +1):
        for j in range(b,d+1):
            lights[i][j] += 1
            
def off_2(up_corner,low_corner):
    global lights
    a,b = up_corner
    c,d = low_corner
    for i in range(a, c +1):
        for j in range(b,d+1):
            lights[i][j] = max(0, lights[i][j] - 1)
            

def toggle_2(up_corner,low_corner):
    global lights
    a,b = up_corner
    c,d = low_corner    
    for i in range(a, c +1):
        for j in range(b,d+1):
            lights[i][j] += 2

ops = {'turn on':on_2, 'turn off':off_2, 'toggle':toggle_2}
lights = [[0 for i in range(1000)] for j in range(1000)]
for order in data:
    instruct, up_corner, low_corner = re.match(r'(\D+) (\d+,\d+)\D+(\d+,\d+)', order).groups()
    up_corner = [int(x) for x in up_corner.split(',')]
    low_corner = [int(x) for x in low_corner.split(',')]
    ops[instruct](up_corner, low_corner)

print('Part 2:', sum(sum(row) for row in lights) )
