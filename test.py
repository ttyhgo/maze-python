from random import shuffle, randrange
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title= title, size = (1000,500))
        self.pnl = wx.Panel(self)
        self.cpnl = []




    def make_maze(self, w = 16, h = 8):

        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        #ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
        #hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

        def walk(x, y):
            vis[y][x] = 1

            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            flag=False
            for (xx, yy) in d:
                if y-1 >= 0 and x-1>= 0 and vis[y-1][x] is 1 and vis[y-1][x-1] is 1 and vis[y][x-1] is 1: continue
                if y-1>=0 and x+1 <= w and vis[y-1][x] is 1 and vis[y-1][x+1] is 1 and vis[y][x+1] is 1: continue
                if y+1<=h and x-1>= 0 and vis[y+1][x] is 1 and vis[y+1][x-1] is 1 and vis[y][x-1] is 1: continue
                if y+1<=h and x+1<= w and vis[y+1][x] is 1 and vis[y+1][x+1] is 1 and vis[y][x+1] is 1: continue
                if vis[yy][xx]: continue
                if xx == x: #hor[max(y, yy)][x] = "+  "
                    self.cpnl.append(wx.Panel(self.pnl,pos=(150+xx*20,max(y,yy)*20), size=(20,20)))
                if yy == y: #ver[y][max(x, xx)] = "   "
                    self.cpnl.append(wx.Panel(self.pnl,pos=(150+max(xx,x)*20,yy*20), size=(20,20)))
                walk(xx, yy)

        walk(0, 0)

        k = 0
        for cp in self.cpnl:
            self.cpnl[k].SetBackgroundColour(wx.Colour(0,0,0))
            k += 1
        self.Show()
        '''
        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        '''
        #return s
i = 0


if __name__ == '__main__':
    app=wx.App()
    e = Example(None, title='Size')
    e.make_maze()
    app.MainLoop()