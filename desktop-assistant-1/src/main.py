from tkinter import Tk
from ui.main_window import MainWindow

def main():
    root = Tk()
    root.geometry("400x600+1000+0")  # 将窗口定位在右上角
    root.title("桌面助手")
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()