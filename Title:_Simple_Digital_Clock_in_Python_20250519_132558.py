Title: Simple Digital Clock in Python

```python
from tkinter import Tk, Label
import time

def time_update():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, time_update)

app = Tk()
app.title("Digital Clock")
clock_label = Label(app, font=('calibri', 40, 'bold'), background='purple', foreground='white')
clock_label.pack(anchor='center')

time_update()
app.mainloop()
```