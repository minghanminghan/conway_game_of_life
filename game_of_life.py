#imports
import random

#rules
#Any live cell with fewer than two live neighbors dies
#Any live cell with two or three live neighbors lives on to the next generation
#Any live cell with more than three live neighbors dies
#Any dead cell with exactly three live neighbors becomes a live cell

class grid:
    def __init__(self, gridLength:int):
        self.length = gridLength
        self.grid = [[False for i in range(self.length)] for j in range(self.length)] #board all False by default
        self.alive = [] #ints holding positions of alive cells

    def populate_random(self):
        for y in range(self.length):
            for x in range(self.length):
                n = random.randint(0, 1)
                if n:
                    self.grid[y][x] = True
                    self.alive.append(self.length*y+x)            
    def populate(self, nums:list) -> None:
        for i in nums:
            y = i // self.length
            x = i % self.length
            #print(f'x: {x}, y: {y}, grid[x][y]: {self.grid[x][y]}')
            self.grid[y][x] = True
            self.alive.append(self.length*y+x)
    
    def get_value_of(self, index:int) -> int: #return true/false given index
        y = index // self.length
        x = index % self.length
        return self.grid[y][x]
    def set_value_of(self, index:int, value:bool) -> None:
        y = index // self.length
        x = index % self.length
        self.grid[y][x] = value
    def sorted_add(self, indexes:list, index:int) -> list:
        count = 0
        while count < len(indexes):
            if indexes[count] > index:
                break
            elif indexes[count] == index:
                return indexes
            count += 1
        indexes.insert(count, index) #python insert syntax covers empty case
        return indexes

    #new step function
    def step(self) -> None:
        #pop all self.alive into a stack
        next_alive = []
        next_dead = []

        temp = []
        while len(self.alive) != 0: #popping all of self.alive and adj cells into temp holder 
            cur_cell = self.alive.pop()
            temp = self.sorted_add(temp, cur_cell)
            for adj in self.get_adjacent_index(cur_cell):
                if adj not in temp:
                    temp = self.sorted_add(temp, adj)
        #print('temp:',temp)

        while len(temp) != 0: #splitting into alive and dead cells
            cur_cell = temp.pop()
            #if self.get_value_of(cur_cell): #cell currently alive
            #    cur_alive = self.sorted_add(cur_alive, cur_cell)
            #else: #cell currently dead
            #    cur_dead = self.sorted_add(cur_dead, cur_cell)
            if self.step_cell(cur_cell): #cell alive on next step
                next_alive = self.sorted_add(next_alive, cur_cell)
                continue
            next_dead = self.sorted_add(next_dead, cur_cell) #cell dead on next step

        for cur_cell in next_alive: #iterating through all of next_dead and next_alive
            self.set_value_of(cur_cell, True)
        for cur_cell in next_dead:
            self.set_value_of(cur_cell, False)
        self.alive = next_alive
        #print('next_dead:', next_dead)
        #print('next_alive:', next_alive)
    '''
        while len(self.alive) != 0:
            #for each cell in stack:
            cur_cell = self.alive.pop()
            temp = [cur_cell]
            #push all adjacent cells into the stack
            for adj in self.get_adjacent_index(cur_cell):
                if adj not in checked:
                    temp.append(adj)
            print('temp:',temp)
            #split into alive and dead cells
            while len(temp) != 0:
                cur_cell = temp.pop()
                checked.append(cur_cell)
                #check status for next step
                if self.step_cell(cur_cell): #cell alive on next step
                    if cur_cell not in next_alive: #try to get rid of this conditional
                        next_alive = self.sorted_add(next_alive, cur_cell)
                    continue
                #cell dead on next step
                if cur_cell not in next_dead: #try to get rid of this conditional
                    next_dead = self.sorted_add(next_dead, cur_cell)
        print('next_alive:',next_alive)
        print('next_dead:',next_dead)
        for live_cell in next_alive:
            self.set_value_of(live_cell, True)
        for dead_cell in next_dead:
            self.set_value_of(dead_cell, False)
        #updating 
        self.alive = next_alive
    '''

    '''
        cur_alive = self.alive
        self.alive.empty()
        
        for cur_cell in cur_alive:
            
            cur_alive.extend(self.get_adjacent_index(cur_cell))
        
        cur_dead = []
        for cur_cell in len(cur_alive) and (not self.get_value_of(cur_cell)) != 0:
            cur_alive.remove(cur_cell)
            cur_dead.append(cur_cell)
        #for each cell in alive:
            #if over/underpopulated, kill
            #else add to self.alive
        #for each cell in dead
            #if adj == 3 add to self.alive
        return
        
    def step(self) -> list: #return self.grid
        #challenge: updating every cell at the same time
        cur_alive = self.alive
        flip = [] #holds indexes to flip
        s = [] #list of indexes to run step_cell method on
        #print('alive:', self.alive)
        while len(cur_alive) != 0: #filling s from cur_alive
            cur_index = cur_alive.pop()
            if self.get_adjacent != 3 or self.get_adjacent != 2: #this kinda sucks
                flip.append(cur_index)
            for adj in self.get_adjacent_index(cur_index):
                if adj not in s:
                    s.append(adj)
        #print('s:', s)
        while len(s) != 0: #iterating through s to find which cells to flip
            cur_index = s.pop()
            cur_value = self.get_value_of(cur_index)
            if (self.step_cell(cur_index) != cur_value):
                flip.append(cur_index)
        while len(flip) != 0:
            cur_index = flip.pop()
            y = cur_index // self.length #expand to (x,y) and flip on self.grid
            x = cur_index % self.length
            self.grid[x][y] = not self.grid[x][y] #flipping
            if not self.grid[y][x]: #false, flipped from true
                self.grid[y][x] = False
                try:
                    self.alive.remove(cur_index)
                except:
                    continue
                continue
            self.alive.append(cur_index) #true, flipped from false
    ''' 
    def step_cell(self, index:int) -> bool:
        cur_state = self.get_value_of(index)
        y = index // self.length
        x = index % self.length
        adj = self.get_adjacent(y, x)
        if cur_state: #alive state
            if adj == 2 or adj == 3: #stays alive if 2 or 3 live neighbors
                return True 
            return False #dies by over/underpopulation
        else: #dead state
            if adj == 3: #coming to live from having 3 neighbors
                return True
            return False #staying dead

    def get_adjacent(self, y:int, x:int) -> int: #returns how many neighbors of the given cell are True
        bound = self.length-1
        count = 0
        #print(f'{3*y+x}', end=' ')

        if x != 0 and self.grid[y][x-1]: #left
            #print(f'left: {3*y+x-1}', end='; ')
            count += 1
        if x != bound and self.grid[y][x+1]: #right
            count += 1
            #print(f'right: {3*y+x+1}', end='; ')
        if y != 0 and self.grid[y-1][x]: #up
            count += 1
            #print(f'up: {3*(y-1)+x}', end='; ')
        if y != bound and self.grid[y+1][x]: #down
            count += 1
            #print(f'down: {3*(y+1)+x}', end='; ')
        if y != 0 and x != 0 and self.grid[y-1][x-1]: #up and left
            count += 1
            #print(f'up left: {3*(y-1)+x-1}', end='; ')
        if y != 0 and x != bound and self.grid[y-1][x+1]: #up and right
            count += 1
            #print(f'up right: {3*(y+1)+x-1}', end='; ')
        if y != bound and x != 0 and self.grid[y+1][x-1]: #down and left
            count += 1
            #print(f'down left: {3*(y-1)+x+1}', end='; ')
        if y != bound and x != bound and self.grid[y+1][x+1]: #down and right
            count += 1
            #print(f'down right: {3*(y+1)+x+1}', end='; ')
        return count
    def get_adjacent_index(self, index:int) -> list[int]:
        y = index // self.length
        x = index % self.length
        bound = self.length-1
        count = []
        if x != 0: #left
            #print(f'left: {3*y+x-1}', end='; ')
            count.append(index-1)
        if x != bound: #right
            count.append(index+1)
            #print(f'right: {3*y+x+1}', end='; ')
        if y != 0: #up
            count.append(index-self.length)
            #print(f'up: {3*(y-1)+x}', end='; ')
        if y != bound: #down
            count.append(index+self.length)
            #print(f'down: {3*(y+1)+x}', end='; ')
        if y != 0 and x != 0: #up and left
            count.append(index-self.length-1)
            #print(f'up left: {3*(y-1)+x-1}', end='; ')
        if y != 0 and x != bound: #up and right
            count.append(index-self.length+1)
            #print(f'up right: {3*(y+1)+x-1}', end='; ')
        if y != bound and x != 0: #down and left
            count.append(index+self.length-1)
            #print(f'down left: {3*(y-1)+x+1}', end='; ')
        if y != bound and x != bound: #down and right
            count.append(index+self.length+1)
            #print(f'down right: {3*(y+1)+x+1}', end='; ')
        return count

    def toString(self) -> str:
        out = ''
        for i in self.grid:
            for j in i:
                if j:
                    out += '[X]'
                else:
                    out += '[ ]'
            out += '\n'
        return out

#main
'''
def main():
    gridLength = 40
    g = grid(gridLength)
    #g.populate([1])
    #g.populate([0, 2, 5, 7, 8, 10, 13, 15])
    g.populate_random()

    for i in range(3):
        #print(f'alive on step {i}: {g.alive}')
        #print('step_cell(5):', g.step_cell(5))
        print(g.toString())
        g.step()
'''
'''
    for y in range(gridLength):
        for x in range(gridLength):
            print(f'[{g.get_adjacent(y, x)}]',end='')
            #g.get_adjacent(y, x)
        print()
'''

#main()