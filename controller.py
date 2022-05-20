import ui
import save

def run():
    temp = ui.init()
    print(temp)
    save.full(temp[0], temp[1], temp[2], temp[3], temp[4])    