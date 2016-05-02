from random import shuffle, randrange
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title= title, size = (1000,500))
        self.pnl = wx.Panel(self)
        self.cpnl = []

    def make_maze(self, w = 16, h = 8):

        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        vis[0][0] = 1
        vis[h-1][w-1] =1
        def walk(x, y):
            vis[y][x] = 1

            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            flag=False
            for (xx, yy) in d:
                if yy-1 >= 0 and xx-1>= 0 and vis[yy-1][xx] is 1 and vis[yy-1][xx-1] is 1 and vis[yy][xx-1] is 1: continue
                if yy-1>=0 and xx+1 <= w-1 and vis[yy-1][xx] is 1 and vis[yy-1][xx+1] is 1 and vis[yy][xx+1] is 1: continue
                if yy+1<=h-1 and xx-1>= 0 and vis[yy+1][xx] is 1 and vis[yy+1][xx-1] is 1 and vis[yy][xx-1] is 1: continue
                if yy+1<=h-1 and xx+1<= w-1 and vis[yy+1][xx] is 1 and vis[yy+1][xx+1] is 1 and vis[yy][xx+1] is 1: continue
                if vis[yy][xx]: continue
                walk(xx, yy)

        walk(2, 3)
        if vis[h-1][w-1] is 0 and vis[h-1][w] is 0 and vis[h][w-1] is 0:
            vis[h-1][w] = 1

        for i in range(0,w):
            for j in range(0,h):
                if vis[j][i] is 1:
                    self.cpnl.append(wx.Panel(self.pnl,pos=(150+i*20,j*20), size=(20,20)))
        for cp in self.cpnl:
            cp.SetBackgroundColour(wx.Colour(0,0,0))
        for l in vis:
            None
            #print l
        self.vis = vis
        self.Show()

def solve_maze(matrix,x=0,y=0, gx = 0, gy= 0, list=[]):
    if x is gx and y is gy:
        return
    matrix[y][x] = 2
    d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
    shuffle(d)
    flag = True
    for (xx,yy) in d:
        if yy < 0 or xx < 0 or x > gx or y > gy: continue
        if yy-1 >= 0 and xx-1>= 0 and matrix[yy-1][xx] is 1 and matrix[yy-1][xx-1] is 1 and matrix[yy][xx-1] is 1: continue
        if yy-1>=0 and xx+1 <= gx and matrix[yy-1][xx] is 1 and matrix[yy-1][xx+1] is 1 and matrix[yy][xx+1] is 1: continue
        if yy+1<=gy and xx-1>= 0 and matrix[yy+1][xx] is 1 and matrix[yy+1][xx-1] is 1 and matrix[yy][xx-1] is 1: continue
        if yy+1<=gy and xx+1<= gx and matrix[yy+1][xx] is 1 and matrix[yy+1][xx+1] is 1 and matrix[yy][xx+1] is 1: continue
        if matrix[yy][xx] is 1:
            matrix[yy][xx] = 2
            list.append((xx,yy))
            flag = False
            solve_maze(matrix, xx, yy, gx, gy, list)
    print flag, x,y
    if flag:
        x,y = list.pop()
        solve_maze(matrix, x, y, gx, gy, list)

w = 16
h = 8
if __name__ == '__main__':
    app=wx.App()
    e = Example(None, title='Size')
    e.make_maze(w,h)
    #solve_maze(e.vis, 0,0,w-1,h-1)
    app.MainLoop()