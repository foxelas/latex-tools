from os.path import join as pathjoin
from os import listdir, remove
from os.path import splitext, exists
import tkinter as tk
from tkinter import filedialog

report_file = pathjoin('demo', 'report.tex')
image_dir = pathjoin('demo', 'img')

image_ext = ['.png', '.jpg', '.jpeg', '.eps', '.pdf']


def is_image(filename):
    _, ext = splitext(filename)
    is_image_file = ext in image_ext
    return is_image_file


def delete_unused_images(report_file, image_dir, delete_files=True):
    image_files = listdir(image_dir)
    image_files = [x for x in image_files if is_image(x)]

    with open(report_file, 'r') as f:
        contents = f.read()
        unused_images = [x for x in image_files if not (x in contents)]
        print(f'Unused images:\n{unused_images}\n')
        message_str.set('Unused images:\n' + str(unused_images) + '\n')

        if delete_files:
            [remove(pathjoin(image_dir, x)) for x in unused_images if exists(pathjoin(image_dir, x))]
            print(f'Deleted all unused files in {image_dir}.')

def set_selected_tex_file():
    root.selected_tex_file = filedialog.askopenfilename(initialdir="/", title="Select .tex file",
                                                        filetypes=[("LaTeX files","*.tex")])
    selected_tex_file_box.replace("1.0", tk.END, root.selected_tex_file)


def selected_image_dir():
    root.selected_image_dir = filedialog.askdirectory(initialdir="/", title="Select image folder")
    selected_image_dir_box.replace("1.0", tk.END, root.selected_image_dir)


root = tk.Tk()

canvas1 = tk.Canvas(root, width=450, height=550)
canvas1.pack()

root.selected_tex_file = ''
root.selected_image_dir = ''


selected_tex_file_label = tk.Label(root, text="Target .tex file")
selected_tex_file_box = tk.Text(root, height=5, width=52)
selected_tex_file_box.pack()
selected_tex_file_button = tk.Button(text='Select',
                    command=set_selected_tex_file,
                    bg='blue', fg='white')
selected_tex_file_button.pack()
selected_tex_file_label.place(x=10, y=10)
selected_tex_file_button.place(x=150, y=10)
selected_tex_file_box.place(x=10, y=50)


selected_image_dir_label = tk.Label(root, text="Target image dir")
selected_image_dir_box = tk.Text(root, height=5, width=52)
selected_image_dir_box.pack()
selected_image_dir_button = tk.Button(text='Select',
                    command=selected_image_dir,
                    bg='blue', fg='white')
selected_image_dir_button.pack()
selected_image_dir_label.place(x=10, y=150)
selected_image_dir_button.place(x=150, y=150)
selected_image_dir_box.place(x=10, y=190)


button1 = tk.Button(text='Delete Unused Images',
                    command=lambda : delete_unused_images(root.selected_tex_file, root.selected_image_dir, True),
                    bg='blue', fg='white')
button1.pack()
button1.place(x=150, y=300)

message_str = tk.StringVar()
message_str.set('')

result_label = tk.Label(root, textvariable=message_str, wraplength=400)
result_label.place(x=10, y=350)

root.mainloop()
